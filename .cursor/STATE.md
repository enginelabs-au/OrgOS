# STATE.md

## Current Objective

- Live Papership web UI is `docs/ui-blueprint/blueprint-2` exactly (D-21 / D-22) at **`/papership`** (D-32). Prism-head mark is app/tab icon only, not in-app. Canonical file is `brand/papership-icon.png`.

## Current Status

- 2026-09-12 owner icon render applied: transparent master plus platform favicon/PWA/iOS/Android/Tauri slots. Name `orgos-icon` replaced by `papership-icon`.
- Provider rename closeout: GitHub `enginelabs-au/papership`, App `papership-dev`, local folder `/Users/camdouglas/papership`, local secrets copied to `~/.config/papership/`. Vercel dashboard name is already `papership`; Git link still shows `enginelabs-au/OrgOS` (redirects).

## Project Phase

- Phase 5 closed (G7 PASS). Active plan: `docs/plans/phase_6_commercial_delivery_plan.md` (R4 / intake 11, draft). One execution phase plan remains after Phase 6 (Phase 7).

## Active Plan

- `docs/plans/phase_6_commercial_delivery_plan.md` (status: draft)

## Active Workstream

- `docs/workstreams/20260910-engine-labs-company-os/manifest.md` (Tier 3; G7 PASS; Phase 6 plan drafted)

## Active Role and Gate

- G7 PASS. G9 not started. Owner residuals in `docs/handover/outstanding-actions-and-decisions.md`.

## Predecessor Handoff

- Phase 5 G7: `project-lead-subagent/phase-5-handoff.md`
- Security Phase 5: `security-engineer-subagent/phase-5-handoff.md` (PASS with residuals)

## Pending Remediation

- Hermes GET `/health` hang (HEAD-first probe already used).
- Mailbox `Environment=` hygiene (owner/VPS).
- Vercel Git connection still lists `enginelabs-au/OrgOS` (redirects to `papership`). Dashboard project name is `papership`.
- Local GitHub App is `papership-dev`. VPS is Hermes only.
- Gmail/Slack live OAuth credentials missing (names wired).

## Owner Decision

- 2026-09-12: leftover sweep to Papership in the current tree; owner will rename GitHub / App / Vercel after other names; then agent updates locked files.
- 2026-09-12: D-22…D-33 stand.

## Active Instructions

- `/instructions/LAUCH.md`, `/instructions/PROJECT_PLANNING.md`, `/instructions/SUBAGENTS.md`, `/instructions/ROLES.md`.

## Active Items

- Phase 6 implementation started (T6-1…T6-4 first slice). G9 not started.

## Files in Active Use

- `/STATE.md`
- `docs/plans/phase_6_commercial_delivery_plan.md`
- `docs/handover/resume-after-provider-rename.md`
- `docs/handover/rename-owner-first-providers.md`
- `docs/handover/outstanding-actions-and-decisions.md`

## Open Blockers

- None in `/memory/blockers/`.

## Attempts Performed

- 2026-09-12: Pass A leftover sweep (NOTICE, grants alias, token, store path). Locked files untouched.
- 2026-09-12: GitHub App locked-file follow-up. Local `/health` `"github":"reachable"`.
- 2026-09-12: SSH `hermes-vps` (user `hermes`) and `droplet-campbell` (user `root`) on `hermes-droplet-campbell`. No `~/.config/orgos`, no `~/.config/papership`, no `GITHUB_APP_*` files, no listener on `:8000`. Did not copy the App PEM onto Hermes (API-only credential).

## Decisions and Assumptions

- D-25 does not authorise live write/external Hermes `accepted`.
- D-32: canonical URL is `/papership`; `/cc-org-dash` is a redirect.
- D-33: owner asked to implement Phase 6 this turn (2026-09-12).
- CA-10 still blocks published rates and live charges. G9 is structure/test-mode only.
- Local GitHub defaults are `papership` / `.papership/loop/`; published `.orgos/loop/` stays readable. Vercel project name is `papership`; Git link may still say OrgOS.

## Current Working State

- Branch `cursor/phase-6-planning-cc89`.
- GitHub App `papership-dev` (App ID `4918983`, installation `161090499`) is live-reachable locally. Product API does not use the App OAuth client pair.

## Next Actions

1. Implement Phase 6 (T6-5…T6-8, remaining role `phase-6-*` artifacts, G9). Do not generate Phase 7 until G9.
2. Do not treat write/external Hermes tools as `accepted`.
3. Optional residual: relink Vercel Git from `OrgOS` to `papership` (redirect works today). GitHub org/App dashboard avatars are owner-only if they still show the old mark.

## Last Updated

- 2026-09-12T09:32Z — Owner prism icon supersedes all prior files; `orgos-icon` → `papership-icon` on web/desktop/PWA/iOS/Android/Tauri.
