---
plan: phase_4_collaboration_connections
status: complete
created: 2026-09-11
updated: 2026-09-12
owner: lead-agent
source_phase: docs/plans/phase_3_release_verification_plan.md
predecessor_gate: G4 owner APPROVE (2026-09-11); D-19 plan; live read `accepted` + PR #1
workstream: docs/workstreams/20260910-engine-labs-company-os/manifest.md
blueprint: docs/blueprints/2026-09-10_engine_labs.md
intake: docs/Company_Agent_System_Blueprint.md (Phase 09)
release: R2 (proposal); gate G5 implementation / G6 owner
risk_tier: tier_3
---

# Phase 4: Collaboration and connections — Engine Labs / Papership

Generated after Phase 3 G3 CONDITIONAL. Owner authorized this plan (D-19) without G4 `APPROVE` or R1 closure. **Do not implement until this file exists and a later turn starts T4-0.** Papership UI remains `apps/web` `/cc-org-dash` and `apps/desktop`. Do not edit `www.enginelabs.com.au`.

## 1. Objective

Build intake Phase 09 (collaboration and connections) for the four R2 registry rows plus the seat and connection surfaces that make them usable: Project Lead and Operator templates, a connection-setup wizard, generalized source-permission intersection, and one additional connector behind the same policy as GitHub. Carry R1 residuals that would make R2 unsafe if ignored.

## 2. Relation to the end-state

R1 delivered a founder-only governed loop substrate. R2 is the first multi-seat, multi-connector slice. It does not start memory-manager / adaptive views (R3) or commercial delivery (R4). After G5, generate an R2 verification/close plan or, only if the owner treats R1+R2 as one closure, the final checklist.

## 3. Entry criteria and inherited evidence

- Phase 3 `complete_conditional`. Worker 27 / API 44. G3 CONDITIONAL (`project-lead-subagent/phase-3-g3-handoff.md`).
- D-19: plan now; not R1 APPROVE.
- Hermes HTTP API on VPS `127.0.0.1:8642`. Papership `/health` `hermes: reachable` via HEAD 405. GET `/health` hangs. Worker `api_server` from capabilities 401/`run_submission` only. Catalogued-read `accepted` allowed (Security live-tools CONDITIONAL).
- GitHub App live PR #1 (`open_pull` `dry_run: false`); AUTH-12 empty-perms refuse on the HTTP route.
- Founder seat only. `/cc-org-dash` People/Inbox still use fixtures in places. Desktop Work stepper exists.
- Usage first-baseline `not_captured` (F-G1 not accepted).
- Four R2 rows still `planned`: B02.01, B12.01, B23.01, P07.01.

## 4. Scope

- Seat templates: Project Lead and Operator (PRD-D.1, AUTH-21). Invite record + grant subset. No live mailbox invite until B12 is bound and OQ-G2 is decided.
- Connection setup view (PRD-A.5 / A.15 B.5): GitHub first (already bound), then one additional connector as **planned/dry-run** until owner supplies app credentials.
- Generalize grant ∩ source-permission intersection beyond GitHub (PRD-D.6).
- P07 sync checkpoints for the bound connector only (import/incremental labels, no silent overwrite).
- Inbox + People screens read Papership API (or honest empty), not `data.jsx` fixtures, on the product path.
- B02: persist a single organisation plus teams/departments as native records (no invented clients).
- B23: guest assignment **design + deny-by-default**. Live guests blocked until OQ-G2.
- Security re-review per new connector destination class (DRR-04, LIC-20).
- Carry T4-0 R1 residuals that block safe connector/tool use.

## 5. Non-goals

- R3 memory manager, adaptive views, personalisation.
- R4 billing, prices, entitlements, mobile, connector SDK.
- Marketing site / Vercel `enginelabs-au-site`.
- Live Hermes side-effecting tools without Security PASS.
- `execute_release`. Second Hermes messaging gateway.
- Wake-word vendor.
- Promoting B08.01 or R1-ACC-6…9 to VERIFIED without new SHA-linked evidence.
- Invented first-baseline metrics.

