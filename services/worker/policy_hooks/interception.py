"""Policy owns tool allow/deny. Prompts cannot override (SP-5 / MEM-22)."""

from __future__ import annotations

import hashlib
import json
from typing import Any, Callable

from policy_hooks.catalog import lookup
from policy_hooks.egress import EgressDenied, assert_egress, extract_targets

PersistFn = Callable[[str, dict[str, Any]], dict[str, Any] | None]
POLICY_VERSION = "d17-2026-09-11"


def action_binding_hash(
    name: str,
    arguments: dict[str, Any] | None = None,
    *,
    target_id: str = "",
    target_version: str = "",
    policy_version: str = POLICY_VERSION,
) -> str:
    """AUTH-10: hash of action type, canonical parameters, target, policy version."""
    payload = {
        "action_type": name,
        "parameters": arguments or {},
        "policy_version": policy_version,
        "target_id": target_id,
        "target_version": target_version,
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(canonical.encode()).hexdigest()


def _target_id(args: dict[str, Any]) -> str:
    for key in ("target_id", "path", "url", "to", "repo"):
        value = args.get(key)
        if value:
            return str(value)
    return ""


def _bind_persist(persist: PersistFn, name: str, args: dict[str, Any]) -> dict[str, Any] | None:
    digest = action_binding_hash(
        name,
        args,
        target_id=_target_id(args),
        target_version=str(args.get("target_version") or ""),
    )
    saved = persist(name, args)
    if not saved:
        return None
    echoed = saved.get("auth10")
    if echoed is not None and echoed != digest:
        raise PolicyError("AUTH-10 hash mismatch")
    return {**saved, "auth10": digest}


class PolicyError(Exception):
    """Raised when Papership policy refuses a tool. Never a model refusal."""

    def __init__(self, detail: str) -> None:
        super().__init__(detail)
        self.detail = detail
        self.source = "policy"


def classify_tool(name: str) -> str | None:
    found = lookup(name)
    return found[0] if found else None


def is_side_effecting(name: str) -> bool:
    found = lookup(name)
    return found is not None and found[1] != "read"


def allow_tool(config: dict[str, Any], name: str) -> bool:
    found = lookup(name)
    if found is None:
        return False
    toolset, risk = found
    if risk == "read":
        return True
    if config.get("interception_verified") is not True:
        return False
    spec = (config.get("side_effecting_toolsets") or {}).get(toolset) or {}
    return spec.get("enabled") is True


def intercept_tool_call(
    config: dict[str, Any],
    name: str,
    arguments: dict[str, Any] | None = None,
    prompt: str | None = None,
    *,
    persist_receipt: PersistFn | None = None,
    persist_approval: PersistFn | None = None,
) -> dict[str, Any]:
    """Allow catalogued tools under risk class. Unknown tools are denied.

    `prompt` is ignored: injection text cannot override policy.
    """
    _ = prompt
    args = arguments or {}
    if not allow_tool(config, name):
        raise PolicyError(f"policy refused tool {name!r}")
    found = lookup(name)
    assert found is not None
    _toolset, risk = found
    for target in extract_targets(args):
        try:
            assert_egress(target)
        except EgressDenied as exc:
            raise PolicyError(str(exc)) from exc
    record: dict[str, Any] = {"tool": name, "risk": risk}
    if risk in {"external", "destructive"}:
        if persist_approval is None:
            raise PolicyError("external tool requires an Papership approval record")
        approval = _bind_persist(persist_approval, name, args)
        if not approval:
            raise PolicyError("API must own the approval record")
        record["approval"] = approval
    if risk in {"write", "external", "destructive"}:
        if persist_receipt is None:
            raise PolicyError("write tool requires an Papership receipt")
        saved = _bind_persist(persist_receipt, name, args)
        if not saved:
            raise PolicyError("API must own the tool receipt")
        record["receipt"] = saved
    return record


def tool_call_from_event(event: dict[str, Any] | None) -> tuple[str, dict[str, Any]] | None:
    """Extract a tool name + args from a Hermes SSE/event payload, if present."""
    if not isinstance(event, dict):
        return None
    typ = str(event.get("type") or event.get("event") or event.get("object") or "").lower()
    nested = event.get("item") if isinstance(event.get("item"), dict) else None
    if nested is None and isinstance(event.get("data"), dict):
        nested = event["data"]
    name = event.get("tool") or event.get("name") or event.get("tool_name")
    args = event.get("arguments") or event.get("args") or event.get("input")
    if nested:
        name = name or nested.get("name") or nested.get("tool") or nested.get("tool_name")
        args = args or nested.get("arguments") or nested.get("args") or nested.get("input")
        typ = typ or str(nested.get("type") or nested.get("event") or "").lower()
    if not name:
        return None
    toolish = (
        "tool" in typ
        or "function_call" in typ
        or event.get("tool")
        or (nested or {}).get("type") in {"function_call", "tool_call", "hermes.tool.progress"}
    )
    if not toolish:
        return None
    return str(name), args if isinstance(args, dict) else {}
