# Decision D-02: Capability registry schema and status vocabulary

## Status

`accepted` — owner-directed H-6 ratification 2026-09-11. Record: `docs/decisions/2026-09-11-owner-ratification-h6.md`. Schema implemented in `packages/contracts`.

Workstream: `docs/workstreams/20260910-engine-labs-company-os/manifest.md`. Phase plan: `docs/plans/phase_0_foundations_plan.md` §7.

## Context

The intake requires a versioned capability registry that records, for each capability, "its user outcome, native or connector owner, read/write actions, data authority, required grants, dependencies, interface components, release phase, implementation status and acceptance evidence", and that tracks "planned, configured, working and unavailable capabilities distinctly" (intake Phase 02; I-02). The registry is the source for the desktop registry view (PRD-C.5), for `unavailable` explanations shown to members (PRD-A.4, A.9), and for the Project Lead's gate rule that no capability is marked complete without demonstrated workflow and verified integration behaviour (I-02, I-08, I-13).

## Decision

1. **Row schema** — as specified in `docs/product.md` §3.1: `domain_id` (`B01`–`B24`, `P01`–`P19`), `capability_id` (`<domain_id>.<nn>`), `user_outcome`, `owner` (`native` | `connector:<provider>`), `read_actions`, `write_actions` (each write routed through the action lifecycle, PRD-E.3), `data_authority` (`native` | `source:<system>` | `shared`), `required_grants` (identifiers from the versioned grant registry, AUTH-04), `dependencies`, `interface_components` (mapped to `docs/ui-blueprint.md`), `release_phase` (implementation phase `07`–`12` and release `R1`–`R4`), `implementation_status`, `acceptance_evidence`, `registry_version`, `status_changed_at`, `status_evidence`. Identifier and version columns are `proposal` additions; the remainder are intake-derived.
2. **Status vocabulary** — exactly four values: `planned`, `configured`, `working`, `unavailable`, with the meanings in `docs/product.md` §3.2. No additional states (for example `beta`, `partial`, `deprecated`) are introduced in release 1; retirement is expressed as `unavailable` with a reason.
3. **Transition rules** — the six rules in `docs/product.md` §3.2 are normative: `configured → working` requires a demonstrated end-to-end workflow, verified behaviour against the real dependency (mocks, reference screens, sample data or a visible control do not qualify) and a linked acceptance evidence record on the release revision; `working → configured` on any invalidating change; every transition records `status_changed_at` and `status_evidence`.
4. **Storage and publication** — `docs/capabilities.md` is the phase-0 human-readable registry (43 rows, all `planned`). From phase 1 the machine-readable schema lives in `packages/contracts` (zod + JSON Schema) and the API serves the registry; the markdown file becomes a generated projection, not a second source of truth.
5. **Gate enforcement** — `project-lead-subagent` rejects any `working` row without the three §3.2 rule-2 elements at every gate (blueprint §15 risk control).

## Alternatives considered

1. **Five-plus status vocabulary (adding `beta`, `deprecated`, `blocked`).** Rejected: the intake names exactly four states; extra states blur the "demonstrated workflow" line the PL gate depends on. `unavailable` with a recorded reason covers blocked and retired cases.
2. **Per-release registry snapshots as separate files.** Rejected: `registry_version` plus `status_changed_at`/`status_evidence` give the same history in one versioned table; snapshots would drift from the served registry.
3. **Free-text status evidence.** Rejected: `acceptance_evidence` and `status_evidence` must be links to evidence records so the verification index (`docs/verification.md`) can be reconciled mechanically.

## Consequences

- Positive: one vocabulary shared by product docs, API, desktop registry view and PL gate; `unavailable` is first-class and visible (PRD-C.5), which the intake requires.
- Negative / costs: every status change carries evidence overhead; the registry service and its schema are phase-1 work before any capability can move off `planned`.
- Follow-ups: implement schema in `packages/contracts` (phase 1); registry API + desktop view (phase 1); Growth's usage measurement row P14 targets `configured` in R1 only (Growth handoff §5.3).

## Evidence and citations

- Intake: `docs/Company_Agent_System_Blueprint.md` Phase 02 (registry sentence; four statuses).
- `docs/product.md` §3.1 (schema table), §3.2 (vocabulary and six transition rules), §4.2 (bucket rule).
- `docs/capabilities.md` (43 rows; EV-S10 row count).
- PM handoff `docs/workstreams/20260910-engine-labs-company-os/product-manager-subagent/handoff.md` §13 (D-02 candidate).
- Security policy `docs/policies/authority-model.md` AUTH-04 (grant identifiers from a versioned registry).
