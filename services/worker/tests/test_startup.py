from __future__ import annotations

import hashlib
from pathlib import Path

import pytest
import yaml

from adapter.interfaces import HermesHealthAdapter, UnwiredAdapter
from policy_hooks.env_allowlist import FORBIDDEN, WORKER_ENV_ALLOWLIST, load_worker_settings
from policy_hooks.startup import StartupPolicyError, load_toolsets, validate_default, validate_startup

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_YAML = ROOT / "config" / "toolsets.yaml"


def test_default_config_starts() -> None:
    config = load_toolsets(DEFAULT_YAML)
    assert config["interception_verified"] is True
    validate_startup(config, root=ROOT)
    validate_default(str(DEFAULT_YAML))


def test_enabled_without_artefact_refuses(tmp_path: Path) -> None:
    config = {
        "interception_verified": False,
        "interception_artefact": {"path": "", "sha256": ""},
        "side_effecting_toolsets": {"terminal": {"enabled": True}},
    }
    with pytest.raises(StartupPolicyError, match="interception_verified is false"):
        validate_startup(config)
    verified_missing = {
        "interception_verified": True,
        "interception_artefact": {"path": str(tmp_path / "missing.bin"), "sha256": "ab" * 32},
        "side_effecting_toolsets": {"terminal": {"enabled": True}},
    }
    with pytest.raises(StartupPolicyError, match="missing"):
        validate_startup(verified_missing)


def test_hash_mismatch_refuses(tmp_path: Path) -> None:
    artefact = tmp_path / "artefact.txt"
    artefact.write_text("contract-test")
    digest = hashlib.sha256(artefact.read_bytes()).hexdigest()
    config = {
        "interception_verified": True,
        "interception_artefact": {"path": str(artefact), "sha256": "00" * 32},
        "side_effecting_toolsets": {"browser": {"enabled": True}},
    }
    with pytest.raises(StartupPolicyError, match="hash mismatch"):
        validate_startup(config)
    config["interception_artefact"]["sha256"] = digest
    config["catalog_sha256"] = hashlib.sha256((ROOT / "policy_hooks" / "catalog.py").read_bytes()).hexdigest()
    validate_startup(config, root=ROOT)


def test_no_network_to_hermes(monkeypatch: pytest.MonkeyPatch) -> None:
    def blocked(*_args, **_kwargs):
        raise AssertionError("network to Hermes is forbidden")

    monkeypatch.setattr("socket.create_connection", blocked)
    adapter = UnwiredAdapter()
    assert adapter.capabilities_check()["wired"] is False
    with pytest.raises(RuntimeError, match="not wired"):
        adapter.start_run(purpose="x")
    source = (ROOT / "adapter" / "interfaces.py").read_text()
    assert "httpx" not in source
    assert "urllib" not in source
    assert "hermes-agent" not in source


def test_documented_capabilities_are_not_a_live_api(monkeypatch: pytest.MonkeyPatch) -> None:
    from adapter.hermes_client import documented_capabilities

    monkeypatch.delenv("HERMES_API_BASE_URL", raising=False)
    monkeypatch.delenv("HERMES_API_SERVER_KEY", raising=False)
    payload = documented_capabilities()
    assert payload["available_on_this_deployment"] is False
    assert payload["features"]["run_approval"] is True


def test_health_adapter_blocks_without_api_server(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("HERMES_API_BASE_URL", raising=False)
    adapter = HermesHealthAdapter()
    result = adapter.start_run(purpose="x")
    assert result["status"] == "blocked_runtime"
    from policy_hooks.interception import PolicyError

    with pytest.raises(PolicyError):
        adapter.start_run(tool="bash")
    assert adapter.capabilities_check()["wired"] is False


def test_database_url_not_in_allowlist(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgresql://should-not-be-read")
    monkeypatch.setenv("DBOS_SYSTEM_DATABASE_URL", "postgresql://should-not-be-read")
    settings = load_worker_settings()
    assert "should-not-be-read" not in str(settings)
    assert "DATABASE_URL" in FORBIDDEN
    assert "HERMES_API_SERVER_KEY" not in FORBIDDEN
    assert "HERMES_API_SERVER_KEY" in WORKER_ENV_ALLOWLIST
    assert "DATABASE_URL" not in str(settings.__dict__)


def test_default_yaml_catalog_enabled_with_artefact() -> None:
    data = yaml.safe_load(DEFAULT_YAML.read_text())
    assert data["interception_verified"] is True
    assert data["interception_artefact"]["sha256"]
    assert data["catalog_sha256"] == hashlib.sha256((ROOT / "policy_hooks" / "catalog.py").read_bytes()).hexdigest()
    for name, spec in data["side_effecting_toolsets"].items():
        assert spec["enabled"] is True, name
