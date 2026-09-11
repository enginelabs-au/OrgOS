import sqlite3

import pytest
from fastapi.testclient import TestClient

from app.store import Store, StoreError
from tests.conftest import make_token


def test_two_principal_store_isolation(client: TestClient, founder_headers: dict[str, str]) -> None:
    created = client.post("/priorities", json={"title": "P1"}, headers=founder_headers)
    assert created.status_code == 200
    other = {"Authorization": f"Bearer {make_token('principal-other')}"}
    listed = client.get("/priorities", headers=other)
    assert listed.status_code == 403
    founder_list = client.get("/priorities", headers=founder_headers)
    assert founder_list.status_code == 200
    assert any(item["title"] == "P1" for item in founder_list.json()["items"])


def test_audit_update_denied(tmp_path) -> None:
    store = Store(str(tmp_path / "iso.sqlite"))
    store.seed_founder()
    aid = store.append_audit("principal-founder", "test", "x", "1")
    with pytest.raises(sqlite3.DatabaseError, match="insert-only"):
        store.try_update_audit(aid)
    store.close()


def test_agent_cannot_hold_approval(tmp_path) -> None:
    store = Store(str(tmp_path / "g.sqlite"))
    store.seed_founder()
    with pytest.raises(StoreError, match="approval"):
        store.add_grant("principal-agent", "approval.release", "tenant-founder")
    store.close()
