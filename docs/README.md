# Project documentation

- `blueprints/` — product, market, architecture, and go-to-market blueprints
- `plans/` — sequential implementation plans and final implementation checklist
- `decisions/` — material architecture and product decision records
- `handover/` — concise operational handovers when needed
- `workstreams/` — task-scoped role manifests, charters, evidence, and handoffs

Agent workflow is defined in root `AGENTS.md`, detailed in `.cursor/AGENTS.md`, and routed through `.cursor/INSTRUCTIONS.md`. Canonical role behavior is defined in `.cursor/instructions/ROLES.md`.

Start or resume the complete product lifecycle with `/launch-pipeline`; its detailed contract is `.cursor/instructions/LAUCH.md`.

## Engine Labs

- Product intake (canonical requirements): `Company_Agent_System_Blueprint.md`
- Strategy blueprint: `blueprints/2026-09-10_engine_labs.md`
- Active plan: `plans/phase_1_foundation_plan.md` (phase 07 Foundation; generated 2026-09-10 from the phase-0 §22 prompt)
- Completed plan: `plans/phase_0_foundations_plan.md` (`complete_conditional`; PL gate 2026-09-10T18:22Z)
- Workstream: `workstreams/20260910-engine-labs-company-os/manifest.md`
- Product documents (phase 0 outputs): `product.md`, `capabilities.md`, `architecture.md`, `ui-blueprint.md` (spec) plus `ui-blueprint/` (pinned `8a843bd` app snapshot, captures, `SOURCE.md`), `roadmap.md`, `verification.md`, `policies/`
- Hey Engine (PRD-E.13): persistent assistant control + wake phrase; R1 ships the control and an honest unavailable state; runtime and wake word are later phases
- Decisions: `decisions/` — D-01…D-06 (`proposed`); D-07 `2026-09-11-tooling-and-pins.md`; D-08 `2026-09-11-worker-data-access.md`
- Next plan (generated after G1): `plans/phase_2_development_loop_plan.md`
