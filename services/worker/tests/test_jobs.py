from jobs import consume_queued_jobs


class FakeStore:
    def __init__(self) -> None:
        self.jobs = [{"id": "job-1", "run_id": "run-1", "status": "queued"}]
        self.receipts: list[str] = []
        self.claimed = False
        self.completed = False

    def list_queued_jobs(self, limit: int = 8):
        return list(self.jobs)[:limit]

    def claim_job(self, job_id: str) -> None:
        self.claimed = True
        self.jobs = []

    def add_receipt(self, job_id: str, step_name: str, idempotency_key: str):
        self.receipts.append(step_name)
        return {"id": idempotency_key, "step_name": step_name}

    def complete_job(self, job_id: str) -> None:
        self.completed = True


def test_consume_claims_and_writes_receipts(monkeypatch) -> None:
    store = FakeStore()
    monkeypatch.setattr("adapter.hermes_client.stream_events", lambda *_a, **_k: iter([]))
    result = consume_queued_jobs(store)
    assert store.claimed is True
    assert "worker.claimed" in store.receipts
    assert result[0]["id"] == "job-1"
