from fastapi.testclient import TestClient

from app.store import CAPABILITY_IDS


def test_registry_returns_43_rows(client: TestClient, founder_headers: dict[str, str]) -> None:
    response = client.get("/registry", headers=founder_headers)
    assert response.status_code == 200
    body = response.json()
    assert body["count"] == 43
    ids = [row["capability_id"] for row in body["items"]]
    assert ids == CAPABILITY_IDS
    assert body["hermes_side_effecting_tools"] == "catalogued"
    for row in body["items"]:
        if row.get("hermes_side_effecting_tool"):
            assert row["implementation_status"] == "unavailable"
