"""Sqlite/file store. Survives process restart. Application-level isolation."""

from __future__ import annotations

import json
import sqlite3
import time
import uuid
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

CAPABILITY_IDS = [
    f"B{i:02d}.01" for i in range(1, 25)
] + [f"P{i:02d}.01" for i in range(1, 20)]

FOUNDER_GRANTS = [
    "org.admin",
    "ledger.read",
    "ledger.write",
    "run.start",
    "run.cancel",
    "registry.read",
    "memory.read",
    "memory.write",
    "usage.read",
    "records.read",
    "search.read",
    "aggregates.read",
    "attachments.read",
    "attachments.write",
    "notifications.read",
    "approval.release",
    "approval.erasure",
    "approval.billing",
    "approval.org.admin",
]

SURFACE_GRANTS = {
    "records": "records.read",
    "search": "search.read",
    "aggregates": "aggregates.read",
    "attachments": "attachments.read",
    "notifications": "notifications.read",
    "memory": "memory.read",
}

SELF_APPROVAL_REFUSED = frozenset(
    {"approval.release", "approval.erasure", "approval.billing", "approval.org.admin"}
)


def _now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())


def _id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex[:12]}"


class StoreError(Exception):
    def __init__(self, message: str, status_code: int = 400) -> None:
        super().__init__(message)
        self.status_code = status_code


