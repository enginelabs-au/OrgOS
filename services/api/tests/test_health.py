from fastapi.testclient import TestClient


def test_health_composite(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["db"] == "ok"
    assert body["dbos"] == "ok"
    assert body["worker_config"] == "ok"
    assert body["hermes"] == "not_configured"
    assert body["github"] == "not_configured"
    assert "x-trace-id" in response.headers
