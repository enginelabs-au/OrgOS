"""Governed memory operations (PRD-F.2, F.3). Credential scan on write."""

from __future__ import annotations

import json
import re
from typing import Any

from app.store import Store, StoreError, _id, _now

MEMORY_KINDS = ("sessions", "preferences", "projects", "domains", "organisation", "skills")
MEMORY_CLASSES = ("source", "approved", "inferred")

CREDENTIAL_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    re.compile(r"(?i)(api[_-]?key|secret|password|bearer)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"(?i)authorization:\s*bearer\s+\S+"),
)


def scan_credentials(text: str) -> None:
    blob = text or ""
    for pattern in CREDENTIAL_PATTERNS:
        if pattern.search(blob):
            raise StoreError("credential-shaped content refused", 422)


def seat_template(store: Store, principal_id: str) -> str:
    row = store.conn.execute(
        "SELECT template FROM seats WHERE principal_id=?", (principal_id,)
    ).fetchone()
    return str(row["template"]) if row else "none"


def _item_dict(row: Any) -> dict[str, Any]:
    item = {k: row[k] for k in row.keys()}
    raw = item.get("provenance") or "{}"
    try:
        item["provenance"] = json.loads(raw) if isinstance(raw, str) else raw
    except json.JSONDecodeError:
        item["provenance"] = {"source": raw}
    return item


def _restricted_source_ids(store: Store, tenant_id: str) -> set[str]:
    rows = store.conn.execute(
        """SELECT id FROM memory_items
           WHERE tenant_id=? AND restriction_scope!='' AND restriction_scope IS NOT NULL
             AND deleted_at IS NULL""",
        (tenant_id,),
    ).fetchall()
    return {r["id"] for r in rows}


def _visible_to(store: Store, principal_id: str, item: dict[str, Any]) -> bool:
    template = seat_template(store, principal_id)
    if item.get("deleted_at"):
        return False
    if template == "operator":
        if item.get("owner_principal_id") != principal_id:
            return False
        return item.get("kind") in {"sessions", "preferences"}
    if template == "project_lead":
        return item.get("kind") in {"projects", "domains", "sessions", "preferences"} or item.get(
            "owner_principal_id"
        ) == principal_id
    return True


def list_memory(store: Store, principal_id: str, query: str = "") -> list[dict[str, Any]]:
    store.require_surface(principal_id, "memory")
    p = store.principal(principal_id)
    rows = store.conn.execute(
        "SELECT * FROM memory_items WHERE tenant_id=? ORDER BY created_at DESC",
        (p["tenant_id"],),
    ).fetchall()
    restricted = _restricted_source_ids(store, p["tenant_id"])
    q = (query or "").strip().lower()
    out: list[dict[str, Any]] = []
    for row in rows:
        item = _item_dict(row)
        if not _visible_to(store, principal_id, item):
            continue
        parent = item.get("parent_id") or ""
        if parent in restricted and item.get("content_class") == "inferred":
            continue
        if q and q not in f"{item.get('title', '')} {item.get('content', '')}".lower():
            continue
        out.append(item)
    return out


def inspect_memory(store: Store, principal_id: str, item_id: str) -> dict[str, Any]:
    items = {row["id"]: row for row in list_memory(store, principal_id)}
    if item_id not in items:
        raise StoreError("memory item not found", 404)
    return items[item_id]


