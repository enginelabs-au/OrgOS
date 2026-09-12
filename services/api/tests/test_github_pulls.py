from datetime import datetime, timezone

from fastapi.testclient import TestClient

from app.main import create_app
from tests.conftest import make_token


def test_list_pulls_not_configured(client: TestClient, founder_headers: dict[str, str]) -> None:
    response = client.get("/github/pulls", headers=founder_headers)
    assert response.status_code == 200
    assert response.json()["status"] == "not_configured"
    assert response.json()["items"] == []


def test_plan_pull_founder(client: TestClient, founder_headers: dict[str, str]) -> None:
    response = client.post(
        "/github/pulls",
        headers=founder_headers,
        json={
            "title": "Papership loop receipt",
            "body": "Planned only",
            "head": "papership/loop-demo",
            "owner": "enginelabs-au",
            "repo": "papership",
            "dry_run": True,
        },
    )
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "planned"
    assert body["dry_run"] is True
    assert body["planned"]["head"] == "papership/loop-demo"


def test_plan_pull_unpriv_denied(client: TestClient, unpriv_headers: dict[str, str]) -> None:
    response = client.post(
        "/github/pulls",
        headers=unpriv_headers,
        json={"title": "x", "head": "y", "dry_run": True, "owner": "o", "repo": "r"},
    )
    assert response.status_code == 403


def test_live_open_requires_reauth(client: TestClient, founder_headers: dict[str, str]) -> None:
    response = client.post(
        "/github/pulls",
        headers=founder_headers,
        json={
            "title": "live",
            "head": "papership/live",
            "owner": "enginelabs-au",
            "repo": "papership",
            "dry_run": False,
        },
    )
    assert response.status_code == 401


def test_live_open_refuses_empty_installation_perms(env_jwt: None, tmp_path, monkeypatch) -> None:
    monkeypatch.setenv("GITHUB_APP_ID", "123")
    monkeypatch.setenv("GITHUB_APP_INSTALLATION_ID", "456")
    key = tmp_path / "app.pem"
    key.write_text("not-a-real-key")
    monkeypatch.setenv("GITHUB_APP_PRIVATE_KEY_PATH", str(key))
    monkeypatch.setattr("app.main.installation_permissions", lambda *_a, **_k: {})
    app = create_app(str(tmp_path / "store.sqlite"))
    client = TestClient(app)
    headers = {
        "Authorization": (
            f"Bearer {make_token('principal-founder', extra={'reauth_at': datetime.now(timezone.utc).timestamp()})}"
        )
    }
    response = client.post(
        "/github/pulls",
        headers=headers,
        json={
            "title": "live",
            "head": "papership/live",
            "owner": "enginelabs-au",
            "repo": "papership",
            "dry_run": False,
        },
    )
    assert response.status_code == 403
    assert "empty" in response.json()["detail"]


def test_live_open_with_reauth_still_needs_app(client: TestClient) -> None:
    headers = {
        "Authorization": (
            f"Bearer {make_token('principal-founder', extra={'reauth_at': datetime.now(timezone.utc).timestamp()})}"
        )
    }
    response = client.post(
        "/github/pulls",
        headers=headers,
        json={
            "title": "live",
            "head": "papership/live",
            "owner": "enginelabs-au",
            "repo": "papership",
            "dry_run": False,
        },
    )
    assert response.status_code == 503
