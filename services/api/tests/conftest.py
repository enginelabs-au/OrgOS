from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

import jwt
import pytest
from fastapi.testclient import TestClient

from app.config import TEST_JWT_SECRET_VALUE
from app.main import create_app

ISSUER = "http://engine.test/auth/v1"
AUDIENCE = "authenticated"


@pytest.fixture
def env_jwt(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("SUPABASE_JWT_SECRET", TEST_JWT_SECRET_VALUE)
    monkeypatch.setenv("ENGINE_JWT_ISSUER", ISSUER)
    monkeypatch.setenv("ENGINE_JWT_AUDIENCE", AUDIENCE)
    monkeypatch.setenv("ENGINE_USAGE_EMIT", "0")
    monkeypatch.setenv("ENGINE_TEST_HOOKS", "1")
    monkeypatch.delenv("HERMES_API_BASE_URL", raising=False)
    monkeypatch.delenv("GITHUB_APP_ID", raising=False)
    monkeypatch.delenv("GITHUB_APP_INSTALLATION_ID", raising=False)
    monkeypatch.delenv("GITHUB_APP_PRIVATE_KEY", raising=False)
    monkeypatch.delenv("GITHUB_APP_PRIVATE_KEY_PATH", raising=False)


def make_token(
    sub: str,
    *,
    grant_version: int = 1,
    lifetime_minutes: int = 15,
    extra: dict | None = None,
) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": sub,
        "iss": ISSUER,
        "aud": AUDIENCE,
        "iat": int(now.timestamp()),
        "exp": int((now + timedelta(minutes=lifetime_minutes)).timestamp()),
        "role": "authenticated",
        "grant_version": grant_version,
        "aal": "aal2",
    }
    if extra:
        payload.update(extra)
    return jwt.encode(payload, TEST_JWT_SECRET_VALUE, algorithm="HS256")


@pytest.fixture
def client(env_jwt: None, tmp_path: Path) -> TestClient:
    app = create_app(str(tmp_path / "store.sqlite"))
    return TestClient(app)


@pytest.fixture
def founder_headers() -> dict[str, str]:
    return {"Authorization": f"Bearer {make_token('principal-founder')}"}


@pytest.fixture
def unpriv_headers() -> dict[str, str]:
    return {"Authorization": f"Bearer {make_token('principal-unpriv')}"}
