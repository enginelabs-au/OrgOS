# STATE.md

## Current Objective

- Restore OrgOS product UI from `docs/ui-blueprint` onto Vercel `orgos`. Do not touch Engine Labs marketing. Close remaining G1 evidence. Phase 2 waits on owner H-4/H-5/GitHub/model key for live spike.

## Current Status

- Product identity corrected (D-10). `apps/web` is the blueprint `/cc-org-dash` UI. Engine Labs site untouched. No extra OrgOS Vercel projects existed to delete.

## Project Phase

- Phase 2 plan active; T2-1 live spike not started (needs Hermes pin / H-5).

## Active Plan

- `docs/plans/phase_2_development_loop_plan.md`

## Active Workstream

- `docs/workstreams/20260910-engine-labs-company-os/manifest.md` (Tier 3)

## Active Role and Gate

- Orchestrating lead. T2-1 blocked on owner Hermes pin + licence (H-5) for a live inventory.

## Predecessor Handoff

- `docs/workstreams/20260910-engine-labs-company-os/project-lead-subagent/phase-1-handoff.md` (CONDITIONAL)

## Pending Remediation

- Cursor Cloud GitHub App access (owner).
- Docker Compose when Docker is installed; local API + `scripts/port-scan.sh` is the substitute.
- Packaged Tauri debug: `apps/desktop/src-tauri/target/debug/bundle/macos/OrgOS.app` (local only, not committed).
- F-G1 emit remains off (recommended until first real run).

## Owner Decision

- D-10: OrgOS is the product; never replace `enginelabs.com.au`.
- Do not delete any non-orgos Vercel projects.
- F-G1: leave emit off unless owner says turn it on after reading `docs/handover/phase-2-owner-actions.md`.

## Active Instructions

- `/instructions/LAUCH.md`, `/instructions/PROJECT_PLANNING.md`, `/instructions/SUBAGENTS.md`, `/instructions/ROLES.md`.

## Active Items

- OrgOS UI: `apps/web` (from `docs/ui-blueprint`)
- Owner actions: `docs/handover/phase-2-owner-actions.md`
- Cloud blocker: `/memory/blockers/cursor-cloud-launch.md`

## Files in Active Use

- `/STATE.md`
- `docs/plans/phase_2_development_loop_plan.md`
- `docs/decisions/2026-09-11-orgos-product-identity.md`
- `apps/web/`
- `docs/ui-blueprint/`
- `/memory/blockers/cursor-cloud-launch.md`

## Open Blockers

- `.cursor/memory/blockers/cursor-cloud-launch.md`

## Attempts Performed

- 2026-09-11: Vercel login works; listed 11 projects; none named web/desktop/api/worker. Restored blueprint into `apps/web`.

## Decisions and Assumptions

- D-01…D-08 accepted (D-09). D-10 accepted.
- API/worker are not Vercel services.

## Current Working State

- Blueprint UI in `apps/web`. Marketing site not touched.

## Next Actions

1. Finish web build + push.
2. Local API + port-scan; Tauri debug bundle if toolchain allows.
3. Wait on H-4/H-5/GitHub App/model key before calling phase 2 implementation ready.

## Last Updated

- 2026-09-11T09:10Z — D-10; blueprint UI restored; Engine Labs site isolated.
