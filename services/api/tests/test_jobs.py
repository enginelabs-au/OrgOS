from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.main import create_app
from app.store import Store
from tests.conftest import make_token


def test_persist_before_202(env_jwt, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("ENGINE_TEST_CRASH_AFTER_PERSIST", "1")
    store_path = str(tmp_path / "crash.sqlite")
    app = create_app(store_path)
    client = TestClient(app, raise_server_exceptions=True)
    headers = {"Authorization": f"Bearer {make_token('principal-founder')}"}
    with pytest.raises(RuntimeError, match="crash after persist"):
        client.post("/jobs", json={"purpose": "dev.long_step"}, headers=headers)
    reopened = Store(store_path)
    count = reopened.conn.execute("SELECT COUNT(*) AS c FROM jobs").fetchone()["c"]
    assert count == 1
    reopened.close()


def test_job_202_and_run_nine_fields(
    client: TestClient, founder_headers: dict[str, str]
) -> None:
    response = client.post("/jobs", json={"purpose": "dev.long_step"}, headers=founder_headers)
    assert response.status_code == 202
    body = response.json()
    run = body["run"]
    for field in (
        "sponsor",
        "acting_identity",
        "purpose",
        "scope",
        "policy_version",
        "model_configuration",
        "budget",
        "deadline",
        "accountable_owner",
    ):
        assert run[field], field
    assert run["model_configuration"] == "none"


def test_sse_resume(client: TestClient, founder_headers: dict[str, str]) -> None:
    created = client.post("/jobs", json={"purpose": "dev.long_step"}, headers=founder_headers)
    job_id = created.json()["id"]
    first = client.get(f"/jobs/{job_id}/events", headers=founder_headers)
    assert first.status_code == 200
    assert "id:" in first.text
    resumed = client.get(f"/jobs/{job_id}/events?last_event_id=1", headers=founder_headers)
    assert resumed.status_code == 200
    assert "id: 1\n" not in resumed.text
    assert "id:" in resumed.text


def test_cancel_vs_disconnect(client: TestClient, founder_headers: dict[str, str]) -> None:
    created = client.post("/jobs", json={"purpose": "held"}, headers=founder_headers)
    job_id = created.json()["id"]
    stream = client.get(f"/jobs/{job_id}/events", headers=founder_headers)
    assert stream.status_code == 200
    after_disconnect = client.get(f"/jobs/{job_id}", headers=founder_headers)
    assert after_disconnect.json()["status"] != "cancelled"
    cancelled = client.post(f"/jobs/{job_id}/cancel", headers=founder_headers)
    assert cancelled.status_code == 200
    assert cancelled.json()["status"] == "cancelled"
    assert client.get(f"/jobs/{job_id}", headers=founder_headers).json()["status"] == "cancelled"


def test_step_idempotency_receipt(client: TestClient, founder_headers: dict[str, str]) -> None:
    created = client.post("/jobs", json={"purpose": "held"}, headers=founder_headers)
    job_id = created.json()["id"]
    first = client.post(
        f"/jobs/{job_id}/steps",
        json={"step_name": "a", "idempotency_key": "key-a"},
        headers=founder_headers,
    )
    second = client.post(
        f"/jobs/{job_id}/steps",
        json={"step_name": "a", "idempotency_key": "key-a"},
        headers=founder_headers,
    )
    assert first.status_code == 200
    assert first.json()["id"] == second.json()["id"]
