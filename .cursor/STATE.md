# STATE.md

## Current Objective

- Phase 2 (intake 08) is the active plan. Start at T2-1 interception spike. Public web is `apps/web` on Vercel project `orgos`.

## Current Status

- Phase 1 G1 still **CONDITIONAL** (H-6 accepted via D-09; live Compose and packaged Tauri still open). Phase 2 plan **active**. T2-1 not implemented.

## Project Phase

- Phase 2 development loop — T2-1 pending.

## Active Plan

- Active: `docs/plans/phase_2_development_loop_plan.md`
- Completed: `docs/plans/phase_1_foundation_plan.md` (`complete_conditional`)

## Active Workstream

- `docs/workstreams/20260910-engine-labs-company-os/manifest.md` (Tier 3)

## Active Role and Gate

- Orchestrating lead. Next implementation: `software-engineer-subagent` T2-1 (`phase-2-t2-1-charter.md`).

## Predecessor Handoff

- `docs/workstreams/20260910-engine-labs-company-os/project-lead-subagent/phase-1-handoff.md` (CONDITIONAL)

## Pending Remediation

- Live Compose + port scan (Docker unavailable on this machine 2026-09-11).
- Packaged Tauri.
- F-G1 emit still off (not implied by H-6).
- Vercel extras cannot be deleted without `vercel login` / token. Domain `enginelabs.com.au` still on `enginelabs-au-site`.
- Cloud Task from this Mac may still report 0 remotes.

## Owner Decision

- H-6: D-01…D-08 and five policies accepted (D-09), owner request 2026-09-11.
- Keep Vercel project `orgos` only. Combine public entry into `apps/web`.
- Do not delete Shuffle / Distroclub / other product projects.
- Phase 2 live Hermes still needs H-4, H-5, GitHub App, model key names.

## Active Instructions

- `/instructions/LAUCH.md`, `/instructions/PROJECT_PLANNING.md`, `/instructions/SUBAGENTS.md`, `/instructions/ROLES.md`.

## Active Items

- Public site: `apps/web`
- Vercel runbook: `/memory/runbooks/vercel-orgos-single-site.md`
- T2-1 charter: `docs/workstreams/20260910-engine-labs-company-os/software-engineer-subagent/phase-2-t2-1-charter.md`
- Risk tier: Tier 3

## Files in Active Use

- `/STATE.md`
- `docs/plans/phase_2_development_loop_plan.md`
- `docs/decisions/2026-09-11-owner-ratification-h6.md`
- `apps/web/`
- `/memory/blockers/cursor-cloud-launch.md`
- `/memory/runbooks/vercel-orgos-single-site.md`

## Open Blockers

- `.cursor/memory/blockers/cursor-cloud-launch.md`
- Vercel project delete + `enginelabs.com.au` move (owner CLI/dashboard)

## Attempts Performed

- 2026-09-11: H-6 recorded; `apps/web` added; Vercel MCP listed 11 projects; CLI has no token; Docker unavailable.

## Decisions and Assumptions

- D-01…D-08 `accepted` (D-09).
- Public website is Vite on `apps/web`, not a port of the full Next `enginelabs-au/site` app.
- Third Vercel “extra” is not identified; only `enginelabs-au-site` is a confirmed Engine Labs public entry besides `orgos`.

## Current Working State

- Monorepo includes `apps/web`. Phase 2 active. Hermes not installed.

## Next Actions

1. Cloud or local T2-1 spike (SP-1…SP-7) per charter.
2. Owner: `npx vercel login`, move `enginelabs.com.au` to `orgos`, delete confirmed extras.
3. Owner when ready: H-4, H-5, GitHub App, model key names.

## Last Updated

- 2026-09-11T08:30Z — H-6 accepted; phase 2 active; single-site web added.
