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

- G11 PASS (2026-09-12). Checklist residuals parked: CA-10, D-25 (OT-10 later), ERA-15 (OT-13 later). OQ-G2 recorded locally.

## Predecessor Handoff

- Phase 7 G11: `project-lead-subagent/phase-7-handoff.md`
- Security Phase 7: `security-engineer-subagent/phase-7-handoff.md` (PASS with residuals)

## Pending Remediation

- OQ-G2 recorded on local store 2026-09-12T15:20Z. Local API is up at `127.0.0.1:8000` after the overlay segfault (OT-24). Vercel still cannot hold this flag.
- Gmail/Slack OAuth start/callback shipped. Host secrets are loaded. Local Gmail (OT-25) and Slack (OT-26) are both connected with sealed tokens. Hermes env was not copied.
- OT-16 done: live Hermes `GET /health` on `:8642` is 200 (~1ms); HEAD 405. Units were active. HEAD-first probe stays.
- OT-29: droplet `active_provider` is OpenRouter; OpenRouter pool exhaustion cleared; free fallbacks restored. Local `~/.hermes/config.yaml` `model.provider` is `openrouter`.
- OT-30: serve now has the OpenRouter key in its EnvironmentFile; `setup.runtime_check` should show ready. Desktop may need one reconnect after the serve restart.
- OT-31: OpenRouter Settings picker now uses the live tool-capable catalog (377). Cap is 999 / uncapped, not None. Serve restarted.
- OT-32: chat OpenRouter featured shortlist is curated (~48) plus current (`openai/gpt-5.6-luna-pro` in featured). Cheap capabilities skip per-model lookups on the long tail. Serve restarted again — Desktop needs one reconnect.
- OT-05 done: live Hermes user systemd has no `Environment=EMAIL_*`. OT-06…OT-14 parked in `docs/handover/future-tasks.md`. OT-15 JWT is sessionStorage + memory. OT-16 GET `/health` is 200.
- Leftover feature branches are gone from git (`main` + `origin/main` only). Cursor may still show closed-PR names. Local and origin `main` are `451a7f3`. Vercel will pick up the Git push.

## Owner Decision

- 2026-09-13: trial competitor-average rate card (D-35) Free/Pro/Max/Enterprise. Charges stay off. Desktop must load current web chrome. Extra git branches are deleted in git. Hermes env must not be reused for Papership OAuth. Destroy-infra is not recommended.

## Active Instructions

- `/instructions/LAUCH.md`, `/instructions/PROJECT_PLANNING.md`, `/instructions/SUBAGENTS.md`, `/instructions/ROLES.md`.

## Active Items

- Live outstanding list: `docs/handover/outstanding-tasks.md` (repeat every turn).
- Owner follows `docs/plans/final_implementation_checklist.md` §6.

## Files in Active Use

- `/STATE.md`
- `docs/handover/outstanding-tasks.md`
- `docs/handover/future-tasks.md`
- `docs/workstreams/20260913-d25-repass/security-engineer-subagent/handoff.md`
- `docs/plans/final_implementation_checklist.md`
- `apps/web/src/api/papership.js`
- `apps/web/src/blueprint2/App.jsx`

## Open Blockers

- None in `/memory/blockers/`.

## Attempts Performed

- 2026-09-12: moved intake + UI spec into `docs/blueprints/` (`company_agent_system_blueprint.md`, `ui-blueprint.md`). Capture folder `docs/ui-blueprint/` stayed put.

## Decisions and Assumptions

- D-25 lift review 2026-09-12 CONDITIONAL; re-pass 2026-09-13 CONDITIONAL — write/external Hermes `accepted` unauthorized (`20260913-d25-repass`).
- D-35 trial rate card published; charges stay off.
- Erasure records intent only; destroy stays false.
- ERA-15 script is list-only.
- No Phase 8. Desktop Tauri loads `@papership/web` at `/papership`. Marketing site untouched.
- Do not copy Hermes VPS env into Papership Gmail/Slack.
- Same Hermes Google Cloud *project* may host a new Papership OAuth client. Same Hermes Slack *app* / tokens must not be reused.

## Current Working State

- Branch `main` @ `451a7f3` (pushed). No leftover local or remote feature refs. Closed PRs 1–5 still exist as GitHub history.
- GitHub App `papership-dev` is local. VPS is Hermes only.
- Local API sources `~/.config/papership/connectors.env`. OT-25 Gmail and OT-26 Slack are both `configured` with `has_token` on the local store. Send stays approval-then-receipt. Vercel still cannot hold these tokens.

## Next Actions

1. Repeat `docs/handover/outstanding-tasks.md` open rows every turn (none open after 2026-09-13 park).
2. Do not treat write/external Hermes tools as `accepted`.
3. Charges stay off until a later owner flip (OT-08, parked).

## Last Updated

- 2026-09-12T17:05Z — Owner asked to push. `451a7f3` on `origin/main` as Cursor Agent after GH007 rejected `shuffle.ops@gmail.com`.
