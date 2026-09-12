# STATE.md

## Current Objective

- Live Papership web UI is `docs/ui-blueprint/blueprint-2` exactly (D-21 / D-22) at **`/papership`** (D-32). At `max-width: 767px` the live chrome is the R4 compressed layout from `OrgOS Mobile.dc.html`. Prism-head mark is app/tab icon only, not in-app.

## Current Status

- Initial development closed. Phases 0–7 complete. Final checklist written. Project blueprints now live under `docs/blueprints/`.

## Project Phase

- Closure. Active plan: `docs/plans/final_implementation_checklist.md`. No Phase 8.

## Active Plan

- `docs/plans/final_implementation_checklist.md` (status: open — owner walk)

## Active Workstream

- `docs/workstreams/20260910-engine-labs-company-os/manifest.md` (Tier 3; G11 PASS)

## Active Role and Gate

- G11 PASS (2026-09-12). Checklist residuals: CA-10, D-25, OQ-G2 live click, Vercel redeploy, ERA-15 real destroy.

## Predecessor Handoff

- Phase 7 G11: `project-lead-subagent/phase-7-handoff.md`
- Security Phase 7: `security-engineer-subagent/phase-7-handoff.md` (PASS with residuals)

## Pending Remediation

- OQ-G2 must be recorded against a reachable API (`127.0.0.1:8000`), not the Vercel static host.
- Gmail/Slack Papership OAuth is still missing. Hermes mailbox/Slack env is a different credential class and will not be copied.
- Hermes GET `/health` hang (HEAD-first probe already used). Hermes units were inactive when last probed.
- Mailbox `Environment=` hygiene (owner/VPS).
- Push `main` after author rewrite (cursoragent@cursor.com).

## Owner Decision

- 2026-09-13: trial competitor-average rate card (D-35) Free/Pro/Max/Enterprise. Charges stay off. Desktop must load current web chrome. Extra git branches may be deleted. Hermes env must not be reused for Papership OAuth. Destroy-infra is not recommended.

## Active Instructions

- `/instructions/LAUCH.md`, `/instructions/PROJECT_PLANNING.md`, `/instructions/SUBAGENTS.md`, `/instructions/ROLES.md`.

## Active Items

- Owner follows `docs/plans/final_implementation_checklist.md` §6.

## Files in Active Use

- `/STATE.md`
- `docs/plans/final_implementation_checklist.md`
- `services/api/app/phase7.py`
- `apps/web/src/blueprint2/App.jsx`
- `scripts/era15-dry-run.mjs`

## Open Blockers

- None in `/memory/blockers/`.

## Attempts Performed

- 2026-09-12: moved intake + UI spec into `docs/blueprints/` (`company_agent_system_blueprint.md`, `ui-blueprint.md`). Capture folder `docs/ui-blueprint/` stayed put.

## Decisions and Assumptions

- D-25 lift review 2026-09-12 CONDITIONAL — write/external Hermes `accepted` unauthorized (`d25-lift-handoff.md`).
- D-35 trial rate card published; charges stay off.
- Erasure records intent only; destroy stays false.
- ERA-15 script is list-only.
- No Phase 8. Desktop Tauri loads `@papership/web` at `/papership`. Marketing site untouched.
- Do not copy Hermes VPS env into Papership Gmail/Slack.

## Current Working State

- Branch `main` (merge `7b1207e`). Feature branches 4/5/6 are ancestors. `origin/orgos-loop-r1-close` left unmerged (stale 5-line OrgOS loop note).
- GitHub App `papership-dev` is local. VPS is Hermes only.

## Next Actions

1. Owner: start local API, then Settings → Data → Record measurement notice.
2. Do not treat write/external Hermes tools as `accepted`.
3. Charges stay off until a later owner flip.

## Last Updated

- 2026-09-13T03:10Z — D-35 trial card, desktop retarget, OQ-G2 copy, branch cleanup.
