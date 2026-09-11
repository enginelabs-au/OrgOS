from fastapi.testclient import TestClient


def test_ledger_create_priority_plan_assignment(
    client: TestClient, founder_headers: dict[str, str]
) -> None:
    priority = client.post("/priorities", json={"title": "Ship foundation"}, headers=founder_headers)
    assert priority.status_code == 200
    plan = client.post(
        "/plans",
        json={"title": "Phase 1", "priority_id": priority.json()["id"]},
        headers=founder_headers,
    )
    assert plan.status_code == 200
    item = client.post(
        "/work-items",
        json={"title": "API", "plan_id": plan.json()["id"]},
        headers=founder_headers,
    )
    assert item.status_code == 200
    assignment = client.post(
        "/assignments",
        json={"work_item_id": item.json()["id"], "principal_id": "principal-founder"},
        headers=founder_headers,
    )
    assert assignment.status_code == 200
    dep_item = client.post("/work-items", json={"title": "Worker"}, headers=founder_headers)
    dep = client.post(
        "/dependencies",
        json={"from_work_item_id": item.json()["id"], "to_work_item_id": dep_item.json()["id"]},
        headers=founder_headers,
    )
    assert dep.status_code == 200
    ref = client.post(
        "/source-references",
        json={"provider": "github", "installation_pointer": "org/repo"},
        headers=founder_headers,
    )
    assert ref.status_code == 200
    listed = client.get("/work-items", headers=founder_headers)
    assert len(listed.json()["items"]) == 2
