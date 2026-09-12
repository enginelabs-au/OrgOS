"""PRD-D.6: Papership grants ∩ provider source permissions. Fail closed."""

from __future__ import annotations

from typing import Any

from app.github_grants import INSTALL_TO_GRANTS, installation_grants

PROVIDER_INSTALL_MAP: dict[str, dict[str, tuple[str, ...]]] = {
    "github": INSTALL_TO_GRANTS,
    "gmail": {
        "gmail.readonly": ("comms.read",),
        "gmail.compose": ("comms.draft",),
        "gmail.send": ("comms.send",),
    },
    "slack": {
        "channels:history": ("comms.read",),
        "chat:write": ("comms.send",),
    },
    "telegram": {
        "bot.message": ("comms.read",),
        "bot.send": ("comms.send",),
    },
    "whatsapp": {
        "messages.read": ("comms.read",),
        "messages.send": ("comms.send",),
    },
}

WRITE_GRANTS = frozenset({"repo.change", "repo.release", "comms.send", "comms.draft"})


def source_grants(provider: str, permissions: dict[str, Any] | None) -> set[str]:
    mapping = PROVIDER_INSTALL_MAP.get((provider or "").strip().lower())
    if mapping is None:
        return set()
    if (provider or "").strip().lower() == "github":
        return installation_grants(permissions)
    granted: set[str] = set()
    for name, level in (permissions or {}).items():
        if str(level).lower() in {"", "none", "false", "0"}:
            continue
        for grant in mapping.get(name, ()):
            granted.add(grant)
    return granted


def intersect_source_grants(
    provider: str,
    papership_grants: set[str],
    source_perms: dict[str, Any] | None,
) -> set[str]:
    """Return the intersection. Empty source perms yield empty (fail closed)."""
    if not source_perms:
        return set()
    prefix = "repo." if provider.strip().lower() == "github" else "comms."
    held = {g for g in papership_grants if g.startswith(prefix)}
    return held & source_grants(provider, source_perms)


def may_live_write(
    provider: str,
    papership_grants: set[str],
    source_perms: dict[str, Any] | None,
) -> bool:
    if not source_perms:
        return False
    return bool(intersect_source_grants(provider, papership_grants, source_perms) & WRITE_GRANTS)
