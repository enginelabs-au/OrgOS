"""Fail-closed startup: side-effecting toolsets require verified interception artefact."""

from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

import yaml

from policy_hooks.env_allowlist import load_worker_settings


class StartupPolicyError(Exception):
    pass


def load_toolsets(path: str | Path) -> dict[str, Any]:
    data = yaml.safe_load(Path(path).read_text())
    if not isinstance(data, dict):
        raise StartupPolicyError("toolsets.yaml must be a mapping")
    return data


def validate_startup(config: dict[str, Any], *, root: Path | None = None) -> None:
    verified = bool(config.get("interception_verified"))
    artefact = config.get("interception_artefact") or {}
    toolsets = config.get("side_effecting_toolsets") or {}
    enabled = [name for name, spec in toolsets.items() if spec and spec.get("enabled")]
    if not enabled:
        return
    if not verified:
        raise StartupPolicyError(
            f"side-effecting toolset(s) enabled ({', '.join(enabled)}) but interception_verified is false"
        )
    artefact_path = artefact.get("path") or ""
    expected = (artefact.get("sha256") or "").lower()
    if not artefact_path or not expected:
        raise StartupPolicyError("enabled side-effecting toolset requires artefact path and sha256")
    full = Path(artefact_path)
    if root is not None and not full.is_absolute():
        full = root / artefact_path
    if not full.is_file():
        raise StartupPolicyError(f"interception artefact missing: {full}")
    digest = hashlib.sha256(full.read_bytes()).hexdigest()
    if digest != expected:
        raise StartupPolicyError("interception artefact hash mismatch")


def validate_default(config_path: str | None = None) -> None:
    settings = load_worker_settings()
    path = config_path or settings.config_path
    config = load_toolsets(path)
    validate_startup(config, root=Path(path).resolve().parent.parent)
