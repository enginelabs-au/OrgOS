# Decision D-09: Owner ratification of D-01…D-08 and the five policies (H-6)

## Status

`accepted` — owner-directed 2026-09-11: finish outstanding gates.

Workstream: `docs/workstreams/20260910-engine-labs-company-os/manifest.md`.

## Context

G1 was CONDITIONAL because H-6 (ratify D-01…D-08 and adopt the five policies) remained open. The owner asked to finish all outstanding gates and proceed.

## Decision

1. D-01 through D-08 are `accepted`.
2. These policies are normative: `docs/policies/authority-model.md`, `docs/policies/memory-governance.md`, `docs/policies/data-residency-and-retention.md`, `docs/policies/erasure-and-offboarding.md`, `docs/policies/licensing.md`.
3. Usage emit (`ENGINE_USAGE_EMIT`) stays off until a separate F-G1 owner accept. This record does not turn emit on.
4. Provider terms (H-4), Hermes licence (H-5), GitHub App values, and model-provider key values remain owner-supplied and are not implied by this ratification.

## Consequences

- A clean G1 PASS still needs live Compose + port scan (Docker was unavailable on the 2026-09-11 close machine) and a packaged Tauri when that toolchain is present.
- Phase 2 may start at T2-1 (interception spike) without waiting on a second H-6 prompt.
