"""D-04 adapter interfaces. UnwiredAdapter stays network-free."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Iterator, Protocol


class RuntimeAdapter(Protocol):
    def start_run(self, **kwargs: Any) -> dict[str, Any]: ...

    def subscribe(self, run_id: str, last_event_id: str | None = None) -> Iterator[dict[str, Any]]: ...

    def stop(self, run_id: str) -> Any: ...

    def forward_approval(self, run_id: str, decision: dict[str, Any]) -> Any: ...

    def capabilities_check(self) -> dict[str, Any]: ...

from adapter.approvals import resolve_owned_approval
from policy_hooks.interception import PolicyError, intercept_tool_call, tool_call_from_event
from policy_hooks.startup import load_toolsets


def _default_config() -> dict[str, Any]:
    return load_toolsets(Path(__file__).resolve().parents[1] / "config" / "toolsets.yaml")


class UnwiredAdapter:
    """Typed adapter with no network and no Hermes client."""

    def start_run(self, **kwargs: Any) -> dict[str, Any]:
        raise RuntimeError("Hermes is not wired in phase 1")

    def subscribe(self, run_id: str, last_event_id: str | None = None) -> Iterator[dict[str, Any]]:
        raise RuntimeError("Hermes is not wired in phase 1")
        yield {}  # pragma: no cover

    def stop(self, run_id: str) -> None:
        raise RuntimeError("Hermes is not wired in phase 1")

    def forward_approval(self, run_id: str, decision: dict[str, Any]) -> None:
        raise RuntimeError("Hermes is not wired in phase 1")

    def capabilities_check(self) -> dict[str, Any]:
        return {"hermes": "not_configured", "wired": False}


class HermesRuntimeAdapter:
    """Typed D-04 operations. Policy runs before any Hermes call."""

    def __init__(self, config: dict[str, Any] | None = None) -> None:
        self.config = config or _default_config()

    def intercept(self, name: str, arguments: dict[str, Any] | None = None, **hooks: Any) -> dict[str, Any]:
        return intercept_tool_call(
            self.config,
            name,
            arguments,
            persist_receipt=hooks.get("persist_receipt"),
            persist_approval=hooks.get("persist_approval"),
        )

    def start_run(self, **kwargs: Any) -> dict[str, Any]:
        if "tool" in kwargs:
            self.intercept(
                str(kwargs.get("tool") or ""),
                kwargs.get("arguments") or {},
                persist_receipt=kwargs.get("persist_receipt"),
                persist_approval=kwargs.get("persist_approval"),
            )
        from adapter.hermes_client import probe_hermes, start_run as hermes_start

        probe = probe_hermes()
        if probe.get("api_server") is not True:
            return {
                "status": "blocked_runtime",
                "reason": "hermes_api_server_unavailable",
                "probe": {k: probe.get(k) for k in ("hermes", "mode", "api_server", "http_status")},
                "purpose": kwargs.get("purpose"),
            }
        if "tool" not in kwargs:
            raise PolicyError("catalogued tool= is required for live Hermes runs")
        code, body = hermes_start(
            purpose=str(kwargs.get("purpose") or "run"),
            idempotency_key=str(kwargs.get("idempotency_key") or ""),
            session_id=kwargs.get("session_id"),
        )
        replayed = code == 202 and bool((body or {}).get("idempotency_replayed") or body.get("Idempotency-Replayed"))
        return {"status": "accepted" if code in {200, 201, 202} else "error", "http_status": code, "body": body, "replayed": replayed}

    def subscribe(self, run_id: str, last_event_id: str | None = None, **hooks: Any) -> Iterator[dict[str, Any]]:
        from adapter.hermes_client import stream_events

        for event in stream_events(run_id, last_event_id):
            parsed = tool_call_from_event(event)
            if parsed is not None:
                self.intercept(
                    parsed[0],
                    parsed[1],
                    persist_receipt=hooks.get("persist_receipt"),
                    persist_approval=hooks.get("persist_approval"),
                )
            yield event

    def stop(self, run_id: str) -> dict[str, Any]:
        from adapter.hermes_client import stop_run

        code, body = stop_run(run_id)
        return {"http_status": code, "body": body}

    def forward_approval(self, run_id: str, decision: dict[str, Any], persist=None) -> dict[str, Any]:
        from adapter.hermes_client import resolve_approval

        def _forward(rid: str, dec: dict[str, Any]) -> dict[str, Any]:
            code, body = resolve_approval(rid, dec)
            return {"http_status": code, "body": body}

        if persist is None:
            raise RuntimeError("approval persist is required")
        return resolve_owned_approval(run_id, decision, persist=persist, forward=_forward)

    def capabilities_check(self) -> dict[str, Any]:
        from adapter.hermes_client import documented_capabilities, probe_hermes

        probe = probe_hermes()
        docs = documented_capabilities()
        return {**probe, "documented": docs}


class HermesHealthAdapter(HermesRuntimeAdapter):
    """Backward-compatible name: now the runtime adapter."""
