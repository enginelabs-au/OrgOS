"""Worker env allowlist — no DATABASE_URL / DBOS_SYSTEM_DATABASE_URL (D-08)."""

from __future__ import annotations

import os
from dataclasses import dataclass

WORKER_ENV_ALLOWLIST = frozenset(
    {
        "ENGINE_API_BASE_URL",
        "ENGINE_STORE_PATH",
        "ENGINE_WORKER_CONFIG",
        "HERMES_API_BASE_URL",
        "HERMES_API_SERVER_KEY",
        "HERMES_VERSION_PIN",
        "PATH",
        "HOME",
        "USER",
        "TMPDIR",
        "LANG",
        "LC_ALL",
        "PYTHONPATH",
        "VIRTUAL_ENV",
        "UV_PROJECT_ENVIRONMENT",
    }
)

FORBIDDEN = frozenset(
    {
        "DATABASE_URL",
        "DBOS_SYSTEM_DATABASE_URL",
        "MODEL_PROVIDER_API_KEY",
        "GITHUB_APP_ID",
        "GITHUB_APP_PRIVATE_KEY",
        "GITHUB_APP_INSTALLATION_ID",
    }
)


@dataclass(frozen=True)
class WorkerSettings:
    api_base_url: str
    config_path: str


def load_worker_settings() -> WorkerSettings:
    for name in FORBIDDEN:
        if name in WORKER_ENV_ALLOWLIST:
            raise RuntimeError(f"forbidden env in allowlist: {name}")
    api = os.environ.get("ENGINE_API_BASE_URL", "") if "ENGINE_API_BASE_URL" in WORKER_ENV_ALLOWLIST else ""
    config = (
        os.environ.get("ENGINE_WORKER_CONFIG", "config/toolsets.yaml")
        if "ENGINE_WORKER_CONFIG" in WORKER_ENV_ALLOWLIST
        else "config/toolsets.yaml"
    )
    return WorkerSettings(api_base_url=api, config_path=config)
