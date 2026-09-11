import os

from app.config import PHASE2_ENV_NAMES, load_settings, settings_public_dict


def test_phase2_env_names_are_not_read(monkeypatch) -> None:
    marker = "should-never-be-read-by-phase1"
    monkeypatch.setenv("HERMES_API_SERVER_KEY", marker)
    monkeypatch.setenv("HERMES_API_BASE_URL", marker)
    monkeypatch.setenv("HERMES_VERSION_PIN", marker)
    monkeypatch.setenv("MODEL_PROVIDER_API_KEY", marker)
    monkeypatch.setenv("GITHUB_APP_ID", marker)
    monkeypatch.setenv("GITHUB_APP_PRIVATE_KEY", marker)
    monkeypatch.setenv("GITHUB_APP_INSTALLATION_ID", marker)
    monkeypatch.setenv("GITHUB_APP_WEBHOOK_SECRET", marker)
    monkeypatch.setenv("SUPABASE_JWT_SECRET", "test-only-not-for-production-jwt-secret-0001")
    settings = load_settings()
    dumped = str(settings_public_dict(settings)) + str(settings)
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
