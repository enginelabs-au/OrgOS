"""UsageEvent emit behind ENGINE_USAGE_EMIT (default off)."""

from __future__ import annotations

import re
from typing import Any

from app.store import Store, StoreError

PROHIBITED_USAGE_FIELDS = {
    "prompt",
    "message",
    "email",
    "content",
    "url",
    "path",
    "credential",
    "token",
    "name",
}

REQUIRED_USAGE_FIELDS = {
    "event_name",
    "event_id",
    "occurred_at",
    "tenant_id",
    "member_pseudonymous_id",
    "run_id",
    "mode",
    "model_band",
    "tokens_input",
    "tokens_output",
    "tokens_cached",
    "tool_call_counts_by_class",
    "duration_ms",
    "estimated_cost_band",
    "outcome_code",
    "schema_version",
}


def _collect_prohibited(value: Any, prefix: str = "") -> list[str]:
    if not isinstance(value, dict):
        return []
    found: list[str] = []
    for key, child in value.items():
        path = f"{prefix}.{key}" if prefix else key
        if key.lower() in PROHIBITED_USAGE_FIELDS:
            found.append(path)
        found.extend(_collect_prohibited(child, path))
    return found


def validate_usage_event(payload: dict[str, Any]) -> None:
    missing = [field for field in REQUIRED_USAGE_FIELDS if field not in payload]
    if missing:
        raise StoreError(f"usage missing fields: {missing}", 422)
    if not re.match(r"^[a-z]+\.[a-z0-9_]+\.[a-z0-9_]+$", str(payload["event_name"])):
        raise StoreError("invalid event_name", 422)
    prohibited = _collect_prohibited(payload)
    if prohibited:
        raise StoreError(f"prohibited UsageEvent field: {', '.join(prohibited)}", 422)


def emit_usage(store: Store, enabled: bool, payload: dict[str, Any]) -> str | None:
    validate_usage_event(payload)
    if not enabled:
        return None
    return store.insert_usage(payload)
