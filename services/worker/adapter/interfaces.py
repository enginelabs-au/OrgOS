"""D-04 adapter interfaces. No Hermes client is wired in phase 1."""

from __future__ import annotations

from typing import Any, Iterator, Protocol


class RuntimeAdapter(Protocol):
    def start_run(self, **kwargs: Any) -> dict[str, Any]: ...

    def subscribe(self, run_id: str, last_event_id: str | None = None) -> Iterator[dict[str, Any]]: ...

    def stop(self, run_id: str) -> None: ...

    def forward_approval(self, run_id: str, decision: dict[str, Any]) -> None: ...

    def capabilities_check(self) -> dict[str, Any]: ...


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
