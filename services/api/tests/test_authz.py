from datetime import datetime, timezone

from fastapi.testclient import TestClient

from tests.conftest import make_token

SURFACES = [
    ("GET", "/records"),
    ("GET", "/search?q=x"),
    ("GET", "/aggregates"),
    ("POST", "/attachments"),
    ("GET", "/notifications"),
    ("GET", "/memory"),
]


def test_unprivileged_denied_on_five_surfaces(
    client: TestClient, unpriv_headers: dict[str, str]
) -> None:
    denied = 0
    for method, path in SURFACES[:5]:
        if method == "GET":
            response = client.get(path, headers=unpriv_headers)
        else:
            response = client.post(path, json={"label": "x"}, headers=unpriv_headers)
        assert response.status_code == 403, path
        denied += 1
    assert denied == 5
    memory = client.get("/memory", headers=unpriv_headers)
    assert memory.status_code == 403


def test_founder_can_use_surfaces(
    client: TestClient, founder_headers: dict[str, str]
) -> None:
    assert client.get("/records", headers=founder_headers).status_code == 200
    assert client.get("/search?q=x", headers=founder_headers).status_code == 200
    assert client.get("/aggregates", headers=founder_headers).status_code == 200
    created = client.post("/attachments", json={"label": "doc"}, headers=founder_headers)
    assert created.status_code == 200
    assert created.json()["ttl_seconds"] == 300
    signed = created.json()["signed_url"]
    fetched = client.get(signed, headers=founder_headers)
    assert fetched.status_code == 200
    expired = client.get(
        signed.split("?")[0] + "?expires=1&sig=deadbeef",
        headers=founder_headers,
    )
    assert expired.status_code == 403
    assert client.get("/notifications", headers=founder_headers).status_code == 200
    assert client.get("/memory", headers=founder_headers).status_code == 200


def test_entitlement_is_not_permission(
    client: TestClient, founder_headers: dict[str, str], unpriv_headers: dict[str, str]
) -> None:
    granted = client.post(
        "/entitlements",
        json={"principal_id": "principal-unpriv", "feature": "records"},
        headers=founder_headers,
    )
    assert granted.status_code == 200
    still_denied = client.get("/records", headers=unpriv_headers)
    assert still_denied.status_code == 403


def test_self_approval_refused(client: TestClient, founder_headers: dict[str, str]) -> None:
    response = client.post(
        "/approvals",
        json={
            "approval_class": "approval.release",
            "requester_id": "principal-founder",
            "target_id": "rel-1",
        },
        headers=founder_headers,
    )
    assert response.status_code == 403
    assert "self-approval" in response.json()["detail"]


def test_effective_grants_are_intersection(
    client: TestClient, founder_headers: dict[str, str]
) -> None:
    response = client.post(
        "/grants/effective",
        json={
            "sponsor": ["ledger.read", "run.start", "org.admin"],
            "toolset": ["ledger.read", "run.start"],
            "mode": ["run.start"],
        },
        headers=founder_headers,
    )
    assert response.status_code == 200
    assert response.json()["effective"] == ["run.start"]


def test_reauth_required_for_destructive(client: TestClient, founder_headers: dict[str, str]) -> None:
    denied = client.post("/admin/destructive", headers=founder_headers)
    assert denied.status_code == 401
    token = make_token(
        "principal-founder",
        extra={"reauth_at": datetime.now(timezone.utc).timestamp()},
    )
    ok = client.post("/admin/destructive", headers={"Authorization": f"Bearer {token}"})
    assert ok.status_code == 200
