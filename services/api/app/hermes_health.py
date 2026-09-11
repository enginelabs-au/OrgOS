"""API-side Hermes reachability. No bearer key. No customer content."""

from __future__ import annotations

import urllib.error
import urllib.request


def _status(url: str, method: str, timeout: float) -> int | None:
    req = urllib.request.Request(url, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return getattr(resp, "status", 200)
    except urllib.error.HTTPError as exc:
        return exc.code
    except (urllib.error.URLError, TimeoutError, OSError):
        return None


def _classify(code: int | None) -> str | None:
    if code is None:
        return None
    if code in {301, 302, 303, 307, 308}:
        return "serve_ui"
    if code in {200, 204, 401, 405}:
        return "reachable"
    return "error"


def probe_hermes(base_url: str, timeout: float = 3.0) -> str:
    url = (base_url or "").rstrip("/")
    if not url:
        return "not_configured"
    target = f"{url}/health"
    # HEAD first: the live gateway GET /health hangs; HEAD 405 is immediate.
    classified = _classify(_status(target, "HEAD", timeout))
    if classified is not None:
        return classified
    classified = _classify(_status(target, "GET", timeout))
    if classified is not None:
        return classified
    return "unreachable"
