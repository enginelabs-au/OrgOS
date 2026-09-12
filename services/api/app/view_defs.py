"""AUTH-29 adaptive view definitions: trusted components only, fallback on fail."""

from __future__ import annotations

import json
from typing import Any

from app.store import Store, StoreError, _now

TRUSTED_COMPONENTS = frozenset(
    {
        "today",
        "work",
        "inbox",
        "people",
        "memory",
        "settings",
        "connections",
        "rail",
        "assistant",
        "status",
        "approvals",
        "evidence",
    }
)
FORBIDDEN_KEYS = frozenset(
    {"filesystem", "shell", "database", "credentials", "fs", "exec", "path", "secret"}
)
STABLE_CHROME = ("tabs", "topbar", "rail", "assistant", "evidence", "approvals", "destructive")
FALLBACK: dict[str, Any] = {
    "schema_version": 1,
    "intent": "fallback",
    "regions": [{"id": "main", "component": "today"}],
    "pins": list(STABLE_CHROME),
    "fallback": True,
    "why": "Invalid or untrusted view definition. Showing the fixed seat template.",
}


def _walk_keys(value: Any) -> set[str]:
    keys: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            keys.add(str(key).lower())
            keys.update(_walk_keys(child))
    elif isinstance(value, list):
        for child in value:
            keys.update(_walk_keys(child))
    return keys


def validate_view_definition(doc: Any) -> tuple[dict[str, Any], bool]:
    if not isinstance(doc, dict):
        return dict(FALLBACK), False
    if int(doc.get("schema_version") or 0) != 1:
        return dict(FALLBACK), False
    if _walk_keys(doc) & FORBIDDEN_KEYS:
        return dict(FALLBACK), False
    regions = doc.get("regions")
    if not isinstance(regions, list) or not regions:
        return dict(FALLBACK), False
    for region in regions:
        if not isinstance(region, dict) or region.get("component") not in TRUSTED_COMPONENTS:
            return dict(FALLBACK), False
    out = {
        "schema_version": 1,
        "intent": str(doc.get("intent") or "custom"),
        "regions": [{"id": str(r.get("id") or "main"), "component": r["component"]} for r in regions],
        "pins": [p for p in (doc.get("pins") or list(STABLE_CHROME)) if p in STABLE_CHROME],
        "fallback": False,
        "why": str(doc.get("why") or "Adapted for the current intent."),
    }
    for name in STABLE_CHROME:
        if name not in out["pins"]:
            out["pins"].append(name)
    return out, True


def _state_row(store: Store, principal_id: str) -> dict[str, Any]:
    p = store.principal(principal_id)
    row = store.conn.execute(
        "SELECT * FROM view_states WHERE tenant_id=? AND principal_id=?",
        (p["tenant_id"], principal_id),
    ).fetchone()
    if row:
        return {
            "definition": json.loads(row["definition"]),
            "pins": json.loads(row["pins"] or "[]"),
            "history": json.loads(row["history"] or "[]"),
            "enabled": bool(row["enabled"]),
        }
    return {"definition": dict(FALLBACK), "pins": list(STABLE_CHROME), "history": [], "enabled": False}


def _save_state(store: Store, principal_id: str, state: dict[str, Any]) -> dict[str, Any]:
    p = store.principal(principal_id)
    store.conn.execute(
        """INSERT INTO view_states (tenant_id, principal_id, definition, pins, history, enabled, updated_at)
           VALUES (?, ?, ?, ?, ?, ?, ?)
           ON CONFLICT(tenant_id, principal_id) DO UPDATE SET
             definition=excluded.definition, pins=excluded.pins, history=excluded.history,
             enabled=excluded.enabled, updated_at=excluded.updated_at""",
        (
            p["tenant_id"],
            principal_id,
            json.dumps(state["definition"]),
            json.dumps(state["pins"]),
            json.dumps(state["history"]),
            1 if state["enabled"] else 0,
            _now(),
        ),
    )
    store.flush()
    return state


def personalisation_enabled(store: Store) -> bool:
    return store.get_setting("personalisation.enabled", "0") in {"1", "true", "yes"}


def set_personalisation(store: Store, principal_id: str, enabled: bool) -> dict[str, Any]:
    if not store.has_grant(principal_id, "org.admin"):
        raise StoreError("denied: org.admin", 403)
    store.set_setting("personalisation.enabled", "1" if enabled else "0")
    store.append_audit(principal_id, "personalisation.toggle", "setting", "personalisation.enabled")
    return inspect_personalisation(store, principal_id)


def inspect_personalisation(store: Store, principal_id: str) -> dict[str, Any]:
    state = _state_row(store, principal_id)
    enabled = personalisation_enabled(store)
    return {
        "enabled": enabled,
        "default": False,
        "current": state["definition"] if enabled else dict(FALLBACK),
        "pins": state["pins"],
        "inspect": {
            "intent": state["definition"].get("intent"),
            "fallback": bool(state["definition"].get("fallback")),
            "why": state["definition"].get("why"),
        },
    }


def current_view(store: Store, principal_id: str) -> dict[str, Any]:
    state = _state_row(store, principal_id)
    if not personalisation_enabled(store):
        return {**dict(FALLBACK), "personalisation": False, "stable_chrome": list(STABLE_CHROME)}
    return {**state["definition"], "personalisation": True, "stable_chrome": list(STABLE_CHROME)}


def preview_view(store: Store, principal_id: str, doc: dict[str, Any]) -> dict[str, Any]:
    validated, ok = validate_view_definition(doc)
    return {"candidate": validated, "accepted": ok, "applied": False}


def apply_view(store: Store, principal_id: str, doc: dict[str, Any]) -> dict[str, Any]:
    if not personalisation_enabled(store):
        raise StoreError("personalisation is disabled", 403)
    validated, ok = validate_view_definition(doc)
    state = _state_row(store, principal_id)
    if ok:
        state["history"].append(state["definition"])
        state["definition"] = validated
        state["enabled"] = True
        _save_state(store, principal_id, state)
    return {"definition": validated if ok else dict(FALLBACK), "applied": ok, "fallback": not ok}


def undo_view(store: Store, principal_id: str) -> dict[str, Any]:
    state = _state_row(store, principal_id)
    if state["history"]:
        state["definition"] = state["history"].pop()
        _save_state(store, principal_id, state)
    return current_view(store, principal_id)


def reset_view(store: Store, principal_id: str) -> dict[str, Any]:
    state = {
        "definition": dict(FALLBACK),
        "pins": list(STABLE_CHROME),
        "history": [],
        "enabled": False,
    }
    _save_state(store, principal_id, state)
    return current_view(store, principal_id)


def pin_region(store: Store, principal_id: str, region: str) -> dict[str, Any]:
    if region not in STABLE_CHROME and region not in TRUSTED_COMPONENTS:
        raise StoreError("unknown pin region", 400)
    state = _state_row(store, principal_id)
    if region not in state["pins"]:
        state["pins"].append(region)
    _save_state(store, principal_id, state)
    return {"pins": state["pins"]}