## 6. Current-state audit

| Area | Reality |
|---|---|
| Identity | Founder JWT + grants. No invite API. |
| Connectors | GitHub App health + dry-run PR. Hermes catalogued, not `accepted`. |
| UI | Desktop: Home/Work/Hey Engine/Runs. Web `/cc-org-dash` still has fixture People/Inbox/agent stub. |
| Policy | D-12/D-14 user-owned data; D-17 tool catalog; worker-only transport key. |
| Measurement | Emit flag exists; F-G1 not accepted. |

## 7. Assumptions, constraints, risks, and decisions

- `accepted` (D-19): plan R2 from G3 CONDITIONAL.
- `provisional`: first extra connector is **Gmail read/draft only** (send stays approval-bound) if the owner later supplies OAuth names; until then the wizard stays dry-run. Slack/Telegram/WhatsApp remain catalogue rows.
- `provisional`: OQ-G2 defaults to **in-product notice required, no live second seat** until the owner records a legal basis.
- `provisional`: B02 teams are founder-only writes in this phase.
- Risk: mailbox credentials already appear in the VPS gateway `Environment=` (owner; do not copy values).
- Constraint: no secrets in repo; API never reads `HERMES_API_SERVER_KEY`.
- D-10…D-18 stand.

## 8. Dependencies

T4-0 (R1 carry, no live tools) → T4-1 seats (templates + tests, no live invite) → T4-2 OQ-G2 notice copy → T4-3 connection wizard (GitHub live-read / dry-run write) → T4-4 intersection generalize → T4-5 B12 contract (fail-closed) → T4-6 P07 checkpoints for GitHub only → T4-7 Inbox/People API wiring → T4-8 B02 org/teams → T4-9 B23 guest deny-by-default → T4-10 Security → T4-11 PL G5.

Live Gmail/Slack apps and a second human user are owner-gated and must not block T4-1…T4-9 code.

## 9. Architecture and affected systems

Keep D-01 monorepo and D-04 adapter. New connector transports live in `services/api` (owner-bound OAuth) or worker policy (Hermes tools), never desktop. Seats are grant templates in the store. Sync state is a native table keyed by connector id. Destination classification for each connector is recorded before enablement.

## 10. Files and paths in scope

`services/api/app/` (seats, invites, connections, sync, grants), `services/api/tests/`, `services/worker/policy_hooks/` only if a new Hermes toolset is catalogued, `apps/desktop/src/views/`, `apps/web/src/components/cc-org-dash/` (People, Inbox, Integrations — remove fixture auth), `packages/ui/`, `docs/capabilities.md` (lead only, evidence-linked), `docs/verification.md`, workstream `phase-4-*`. No Engine Labs marketing project.

## 11. Supporting documents to create or update

- This plan (canonical).
- D-19 (done).
- `docs/handover/phase-4-owner-actions.md` as human actions accumulate.
- Role charters under `docs/workstreams/20260910-engine-labs-company-os/<role>/phase-4-*.md` when implementation starts.
- Registry rows move from `planned` only with evidence (D-02).

## 12. Ordered implementation tasks

**T4-0 R1 carry (complete 2026-09-11)** — Owner APPROVE landed live catalogued-read `accepted` and PR #1. HEAD-405 ≠ `api_server`; AUTH-12 empty-perms refuse; 302 serve-UI unit test exists; usage emit on (enum only). Deps: this plan. **Done.**

**T4-1 Seat templates (complete 2026-09-11)** — Persist `founder` / `project_lead` / `operator` templates; `POST /members/invites` creates a principal + subset grants, does not send mail. Tests: Operator/PL cannot `org.admin` invite or grant (PRD-D.3). Deps: T4-0. **Done.**

