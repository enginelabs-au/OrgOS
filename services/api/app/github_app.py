"""GitHub App transport — health, plan, and opt-in pull-request open."""

from __future__ import annotations

import base64
import json
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Callable

import jwt

RequestFn = Callable[..., tuple[int, dict[str, Any]]]


def probe_github(
    app_id: str,
    installation_id: str,
    key_path: str,
    *,
    live: bool = True,
    timeout: float = 3.0,
) -> str:
    if not (app_id or "").strip() or not (installation_id or "").strip() or not (key_path or "").strip():
        return "not_configured"
    path = Path(key_path).expanduser()
    if not path.is_file():
        return "missing_key"
    if not live:
        return "configured"
    try:
        token = _app_jwt(app_id.strip(), path)
        code, _ = github_request(
            "GET",
            f"https://api.github.com/app/installations/{installation_id.strip()}",
            token=token,
            timeout=timeout,
        )
    except (urllib.error.URLError, TimeoutError, OSError, ValueError):
        return "unreachable"
    if code in {200, 204}:
        return "reachable"
    if code in {401, 403, 404}:
        return "error"
    return "error"


def plan_pull(
    *,
    owner: str,
    repo: str,
    title: str,
    body: str,
    head: str,
    base: str = "main",
) -> dict[str, str]:
    slug = "".join(ch if ch.isalnum() or ch in "-_" else "-" for ch in head).strip("-") or "papership-loop"
    return {
        "owner": owner,
        "repo": repo,
        "title": title,
        "body": body,
        "head": head,
        "base": base,
        "file_path": f".papership/loop/{slug}.md",
        "legacy_file_path": f".orgos/loop/{slug}.md",
    }


def receipt_read_paths(planned: dict[str, str]) -> tuple[str, ...]:
    """New receipts first; published .orgos/loop files stay readable."""
    current = planned.get("file_path") or ""
    legacy = planned.get("legacy_file_path") or ""
    return tuple(path for path in (current, legacy) if path)


def open_pull(
    app_id: str,
    installation_id: str,
    key_path: str,
    *,
    owner: str,
    repo: str,
    title: str,
    body: str,
    head: str,
    base: str = "main",
    dry_run: bool = True,
    request: RequestFn | None = None,
    timeout: float = 8.0,
) -> dict[str, Any]:
    if not owner.strip() or not repo.strip():
        raise GithubError(503, "repository not configured")
    if not title.strip() or not head.strip():
        raise GithubError(400, "title and head are required")
    planned = plan_pull(owner=owner.strip(), repo=repo.strip(), title=title.strip(), body=body, head=head.strip(), base=base.strip() or "main")
    if dry_run:
        return {"status": "planned", "dry_run": True, "planned": planned}
    if not (app_id or "").strip() or not (installation_id or "").strip() or not (key_path or "").strip():
        raise GithubError(503, "github app not configured")
    path = Path(key_path).expanduser()
    if not path.is_file():
        raise GithubError(503, "github key missing")
    http = request or github_request
    token = installation_token(app_id, installation_id, path, request=http, timeout=timeout)
    sha = _default_branch_sha(http, token, planned["owner"], planned["repo"], planned["base"], timeout)
    _ensure_branch(http, token, planned, sha, timeout)
    _put_receipt(http, token, planned, timeout)
    code, payload = http(
        "POST",
        f"https://api.github.com/repos/{planned['owner']}/{planned['repo']}/pulls",
        token=token,
        payload={"title": planned["title"], "body": planned["body"], "head": planned["head"], "base": planned["base"]},
        timeout=timeout,
    )
    if code not in {200, 201}:
        raise GithubError(code if 400 <= code < 600 else 502, str(payload.get("message") or "pull create failed"))
    return {
        "status": "opened",
        "dry_run": False,
        "planned": planned,
        "number": payload.get("number"),
        "url": payload.get("html_url"),
    }


def installation_permissions(
    app_id: str,
    installation_id: str,
    key_path: str,
    *,
    request: RequestFn | None = None,
    timeout: float = 8.0,
) -> dict[str, Any]:
    if not (app_id or "").strip() or not (installation_id or "").strip() or not (key_path or "").strip():
        return {}
    path = Path(key_path).expanduser()
    if not path.is_file():
        return {}
    http = request or github_request
    token = _app_jwt(app_id.strip(), path)
    code, payload = http(
        "GET",
        f"https://api.github.com/app/installations/{installation_id.strip()}",
        token=token,
        timeout=timeout,
    )
    if code != 200 or not isinstance(payload, dict):
        return {}
    perms = payload.get("permissions") or {}
    return perms if isinstance(perms, dict) else {}


