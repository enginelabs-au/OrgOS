# STATE.md

## Current Objective

- Live Papership web UI is `docs/ui-blueprint/blueprint-2` exactly (D-21). Prism-head mark is app/tab icon only, not in-app.

## Current Status

- Phase 4 **implementation** (not planning). Plan exists and is `implementing`. T4-0 and T4-1 are done. Blueprint-2 port mounted at `/cc-org-dash`. Hybrid of blueprint-1 chrome withdrawn. Live slugs (`orgos` / `OrgOS` on GitHub, Vercel, `~/.config/orgos/`) left as residuals.

## Project Phase

- Phase 4 implementation, paused after the D-21 UI pivot. Next planned task is T4-2. Do not generate Phase 5 until G5.

## Active Plan

- `docs/plans/phase_4_collaboration_connections_plan.md`

## Active Workstream

- `docs/workstreams/20260910-engine-labs-company-os/manifest.md` (Tier 3; index is stale vs Phase 4)

## Active Role and Gate

- Owner visual review of the D-21 blueprint-2 port. T4-2 (OQ-G2 notice + `oq_g2_recorded` gate) is the next Phase 4 implementation task.

## Predecessor Handoff

- Security live-tools CONDITIONAL: `security-engineer-subagent/phase-3-live-tools-handoff.md`
- Owner handoff: `delivery/owner-handoff.md` (`APPROVE`)

## Pending Remediation

- Hermes GET `/health` hang.
- Mailbox `Environment=` hygiene.
- Worker job consumer / subscribe (F-T33-SEC-03/09).
- AUTH-12 HTTP not used for PR #1.
- Residual live slugs still named OrgOS until the owner renames those providers.

## Owner Decision

- 2026-09-12: product UI is blueprint-2 exactly (D-21); product name Papership (D-20).
- 2026-09-11: live tools + real PR + leftovers, then APPROVE, then Phase 4.

## Active Instructions

- `/instructions/LAUCH.md`, `/instructions/PROJECT_PLANNING.md`, `/instructions/SUBAGENTS.md`, `/instructions/ROLES.md`.

## Active Items

- Blueprint-2 exact port (complete, pending owner visual review).

## Files in Active Use

- `/STATE.md`
- `docs/decisions/2026-09-12-blueprint-2-product-ui.md`
- `apps/web/src/blueprint2/App.jsx`
- `apps/web/src/pages/cc-org-dash.jsx`

## Open Blockers

- None in `/memory/blockers/`.

## Attempts Performed

- 2026-09-12: replaced hybrid with blueprint-2 port; D-21; Today shell verified at http://127.0.0.1:5173/cc-org-dash.
- 2026-09-11: live `memory_read` `accepted`; PR https://github.com/enginelabs-au/OrgOS/pull/1.

## Decisions and Assumptions

- D-21: web product UI is blueprint-2 exactly. Fixture copy from the mock is allowed. Desktop Tauri is not this port. Mobile bottom tabs are R4.
- D-20: Papership is the display name. Folder rename of `~/OrgOS` is safe. Do not rename GitHub/Vercel/App slugs in code until those providers change.

## Current Working State

- In-app product icon removed from web (top bar, auth, compose, Hey) and desktop wordmark/sign-in. Favicon, PWA, and Tauri icons unchanged.

## Next Actions

1. Owner visual review of the blueprint-2 port (Hey dock, theme cycle, remaining tabs).
2. Resume T4-2: Settings → Data measurement notice and `oq_g2_recorded` gate (legal OQ-G2 is required only before a live second seat).
3. Continue T4-3…T4-11 after T4-2; do not generate Phase 5 until G5.
4. Do not treat write/external Hermes tools as `accepted`.

## Last Updated

- 2026-09-12T04:30Z — status review: Phase 4 implementation (T4-0/T4-1 done; T4-2 next).
