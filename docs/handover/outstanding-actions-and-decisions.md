# Outstanding actions and decisions

Canonical log after Phase 5 G7 PASS (2026-09-12) and owner authorization to plan Phase 6. Do not store secret values here.

Related: `docs/decisions/2026-09-12-phase-4-closeout.md` (D-22…D-30), `docs/decisions/2026-09-12-phase-5-planning-authorized.md` (D-31), `docs/decisions/2026-09-12-papership-canonical-route.md` (D-32), `docs/decisions/2026-09-12-phase-6-planning-authorized.md` (D-33), `docs/decisions/2026-09-12-phase-7-planning-authorized.md` (D-34), `docs/handover/phase-4-owner-actions.md`, `docs/plans/phase_6_commercial_delivery_plan.md`, `docs/plans/phase_7_ecosystem_mobile_plan.md`, `docs/handover/resume-after-provider-rename.md`.

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
| D-29 | Historical public labels Free / Basic / Professional / Enterprise | Superseded for display by D-35 Free / Pro / Max / Enterprise |
| D-35 | Trial rate card published | Charges stay off until a later owner flip |
| D-30 | No public build-log | Record only until a later publish decision |
| D-31 | Owner authorized Phase 5 **planning** | Generate `phase_5_company_operations_plan.md`; implemented; G7 PASS |
| D-32 | Canonical product route is `/papership` | Leftover `/cc-org-dash` redirects; storage keys `papership-*` with legacy migrate |
| D-33 | Owner authorized Phase 6 **planning** | Generate `phase_6_commercial_delivery_plan.md`; implemented; G9 PASS |
| D-34 | Owner authorized Phase 7 **planning** | Implemented; G11 PASS |

Also standing: D-12 / D-14 user-owned data; AUTH-25 / D-17 Hermes catalog; AUTH-29 adaptive views are schema-validated trusted components with no filesystem/shell/database/credential access.

## 2. Owner-only residuals (none block Phase 7 planning)

| Action | Why agent cannot | Blocks planning? | Blocks a live second seat / live connector? |
|---|---|---|---|
| Click **Record measurement notice** on the live store (Settings → Data) | live tenant | no | yes for a real second human or guest |
| Create Google OAuth client and Slack app; set `GMAIL_OAUTH_CLIENT_ID`, `GMAIL_OAUTH_REDIRECT_URL`, `SLACK_CLIENT_ID` on the API host | owner accounts | no | yes for live Gmail/Slack |
| Relink/rename Vercel project `orgos` | provider dashboard | no | no |
| Move mailbox credentials off systemd `Environment=` | VPS owner | no | hygiene, not a plan gate |
| Hermes GET `/health` hang | Hermes ops | no | HEAD-first probe already used |
| Apple signing, DigitalOcean, backup restore drill | accounts | no | R1 residual |
| `execute_release` | owner | no | publication |
| Fire live write/external Hermes tools | needs a **new** Security PASS | no | do not treat D-25 as that licence |
| Public build-log | D-30 | no | later explicit publish decision |
| Local folder rename `~/OrgOS` → `~/Papership` | operator machine | no | safe after reopen |
| CA-10 publish rates; CA-10 activate charges (two decisions) | owner commercial gate | no for G9 structure / G11 | yes for any public number or charge |
| Apple Developer + App Store / Google Play + signing | owner accounts | no for G11 simulator shells | yes for store listings |

Local GitHub App follow-up is done (`papership-dev`, `GITHUB_APP_REPO=papership`, new receipts `.papership/loop/`, dual-read `.orgos/loop/`). VPS has no host GitHub App env to change. Vercel slug remains an owner residual.

## 3. Agent-capable next work

Closed 2026-09-12. `docs/plans/final_implementation_checklist.md` is written. OQ-G2 and erasure-intent buttons exist. ERA-15 dry-run is list-only (`node scripts/era15-dry-run.mjs`). Remaining work is the owner walk in that checklist. No Phase 8.

## 4. Closed owner questions (do not re-ask)

OQ-2, OQ-3, OQ-4, OQ-G1, OQ-G2 are accepted (D-27…D-30, D-23). Visual review is approved (D-22). Security pass for Phase 4 connectors is accepted (D-25).
