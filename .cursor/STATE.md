# STATE.md

## Current Objective

- Live Papership web UI is `docs/ui-blueprint/blueprint-2` exactly (D-21 / D-22) at **`/papership`** (D-32). At `max-width: 767px` the live chrome is the R4 compressed layout from `OrgOS Mobile.dc.html`. Prism-head mark is app/tab icon only, not in-app.

## Current Status

- Web mobile chrome shipped: bottom tabs Today/Work/Inbox/Hey Engine, left rail sheet, full-screen Hey Engine sheet, 2×2 health, 44px Approve/Reject/Stop.
- Phase 6 G9 PASS (residuals). Phase 7 native-client plan not generated until owner proceeds.

## Project Phase

- Phase 6 closed (G9 PASS with residuals). Active plan: `docs/plans/phase_6_commercial_delivery_plan.md` (complete). Next plan after owner proceeds: `docs/plans/phase_7_ecosystem_mobile_plan.md`.

## Active Plan

- `docs/plans/phase_6_commercial_delivery_plan.md` (status: complete)

## Active Workstream

- `docs/workstreams/20260910-engine-labs-company-os/manifest.md` (Tier 3; G9 PASS)

## Active Role and Gate

- G9 PASS (2026-09-12). Residuals: CA-10, D-25, Stripe test account, OQ-G2 live notice.
- This turn skipped a new role matrix: implementing already-specified R4 mobile HTML (PM/Security/Growth/PL not needed; UI spec is the blueprint).

## Predecessor Handoff

- Phase 6 G9: `project-lead-subagent/phase-6-handoff.md`
- Security Phase 6: `security-engineer-subagent/phase-6-handoff.md` (PASS with residuals)

## Pending Remediation

- Hermes GET `/health` hang (HEAD-first probe already used).
- Mailbox `Environment=` hygiene (owner/VPS).
- Vercel project `papership` Git link is `enginelabs-au/papership` (verified 2026-09-12). Latest production deploy `dpl_pZLd2HSgook6cPtmsrFPvbu4SSu6` was ERROR.
- Local GitHub App is `papership-dev`. VPS is Hermes only.
- Gmail/Slack live OAuth credentials missing (names wired).
- GitHub org/App dashboard avatars are owner-only.

## Owner Decision

- 2026-09-12: leftover sweep to Papership in the current tree; owner will rename GitHub / App / Vercel after other names; then agent updates locked files.
- 2026-09-12: D-22…D-33 stand. D-21 item 5 updated: live web ships R4 compressed chrome at ≤767px.
- 2026-09-12: purple icon plate stays; only pixels outside the rounded square may be cleared.

## Active Instructions

- `/instructions/LAUCH.md`, `/instructions/PROJECT_PLANNING.md`, `/instructions/SUBAGENTS.md`, `/instructions/ROLES.md`.

## Active Items

- Phase 6 complete. Web mobile chrome adapted. Wait for owner before Phase 7 planning.

## Files in Active Use

- `/STATE.md`
- `apps/web/src/blueprint2/App.jsx`
- `apps/web/src/blueprint2/screens.jsx`
- `apps/web/src/blueprint2/blueprint2.css`
- `docs/decisions/2026-09-12-blueprint-2-product-ui.md`

## Open Blockers

- None in `/memory/blockers/`.

## Attempts Performed

- 2026-09-12: Restored purple plate on `papership-icon`; fringe-only transparency.
- 2026-09-12: T6-5…T6-8 + G9 artifacts. pytest 8; static scan 5.
- 2026-09-12: Live web R4 mobile chrome. Today verified at 390×844; desktop 1280×800 still docked. Static scan 6. MCP click-through of Work/Inbox/Hey blocked by fail-closed hook.

## Decisions and Assumptions

- D-25 does not authorise live write/external Hermes `accepted`.
- D-32: canonical URL is `/papership`; `/cc-org-dash` is a redirect.
- D-33: owner asked to implement Phase 6 (2026-09-12).
- CA-10 still blocks published rates and live charges. G9 is structure/test-mode only.
- Local GitHub defaults are `papership` / `.papership/loop/`; published `.orgos/loop/` stays readable. Vercel project name is `papership`; Git link is `enginelabs-au/papership`.
- Face ID / fingerprint on the auth card are offered on narrow viewports only; they do not authenticate in the browser.

## Current Working State

- Branch `cursor/phase-6-planning-cc89`.
- GitHub App `papership-dev` (App ID `4918983`, installation `161090499`) is live-reachable locally. Product API does not use the App OAuth client pair.

## Next Actions

1. Owner proceeds → generate `docs/plans/phase_7_ecosystem_mobile_plan.md` (do not implement until asked).
2. Do not treat write/external Hermes tools as `accepted`.
3. Optional: replace GitHub org/App dashboard avatars.
4. Owner asked whether Phase 7 planning can start — yes (plan only; do not implement until asked).

## Last Updated

- 2026-09-12T10:36Z — Ready to commit/push mobile chrome + inset-squircle icon. Phase 6 remains G9 PASS; Phase 7 planning is unblocked.