def _write_row(
    store: Store,
    *,
    principal_id: str,
    tenant_id: str,
    title: str,
    kind: str,
    cls: str,
    content: str,
    content_class: str,
    parent_id: str | None,
    version: int,
    restriction_scope: str = "",
    provenance: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if not store.has_grant(principal_id, "memory.write") and not store.has_grant(principal_id, "org.admin"):
        raise StoreError("denied: memory.write", 403)
    scan_credentials(f"{title}\n{content}")
    if kind not in MEMORY_KINDS:
        raise StoreError("unknown memory kind", 400)
    if cls not in MEMORY_CLASSES:
        raise StoreError("unknown memory class", 400)
    now = _now()
    mid = _id("mem")
    prov = provenance or {
        "source": "native",
        "owner": principal_id,
        "source_permissions": "memory.write",
        "created_at": now,
        "updated_at": now,
        "verification": "unverified",
        "expiry": "",
        "version": version,
        "class": cls,
        "kind": kind,
        "restriction_scope": restriction_scope,
        "parent_id": parent_id or "",
    }
    store.conn.execute(
        """INSERT INTO memory_items
           (id, tenant_id, kind, class, provenance, created_at, title, owner_principal_id,
            version, restriction_scope, archived_at, expires_at, content_class, parent_id,
            content, deleted_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (
            mid,
            tenant_id,
            kind,
            cls,
            json.dumps(prov),
            now,
            title,
            principal_id,
            version,
            restriction_scope,
            None,
            None,
            content_class,
            parent_id,
            content,
            None,
        ),
    )
    store.append_audit(principal_id, "memory.write", "memory", mid)
    store.flush()
    return inspect_memory(store, principal_id, mid)


def create_memory(store: Store, principal_id: str, body: dict[str, Any]) -> dict[str, Any]:
    p = store.principal(principal_id)
    return _write_row(
        store,
        principal_id=principal_id,
        tenant_id=p["tenant_id"],
        title=str(body.get("title") or "Untitled"),
        kind=str(body.get("kind") or "projects"),
        cls=str(body.get("class") or "source"),
        content=str(body.get("content") or ""),
        content_class=str(body.get("content_class") or "source"),
        parent_id=None,
        version=1,
    )


def correct_memory(store: Store, principal_id: str, item_id: str, body: dict[str, Any]) -> dict[str, Any]:
    _require_mutate(store, principal_id, item_id, allow_operator=False)
    current = inspect_memory(store, principal_id, item_id)
    p = store.principal(principal_id)
    return _write_row(
        store,
        principal_id=principal_id,
        tenant_id=p["tenant_id"],
        title=str(body.get("title") or current["title"]),
        kind=current["kind"],
        cls=current["class"],
        content=str(body.get("content") or current.get("content") or ""),
        content_class=current.get("content_class") or "source",
        parent_id=item_id,
        version=int(current.get("version") or 1) + 1,
        restriction_scope=current.get("restriction_scope") or "",
        provenance={**(current.get("provenance") or {}), "updated_at": _now(), "parent_id": item_id, "version": int(current.get("version") or 1) + 1},
    )


def merge_memory(store: Store, principal_id: str, left_id: str, right_id: str) -> dict[str, Any]:
    left = inspect_memory(store, principal_id, left_id)
    right = inspect_memory(store, principal_id, right_id)
    _require_mutate(store, principal_id, left_id, allow_operator=False)
    p = store.principal(principal_id)
    return _write_row(
        store,
        principal_id=principal_id,
        tenant_id=p["tenant_id"],
        title=f"{left.get('title')} + {right.get('title')}",
        kind=left["kind"],
        cls="approved",
        content=f"{left.get('content') or ''}\n---\n{right.get('content') or ''}",
        content_class="inferred",
        parent_id=left_id,
        version=1,
        provenance={
            "source": "merge",
            "owner": principal_id,
            "merged": [left_id, right_id],
            "created_at": _now(),
            "updated_at": _now(),
            "verification": "merged",
            "expiry": "",
            "version": 1,
            "class": "approved",
            "kind": left["kind"],
            "restriction_scope": "",
            "parent_id": left_id,
        },
    )


def restrict_memory(store: Store, principal_id: str, item_id: str, scope: str) -> dict[str, Any]:
    _require_mutate(store, principal_id, item_id, allow_operator=False)
    inspect_memory(store, principal_id, item_id)
    store.conn.execute(
        "UPDATE memory_items SET restriction_scope=? WHERE id=?",
        (scope or "restricted", item_id),
    )
    store.append_audit(principal_id, "memory.restrict", "memory", item_id)
    store.flush()
    return inspect_memory(store, principal_id, item_id)


def archive_memory(store: Store, principal_id: str, item_id: str) -> dict[str, Any]:
    _require_mutate(store, principal_id, item_id, allow_operator=False)
    inspect_memory(store, principal_id, item_id)
    store.conn.execute(
        "UPDATE memory_items SET archived_at=? WHERE id=?",
        (_now(), item_id),
    )
    store.append_audit(principal_id, "memory.archive", "memory", item_id)
    store.flush()
    return inspect_memory(store, principal_id, item_id)


def export_memory(store: Store, principal_id: str, item_id: str) -> dict[str, Any]:
    item = inspect_memory(store, principal_id, item_id)
    job = store.persist_job(principal_id, "memory.export")
    store.add_receipt(job["id"], "memory.export", f"{job['id']}:export")
    store.complete_job(job["id"])
    return {"job_id": job["id"], "item": item, "scope": "item"}


def delete_memory(store: Store, principal_id: str, item_id: str) -> dict[str, Any]:
    if not store.has_grant(principal_id, "org.admin"):
        raise StoreError("denied: scoped delete is founder-only", 403)
    inspect_memory(store, principal_id, item_id)
    now = _now()
    store.conn.execute(
        "UPDATE memory_items SET deleted_at=?, archived_at=COALESCE(archived_at, ?) WHERE id=?",
        (now, now, item_id),
    )
    store.append_audit(principal_id, "memory.delete", "memory", item_id)
    store.flush()
    return {"id": item_id, "deleted": True, "erasure": "not_org_wide"}


def _require_mutate(store: Store, principal_id: str, item_id: str, *, allow_operator: bool) -> None:
    template = seat_template(store, principal_id)
    if template == "operator" and not allow_operator:
        raise StoreError("operator inspect-only", 403)
    if not store.has_grant(principal_id, "memory.write") and not store.has_grant(principal_id, "org.admin"):
        raise StoreError("denied: memory.write", 403)
    inspect_memory(store, principal_id, item_id)
