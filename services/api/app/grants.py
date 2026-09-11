"""Grant rules: agents cannot hold approval.*; self-approval refused; intersection."""

from __future__ import annotations

from app.store import SELF_APPROVAL_REFUSED, Store, StoreError, effective_grants

__all__ = [
    "SELF_APPROVAL_REFUSED",
    "StoreError",
    "effective_grants",
    "assert_agent_cannot_hold_approval",
    "assert_not_self_approval",
]


def assert_agent_cannot_hold_approval(store: Store, principal_id: str, grant_class: str) -> None:
    store.add_grant(principal_id, grant_class, store.principal(principal_id)["tenant_id"])


def assert_not_self_approval(requester_id: str, decider_id: str, approval_class: str) -> None:
    normalized = approval_class if approval_class.startswith("approval.") else f"approval.{approval_class}"
    if normalized in SELF_APPROVAL_REFUSED and requester_id == decider_id:
        raise StoreError("self-approval refused", 403)
