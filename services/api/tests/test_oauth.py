from urllib.parse import parse_qs, urlparse

from fastapi.testclient import TestClient

from app.main import create_app


def _oauth_client(monkeypatch, tmp_path, *, secret: bool = True) -> TestClient:
    monkeypatch.setenv("SUPABASE_JWT_SECRET", "test-only-not-for-production-jwt-secret-0001")
    monkeypatch.setenv("ENGINE_JWT_ISSUER", "http://engine.test/auth/v1")
    monkeypatch.setenv("ENGINE_JWT_AUDIENCE", "authenticated")
    monkeypatch.setenv("ENGINE_TEST_HOOKS", "1")
    monkeypatch.setenv("ENGINE_API_CORS_ORIGINS", "http://127.0.0.1:5173")
    monkeypatch.setenv("GMAIL_OAUTH_CLIENT_ID", "gmail-public-client-id")
    monkeypatch.setenv("GMAIL_OAUTH_REDIRECT_URL", "http://127.0.0.1:8000/oauth/gmail/callback")
    monkeypatch.setenv("SLACK_CLIENT_ID", "slack-public-client-id")
    monkeypatch.setenv("SLACK_OAUTH_REDIRECT_URL", "http://localhost:8000/oauth/slack/callback")
    if secret:
        monkeypatch.setenv("GMAIL_OAUTH_CLIENT_SECRET", "gmail-test-secret")
        monkeypatch.setenv("SLACK_CLIENT_SECRET", "slack-test-secret")
    else:
        monkeypatch.delenv("GMAIL_OAUTH_CLIENT_SECRET", raising=False)
        monkeypatch.delenv("SLACK_CLIENT_SECRET", raising=False)
    return TestClient(create_app(str(tmp_path / "oauth.sqlite")))


def test_gmail_connect_stays_planned_without_client_id(client, founder_headers) -> None:
    response = client.post("/connections/gmail/connect", headers=founder_headers)
    assert response.status_code == 200
    assert response.json()["status"] == "planned"
    assert response.json()["enabled"] is False
    assert "authorize_url" not in response.json()


def test_connect_without_secret_is_conflict(monkeypatch, tmp_path, founder_headers) -> None:
    client = _oauth_client(monkeypatch, tmp_path, secret=False)
    response = client.post("/connections/gmail/connect", headers=founder_headers)
    assert response.status_code == 409
    assert "GMAIL_OAUTH_CLIENT_SECRET" in response.json()["detail"]
    assert "gmail-test-secret" not in str(response.json())


def test_start_and_callback_store_token_without_leaking(monkeypatch, tmp_path, founder_headers) -> None:
    client = _oauth_client(monkeypatch, tmp_path)
    leaked = "secret-access-token-do-not-leak"

    def fake_exchange(settings, provider, code):
        assert provider == "gmail"
        assert code == "one-time-code"
        return {
            "provider": "gmail",
            "access_token": leaked,
            "refresh_token": "secret-refresh",
            "token_type": "Bearer",
            "scope": "gmail.readonly",
            "expires_in": 3600,
        }

    monkeypatch.setattr("app.oauth.exchange_code", fake_exchange)
    started = client.post("/connections/gmail/connect", headers=founder_headers)
    assert started.status_code == 200
    body = started.json()
    assert body["status"] == "pending_oauth"
    assert "accounts.google.com" in body["authorize_url"]
    assert "gmail-public-client-id" in body["authorize_url"]
    assert "include_granted_scopes=false" in body["authorize_url"]
    assert "gmail-test-secret" not in body["authorize_url"]
    state = parse_qs(urlparse(body["authorize_url"]).query)["state"][0]
    callback = client.get(
        "/oauth/gmail/callback",
        params={"code": "one-time-code", "state": state},
        follow_redirects=False,
    )
    assert callback.status_code == 302
    location = callback.headers["location"]
    assert "oauth=gmail" in location
    assert "result=ok" in location
    assert leaked not in location
    listing = client.get("/connections", headers=founder_headers)
    dumped = listing.text
    assert leaked not in dumped
    assert "secret-refresh" not in dumped
    assert "gmail-test-secret" not in dumped
    gmail = next(row for row in listing.json()["items"] if row["id"] == "gmail")
    assert gmail["status"] == "configured"
    assert gmail["enabled"] is True
    assert gmail["has_token"] is True
    assert "token_blob" not in gmail
    replay = client.get(
        "/oauth/gmail/callback",
        params={"code": "one-time-code", "state": state},
        follow_redirects=False,
    )
    assert replay.status_code == 302
    assert "result=error" in replay.headers["location"]
    assert "invalid_state" in replay.headers["location"]


def test_slack_start_url(monkeypatch, tmp_path, founder_headers) -> None:
    client = _oauth_client(monkeypatch, tmp_path)
    started = client.post("/connections/slack/connect", headers=founder_headers)
    assert started.status_code == 200
    url = started.json()["authorize_url"]
    assert "slack.com/oauth/v2/authorize" in url
    assert "channels%3Aread" in url
    assert "slack-test-secret" not in url


def test_unpriv_cannot_start_oauth(monkeypatch, tmp_path, unpriv_headers) -> None:
    client = _oauth_client(monkeypatch, tmp_path)
    assert client.post("/connections/gmail/connect", headers=unpriv_headers).status_code == 403


def test_frontend_redirect_prefers_vite(monkeypatch) -> None:
    monkeypatch.setenv("SUPABASE_JWT_SECRET", "test-only-not-for-production-jwt-secret-0001")
    monkeypatch.setenv("ENGINE_API_CORS_ORIGINS", "http://127.0.0.1:4173,http://127.0.0.1:5173,http://localhost:5173")
    from app.config import load_settings
    from app.oauth import frontend_redirect

    url = frontend_redirect(load_settings(), "gmail", "ok")
    assert url.startswith("http://localhost:5173/papership?")
    assert "oauth=gmail" in url
    assert "tab=integrations" in url


def test_public_settings_do_not_include_secrets(monkeypatch) -> None:
    monkeypatch.setenv("GMAIL_OAUTH_CLIENT_SECRET", "should-never-be-public")
    monkeypatch.setenv("SLACK_CLIENT_SECRET", "should-never-be-public")
    monkeypatch.setenv("GMAIL_OAUTH_CLIENT_ID", "public-id")
    monkeypatch.setenv("SLACK_CLIENT_ID", "public-slack")
    from app.config import load_settings, settings_public_dict

    dumped = str(settings_public_dict(load_settings()))
    assert "should-never-be-public" not in dumped
    assert "has_gmail_oauth_secret" in dumped
