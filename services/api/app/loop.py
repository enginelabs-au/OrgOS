"""PRD-B.1 development-loop stages."""

from __future__ import annotations

LOOP_STAGES = (
    "request",
    "research",
    "specification",
    "plan",
    "assignment",
    "isolated_change",
    "tests",
    "review",
    "release_proposal",
    "monitoring",
    "retained_knowledge",
)


def stage_index(name: str) -> int:
    try:
        return LOOP_STAGES.index(name)
    except ValueError as exc:
        raise ValueError(f"unknown loop stage {name!r}") from exc


def can_advance(current: str, nxt: str) -> bool:
    return stage_index(nxt) >= stage_index(current)
