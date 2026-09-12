"""Claim queued Papership jobs and persist a subscribe receipt. No Hermes key on the API."""

from __future__ import annotations

from typing import Any

from adapter.interfaces import HermesRuntimeAdapter
from policy_hooks.interception import PolicyError


def consume_queued_jobs(store: Any, *, limit: int = 8) -> list[dict[str, Any]]:
    """Claim queued jobs, intercept subscribe, write receipts. Safe if Hermes is down."""
    claimed: list[dict[str, Any]] = []
    adapter = HermesRuntimeAdapter()
    for job in store.list_queued_jobs(limit=limit):
        job_id = job["id"]
        store.claim_job(job_id)
        try:
            store.add_receipt(job_id, "worker.claimed", f"{job_id}:claimed")
            events = list(
                adapter.subscribe(
                    job.get("run_id") or job_id,
                    persist_receipt=lambda name, _args, jid=job_id: store.add_receipt(
                        jid, f"tool.{name}", f"{jid}:tool:{name}"
                    ),
                )
            )
            store.add_receipt(job_id, "worker.subscribed", f"{job_id}:subscribed")
            store.complete_job(job_id)
            claimed.append({"id": job_id, "status": "completed", "events": len(events)})
        except PolicyError as exc:
            store.add_receipt(job_id, "worker.intercepted", f"{job_id}:intercepted")
            claimed.append({"id": job_id, "status": "intercepted", "detail": exc.detail})
        except Exception as exc:  # Hermes down or stream empty is non-fatal
            store.add_receipt(job_id, "worker.idle", f"{job_id}:idle")
            claimed.append({"id": job_id, "status": "idle", "detail": type(exc).__name__})
    return claimed
