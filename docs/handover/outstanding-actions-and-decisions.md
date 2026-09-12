# Outstanding actions and decisions

Canonical log after Phase 4 G5 PASS (2026-09-12) and owner authorization to plan Phase 5. Do not store secret values here.

Related: `docs/decisions/2026-09-12-phase-4-closeout.md` (D-22…D-30), `docs/decisions/2026-09-12-phase-5-planning-authorized.md` (D-31), `docs/handover/phase-4-owner-actions.md`, `docs/plans/phase_5_company_operations_plan.md`.

## 1. Standing product decisions (still binding)

| ID | Decision | Consequence |
|---|---|---|
| D-20 | Product name is **Papership**; Engine Labs is the company | Do not edit `www.enginelabs.com.au` or Vercel `enginelabs-au-site` |
| D-21 / D-22 | Live chrome is `docs/ui-blueprint/blueprint-2` exactly; visual review approved | Prism-head mark is app/tab icon only; no hybrid overlay |
| D-23 | OQ-G2 measurement notice and legal basis accepted | Store stays fail-closed until live `POST /settings/oq-g2` |
| D-24 | Gmail/Slack proceed as contract + wizard | Live OAuth needs owner credentials; send = approval then receipt |
| D-25 | Phase 4 security pass accepted for seats/wizard/destination class/intersection | Does **not** authorise live write or external Hermes `accepted` |
| D-26 | In-repo slug `papership` / UI **Papership** | Do not rename the GitHub remote from this workstream |
| D-27 | First R3 domains: B01 strategy/governance, B03 people/capacity; memory manager + adaptive views are R3 core | Phase 5 scope |
| D-28 | R2 = intake 09, R3 = 10, R4 = 11+12 | Phase numbering locked |
| D-29 | Public tier labels Free / Basic / Professional / Enterprise | **No prices**, allowances, seat counts, or rates until R4 CA-10 |
| D-30 | No public build-log | Record only until a later publish decision |
| D-31 | Owner authorized Phase 5 **planning** (this turn) | Generate `phase_5_company_operations_plan.md`; do not implement until asked |

Also standing: D-12 / D-14 user-owned data; AUTH-25 / D-17 Hermes catalog; AUTH-29 adaptive views are schema-validated trusted components with no filesystem/shell/database/credential access.

## 2. Owner-only residuals (none block Phase 5 planning)

| Action | Why agent cannot | Blocks planning? | Blocks a live second seat / live connector? |
|---|---|---|---|
| `POST /settings/oq-g2` on the live store | live tenant | no | yes for a real second human or guest |
| Create Google OAuth client and Slack app; set `GMAIL_OAUTH_CLIENT_ID`, `GMAIL_OAUTH_REDIRECT_URL`, `SLACK_CLIENT_ID` on the API host | owner accounts | no | yes for live Gmail/Slack |
| Rename GitHub `enginelabs-au/OrgOS`, App `orgos-dev`, Vercel `orgos`, then keep `GITHUB_APP_REPO` in sync | provider dashboards | no | no |
| Move mailbox credentials off systemd `Environment=` | VPS owner | no | hygiene, not a plan gate |
| Hermes GET `/health` hang | Hermes ops | no | HEAD-first probe already used |
| Apple signing, DigitalOcean, backup restore drill | accounts | no | R1 residual |
| `execute_release` | owner | no | publication |
| Fire live write/external Hermes tools | needs a **new** Security PASS | no | do not treat D-25 as that licence |
| Public build-log | D-30 | no | later explicit publish decision |
| Local folder rename `~/OrgOS` → `~/Papership` | operator machine | no | safe after reopen |

Live receipt path `.orgos/loop/` and `GITHUB_APP_REPO` stay as-is until the owner renames the GitHub repository.

## 3. Agent-capable next work (not started this turn)

Phase 5 implementation is **closed** (G7, 2026-09-12). Do not start Phase 6 until the owner asks.

G7 closed. Two execution phase plans remain: Phase 6 (R4 commercial), Phase 7 (R4 ecosystem/mobile). Verification phases 13–18 re-run per release and are not extra build phases.

## 4. Closed owner questions (do not re-ask)

OQ-2, OQ-3, OQ-4, OQ-G1, OQ-G2 are accepted (D-27…D-30, D-23). Visual review is approved (D-22). Security pass for Phase 4 connectors is accepted (D-25).
