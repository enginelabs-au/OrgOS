from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

from app.github_app import GithubError, list_pulls, open_pull, plan_pull, probe_github, receipt_read_paths


def _write_pem(path) -> None:
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    path.write_bytes(
        key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )


def test_probe_empty_is_not_configured() -> None:
    assert probe_github("", "", "") == "not_configured"


def test_probe_missing_key(tmp_path) -> None:
    assert probe_github("1", "2", str(tmp_path / "absent.pem")) == "missing_key"


def test_probe_configured_without_live(tmp_path) -> None:
    pem = tmp_path / "app.pem"
    pem.write_text("-----BEGIN PLACEHOLDER-----\n")
    assert probe_github("1", "2", str(pem), live=False) == "configured"


def test_plan_pull_sanitizes_path() -> None:
    planned = plan_pull(
        owner="enginelabs-au",
        repo="papership",
        title="Loop receipt",
        body="Phase 2",
        head="papership/loop t2-3",
    )
    assert planned["file_path"] == ".papership/loop/papership-loop-t2-3.md"
    assert planned["legacy_file_path"] == ".orgos/loop/papership-loop-t2-3.md"
    assert planned["base"] == "main"
    assert receipt_read_paths(planned) == (
        ".papership/loop/papership-loop-t2-3.md",
        ".orgos/loop/papership-loop-t2-3.md",
    )


def test_open_pull_dry_run_does_not_call_github() -> None:
    called = []

    def boom(*_a, **_k):
        called.append(1)
        raise AssertionError("network")

    result = open_pull(
        "",
        "",
        "",
        owner="enginelabs-au",
        repo="papership",
        title="Wire PR client",
        body="dry run",
        head="papership/pr-client",
        dry_run=True,
        request=boom,
    )
    assert result["status"] == "planned"
    assert result["dry_run"] is True
    assert result["planned"]["head"] == "papership/pr-client"
    assert called == []


def test_open_pull_live_uses_installation_and_creates(tmp_path) -> None:
    pem = tmp_path / "app.pem"
    _write_pem(pem)
    calls: list[str] = []

    def fake(method, url, **_k):
        calls.append(f"{method} {url}")
        if url.endswith("/access_tokens"):
            return 201, {"token": "ghs_test"}
        if "/git/ref/heads/main" in url:
            return 200, {"object": {"sha": "abc123"}}
        if url.endswith("/git/refs"):
            return 201, {"ref": "refs/heads/papership/pr-client"}
        if "/contents/" in url:
            return 201, {"content": {"path": ".papership/loop/papership-pr-client.md"}}
        if url.endswith("/pulls"):
            return 201, {"number": 42, "html_url": "https://github.com/enginelabs-au/papership/pull/42"}
        return 404, {"message": "unexpected"}

    result = open_pull(
        "1",
        "2",
        str(pem),
        owner="enginelabs-au",
        repo="papership",
        title="Wire PR client",
        body="live",
        head="papership/pr-client",
        dry_run=False,
        request=fake,
    )
    assert result["status"] == "opened"
    assert result["number"] == 42
    assert any("/access_tokens" in c for c in calls)
    assert any(c.startswith("POST ") and c.endswith("/pulls") for c in calls)


def test_open_pull_missing_title() -> None:
    try:
        open_pull("", "", "", owner="o", repo="r", title="", body="", head="x")
    except GithubError as exc:
        assert exc.status_code == 400
    else:
        raise AssertionError("expected GithubError")


def test_list_pulls_not_configured() -> None:
    assert list_pulls("", "", "", owner="", repo="")["status"] == "not_configured"
