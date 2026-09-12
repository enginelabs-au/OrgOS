"""AUTH-12: Papership repo grants ∩ GitHub App installation permissions."""

from __future__ import annotations

from typing import Any

# GitHub installation permission → Papership grant classes (write/admin only).
INSTALL_TO_GRANTS: dict[str, tuple[str, ...]] = {
    "contents": ("repo.branch", "repo.change"),
    "pull_requests": ("repo.change",),
    "checks": ("repo.check",),
    "actions": ("repo.check",),
    "administration": ("repo.release",),
    "contents_release": ("repo.release",),
}


def installation_grants(permissions: dict[str, Any] | None) -> set[str]:
    granted: set[str] = set()
    for name, level in (permissions or {}).items():
        if str(level).lower() not in {"write", "admin"}:
            continue
        for grant in INSTALL_TO_GRANTS.get(name, ()):
            granted.add(grant)
    return granted


def intersect_repo_grants(papership_grants: set[str], permissions: dict[str, Any] | None) -> set[str]:
    repo = {g for g in papership_grants if g.startswith("repo.")}
    return repo & installation_grants(permissions)


def may_open_pull(papership_grants: set[str], permissions: dict[str, Any] | None) -> bool:
    return "repo.change" in intersect_repo_grants(papership_grants, permissions)