def list_pulls(
    app_id: str,
    installation_id: str,
    key_path: str,
    *,
    owner: str,
    repo: str,
    request: RequestFn | None = None,
    timeout: float = 8.0,
) -> dict[str, Any]:
    if not owner.strip() or not repo.strip():
        return {"status": "not_configured", "items": []}
    if not (app_id or "").strip() or not (installation_id or "").strip() or not (key_path or "").strip():
        return {"status": "not_configured", "items": []}
    path = Path(key_path).expanduser()
    if not path.is_file():
        return {"status": "missing_key", "items": []}
    http = request or github_request
    token = installation_token(app_id, installation_id, path, request=http, timeout=timeout)
    code, payload = http(
        "GET",
        f"https://api.github.com/repos/{owner.strip()}/{repo.strip()}/pulls?state=open&per_page=20",
        token=token,
        timeout=timeout,
    )
    if code != 200 or not isinstance(payload, list):
        return {"status": "error", "items": []}
    items = [
        {
            "number": row.get("number"),
            "title": row.get("title"),
            "url": row.get("html_url"),
            "head": (row.get("head") or {}).get("ref"),
            "base": (row.get("base") or {}).get("ref"),
        }
        for row in payload
        if isinstance(row, dict)
    ]
    return {"status": "ok", "items": items}


def installation_token(
    app_id: str,
    installation_id: str,
    pem_path: Path,
    *,
    request: RequestFn,
    timeout: float = 8.0,
) -> str:
    app_jwt = _app_jwt(app_id.strip(), pem_path)
    code, payload = request(
        "POST",
        f"https://api.github.com/app/installations/{installation_id.strip()}/access_tokens",
        token=app_jwt,
        payload={},
        timeout=timeout,
    )
    token = str(payload.get("token") or "")
    if code not in {200, 201} or not token:
        raise GithubError(code if 400 <= code < 600 else 502, "installation token failed")
    return token


def github_request(
    method: str,
    url: str,
    *,
    token: str,
    payload: dict[str, Any] | None = None,
    timeout: float = 8.0,
) -> tuple[int, Any]:
    data = None
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "Papership",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if payload is not None:
        data = json.dumps(payload).encode()
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            code = getattr(resp, "status", 200)
    except urllib.error.HTTPError as exc:
        raw = exc.read()
        code = exc.code
    body: Any = {}
    if raw:
        try:
            body = json.loads(raw.decode())
        except json.JSONDecodeError:
            body = {"raw": raw.decode(errors="replace")[:200]}
    return code, body


class GithubError(Exception):
    def __init__(self, status_code: int, detail: str) -> None:
        super().__init__(detail)
        self.status_code = status_code
        self.detail = detail


def _app_jwt(app_id: str, pem_path: Path) -> str:
    now = int(time.time())
    pem = pem_path.read_bytes()
    return jwt.encode(
        {"iat": now - 30, "exp": now + 540, "iss": app_id},
        pem,
        algorithm="RS256",
    )


def _default_branch_sha(
    http: RequestFn,
    token: str,
    owner: str,
    repo: str,
    base: str,
    timeout: float,
) -> str:
    code, payload = http(
        "GET",
        f"https://api.github.com/repos/{owner}/{repo}/git/ref/heads/{base}",
        token=token,
        timeout=timeout,
    )
    sha = str(((payload or {}).get("object") or {}).get("sha") or "")
    if code != 200 or not sha:
        raise GithubError(502, "could not read base branch")
    return sha


def _ensure_branch(http: RequestFn, token: str, planned: dict[str, str], sha: str, timeout: float) -> None:
    code, payload = http(
        "POST",
        f"https://api.github.com/repos/{planned['owner']}/{planned['repo']}/git/refs",
        token=token,
        payload={"ref": f"refs/heads/{planned['head']}", "sha": sha},
        timeout=timeout,
    )
    if code in {200, 201}:
        return
    if code == 422 and "Reference already exists" in str(payload):
        return
    raise GithubError(code if 400 <= code < 600 else 502, str(payload.get("message") or "branch create failed"))


def _put_receipt(http: RequestFn, token: str, planned: dict[str, str], timeout: float) -> None:
    content = base64.b64encode(
        f"# Papership loop\n\n{planned['title']}\n\n{planned['body']}\n".encode()
    ).decode()
    code, payload = http(
        "PUT",
        f"https://api.github.com/repos/{planned['owner']}/{planned['repo']}/contents/{planned['file_path']}",
        token=token,
        payload={
            "message": f"papership: {planned['title']}",
            "content": content,
            "branch": planned["head"],
        },
        timeout=timeout,
    )
    if code not in {200, 201}:
        raise GithubError(code if 400 <= code < 600 else 502, str(payload.get("message") or "receipt write failed"))
