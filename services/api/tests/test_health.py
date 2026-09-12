from fastapi.testclient import TestClient


def test_health_composite(client: TestClient) -> None:
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["db"] == "ok"
    assert body["dbos"] == "ok"
    assert body["worker_config"] == "ok"
    assert body["hermes"] == "not_configured"
    assert body["hermes_pin"] == ""
    assert body["usage_emit"] is False
    assert body["github"] == "not_configured"
    assert "x-trace-id" in response.headers


def test_cors_preflight_allows_localhost_vite(client: TestClient) -> None:
    response = client.options(
        "/connections/gmail/connect",
        headers={
            "Origin": "http://localhost:5173",
            "Access-Control-Request-Method": "POST",
        },
    )
    assert response.status_code in {200, 204}
    assert response.headers.get("access-control-allow-origin") == "http://localhost:5173"
