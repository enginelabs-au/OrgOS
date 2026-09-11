from adapter.approvals import resolve_owned_approval
from policy_hooks.interception import PolicyError


def test_never_forward_if_api_does_not_persist() -> None:
    forwarded: list[str] = []

    def persist(_run_id: str, _decision: dict) -> None:
        return None

    def forward(run_id: str, _decision: dict) -> str:
        forwarded.append(run_id)
        return "ok"

    try:
        resolve_owned_approval("run-1", {"choice": "deny"}, persist=persist, forward=forward)
    except PolicyError as exc:
        assert "own the approval" in exc.detail
    else:
        raise AssertionError("expected PolicyError")
    assert forwarded == []


def test_forward_only_after_api_record() -> None:
    def persist(run_id: str, decision: dict) -> dict:
        return {"id": "approval-1", "run_id": run_id, "decision": decision}

    def forward(run_id: str, decision: dict) -> dict:
        return {"hermes": "accepted", "run_id": run_id, "choice": decision["choice"]}

    result = resolve_owned_approval("run-9", {"choice": "deny"}, persist=persist, forward=forward)
    assert result["record"]["id"] == "approval-1"
    assert result["forwarded"]["hermes"] == "accepted"


def test_hermes_stays_pending_if_never_forwarded() -> None:
    hermes_state = {"status": "waiting_approval"}

    def persist(run_id: str, decision: dict) -> dict:
        return {"id": "a", "run_id": run_id, "decision": decision}

    def no_forward(_run_id: str, _decision: dict) -> None:
        return None

    resolve_owned_approval("run-2", {"choice": "once"}, persist=persist, forward=no_forward)
    assert hermes_state["status"] == "waiting_approval"
