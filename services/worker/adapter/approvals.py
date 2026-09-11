"""SP-3: Engine Labs API owns the approval record; adapter only forwards."""

from __future__ import annotations

from typing import Any, Callable

from policy_hooks.interception import PolicyError

PersistFn = Callable[[str, dict[str, Any]], dict[str, Any] | None]
ForwardFn = Callable[[str, dict[str, Any]], Any]


def resolve_owned_approval(
    run_id: str,
    decision: dict[str, Any],
    *,
    persist: PersistFn,
    forward: ForwardFn,
) -> dict[str, Any]:
    """Persist the Papership approval first. Never forward if persist fails.

    Hermes `/approval` is transport only (D-04 item 6, D-S1).
    """
    if not (run_id or "").strip():
        raise PolicyError("approval missing run_id")
    record = persist(run_id, decision)
    if not record:
        raise PolicyError("API must own the approval record")
    forwarded = forward(run_id, decision)
    return {"record": record, "forwarded": forwarded}
