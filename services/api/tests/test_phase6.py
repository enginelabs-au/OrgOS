from fastapi.testclient import TestClient


def test_allowance_is_not_permission(
    client: TestClient, founder_headers: dict[str, str], unpriv_headers: dict[str, str]
) -> None:
    granted = client.post(
        "/allowances",
        json={
            "principal_id": "principal-unpriv",
            "feature": "records",
            "band": "standard",
            "plan_label": "professional",
        },
        headers=founder_headers,
    )
    assert granted.status_code == 200
    body = granted.json()
    assert body["band"] == "standard"
    assert body["plan_label"] == "professional"
    assert "184640" not in str(body)
    assert "$" not in str(body)
    still_denied = client.get("/records", headers=unpriv_headers)
    assert still_denied.status_code == 403


def test_unpriv_cannot_create_allowance(client: TestClient, unpriv_headers: dict[str, str]) -> None:
    response = client.post(
        "/allowances",
        json={"principal_id": "principal-unpriv", "feature": "x", "band": "low", "plan_label": "free"},
        headers=unpriv_headers,
    )
    assert response.status_code == 403


def test_unknown_band_rejected(client: TestClient, founder_headers: dict[str, str]) -> None:
    response = client.post(
        "/allowances",
        json={"principal_id": "principal-founder", "feature": "x", "band": "unlimited", "plan_label": "free"},
        headers=founder_headers,
    )
    assert response.status_code == 400


def test_reserve_reconcile_and_duplicate(
    client: TestClient, founder_headers: dict[str, str]
) -> None:
    created = client.post(
        "/allowances",
        json={"principal_id": "principal-founder", "feature": "runs", "band": "low", "plan_label": "basic"},
        headers=founder_headers,
    )
    assert created.status_code == 200
    first = client.post("/allowances/reserve", json={"feature": "runs"}, headers=founder_headers)
    assert first.status_code == 200
    assert first.json()["status"] == "reserved"
    dup = client.post("/allowances/reserve", json={"feature": "runs"}, headers=founder_headers)
    assert dup.status_code == 409
    rec = client.post(
        "/allowances/reconcile",
        json={"reservation_id": first.json()["id"]},
        headers=founder_headers,
    )
    assert rec.status_code == 200
    assert rec.json()["status"] == "reconciled"


def test_exhausted_band_pauses_new_work(client: TestClient, founder_headers: dict[str, str]) -> None:
    client.post(
        "/allowances",
        json={"principal_id": "principal-founder", "feature": "dispatch", "band": "exhausted", "plan_label": "free"},
        headers=founder_headers,
    )
    paused = client.post("/allowances/reserve", json={"feature": "dispatch"}, headers=founder_headers)
    assert paused.status_code == 403
    assert "exports" in paused.json()["detail"]
    assert client.get("/records", headers=founder_headers).status_code == 200


def test_charge_route_stays_disabled(client: TestClient, founder_headers: dict[str, str]) -> None:
    response = client.post("/billing/charge", json={"amount": 1}, headers=founder_headers)
    assert response.status_code == 403
    mine = client.get("/allowances/me", headers=founder_headers)
    assert mine.status_code == 200
    assert mine.json()["charges_enabled"] is False


def test_rate_card_is_unpublished(client: TestClient, founder_headers: dict[str, str]) -> None:
    response = client.get("/billing/rate-card", headers=founder_headers)
    assert response.status_code == 200
    body = response.json()
    assert body["published"] is False
    assert body["entries"] == []
    assert "$" not in str(body)


def test_licenses_hook_identifiers_only(client: TestClient, founder_headers: dict[str, str]) -> None:
    response = client.get("/licenses", headers=founder_headers)
    assert response.status_code == 200
    body = response.json()
    assert body["license_present"] is True
    assert body["notice_present"] is True
    assert body["charges_enabled"] is False
    assert "LICENSE" in body["identifiers"]
    assert "$" not in str(body)