**T4-2 Measurement notice (complete 2026-09-12)** — Settings → Data copy for “What Papership measures”; `POST /settings/oq-g2` required before a non-founder seat. Owner accepted OQ-G2 (D-23). Deps: T4-1. **Done.**

**T4-3 Connection wizard (complete 2026-09-12)** — `GET /connections` + blueprint-2 Integrations overlay. GitHub `configured`; Gmail/Slack/Telegram/WhatsApp `planned` + handoff. No client secrets. Deps: T4-1. **Done.**

**T4-4 Intersection (complete 2026-09-12)** — `intersect_source_grants(provider, papership_grants, source_perms)`. Empty source perms fail closed. Deps: T4-3. **Done.**

**T4-5 B12 contract (complete 2026-09-12)** — Deny-by-default catalogue. Gmail/Slack planned/dry-run until owner OAuth names. Send = approval then receipt. Deps: T4-4. **Done.**

**T4-6 P07 GitHub checkpoints (complete 2026-09-12)** — Checkpoint on `GET /github/pulls` and `POST /connections/github/sync`. GitHub-only. Deps: T4-3. **Done.**

**T4-7 Product People/Inbox (complete 2026-09-12)** — Blueprint-2 People/Inbox overlay via `apps/web/src/api/papership.js`. Unauthenticated = honest empty. Desktop Connections/Settings mirrored. Deps: T4-1. **Done.**

**T4-8 B02 org/teams (complete 2026-09-12)** — Native org + teams; founder write; list on People. Deps: T4-1. **Done.**

**T4-9 B23 guests (complete 2026-09-12)** — Guest template + `POST /guests` refuses until OQ-G2. Deps: T4-2. **Done.**

**T4-10 Security (complete 2026-09-12)** — Owner accepted Phase 4 security pass (D-25). Destination class + intersection required. Write/external Hermes still gated. **Done (PASS with residuals).**

**T4-11 PL G5 (complete 2026-09-12)** — Role artifacts, verification R2 rows, capabilities `configured` with evidence. Phase 5 not generated from this file. **Done.**

## 13. Adaptive role and delegation map

| Role ID | Required or skipped | Reason | Predecessor | Status |
|---|---|---|---|---|
| product-manager-subagent | required | R2 ACC for seats, wizard, connectors | D-19 / this plan | PASS |
| ui-ux-developer-subagent | required | Connection setup + People/Inbox + Operator chrome (PRD-A.14) | PM | PASS |
| software-engineer-subagent | required | T4-0…T4-9 | UI/UX | PASS |
| security-engineer-subagent | required | T4-10; seats + connectors | SE | PASS (residuals: live OAuth, write Hermes) |
| growth-marketing-subagent | required | OQ-G2 notice; no prices; no invented baselines | Security | PASS |
| project-lead-subagent | required | G5 | Growth | PASS |

Charters are written when implementation starts. Same workstream id.

## 14. Test and validation matrix

| Requirement | Method | Expected |
|---|---|---|
| PRD-D.1 seats | pytest three templates; Operator 403 on admin | pass |
| PRD-D.3 delegation ceiling | PL cannot grant `org.admin` | pass |
| OQ-G2 | activating second seat without flag → 403 | pass |
| PRD-A.5 wizard | GitHub health; unsupported provider handoff | pass |
| PRD-D.6 intersection | empty source perms refuse live write | pass |
| B12 | unknown provider deny; send needs approval | pass |
| P07 | checkpoint row after GitHub list | pass |
| B23 | guest create refused | pass |
| AUTH-25 | no live Hermes `accepted` unless Security PASS | residual recorded |
| CA-10 | no prices in UI/docs | scan clean |

## 15. Security, privacy, reliability, accessibility, and performance checks

Carry F-T33-SEC-01…08. New connectors: destination class, least privilege, no desktop secrets, D-14 (user owns connected content). Operator UI: no prompts/schemas/runtime config (PRD-A.14). Closed Hey Engine stays unmounted. Contrast D-06/D-15. Reliability: sync failure is visible, not silent. No second gateway.

