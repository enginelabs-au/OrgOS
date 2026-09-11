from tests.conftest import make_token


def test_seat_templates_list_three(client, founder_headers) -> None:
    response = client.get("/seats/templates", headers=founder_headers)
    assert response.status_code == 200
    ids = {row["id"] for row in response.json()["items"]}
    assert ids == {"founder", "project_lead", "operator"}
    founder = next(row for row in response.json()["items"] if row["id"] == "founder")
    assert "org.admin" in founder["grants"]
    operator = next(row for row in response.json()["items"] if row["id"] == "operator")
    assert "org.admin" not in operator["grants"]


def test_unpriv_cannot_invite(client, unpriv_headers) -> None:
    response = client.post("/members/invites", headers=unpriv_headers, json={"template": "operator"})
    assert response.status_code == 403


def test_founder_invite_operator_has_no_admin(client, founder_headers) -> None:
    created = client.post(
        "/members/invites",
        headers=founder_headers,
        json={"template": "operator", "label": "ops"},
    )
    assert created.status_code == 200
    body = created.json()
    assert body["mail"] == "not_sent"
    assert body["template"] == "operator"
    assert "org.admin" not in body["grants"]
    invited = {"Authorization": f"Bearer {make_token(body['principal_id'])}"}
    denied = client.post(
        "/grants",
        headers=invited,
        json={"principal_id": "principal-unpriv", "grant_class": "org.admin"},
    )
    assert denied.status_code == 403


def test_founder_invite_cannot_be_founder_template(client, founder_headers) -> None:
    response = client.post("/members/invites", headers=founder_headers, json={"template": "founder"})
    assert response.status_code == 400


def test_project_lead_cannot_grant_beyond_template(client, founder_headers) -> None:
    created = client.post(
        "/members/invites",
        headers=founder_headers,
        json={"template": "project_lead"},
    )
    assert created.status_code == 200
    assert "org.admin" not in created.json()["grants"]
    assert "ledger.write" in created.json()["grants"]
    invited = {"Authorization": f"Bearer {make_token(created.json()['principal_id'])}"}
    denied = client.post(
        "/members/invites",
        headers=invited,
        json={"template": "operator"},
    )
    assert denied.status_code == 403
