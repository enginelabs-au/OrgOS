import os

from app.config import PHASE2_ENV_NAMES, load_settings, settings_public_dict


def test_phase2_env_names_are_not_read(monkeypatch) -> None:
    marker = "should-never-be-read-by-phase1"
    monkeypatch.setenv("HERMES_API_SERVER_KEY", marker)
    monkeypatch.setenv("HERMES_API_BASE_URL", "http://127.0.0.1:9119")
    monkeypatch.setenv("HERMES_VERSION_PIN", "v0.21.1")
    monkeypatch.setenv("MODEL_PROVIDER_API_KEY", marker)
    monkeypatch.setenv("GITHUB_APP_ID", "4908453")
    monkeypatch.setenv("GITHUB_APP_PRIVATE_KEY", "/tmp/orgos-github-app.pem")
    monkeypatch.setenv("GITHUB_APP_INSTALLATION_ID", "160851156")
    monkeypatch.setenv("GITHUB_APP_OWNER", "enginelabs-au")
    monkeypatch.setenv("GITHUB_APP_REPO", "Papership")
    monkeypatch.setenv("GITHUB_APP_WEBHOOK_SECRET", marker)
    monkeypatch.setenv("SUPABASE_JWT_SECRET", "test-only-not-for-production-jwt-secret-0001")
    settings = load_settings()
    dumped = str(settings_public_dict(settings)) + str(settings)
    assert settings.hermes_api_base_url == "http://127.0.0.1:9119"
    assert settings.hermes_version_pin == "v0.21.1"
    assert settings.github_app_id == "4908453"
    assert settings.github_installation_id == "160851156"
    assert settings.github_private_key_path == "/tmp/orgos-github-app.pem"
    assert settings.github_owner == "enginelabs-au"
    assert settings.github_repo == "Papership"
    assert marker not in dumped
    for name in PHASE2_ENV_NAMES:
        assert name not in dumped
        # load_settings must not have called os.environ.get on these names
        assert os.environ.get(name) == marker


def test_migration_sql_has_rls_and_insert_only_audit() -> None:
    from pathlib import Path

    sql = Path(__file__).resolve().parents[1].joinpath("migrations/001_init.sql").read_text()
    assert "NOSUPERUSER" in sql
    assert "NOBYPASSRLS" in sql
    assert "engine_app" in sql
    assert "SET LOCAL" in sql
    assert "GRANT INSERT, SELECT ON engine.audit_records" in sql
    assert "UPDATE and DELETE are intentionally not granted" in sql