## 16. Environment-variable registry

Names only. No values.

| Variable name | Purpose | Scope | Required by phase | Source | Status |
|---|---|---|---|---|---|
| HERMES_API_BASE_URL | API probe | API | carried | existing | wired |
| HERMES_VERSION_PIN | pin | API/worker | carried | existing | wired |
| HERMES_API_SERVER_KEY | Hermes transport | worker only | carried | VPS | must not reach API |
| GITHUB_APP_* | repo connector | API | carried | existing | wired |
| GMAIL_OAUTH_CLIENT_ID | future B12 | API | T4-5 live only | owner | missing |
| GMAIL_OAUTH_REDIRECT_URL | future B12 | API | T4-5 live only | owner | missing |
| SLACK_CLIENT_ID | future B12 | API | later | owner | missing |

Do not add provider client secrets to the API allowlist until T4-5 Security PASS.

## 17. Deferred human-action queue

| Action | Why agent cannot | Earliest | Blocking now? |
|---|---|---|---|
| OQ-G2 legal basis / notice accept | legal/owner | before live second seat | no for templates |
| Gmail/Slack developer apps | owner accounts | T4-5 live | no for contract |
| Security PASS for Hermes `accepted` | independent gate | before tool runs | no for seats/wizard |
| Live GitHub `dry_run: false` | owner reauth | publication | no |
| F-G1 usage emit | owner | measurement | no |
| Move mailbox creds off systemd Environment= | VPS owner | now recommended | no |
| G4 R1 APPROVE | owner | R1 close | no (D-19) |

## 18. Rollback

Disable new connector `enabled` flags; refuse-start if artefact missing. Invites already persisted stay but grants can be revoked. No production DNS to roll back.

## 19. Acceptance (G5)

Three seat templates plus guest exist in the store with tests; connection wizard shows GitHub as configured and others as planned; intersection fail-closed; guest create refused until OQ-G2; People/Inbox not fixture-auth; no prices; no live write/external `accepted` tools; every required role has a verdict; R2 rows B02.01, B12.01, B23.01, P07.01 are `configured` with evidence (not `working`).

**G5 PASS** — 2026-09-12.

## 20. Completion evidence

- API `PYTHONPATH=/tmp/pydeps:. pytest -q` → 66 passed (2026-09-12).
- Worker job consumer unit: `services/worker/tests/test_jobs.py`. AUTH-25 yaml hashes refreshed to current catalog/artefact.
- UI: `apps/web/src/api/papership.js`, blueprint-2 People/Inbox/Connections/Settings, desktop Connections `/connections` + Settings measurement copy.
- Decisions: `docs/decisions/2026-09-12-phase-4-closeout.md` (D-22…D-30).
- Registry: `docs/capabilities.md` 0.1.2-phase4.
- Verification: `docs/verification.md` §6b.
- Role artifacts: `docs/workstreams/20260910-engine-labs-company-os/<role>/phase-4-handoff.md`.
- Owner queue: `docs/handover/phase-4-owner-actions.md`.

## 21. Deviations and follow-ups

Entered from G3 CONDITIONAL via D-19, not G4 APPROVE. R1-ACC-6…9 remain PARTIAL. Phase 5 (company operations) is not generated from this file.

## 22. Next Plan Generation Prompt

Read `/AGENTS.md`, the complete core agent context, `/instructions/PROJECT_PLANNING.md`, `/instructions/ROLES.md`, `docs/plans/phase_0_foundations_plan.md`, this completed plan, phase 3 plan, workstream handoffs, `docs/roadmap.md`, `docs/verification.md`. Confirm G5 and every required role gate. Then generate exactly one next plan: either `docs/plans/phase_5_company_operations_plan.md` (R3) or, if the owner is closing R1+R2 together, `docs/plans/final_implementation_checklist.md`. Do not implement that phase until the file exists.