class Store:
    def __init__(self, path: str) -> None:
        self.path = str(Path(path))
        Path(self.path).parent.mkdir(parents=True, exist_ok=True)
        self.conn = sqlite3.connect(self.path, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA journal_mode=WAL")
        self.conn.execute("PRAGMA foreign_keys=ON")
        self._init_schema()
        self.flush()

    def flush(self) -> None:
        self.conn.commit()

    def close(self) -> None:
        self.flush()
        self.conn.close()

    def _init_schema(self) -> None:
        self.conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS principals (
              id TEXT PRIMARY KEY,
              tenant_id TEXT NOT NULL,
              kind TEXT NOT NULL,
              seat_id TEXT,
              grant_version INTEGER NOT NULL DEFAULT 1
            );
            CREATE TABLE IF NOT EXISTS seats (
              id TEXT PRIMARY KEY,
              tenant_id TEXT NOT NULL,
              template TEXT NOT NULL,
              principal_id TEXT
            );
            CREATE TABLE IF NOT EXISTS grants (
              id TEXT PRIMARY KEY,
              principal_id TEXT NOT NULL,
              tenant_id TEXT NOT NULL,
              grant_class TEXT NOT NULL,
              scope TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS entitlements (
              id TEXT PRIMARY KEY,
              tenant_id TEXT NOT NULL,
              principal_id TEXT NOT NULL,
              feature TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS organisations (
              id TEXT PRIMARY KEY,
              tenant_id TEXT NOT NULL,
              name TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS registry (
              capability_id TEXT PRIMARY KEY,
              domain_id TEXT NOT NULL,
              payload TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS priorities (
              id TEXT PRIMARY KEY,
              tenant_id TEXT NOT NULL,
              title TEXT NOT NULL,
              owner_principal_id TEXT NOT NULL,
              created_at TEXT NOT NULL,
              updated_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS plans (
              id TEXT PRIMARY KEY,
              tenant_id TEXT NOT NULL,
              title TEXT NOT NULL,
              priority_id TEXT,
              created_at TEXT NOT NULL,
              updated_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS work_items (
              id TEXT PRIMARY KEY,
              tenant_id TEXT NOT NULL,
              title TEXT NOT NULL,
              plan_id TEXT,
              stage TEXT NOT NULL,
              stage_changed_at TEXT NOT NULL,
              created_at TEXT NOT NULL,
              updated_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS assignments (
              id TEXT PRIMARY KEY,
              tenant_id TEXT NOT NULL,
              work_item_id TEXT NOT NULL,
              principal_id TEXT NOT NULL,
              created_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS dependencies (
              id TEXT PRIMARY KEY,
              tenant_id TEXT NOT NULL,
              from_work_item_id TEXT NOT NULL,
              to_work_item_id TEXT NOT NULL,
              created_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS source_references (
              id TEXT PRIMARY KEY,
              tenant_id TEXT NOT NULL,
              work_item_id TEXT,
              provider TEXT NOT NULL,
              installation_pointer TEXT NOT NULL,
              created_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS jobs (
              id TEXT PRIMARY KEY,
              tenant_id TEXT NOT NULL,
              status TEXT NOT NULL,
              purpose TEXT NOT NULL,
              created_at TEXT NOT NULL,
              updated_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS job_events (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              job_id TEXT NOT NULL,
              tenant_id TEXT NOT NULL,
              type TEXT NOT NULL,
              payload TEXT NOT NULL,
              created_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS runs (
              id TEXT PRIMARY KEY,
              job_id TEXT NOT NULL,
              tenant_id TEXT NOT NULL,
              sponsor TEXT NOT NULL,
              acting_identity TEXT NOT NULL,
              purpose TEXT NOT NULL,
              scope TEXT NOT NULL,
              policy_version TEXT NOT NULL,
              model_configuration TEXT NOT NULL,
              budget TEXT NOT NULL,
              deadline TEXT NOT NULL,
              accountable_owner TEXT NOT NULL,
              created_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS receipts (
              id TEXT PRIMARY KEY,
              job_id TEXT NOT NULL,
              tenant_id TEXT NOT NULL,
              step_name TEXT NOT NULL,
              idempotency_key TEXT NOT NULL UNIQUE,
              created_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS audit_records (
              id TEXT PRIMARY KEY,
              tenant_id TEXT NOT NULL,
              actor_principal_id TEXT NOT NULL,
              action TEXT NOT NULL,
              target_type TEXT NOT NULL,
              target_id TEXT NOT NULL,
              created_at TEXT NOT NULL
            );
            CREATE TRIGGER IF NOT EXISTS audit_no_update
              BEFORE UPDATE ON audit_records
            BEGIN
              SELECT RAISE(ABORT, 'audit is insert-only');
            END;
            CREATE TRIGGER IF NOT EXISTS audit_no_delete
              BEFORE DELETE ON audit_records
            BEGIN
              SELECT RAISE(ABORT, 'audit is insert-only');
            END;
            CREATE TABLE IF NOT EXISTS usage_events (
              id TEXT PRIMARY KEY,
              tenant_id TEXT NOT NULL,
              payload TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS notifications (
              id TEXT PRIMARY KEY,
              tenant_id TEXT NOT NULL,
              principal_id TEXT NOT NULL,
              body_kind TEXT NOT NULL,
              created_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS memory_items (
              id TEXT PRIMARY KEY,
              tenant_id TEXT NOT NULL,
              kind TEXT NOT NULL,
              class TEXT NOT NULL,
              provenance TEXT NOT NULL,
              created_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS attachments (
              id TEXT PRIMARY KEY,
              tenant_id TEXT NOT NULL,
              label TEXT NOT NULL,
              created_at TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS approvals (
              id TEXT PRIMARY KEY,
              tenant_id TEXT NOT NULL,
              approval_class TEXT NOT NULL,
              requester_id TEXT NOT NULL,
              target_id TEXT NOT NULL,
              target_version TEXT NOT NULL,
              status TEXT NOT NULL
            );
            """
        )
        self.flush()

    def row_to_dict(self, row: sqlite3.Row | None) -> dict[str, Any] | None:
        if row is None:
            return None
        return {k: row[k] for k in row.keys()}

    def seed_founder(self) -> None:
        if self.conn.execute("SELECT 1 FROM principals WHERE id='principal-founder'").fetchone():
            self._seed_registry()
            self.flush()
            return
        now = _now()
        self.conn.execute(
            "INSERT INTO organisations (id, tenant_id, name) VALUES (?, ?, ?)",
            ("org-founder", "tenant-founder", "Engine Labs"),
        )
        self.conn.execute(
            "INSERT INTO seats (id, tenant_id, template, principal_id) VALUES (?, ?, ?, ?)",
            ("seat-founder", "tenant-founder", "founder", "principal-founder"),
        )
        self.conn.execute(
            "INSERT INTO principals (id, tenant_id, kind, seat_id, grant_version) VALUES (?, ?, ?, ?, ?)",
            ("principal-founder", "tenant-founder", "human", "seat-founder", 1),
        )
        self.conn.execute(
            "INSERT INTO principals (id, tenant_id, kind, seat_id, grant_version) VALUES (?, ?, ?, ?, ?)",
            ("principal-unpriv", "tenant-founder", "human", None, 1),
        )
        self.conn.execute(
            "INSERT INTO principals (id, tenant_id, kind, seat_id, grant_version) VALUES (?, ?, ?, ?, ?)",
            ("principal-agent", "tenant-founder", "agent", None, 1),
        )
        self.conn.execute(
            "INSERT INTO principals (id, tenant_id, kind, seat_id, grant_version) VALUES (?, ?, ?, ?, ?)",
            ("principal-other", "tenant-other", "human", None, 1),
        )
        for cls in FOUNDER_GRANTS:
            self.conn.execute(
                "INSERT INTO grants (id, principal_id, tenant_id, grant_class, scope) VALUES (?, ?, ?, ?, ?)",
                (_id("grant"), "principal-founder", "tenant-founder", cls, "org"),
            )
        self.conn.execute(
            "INSERT INTO notifications (id, tenant_id, principal_id, body_kind, created_at) VALUES (?, ?, ?, ?, ?)",
            ("notif-1", "tenant-founder", "principal-founder", "job_completed", now),
        )
        self.conn.execute(
            "INSERT INTO memory_items (id, tenant_id, kind, class, provenance, created_at) VALUES (?, ?, ?, ?, ?, ?)",
            ("mem-1", "tenant-founder", "project", "approved", "seed", now),
        )
        self._seed_registry()
        self.append_audit("principal-founder", "seed", "organisation", "org-founder")
        self.flush()

    def _seed_registry(self) -> None:
        if self.conn.execute("SELECT COUNT(*) AS c FROM registry").fetchone()["c"] >= 43:
            return
        now = _now()
        for cap in CAPABILITY_IDS:
            domain = cap.split(".")[0]
            hermes_tool = False
            status = "planned"
            row = {
                "domain_id": domain,
                "capability_id": cap,
                "user_outcome": f"Seed row {cap}",
                "owner": "native",
                "read_actions": ["read"],
                "write_actions": ["write"],
                "data_authority": "native",
                "required_grants": ["registry.read"],
                "dependencies": [],
                "interface_components": ["registry"],
                "release_phase": "07 / R1",
                "implementation_status": status,
                "acceptance_evidence": "n/a — planned row",
                "registry_version": "0.1.0-phase0",
                "status_changed_at": now,
                "status_evidence": "phase-1-seed",
                "hermes_side_effecting_tool": hermes_tool,
                "hermes_side_effecting_tools": "unavailable",
            }
            self.conn.execute(
                "INSERT OR REPLACE INTO registry (capability_id, domain_id, payload) VALUES (?, ?, ?)",
                (cap, domain, json.dumps(row)),
            )

    def principal(self, principal_id: str) -> dict[str, Any]:
        row = self.conn.execute("SELECT * FROM principals WHERE id=?", (principal_id,)).fetchone()
        if not row:
            raise StoreError("unknown principal", 401)
        return self.row_to_dict(row)  # type: ignore[return-value]

    def grant_classes(self, principal_id: str) -> set[str]:
        rows = self.conn.execute(
            "SELECT grant_class FROM grants WHERE principal_id=?", (principal_id,)
        ).fetchall()
        return {r["grant_class"] for r in rows}

    def has_grant(self, principal_id: str, grant_class: str) -> bool:
        return grant_class in self.grant_classes(principal_id)

    def require_surface(self, principal_id: str, surface: str) -> None:
        needed = SURFACE_GRANTS[surface]
        classes = self.grant_classes(principal_id)
        if needed not in classes and "org.admin" not in classes:
            raise StoreError(f"denied: {surface}", 403)

    def add_grant(self, principal_id: str, grant_class: str, tenant_id: str) -> dict[str, Any]:
        principal = self.principal(principal_id)
        if principal["kind"] == "agent" and grant_class.startswith("approval."):
            raise StoreError("agent principals cannot hold approval.* grants", 400)
        self.conn.execute(
            "INSERT INTO grants (id, principal_id, tenant_id, grant_class, scope) VALUES (?, ?, ?, ?, ?)",
            (_id("grant"), principal_id, tenant_id, grant_class, "org"),
        )
        self.flush()
        return {"principal_id": principal_id, "grant_class": grant_class}

    def add_entitlement(self, principal_id: str, feature: str, tenant_id: str) -> dict[str, Any]:
        eid = _id("ent")
        self.conn.execute(
            "INSERT INTO entitlements (id, tenant_id, principal_id, feature) VALUES (?, ?, ?, ?)",
            (eid, tenant_id, principal_id, feature),
        )
        self.flush()
        return {"id": eid, "principal_id": principal_id, "feature": feature}

    def entitlements(self, principal_id: str) -> list[dict[str, Any]]:
        rows = self.conn.execute(
            "SELECT * FROM entitlements WHERE principal_id=?", (principal_id,)
        ).fetchall()
        return [self.row_to_dict(r) for r in rows]  # type: ignore[misc]

    def decide_approval(
        self,
        *,
        approval_class: str,
        requester_id: str,
        decider_id: str,
        target_id: str,
        target_version: str,
        tenant_id: str,
    ) -> dict[str, Any]:
        if (
            approval_class in SELF_APPROVAL_REFUSED
            or approval_class.removeprefix("approval.")
            in {"release", "erasure", "billing", "org.admin"}
        ) and requester_id == decider_id:
            raise StoreError("self-approval refused", 403)
        if not self.has_grant(decider_id, approval_class) and not self.has_grant(
            decider_id, "org.admin"
        ):
            raise StoreError("approval grant missing", 403)
        aid = _id("appr")
        self.conn.execute(
            """INSERT INTO approvals (id, tenant_id, approval_class, requester_id, target_id, target_version, status)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (aid, tenant_id, approval_class, requester_id, target_id, target_version, "approved"),
        )
        self.flush()
        return {"id": aid, "status": "approved"}

    def void_approval_if_changed(self, target_id: str, new_version: str) -> int:
        cur = self.conn.execute(
            "UPDATE approvals SET status='voided' WHERE target_id=? AND target_version!=? AND status='approved'",
            (target_id, new_version),
        )
        self.flush()
        return cur.rowcount

    def list_registry(self) -> list[dict[str, Any]]:
        rows = self.conn.execute("SELECT payload FROM registry ORDER BY capability_id").fetchall()
        items = [json.loads(r["payload"]) for r in rows]
        for item in items:
            if item.get("hermes_side_effecting_tool"):
                item["implementation_status"] = "unavailable"
        return items

    def append_audit(self, actor: str, action: str, target_type: str, target_id: str) -> str:
        tenant = self.principal(actor)["tenant_id"] if actor.startswith("principal-") else "tenant-founder"
        try:
            tenant = self.principal(actor)["tenant_id"]
        except StoreError:
            tenant = "tenant-founder"
        aid = _id("audit")
        self.conn.execute(
            """INSERT INTO audit_records (id, tenant_id, actor_principal_id, action, target_type, target_id, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (aid, tenant, actor, action, target_type, target_id, _now()),
        )
        self.flush()
        return aid

    def try_update_audit(self, audit_id: str) -> None:
        self.conn.execute("UPDATE audit_records SET action='tamper' WHERE id=?", (audit_id,))

    def create_priority(self, principal_id: str, title: str) -> dict[str, Any]:
        if not self.has_grant(principal_id, "ledger.write") and not self.has_grant(principal_id, "org.admin"):
            raise StoreError("denied: ledger", 403)
        p = self.principal(principal_id)
        now = _now()
        pid = _id("pri")
        self.conn.execute(
            """INSERT INTO priorities (id, tenant_id, title, owner_principal_id, created_at, updated_at)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (pid, p["tenant_id"], title, principal_id, now, now),
        )
        self.append_audit(principal_id, "priority.create", "priority", pid)
        self.flush()
        return self.row_to_dict(self.conn.execute("SELECT * FROM priorities WHERE id=?", (pid,)).fetchone())  # type: ignore[return-value]

    def create_plan(self, principal_id: str, title: str, priority_id: str | None = None) -> dict[str, Any]:
        if not self.has_grant(principal_id, "ledger.write") and not self.has_grant(principal_id, "org.admin"):
            raise StoreError("denied: ledger", 403)
        p = self.principal(principal_id)
        now = _now()
        pid = _id("plan")
        self.conn.execute(
            """INSERT INTO plans (id, tenant_id, title, priority_id, created_at, updated_at)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (pid, p["tenant_id"], title, priority_id, now, now),
        )
        self.append_audit(principal_id, "plan.create", "plan", pid)
        self.flush()
        return self.row_to_dict(self.conn.execute("SELECT * FROM plans WHERE id=?", (pid,)).fetchone())  # type: ignore[return-value]

    def create_work_item(self, principal_id: str, title: str, plan_id: str | None = None) -> dict[str, Any]:
        if not self.has_grant(principal_id, "ledger.write") and not self.has_grant(principal_id, "org.admin"):
            raise StoreError("denied: ledger", 403)
        p = self.principal(principal_id)
        now = _now()
        wid = _id("wi")
        self.conn.execute(
            """INSERT INTO work_items (id, tenant_id, title, plan_id, stage, stage_changed_at, created_at, updated_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (wid, p["tenant_id"], title, plan_id, "request", now, now, now),
        )
        self.append_audit(principal_id, "work_item.create", "work_item", wid)
        self.flush()
        return self.row_to_dict(self.conn.execute("SELECT * FROM work_items WHERE id=?", (wid,)).fetchone())  # type: ignore[return-value]

    def create_assignment(self, principal_id: str, work_item_id: str, assignee: str) -> dict[str, Any]:
        if not self.has_grant(principal_id, "ledger.write") and not self.has_grant(principal_id, "org.admin"):
            raise StoreError("denied: ledger", 403)
        p = self.principal(principal_id)
        aid = _id("asg")
        now = _now()
        self.conn.execute(
            """INSERT INTO assignments (id, tenant_id, work_item_id, principal_id, created_at)
               VALUES (?, ?, ?, ?, ?)""",
            (aid, p["tenant_id"], work_item_id, assignee, now),
        )
        self.flush()
        return {"id": aid, "work_item_id": work_item_id, "principal_id": assignee}

    def create_dependency(self, principal_id: str, src: str, dst: str) -> dict[str, Any]:
        if not self.has_grant(principal_id, "ledger.write") and not self.has_grant(principal_id, "org.admin"):
            raise StoreError("denied: ledger", 403)
        p = self.principal(principal_id)
        did = _id("dep")
        self.conn.execute(
            """INSERT INTO dependencies (id, tenant_id, from_work_item_id, to_work_item_id, created_at)
               VALUES (?, ?, ?, ?, ?)""",
            (did, p["tenant_id"], src, dst, _now()),
        )
        self.flush()
        return {"id": did, "from_work_item_id": src, "to_work_item_id": dst}

    def create_source_reference(self, principal_id: str, provider: str, pointer: str) -> dict[str, Any]:
        if not self.has_grant(principal_id, "ledger.write") and not self.has_grant(principal_id, "org.admin"):
            raise StoreError("denied: ledger", 403)
        p = self.principal(principal_id)
        sid = _id("sref")
        self.conn.execute(
            """INSERT INTO source_references (id, tenant_id, provider, installation_pointer, created_at)
               VALUES (?, ?, ?, ?, ?)""",
            (sid, p["tenant_id"], provider, pointer, _now()),
        )
        self.flush()
        return {"id": sid, "provider": provider, "installation_pointer": pointer}

    def list_visible(self, table: str, principal_id: str) -> list[dict[str, Any]]:
        p = self.principal(principal_id)
        if table in {"priorities", "plans", "work_items", "assignments", "dependencies", "source_references", "jobs"}:
            if not self.has_grant(principal_id, "ledger.read") and not self.has_grant(principal_id, "org.admin"):
                raise StoreError(f"denied: {table}", 403)
        rows = self.conn.execute(f"SELECT * FROM {table} WHERE tenant_id=?", (p["tenant_id"],)).fetchall()
        return [self.row_to_dict(r) for r in rows]  # type: ignore[misc]

    def persist_job(self, principal_id: str, purpose: str) -> dict[str, Any]:
        if not self.has_grant(principal_id, "run.start") and not self.has_grant(principal_id, "org.admin"):
            raise StoreError("denied: run.start", 403)
        p = self.principal(principal_id)
        now = _now()
        jid = _id("job")
        rid = _id("run")
        self.conn.execute(
            """INSERT INTO jobs (id, tenant_id, status, purpose, created_at, updated_at)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (jid, p["tenant_id"], "queued", purpose, now, now),
        )
        self.conn.execute(
            """INSERT INTO runs (
                 id, job_id, tenant_id, sponsor, acting_identity, purpose, scope,
                 policy_version, model_configuration, budget, deadline, accountable_owner, created_at
               ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                rid,
                jid,
                p["tenant_id"],
                principal_id,
                principal_id,
                purpose,
                "tenant",
                "1",
                "none",
                "none",
                "2026-12-31T00:00:00Z",
                principal_id,
                now,
            ),
        )
        self._add_event(jid, p["tenant_id"], "job.persisted", {"job_id": jid, "run_id": rid})
        self.append_audit(principal_id, "job.create", "job", jid)
        self.flush()
        return {"id": jid, "run_id": rid, "status": "queued", "purpose": purpose}

    def start_job(self, job_id: str) -> None:
        self.conn.execute(
            "UPDATE jobs SET status='running', updated_at=? WHERE id=?",
            (_now(), job_id),
        )
        job = self.conn.execute("SELECT * FROM jobs WHERE id=?", (job_id,)).fetchone()
        self._add_event(job_id, job["tenant_id"], "job.started", {"job_id": job_id})
        self.flush()

    def complete_job(self, job_id: str) -> None:
        self.conn.execute(
            "UPDATE jobs SET status='completed', updated_at=? WHERE id=?",
            (_now(), job_id),
        )
        job = self.conn.execute("SELECT * FROM jobs WHERE id=?", (job_id,)).fetchone()
        self._add_event(job_id, job["tenant_id"], "job.completed", {"job_id": job_id})
        self.flush()

    def cancel_job(self, principal_id: str, job_id: str) -> dict[str, Any]:
        if not self.has_grant(principal_id, "run.cancel") and not self.has_grant(principal_id, "org.admin"):
            raise StoreError("denied: run.cancel", 403)
        job = self.conn.execute("SELECT * FROM jobs WHERE id=?", (job_id,)).fetchone()
        if not job:
            raise StoreError("job not found", 404)
        self.conn.execute(
            "UPDATE jobs SET status='cancelled', updated_at=? WHERE id=?",
            (_now(), job_id),
        )
        self._add_event(job_id, job["tenant_id"], "job.cancelled", {"job_id": job_id})
        self.flush()
        return {"id": job_id, "status": "cancelled"}

    def get_job(self, job_id: str) -> dict[str, Any]:
        job = self.conn.execute("SELECT * FROM jobs WHERE id=?", (job_id,)).fetchone()
        if not job:
            raise StoreError("job not found", 404)
        run = self.conn.execute("SELECT * FROM runs WHERE job_id=?", (job_id,)).fetchone()
        data = self.row_to_dict(job)
        data["run"] = self.row_to_dict(run)
        return data  # type: ignore[return-value]

    def _add_event(self, job_id: str, tenant_id: str, typ: str, payload: dict[str, Any]) -> int:
        cur = self.conn.execute(
            """INSERT INTO job_events (job_id, tenant_id, type, payload, created_at)
               VALUES (?, ?, ?, ?, ?)""",
            (job_id, tenant_id, typ, json.dumps(payload), _now()),
        )
        return int(cur.lastrowid)

    def events_after(self, job_id: str, last_event_id: int = 0) -> list[dict[str, Any]]:
        rows = self.conn.execute(
            "SELECT * FROM job_events WHERE job_id=? AND id>? ORDER BY id",
            (job_id, last_event_id),
        ).fetchall()
        out = []
        for r in rows:
            item = self.row_to_dict(r)
            item["payload"] = json.loads(item["payload"])
            out.append(item)
        return out

    def add_receipt(self, job_id: str, step_name: str, idempotency_key: str) -> dict[str, Any]:
        existing = self.conn.execute(
            "SELECT * FROM receipts WHERE idempotency_key=?", (idempotency_key,)
        ).fetchone()
        if existing:
            return self.row_to_dict(existing)  # type: ignore[return-value]
        job = self.conn.execute("SELECT * FROM jobs WHERE id=?", (job_id,)).fetchone()
        if not job:
            raise StoreError("job not found", 404)
        rid = _id("rcpt")
        self.conn.execute(
            """INSERT INTO receipts (id, job_id, tenant_id, step_name, idempotency_key, created_at)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (rid, job_id, job["tenant_id"], step_name, idempotency_key, _now()),
        )
        self._add_event(job_id, job["tenant_id"], "step.receipt", {"receipt_id": rid, "step": step_name})
        self.flush()
        return {"id": rid, "job_id": job_id, "step_name": step_name, "idempotency_key": idempotency_key}

    def create_attachment(self, principal_id: str, label: str) -> dict[str, Any]:
        self.require_surface(principal_id, "attachments")
        if not self.has_grant(principal_id, "attachments.write") and not self.has_grant(
            principal_id, "org.admin"
        ):
            raise StoreError("denied: attachments", 403)
        p = self.principal(principal_id)
        aid = _id("att")
        self.conn.execute(
            "INSERT INTO attachments (id, tenant_id, label, created_at) VALUES (?, ?, ?, ?)",
            (aid, p["tenant_id"], label, _now()),
        )
        self.flush()
        return {"id": aid, "label": label}

    def get_attachment(self, attachment_id: str) -> dict[str, Any]:
        row = self.conn.execute("SELECT * FROM attachments WHERE id=?", (attachment_id,)).fetchone()
        if not row:
            raise StoreError("attachment not found", 404)
        return self.row_to_dict(row)  # type: ignore[return-value]

    def list_notifications(self, principal_id: str) -> list[dict[str, Any]]:
        self.require_surface(principal_id, "notifications")
        p = self.principal(principal_id)
        rows = self.conn.execute(
            "SELECT * FROM notifications WHERE tenant_id=?", (p["tenant_id"],)
        ).fetchall()
        return [self.row_to_dict(r) for r in rows]  # type: ignore[misc]

    def list_memory(self, principal_id: str) -> list[dict[str, Any]]:
        self.require_surface(principal_id, "memory")
        p = self.principal(principal_id)
        rows = self.conn.execute(
            "SELECT * FROM memory_items WHERE tenant_id=?", (p["tenant_id"],)
        ).fetchall()
        return [self.row_to_dict(r) for r in rows]  # type: ignore[misc]

    def list_records(self, principal_id: str) -> list[dict[str, Any]]:
        self.require_surface(principal_id, "records")
        return self.list_visible("work_items", principal_id) if self.has_grant(principal_id, "ledger.read") or self.has_grant(principal_id, "org.admin") else []

    def search(self, principal_id: str, query: str) -> list[dict[str, Any]]:
        self.require_surface(principal_id, "search")
        p = self.principal(principal_id)
        if not self.has_grant(principal_id, "ledger.read") and not self.has_grant(principal_id, "org.admin"):
            raise StoreError("denied: search", 403)
        like = f"%{query}%"
        rows = self.conn.execute(
            "SELECT * FROM work_items WHERE tenant_id=? AND title LIKE ?",
            (p["tenant_id"], like),
        ).fetchall()
        return [self.row_to_dict(r) for r in rows]  # type: ignore[misc]

    def aggregates(self, principal_id: str) -> dict[str, int]:
        self.require_surface(principal_id, "aggregates")
        p = self.principal(principal_id)
        if not self.has_grant(principal_id, "ledger.read") and not self.has_grant(principal_id, "org.admin"):
            raise StoreError("denied: aggregates", 403)
        count = self.conn.execute(
            "SELECT COUNT(*) AS c FROM work_items WHERE tenant_id=?", (p["tenant_id"],)
        ).fetchone()["c"]
        return {"work_items": int(count)}

    def insert_usage(self, payload: dict[str, Any]) -> str:
        uid = payload.get("event_id") or _id("use")
        self.conn.execute(
            "INSERT INTO usage_events (id, tenant_id, payload) VALUES (?, ?, ?)",
            (uid, payload.get("tenant_id", "tenant-founder"), json.dumps(payload)),
        )
        self.flush()
        return str(uid)

    def usage_count(self) -> int:
        return int(self.conn.execute("SELECT COUNT(*) AS c FROM usage_events").fetchone()["c"])

    def health_db(self) -> str:
        try:
            self.conn.execute("SELECT 1")
            return "ok"
        except sqlite3.Error:
            return "error"


def effective_grants(sponsor: set[str], toolset: set[str], mode: set[str]) -> set[str]:
    return set(sponsor) & set(toolset) & set(mode)


@contextmanager
def open_store(path: str) -> Iterator[Store]:
    store = Store(path)
    try:
        yield store
    finally:
        store.close()
