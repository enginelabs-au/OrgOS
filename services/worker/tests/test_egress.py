from policy_hooks.egress import EgressDenied, allow_egress, assert_egress, extract_targets


def test_allowlisted_hosts() -> None:
    assert allow_egress("https://api.github.com/repos/enginelabs-au/Papership")
    assert allow_egress("127.0.0.1:9119")
    assert allow_egress("localhost")
    assert allow_egress("https://docs.github.com")
    assert allow_egress("https://example.com/search")


def test_private_and_metadata_denied() -> None:
    assert allow_egress("http://192.168.1.1") is False
    assert allow_egress("http://10.0.0.4") is False
    try:
        assert_egress("http://169.254.169.254/latest/meta-data")
    except EgressDenied as exc:
        assert exc.source == "policy"
        assert "169.254.169.254" in exc.host
    else:
        raise AssertionError("expected EgressDenied")


def test_extract_targets_from_args() -> None:
    assert "https://api.github.com" in extract_targets({"url": "https://api.github.com"})
