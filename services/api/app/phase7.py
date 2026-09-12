"""Phase 7 packs, payment proposals, and field evidence. No executable eval."""

from __future__ import annotations

from typing import Any

from app.store import Store, StoreError, _id, _now

R4_SHELLS = (
    {
        "id": "B14",
        "label": "Treasury and payments",
        "status": "configured",
        "needs_connection": True,
        "native": "payment_proposals",
        "source": "unavailable",
    },
    {
        "id": "B19",
        "label": "Inventory and facilities",
        "status": "configured",
        "needs_connection": True,
        "native": None,
        "source": "unavailable",
    },
    {
        "id": "B20",
        "label": "Field, dispatch, offline capture",
        "status": "configured",
        "needs_connection": True,
        "native": "field_evidence",
        "source": "unavailable",
    },
    {
        "id": "B21",
        "label": "Quality, BOM, inspections",
        "status": "configured",
        "needs_connection": True,
        "native": None,
        "source": "unavailable",
    },
    {
        "id": "B24",
        "label": "Sector packs",
        "status": "configured",
        "needs_connection": True,
        "native": "domain_packs",
        "source": "unavailable",
    },
)

PACKS: dict[str, dict[str, Any]] = {
    "education-demo": {
        "id": "education-demo",
        "version": "1.0.0",
        "kind": "declarative",
        "domain_ids": ["B24"],
        "label": "Education records (demo)",
        "description": "Declarative sector-pack fixture. No executable code.",
        "grants_declared": ["ledger.read"],
        "custom_fields": [{"id": "enrolment_ref", "type": "string", "required": False}],
        "executable": False,
    },
    "example-executable": {
        "id": "example-executable",
        "version": "0.0.1",
        "kind": "executable",
        "domain_ids": ["P19"],
        "label": "Example executable pack",
        "description": "Catalogued only. Activation stays denied unless the execution flag and trust review both pass. No runtime eval.",
        "grants_declared": [],
        "custom_fields": [],
        "executable": True,
    },
}


