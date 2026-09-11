"""SP-6: network tools cannot hit private, link-local, or cloud-metadata hosts."""

from __future__ import annotations

import ipaddress
import re
from urllib.parse import urlparse

ALLOWED_EXACT = frozenset(
    {
        "127.0.0.1",
        "localhost",
        "api.github.com",
        "github.com",
        "openrouter.ai",
        "api.openrouter.ai",
        "hermes-agent.nousresearch.com",
    }
)

ALLOWED_SUFFIXES = (
    ".github.com",
    ".githubusercontent.com",
    ".openrouter.ai",
    ".nousresearch.com",
    ".vercel.com",
    ".vercel.app",
    ".enginelabs.com.au",
)

BLOCKED_EXACT = frozenset(
    {
        "169.254.169.254",
        "metadata.google.internal",
        "metadata.google.com",
    }
)

_URL_RE = re.compile(r"https?://[^\s\"']+", re.I)


class EgressDenied(Exception):
    def __init__(self, host: str) -> None:
        super().__init__(f"egress denied: {host}")
        self.host = host
        self.source = "policy"


def host_from_target(target: str) -> str:
    raw = (target or "").strip()
    if "://" not in raw:
        raw = f"https://{raw}"
    parsed = urlparse(raw)
    return (parsed.hostname or "").lower()


def _is_blocked_ip(host: str) -> bool:
    try:
        addr = ipaddress.ip_address(host)
    except ValueError:
        return False
    return bool(
        addr.is_private
        or addr.is_loopback
        or addr.is_link_local
        or addr.is_reserved
        or addr.is_multicast
    )


def allow_egress(target: str) -> bool:
    host = host_from_target(target)
    if not host or host in BLOCKED_EXACT:
        return False
    if host in {"127.0.0.1", "localhost"}:
        return True
    if _is_blocked_ip(host):
        return False
    if host in ALLOWED_EXACT:
        return True
    if any(host.endswith(suffix) for suffix in ALLOWED_SUFFIXES):
        return True
    # Public DNS names (not raw private IPs) are allowed for web/browser research.
    if "." in host and not host.endswith(".local") and not host.endswith(".internal"):
        return True
    return False


def assert_egress(target: str) -> None:
    if not allow_egress(target):
        raise EgressDenied(host_from_target(target) or target)


def extract_targets(arguments: dict[str, object] | None) -> list[str]:
    if not arguments:
        return []
    found: list[str] = []
    for key in ("url", "href", "host", "endpoint", "target"):
        value = arguments.get(key)
        if isinstance(value, str) and value.strip():
            found.append(value.strip())
    blob = " ".join(str(v) for v in arguments.values() if isinstance(v, str))
    found.extend(_URL_RE.findall(blob))
    return found
