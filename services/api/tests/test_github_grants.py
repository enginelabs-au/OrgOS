from app.github_grants import intersect_repo_grants, may_open_pull


def test_intersection_requires_both_sides() -> None:
    orgos = {"repo.branch", "repo.change", "repo.check", "repo.release", "org.admin"}
    perms = {"contents": "write", "pull_requests": "write", "metadata": "read"}
    effective = intersect_repo_grants(orgos, perms)
    assert "repo.change" in effective
    assert "repo.branch" in effective
    assert "repo.release" not in effective
    assert may_open_pull(orgos, perms) is True
    assert may_open_pull(orgos, {"contents": "read"}) is False