def migrate_phase7(store: Store) -> None:
    store.conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS pack_installs (
          id TEXT PRIMARY KEY,
          tenant_id TEXT NOT NULL,
          pack_id TEXT NOT NULL,
          installed_by TEXT NOT NULL,
          status TEXT NOT NULL,
          created_at TEXT NOT NULL,
          UNIQUE (tenant_id, pack_id)
        );
        CREATE TABLE IF NOT EXISTS pack_trust_reviews (
          id TEXT PRIMARY KEY,
          tenant_id TEXT NOT NULL,
          pack_id TEXT NOT NULL,
          install_id TEXT NOT NULL,
          verdict TEXT NOT NULL,
          reviewed_by TEXT,
          created_at TEXT NOT NULL,
          updated_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS pack_custom_fields (
          id TEXT PRIMARY KEY,
          tenant_id TEXT NOT NULL,
          pack_id TEXT NOT NULL,
          field_id TEXT NOT NULL,
          field_type TEXT NOT NULL,
          created_at TEXT NOT NULL,
          UNIQUE (tenant_id, pack_id, field_id)
        );
        CREATE TABLE IF NOT EXISTS payment_proposals (
          id TEXT PRIMARY KEY,
          tenant_id TEXT NOT NULL,
          created_by TEXT NOT NULL,
          payee_label TEXT NOT NULL,
          amount_entered TEXT NOT NULL,
          currency TEXT NOT NULL,
          status TEXT NOT NULL,
          created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS bank_detail_changes (
          id TEXT PRIMARY KEY,
          tenant_id TEXT NOT NULL,
          actor_id TEXT NOT NULL,
          note TEXT NOT NULL,
          status TEXT NOT NULL,
          created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS field_evidence (
          id TEXT PRIMARY KEY,
          tenant_id TEXT NOT NULL,
          principal_id TEXT NOT NULL,
          idempotency_key TEXT NOT NULL,
          label TEXT NOT NULL,
          status TEXT NOT NULL,
          captured_offline INTEGER NOT NULL DEFAULT 0,
          created_at TEXT NOT NULL,
          UNIQUE (tenant_id, principal_id, idempotency_key)
        );
        CREATE TABLE IF NOT EXISTS erasure_requests (
          id TEXT PRIMARY KEY,
          tenant_id TEXT NOT NULL,
          requested_by TEXT NOT NULL,
          confirmations TEXT NOT NULL,
          status TEXT NOT NULL,
          destroyed INTEGER NOT NULL DEFAULT 0,
          created_at TEXT NOT NULL
        );
        """
    )
    store.flush()


def domain_shells() -> list[dict[str, Any]]:
    return [
        {
            **row,
            "live_write": False,
            "handoff": "Live source write is refused. Native records only where noted.",
        }
        for row in R4_SHELLS
    ]


def known_shell_ids() -> set[str]:
    return {row["id"] for row in R4_SHELLS}


def list_packs(store: Store, tenant_id: str) -> list[dict[str, Any]]:
    rows = []
    for pack in PACKS.values():
        rows.append(_pack_with_state(store, tenant_id, pack))
    return rows


def get_pack(store: Store, tenant_id: str, pack_id: str) -> dict[str, Any]:
    pack = PACKS.get(pack_id)
    if pack is None:
        raise StoreError("unknown pack", 404)
    return _pack_with_state(store, tenant_id, pack)


def _pack_with_state(store: Store, tenant_id: str, pack: dict[str, Any]) -> dict[str, Any]:
    install = store.row_to_dict(
        store.conn.execute(
            "SELECT * FROM pack_installs WHERE tenant_id=? AND pack_id=?",
            (tenant_id, pack["id"]),
        ).fetchone()
    )
    trust = store.row_to_dict(
        store.conn.execute(
            """SELECT * FROM pack_trust_reviews
               WHERE tenant_id=? AND pack_id=?
               ORDER BY created_at DESC LIMIT 1""",
            (tenant_id, pack["id"]),
        ).fetchone()
    )
    fields = [
        store.row_to_dict(row)
        for row in store.conn.execute(
            "SELECT field_id, field_type FROM pack_custom_fields WHERE tenant_id=? AND pack_id=?",
            (tenant_id, pack["id"]),
        ).fetchall()
    ]
    return {
        **pack,
        "installed": bool(install),
        "install_status": install["status"] if install else "not_installed",
        "trust_verdict": trust["verdict"] if trust else "none",
        "tenant_custom_fields": fields,
        "execution": "denied",
    }


def install_pack(store: Store, principal_id: str, tenant_id: str, pack_id: str) -> dict[str, Any]:
    if not store.has_grant(principal_id, "org.admin"):
        raise StoreError("denied: org.admin", 403)
    if pack_id not in PACKS:
        raise StoreError("unknown pack", 404)
    existing = store.conn.execute(
        "SELECT id FROM pack_installs WHERE tenant_id=? AND pack_id=?",
        (tenant_id, pack_id),
    ).fetchone()
    if existing:
        return get_pack(store, tenant_id, pack_id)
    now = _now()
    install_id = _id("pack")
    store.conn.execute(
        """INSERT INTO pack_installs(id, tenant_id, pack_id, installed_by, status, created_at)
           VALUES (?,?,?,?,?,?)""",
        (install_id, tenant_id, pack_id, principal_id, "installed", now),
    )
    store.conn.execute(
        """INSERT INTO pack_trust_reviews(
             id, tenant_id, pack_id, install_id, verdict, reviewed_by, created_at, updated_at
           ) VALUES (?,?,?,?,?,?,?,?)""",
        (_id("trust"), tenant_id, pack_id, install_id, "pending", None, now, now),
    )
    store.append_audit(principal_id, "pack.install", "pack", pack_id)
    store.flush()
    return get_pack(store, tenant_id, pack_id)


def review_pack_trust(
    store: Store, principal_id: str, tenant_id: str, pack_id: str, verdict: str
) -> dict[str, Any]:
    if not store.has_grant(principal_id, "org.admin"):
        raise StoreError("denied: org.admin", 403)
    if pack_id not in PACKS:
        raise StoreError("unknown pack", 404)
    if verdict not in {"accepted", "refused"}:
        raise StoreError("verdict must be accepted or refused", 400)
    row = store.conn.execute(
        """SELECT id FROM pack_trust_reviews
           WHERE tenant_id=? AND pack_id=? ORDER BY created_at DESC LIMIT 1""",
        (tenant_id, pack_id),
    ).fetchone()
    if row is None:
        raise StoreError("pack is not installed", 400)
    store.conn.execute(
        "UPDATE pack_trust_reviews SET verdict=?, reviewed_by=?, updated_at=? WHERE id=?",
        (verdict, principal_id, _now(), row["id"]),
    )
    store.append_audit(principal_id, "pack.trust", "pack", pack_id)
    store.flush()
    return get_pack(store, tenant_id, pack_id)


def define_custom_field(
    store: Store, principal_id: str, tenant_id: str, pack_id: str, field_id: str, field_type: str
) -> dict[str, Any]:
    if not store.has_grant(principal_id, "org.admin"):
        raise StoreError("denied: org.admin", 403)
    if pack_id not in PACKS:
        raise StoreError("unknown pack", 404)
    installed = store.conn.execute(
        "SELECT 1 FROM pack_installs WHERE tenant_id=? AND pack_id=?",
        (tenant_id, pack_id),
    ).fetchone()
    if installed is None:
        raise StoreError("pack is not installed", 400)
    fid = (field_id or "").strip()
    ftype = (field_type or "").strip()
    if not fid or not ftype:
        raise StoreError("field_id and field_type required", 400)
    store.conn.execute(
        """INSERT OR IGNORE INTO pack_custom_fields(id, tenant_id, pack_id, field_id, field_type, created_at)
           VALUES (?,?,?,?,?,?)""",
        (_id("field"), tenant_id, pack_id, fid, ftype, _now()),
    )
    store.flush()
    return get_pack(store, tenant_id, pack_id)


def activate_pack(
    store: Store,
    principal_id: str,
    tenant_id: str,
    pack_id: str,
    *,
    execution_enabled: bool,
) -> dict[str, Any]:
    if not store.has_grant(principal_id, "org.admin"):
        raise StoreError("denied: org.admin", 403)
    pack = PACKS.get(pack_id)
    if pack is None:
        raise StoreError("unknown pack", 404)
    state = get_pack(store, tenant_id, pack_id)
    if not execution_enabled:
        raise StoreError("pack execution disabled", 403)
    if not pack["executable"]:
        raise StoreError("declarative packs do not execute", 403)
    if state["trust_verdict"] != "accepted":
        raise StoreError("trust review must be accepted", 403)
    raise StoreError("no executable runtime is registered", 403)


def list_proposals(store: Store, principal_id: str) -> list[dict[str, Any]]:
    if not store.has_grant(principal_id, "ledger.read") and not store.has_grant(principal_id, "org.admin"):
        raise StoreError("denied", 403)
    tenant_id = store.principal(principal_id)["tenant_id"]
    return [
        store.row_to_dict(row)
        for row in store.conn.execute(
            "SELECT * FROM payment_proposals WHERE tenant_id=? ORDER BY created_at DESC",
            (tenant_id,),
        ).fetchall()
    ]


def create_proposal(store: Store, principal_id: str, body: dict[str, Any]) -> dict[str, Any]:
    if not store.has_grant(principal_id, "ledger.write") and not store.has_grant(principal_id, "org.admin"):
        raise StoreError("denied", 403)
    tenant_id = store.principal(principal_id)["tenant_id"]
    payee = str(body.get("payee_label") or "").strip()
    amount = str(body.get("amount_entered") or "").strip()
    currency = str(body.get("currency") or "AUD").strip() or "AUD"
    if not payee or not amount:
        raise StoreError("payee_label and amount_entered required", 400)
    row = {
        "id": _id("pay"),
        "tenant_id": tenant_id,
        "created_by": principal_id,
        "payee_label": payee,
        "amount_entered": amount,
        "currency": currency,
        "status": "draft",
        "payout": False,
        "created_at": _now(),
    }
    store.conn.execute(
        """INSERT INTO payment_proposals(
             id, tenant_id, created_by, payee_label, amount_entered, currency, status, created_at
           ) VALUES (?,?,?,?,?,?,?,?)""",
        (
            row["id"],
            row["tenant_id"],
            row["created_by"],
            row["payee_label"],
            row["amount_entered"],
            row["currency"],
            row["status"],
            row["created_at"],
        ),
    )
    store.append_audit(principal_id, "payment.propose", "payment_proposal", row["id"])
    store.flush()
    return {**row, "payout": False}


def approve_proposal(store: Store, principal_id: str, proposal_id: str) -> dict[str, Any]:
    designated = store.has_grant(principal_id, "approval.billing") or store.has_grant(
        principal_id, "org.admin"
    )
    if not designated:
        raise StoreError("designated authority required", 403)
    row = store.row_to_dict(
        store.conn.execute("SELECT * FROM payment_proposals WHERE id=?", (proposal_id,)).fetchone()
    )
    if row is None:
        raise StoreError("unknown proposal", 404)
    if row["tenant_id"] != store.principal(principal_id)["tenant_id"]:
        raise StoreError("denied", 403)
    store.conn.execute(
        "UPDATE payment_proposals SET status=? WHERE id=?",
        ("approved", proposal_id),
    )
    store.append_audit(principal_id, "payment.approve", "payment_proposal", proposal_id)
    store.flush()
    row["status"] = "approved"
    row["payout"] = False
    return row


def change_bank_details(store: Store, principal_id: str, note: str) -> dict[str, Any]:
    if not store.has_grant(principal_id, "org.admin"):
        raise StoreError("denied: org.admin", 403)
    tenant_id = store.principal(principal_id)["tenant_id"]
    row = {
        "id": _id("bank"),
        "tenant_id": tenant_id,
        "actor_id": principal_id,
        "note": (note or "").strip() or "bank detail change requested",
        "status": "recorded",
        "provider_write": False,
        "created_at": _now(),
    }
    store.conn.execute(
        """INSERT INTO bank_detail_changes(id, tenant_id, actor_id, note, status, created_at)
           VALUES (?,?,?,?,?,?)""",
        (row["id"], row["tenant_id"], row["actor_id"], row["note"], row["status"], row["created_at"]),
    )
    store.append_audit(principal_id, "payment.bank_details", "bank_detail_change", row["id"])
    store.flush()
    return row


def list_field_evidence(store: Store, principal_id: str) -> list[dict[str, Any]]:
    if not store.has_grant(principal_id, "ledger.read") and not store.has_grant(principal_id, "org.admin"):
        raise StoreError("denied", 403)
    tenant_id = store.principal(principal_id)["tenant_id"]
    return [
        store.row_to_dict(row)
        for row in store.conn.execute(
            """SELECT * FROM field_evidence
               WHERE tenant_id=? AND principal_id=?
               ORDER BY created_at DESC""",
            (tenant_id, principal_id),
        ).fetchall()
    ]


def capture_field_evidence(store: Store, principal_id: str, body: dict[str, Any]) -> dict[str, Any]:
    if not store.has_grant(principal_id, "ledger.write") and not store.has_grant(principal_id, "org.admin"):
        raise StoreError("denied", 403)
    tenant_id = store.principal(principal_id)["tenant_id"]
    key = str(body.get("idempotency_key") or "").strip()
    label = str(body.get("label") or "").strip()
    if not key or not label:
        raise StoreError("idempotency_key and label required", 400)
    existing = store.row_to_dict(
        store.conn.execute(
            """SELECT * FROM field_evidence
               WHERE tenant_id=? AND principal_id=? AND idempotency_key=?""",
            (tenant_id, principal_id, key),
        ).fetchone()
    )
    if existing:
        existing["replayed"] = True
        return existing
    row = {
        "id": _id("ev"),
        "tenant_id": tenant_id,
        "principal_id": principal_id,
        "idempotency_key": key,
        "label": label,
        "status": "synced",
        "captured_offline": 1 if body.get("captured_offline") else 0,
        "created_at": _now(),
        "replayed": False,
    }
    store.conn.execute(
        """INSERT INTO field_evidence(
             id, tenant_id, principal_id, idempotency_key, label, status, captured_offline, created_at
           ) VALUES (?,?,?,?,?,?,?,?)""",
        (
            row["id"],
            row["tenant_id"],
            row["principal_id"],
            row["idempotency_key"],
            row["label"],
            row["status"],
            row["captured_offline"],
            row["created_at"],
        ),
    )
    store.append_audit(principal_id, "field.evidence", "field_evidence", row["id"])
    store.flush()
    return row


def refuse_dispatch() -> None:
    raise StoreError("unavailable: live logistics connector is not configured", 403)


REQUIRED_ERASURE_CONFIRMATIONS = ("erase", "tenant", "irreversible")


def request_erasure(
    store: Store, principal_id: str, tenant_id: str, confirmations: list[Any] | None
) -> dict[str, Any]:
    designated = store.has_grant(principal_id, "org.admin") or store.has_grant(
        principal_id, "approval.erasure"
    )
    if not designated:
        raise StoreError("denied", 403)
    words = [str(item).strip().lower() for item in (confirmations or [])]
    if words != list(REQUIRED_ERASURE_CONFIRMATIONS):
        raise StoreError("three confirmations required: erase, tenant, irreversible", 400)
    row = {
        "id": _id("era"),
        "tenant_id": tenant_id,
        "requested_by": principal_id,
        "confirmations": ",".join(words),
        "status": "recorded",
        "destroyed": False,
        "created_at": _now(),
        "note": "Organisation-wide destroy is not executed. This records owner intent only.",
    }
    store.conn.execute(
        """INSERT INTO erasure_requests(
             id, tenant_id, requested_by, confirmations, status, destroyed, created_at
           ) VALUES (?,?,?,?,?,?,?)""",
        (
            row["id"],
            row["tenant_id"],
            row["requested_by"],
            row["confirmations"],
            row["status"],
            0,
            row["created_at"],
        ),
    )
    store.append_audit(principal_id, "erasure.request", "erasure_request", row["id"])
    store.flush()
    return row


def erasure_status(store: Store, principal_id: str, tenant_id: str) -> dict[str, Any]:
    if not store.has_grant(principal_id, "org.admin") and not store.has_grant(
        principal_id, "approval.erasure"
    ):
        raise StoreError("denied", 403)
    rows = [
        store.row_to_dict(row)
        for row in store.conn.execute(
            """SELECT id, status, destroyed, created_at
               FROM erasure_requests WHERE tenant_id=? ORDER BY created_at DESC""",
            (tenant_id,),
        ).fetchall()
    ]
    latest = rows[0] if rows else None
    return {
        "status": latest["status"] if latest else "none",
        "destroyed": False,
        "items": [{**row, "destroyed": False} for row in rows],
    }
