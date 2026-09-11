from fastapi.testclient import TestClient

VALID = {
    "event_name": "work.item.created",
    "event_id": "11111111-1111-4111-8111-111111111111",
    "occurred_at": "2026-09-11T04:00:00Z",
    "tenant_id": "tenant-founder",
    "member_pseudonymous_id": "pseudo-1",
    "run_id": None,
    "mode": None,
    "model_band": None,
    "tokens_input": None,
    "tokens_output": None,
    "tokens_cached": None,
    "tool_call_counts_by_class": {},
    "duration_ms": None,
    "estimated_cost_band": None,
    "outcome_code": "success",
    "schema_version": "1",
}


def test_usage_flag_off_emits_zero(
    client: TestClient, founder_headers: dict[str, str]
) -> None:
    posted = client.post("/usage", json=VALID, headers=founder_headers)
    assert posted.status_code == 200
    assert posted.json()["emitted"] is False
    count = client.get("/usage/count", headers=founder_headers)
    assert count.json()["count"] == 0


def test_prohibited_usage_fields(client: TestClient, founder_headers: dict[str, str]) -> None:
    for field in ("prompt", "message", "email", "content", "url", "path", "credential", "token", "name"):
        payload = {**VALID, field: "nope"}
        response = client.post("/usage", json=payload, headers=founder_headers)
        assert response.status_code == 422, field
    assert client.get("/usage/count", headers=founder_headers).json()["count"] == 0
