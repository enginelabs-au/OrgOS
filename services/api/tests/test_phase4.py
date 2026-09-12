from app.source_grants import intersect_source_grants, may_live_write


def test_local_session_can_record_oq_g2(client) -> None:
    session = client.post("/auth/local-session")
    assert session.status_code == 200
    token = session.json()["access_token"]
    recorded = client.post("/settings/oq-g2", headers={"Authorization": f"Bearer {token}"})
    assert recorded.status_code == 200
    assert recorded.json()["oq_g2_recorded"] is True


def test_invite_without_oq_g2_is_forbidden(client, founder_headers) -> None:
    response = client.post(
        "/members/invites",
        headers=founder_headers,
        json={"template": "operator"},
    )
    assert response.status_code == 403
    assert "oq_g2" in response.json()["detail"]


def test_measurement_notice_and_second_seat(client, founder_headers) -> None:
    notice = client.get("/settings/measurement", headers=founder_headers)
    assert notice.status_code == 200
    body = notice.json()
    assert body["title"] == "What Papership measures"
    assert body["oq_g2_recorded"] is False
    assert all("price" not in item.lower() for item in body["items"])
    recorded = client.post("/settings/oq-g2", headers=founder_headers)
    assert recorded.status_code == 200
    assert recorded.json()["oq_g2_recorded"] is True
    invited = client.post(
        "/members/invites",
        headers=founder_headers,
        json={"template": "operator", "label": "ops"},
    )
    assert invited.status_code == 200
    assert invited.json()["mail"] == "not_sent"


def test_unpriv_cannot_record_oq_g2(client, unpriv_headers) -> None:
    assert client.post("/settings/oq-g2", headers=unpriv_headers).status_code == 403


def test_guest_refused_until_oq_g2(client, founder_headers) -> None:
    refused = client.post("/guests", headers=founder_headers, json={"scope": "CCO-245"})
    assert refused.status_code == 403
    client.post("/settings/oq-g2", headers=founder_headers)
    created = client.post("/guests", headers=founder_headers, json={"scope": "CCO-245"})
    assert created.status_code == 200
    assert created.json()["template"] == "guest"
    assert created.json()["deny_by_default"] is True
    assert "org.admin" not in created.json()["grants"]


def test_people_inbox_ready_or_empty(client, founder_headers) -> None:
    people = client.get("/people", headers=founder_headers)
    assert people.status_code == 200
    assert people.json()["state"] == "ready"
    assert any(row["id"] == "principal-founder" for row in people.json()["items"])
    inbox = client.get("/inbox", headers=founder_headers)
    assert inbox.status_code == 200
    assert inbox.json()["state"] == "empty"
    assert inbox.json()["items"] == []


def test_org_and_teams(client, founder_headers, unpriv_headers) -> None:
    org = client.get("/organisation", headers=founder_headers)
    assert org.status_code == 200
    assert org.json()["name"]
    teams = client.get("/teams", headers=founder_headers)
    assert teams.status_code == 200
    assert any(row["name"] == "Platform" for row in teams.json()["items"])
    denied = client.post("/teams", headers=unpriv_headers, json={"name": "Ops"})
    assert denied.status_code == 403
    created = client.post("/teams", headers=founder_headers, json={"name": "Governance", "department": "Governance"})
    assert created.status_code == 200
    assert created.json()["name"] == "Governance"


def test_connection_wizard_and_unknown_provider(client, founder_headers) -> None:
    listing = client.get("/connections", headers=founder_headers)
    assert listing.status_code == 200
    ids = {row["id"] for row in listing.json()["items"]}
    assert {"github", "gmail", "slack", "telegram", "whatsapp"} <= ids
    github = next(row for row in listing.json()["items"] if row["id"] == "github")
    assert github["destination_class"] == "source_control"
    gmail = client.post("/connections/gmail/connect", headers=founder_headers)
    assert gmail.status_code == 200
    assert gmail.json()["status"] == "planned"
    assert gmail.json()["enabled"] is False
    unknown = client.post("/connections/unknown/connect", headers=founder_headers)
    assert unknown.status_code == 403


def test_send_needs_approval_and_intersection(client, founder_headers) -> None:
    missing = client.post("/connections/gmail/send", headers=founder_headers, json={})
    assert missing.status_code == 403
    empty = client.post(
        "/connections/gmail/send",
        headers=founder_headers,
        json={"source_perms": {}, "approval_id": "x", "target_id": "gmail"},
    )
    assert empty.status_code == 403
    no_appr = client.post(
        "/connections/gmail/send",
        headers=founder_headers,
        json={"source_perms": {"gmail.send": "write"}},
    )
    assert no_appr.status_code == 403
    assert "approval" in no_appr.json()["detail"]


def test_intersect_fail_closed() -> None:
    grants = {"repo.change", "comms.send", "org.admin"}
    assert intersect_source_grants("github", grants, {}) == set()
    assert may_live_write("github", grants, {}) is False
    assert "repo.change" in intersect_source_grants("github", grants, {"contents": "write", "pull_requests": "write"})
    assert "comms.send" in intersect_source_grants("gmail", grants, {"gmail.send": "write"})
    assert intersect_source_grants("unknown", grants, {"x": "write"}) == set()


def test_github_checkpoint_after_list(client, founder_headers) -> None:
    response = client.get("/github/pulls", headers=founder_headers)
    assert response.status_code == 200
    checkpoint = response.json()["checkpoint"]
    assert checkpoint["provider"] == "github"
    assert checkpoint["last_sync"]
    sync = client.post(
        "/connections/github/sync",
        headers=founder_headers,
        json={"lineage": "pulls", "label": "incremental"},
    )
    assert sync.status_code == 200
    assert sync.json()["label"] == "incremental"


def test_usage_baseline_first_baseline(client, founder_headers) -> None:
    empty = client.get("/usage/baseline", headers=founder_headers)
    assert empty.status_code == 200
    assert empty.json()["label"] == "first-baseline"
    captured = client.post("/usage/baseline", headers=founder_headers)
    assert captured.status_code == 200
    assert captured.json()["label"] == "first-baseline"
    assert captured.json()["event_count"] == 0
    assert captured.json()["task_completion"] == "not_captured"


def test_seat_templates_include_guest(client, founder_headers) -> None:
    response = client.get("/seats/templates", headers=founder_headers)
    ids = {row["id"] for row in response.json()["items"]}
    assert {"founder", "project_lead", "operator", "guest"} <= ids


def test_http_auth12_empty_perms_is_the_publication_path(client, founder_headers) -> None:
    # AUTH-12 lives on POST /github/pulls, not a library bypass.
    planned = client.post(
        "/github/pulls",
        headers=founder_headers,
        json={"title": "Papership", "head": "papership/loop", "dry_run": True, "owner": "enginelabs-au", "repo": "Papership"},
    )
    assert planned.status_code == 200
    assert planned.json()["dry_run"] is True


def test_intersect_route(client, founder_headers) -> None:
    response = client.post(
        "/grants/intersect",
        headers=founder_headers,
        json={"provider": "github", "source_perms": {}},
    )
    assert response.status_code == 200
    assert response.json()["effective"] == []
    assert response.json()["live_write"] is False
