from app.loop import LOOP_STAGES
from fastapi.testclient import TestClient


def test_loop_stages_forward_only(client: TestClient, founder_headers: dict[str, str]) -> None:
    item = client.post("/work-items", json={"title": "Loop demo"}, headers=founder_headers)
    assert item.status_code == 200
    wid = item.json()["id"]
    assert item.json()["stage"] == "request"
    research = client.post(
        f"/work-items/{wid}/stage",
        json={"stage": "research", "evidence": "notes"},
        headers=founder_headers,
    )
    assert research.status_code == 200
    assert research.json()["stage"] == "research"
    back = client.post(
        f"/work-items/{wid}/stage",
        json={"stage": "request"},
        headers=founder_headers,
    )
    assert back.status_code == 400
    isolated = client.post(
        f"/work-items/{wid}/stage",
        json={"stage": "isolated_change", "evidence": "papership/loop-demo"},
        headers=founder_headers,
    )
    assert isolated.status_code == 200
    assert isolated.json()["stage"] == "isolated_change"
    detail = client.get(f"/work-items/{wid}", headers=founder_headers)
    assert len(detail.json()["loop"]) >= 2


def test_r1_acc6_walks_all_loop_stages(client: TestClient, founder_headers: dict[str, str]) -> None:
    item = client.post(
        "/work-items",
        json={"title": "R1-ACC-6 loop receipt"},
        headers=founder_headers,
    )
    assert item.status_code == 200
    wid = item.json()["id"]
    for stage in LOOP_STAGES[1:]:
        response = client.post(
            f"/work-items/{wid}/stage",
            json={"stage": stage, "evidence": f"t3-4:{stage}"},
            headers=founder_headers,
        )
        assert response.status_code == 200, stage
        assert response.json()["stage"] == stage
    planned = client.post(
        "/github/pulls",
        headers=founder_headers,
        json={
            "title": "R1-ACC-6 release proposal only",
            "body": "Dry-run receipt. Do not execute_release.",
            "head": "papership/r1-acc6-loop",
            "owner": "enginelabs-au",
            "repo": "papership",
            "dry_run": True,
        },
    )
    assert planned.status_code == 200
    assert planned.json()["dry_run"] is True
    first = client.post("/runs", json={"purpose": "acc6", "idempotency_key": "acc6:start"}, headers=founder_headers)
    second = client.post("/runs", json={"purpose": "acc6", "idempotency_key": "acc6:start"}, headers=founder_headers)
    assert first.status_code == 202
    assert second.status_code == 202
    assert first.json()["job"]["id"] != ""
    detail = client.get(f"/work-items/{wid}", headers=founder_headers)
    assert detail.json()["stage"] == "retained_knowledge"
    assert [row["stage"] for row in detail.json()["loop"]] == list(LOOP_STAGES[1:])


def test_unpriv_cannot_advance(client: TestClient, unpriv_headers: dict[str, str], founder_headers: dict[str, str]) -> None:
    item = client.post("/work-items", json={"title": "Secret"}, headers=founder_headers)
    denied = client.post(
        f"/work-items/{item.json()['id']}/stage",
        json={"stage": "research"},
        headers=unpriv_headers,
    )
    assert denied.status_code == 403
