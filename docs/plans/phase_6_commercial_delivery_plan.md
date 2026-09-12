---
plan: phase_6_commercial_delivery
status: draft
created: 2026-09-12
updated: 2026-09-12
owner: lead-agent
source_phase: docs/plans/phase_5_company_operations_plan.md
predecessor_gate: G7 PASS (2026-09-12); D-27…D-33
workstream: docs/workstreams/20260910-engine-labs-company-os/manifest.md
blueprint: docs/blueprints/2026-09-10_engine_labs.md
intake: docs/Company_Agent_System_Blueprint.md (Phase 11)
release: R4 commercial slice (accepted D-28); gate G9 implementation / G10 owner
risk_tier: tier_3
---

# Phase 6: Commercial delivery — Engine Labs / Papership

Generated after Phase 5 G7 PASS. Owner authorized the plan (D-33) after a product click-through and the leftover `/cc-org-dash` rename (D-32). Papership UI remains `docs/ui-blueprint/blueprint-2` at **`/papership`**. Do not edit `www.enginelabs.com.au`. **Do not implement this plan until the owner asks.**

## 1. Objective

Build intake Phase 11 (commercial delivery) for the R4 commercial slice: structure entitlements, allowances, reservations, and limit enforcement in **billing test mode before any charge** (PRD-G.12). Settings/Plan chrome uses the accepted public labels Free / Basic / Professional / Enterprise (D-29 / OQ-4). Licensing-state (ERA-17) becomes a `configured` hook if evidence exists. No prices, allowance-as-numbers, seat counts, or rates appear until the two owner CA-10 decisions (publish rates; activate charges).

## 2. Relation to the project end-state

Phases 0–5 closed foundations, the development loop, R1 verification, R2 seats/connections, and R3 company operations. R4 is split (D-28): this phase is intake **11 only** (commercial structure). Intake **12** (ecosystem, mobile, remaining market domains, P19 SDK/packs) is Phase 7 and is **not** generated from this file. After G9, generate exactly one next plan: `docs/plans/phase_7_ecosystem_mobile_plan.md`. One execution phase plan remains after this phase. Verification phases 13–18 re-run at R4 close; they are not extra build phases.

## 3. Entry criteria and inherited evidence

- Phase 5 `complete`. G7 PASS 2026-09-12 (`project-lead-subagent/phase-5-handoff.md`). API pytest 77 passed; worker 33 passed.
- Decisions D-22…D-31 stand; D-32 canonical route `/papership`; D-33 authorizes this plan only.
- People/Inbox/Memory overlay via `apps/web/src/api/papership.js`; unauthenticated = honest empty.
- Usage first-baseline is `not_captured` when `event_count=0` (`GET /usage/baseline`). `ENGINE_USAGE_EMIT` defaults off.
- Existing `entitlements` table stores `principal_id` + `feature` only. `test_entitlement_is_not_permission` already proves a feature flag is not a grant. No allowance, reservation, or limit rows.
- Stripe packages `@stripe/stripe-js` and `@stripe/react-stripe-js` are in `apps/web/package.json` and are **unused** in `apps/web/src`. They must not charge.
- P18.01 usage measurement is `configured` (schema + flag). Billing, quotas, and entitlements remain R4.
- OQ-G2 default remains `oq_g2_recorded=false` until live `POST /settings/oq-g2`.
- Live write/external Hermes stay gated (D-25).
- Outstanding owner residuals: `docs/handover/outstanding-actions-and-decisions.md`. None block this **plan**. CA-10 still blocks published rates and live charges.
- Route rename evidence: `apps/web/src/App.jsx` mounts `/papership`; leftover aliases redirect; static scan asserts the mount.

## 4. Scope

- Entitlement, allowance, and reservation records in the store, with fail-closed limit checks in **billing test mode**. A reached limit pauses new chargeable work only; records, exports, and pending decisions stay accessible and the copy says so (PRD-G.4).
- Settings → Plan chrome using D-29 labels only. Non-billing views may show remaining-allowance **bands** and estimated action cost **bands**, never money or unpublished quantities (PRD-G.6). Tokens and money stay separate figures (PRD-G.2).
- Versioned rate-card **schema** (CA-3) with no published numbers. Every future charge must reference rate-card version + ledger entry — the schema exists; values stay empty until CA-10.
- Stripe **test-mode** wiring: environment-variable **names** only; no charge API; no live-mode keys; no webhook that records a paid invoice.
- Licensing-state hook (ERA-17) as `configured` if LICENSE/NOTICE/inventory/Hermes evidence already exists; otherwise stay `planned` with an honest Settings row.
- Security review of billing reconciliation (CA-4) as a Phase 6 **gate**, not a waiver. Four entitlement/usage models in test mode, including no duplicate charges (PRD-G.12, V17-2/3).
- Growth CA-1…CA-10 evidence checklist. First-baseline stays `not_captured` if no events. Price scan remains clean.
- R4 registry rows **B14, B19, B20, B21, B24, P19** stay `planned` unless this phase only adds deny-by-default catalogue shells. Do **not** implement live treasury, inventory, mobile, or SDK.

## 5. Non-goals

- Phase 7 mobile clients, connector SDK / domain packs (P19 live), remaining market domains as live connectors.
- Publishing prices or activating charges (CA-10 — two separate owner decisions).
- Inventing allowance quantities, seat counts, rates, KPI, or usage numbers.
- Marketing site / Vercel `enginelabs-au-site`.
- Live write or external Hermes `accepted` (needs a new Security PASS; D-25 is not that licence).
- Live Stripe charges, live webhooks that mark invoices paid, or adding live-mode secret names as required.
- Org-wide erasure drill (PRD-F.8) and decommissioning drill (ERA-15) as completed commercial activation — record them; do not treat them as G9 unless already evidenced.
- Renaming GitHub / Vercel / App remotes, or changing live receipt path `.orgos/loop/`.
- Public build-log (D-30).
- Generating Phase 7 or the final checklist from this file.

## 6. Current-state audit

| Area | Reality |
|---|---|
| Public route | `/papership` mounts blueprint-2 (D-32). `/cc-org-dash` and old aliases redirect. Storage keys `papership-auth` / `papership-theme` with one-time migrate from `cc-org-dash-*`. |
| Entitlements | `entitlements(id, tenant_id, principal_id, feature)` + `POST /entitlements` / `GET /entitlements/me`. Feature flag ≠ permission. |
| Allowances / reservations | None. Usage events exist; budget reservation/reconcile events are named in the roadmap (`usage.budget.reserved/reconciled`) and not enforced. |
| Rate card | Not present. P18 says rate card is R4. |
| Stripe | Dependencies present, **zero source imports**. No test-mode env names wired. |
| Settings / Plan | Blueprint-2 Settings panes exist (Permissions and others). No D-29 tier chrome. |
| Licensing (ERA-17) | `docs/policies/licensing.md` is `proposed`. LICENSE/NOTICE exist in repo. No in-product licensing-state hook. |
| Usage / first-baseline | Emit off by default; `not_captured` at zero events. |
| R4 domains | B14, B19, B20, B21, B24, P19 all `planned`. |
| Auth | Founder JWT; second seat / guest refuse until OQ-G2. |
| Hermes | Catalogued read `accepted` only; write/external gated. |
| Product UI click-through | Recorded in this planning turn (see §20). Overlay depends on local API; unauthenticated surfaces stay honest-empty. |

## 7. Assumptions, constraints, risks, and decisions

- `accepted` (D-28): this phase is intake 11 / R4 commercial only.
- `accepted` (D-29): public labels Free / Basic / Professional / Enterprise; no prices.
- `accepted` (D-32): canonical URL `/papership`.
- `accepted` (D-33): plan now; do not implement in the planning turn.
- `provisional`: Phase 6 lands **structure and test-mode enforcement**, not published rates. Internal ids may remain intake Tier 1–4; UI shows D-29 labels only.
- `provisional`: allowance rows may store a **band enum** or an unpublished numeric field that tests assert is never serialized to the UI or public docs. Prefer band enums until CA-10.
- `provisional`: Stripe test-mode publishable name is carried for a future Settings/Plan “test checkout” that **does not run** until CA-10. Wiring ≠ activation.
- `provisional`: CA-1/CA-2 remain `not_captured` if no realistic concurrency or completed-outcome cost exists. Do not invent them to force CA-10.
- `provisional`: org-wide erasure (PRD-F.8) and ERA-15 decommissioning stay owner/later unless already evidenced; they do not block writing this plan.
- Constraint: no secrets in repo; no live Stripe secret values; fail-closed hooks apply.
- Constraint: entitlement is not a grant (existing test). Limit checks must not grant `org.admin` or bypass AUTH.
- Constraint: D-12 / D-14 — users own their data; billing records are tenant-scoped; no cross-tenant benchmarking.
- Risk: leftover Stripe packages tempt a live Elements checkout. Implementation must keep charge paths behind an explicit `billing_charges_enabled=false` default.
- Risk: Settings/Plan copy can accidentally show fixture prices from old cc-org-dash Settings. Scan must fail the build if currency symbols or invented rates appear.
- D-12, D-14, D-21, D-22, D-25, D-26, D-29, D-30, D-32 stand.

## 8. Dependencies

T6-0 (document residuals + D-32 evidence; no commercial code) → T6-1 entitlement/allowance schema + tests → T6-2 reservation + fail-closed limit enforcement (test mode) → T6-3 Settings/Plan tier UI (labels + bands only) → T6-4 Stripe test-mode wiring (env names, no charge) → T6-5 licensing-state / ERA-17 hook → T6-6 Security (CA-4 reconciliation; no secrets; D-25 residual) → T6-7 Growth (CA-1…CA-10 checklist; first-baseline; price scan) → T6-8 PL G9.

T6-3 may start after T6-1 (labels do not need reservations). T6-4 must not enable charges. T6-5 is independent of Stripe. Owner CA-10 / OQ-G2 / provider renames stay off the critical path for G9 **structure**. Publishing rates is explicitly **not** a G9 requirement.

## 9. Architecture and affected systems

Keep D-01 monorepo and D-04 adapter. Commercial records live in `services/api` store + HTTP, never in desktop secrets or browser Stripe live keys. Limit enforcement is server-side: the API reserves, checks, and pauses chargeable work; the web client only displays remaining **bands** and honest pause copy. Worker/Hermes catalog is unchanged; do not add write/external `accepted` tools. Stripe, if touched, is test-mode configuration only — no paid invoice state machine. Licensing-state is a read of existing artefacts plus an in-product status, not a new licence grant.

## 10. Files and paths in scope

- `services/api/app/store.py`, `services/api/app/main.py`, new helpers as needed (`billing.py` / `entitlements.py` — only if existing modules cannot hold the schema)
- `services/api/app/usage.py` (reservation/reconcile event names; emit still flagged)
- `services/api/tests/` (new `test_phase6.py`; keep `test_entitlement_is_not_permission`)
- `apps/web/src/api/papership.js`
- `apps/web/src/blueprint2/App.jsx`, `apps/web/src/blueprint2/screens.jsx` (Settings/Plan only; no chrome redesign)
- `apps/web/src/App.jsx` / `apps/web/src/pages/papership.jsx` already updated this planning turn (D-32)
- `apps/desktop/src/views/` only if Settings already mirrors web (keep parity; no new desktop shell)
- `docs/capabilities.md` (lead only, evidence-linked)
- `docs/verification.md` § R4 commercial residuals (V17)
- `docs/policies/licensing.md` if ERA-17 becomes `configured`
- Workstream `docs/workstreams/20260910-engine-labs-company-os/<role>/phase-6-*` when implementation starts

No Engine Labs marketing project. No live `.orgos/loop/` path change.

## 11. Supporting documents to create or update

- This plan (canonical).
- D-32 and D-33 (done this planning turn).
- `docs/handover/outstanding-actions-and-decisions.md` (done; update if residuals change).
- Role charters/plans/evidence/handoffs `phase-6-*` when implementation starts — not in the planning turn.
- Registry rows move from `planned` only with evidence (D-02). Phase 6 target status is `configured` for commercial **structure** (expected candidates: P18 billing/entitlement subset, ERA-17 hook if evidenced). R4 domain shells stay `planned` unless deny-by-default catalogue rows are added with evidence.
- `docs/verification.md` V17 commercial rows updated at G9.
- Next plan after G9: `docs/plans/phase_7_ecosystem_mobile_plan.md` (do not write it now).

## 12. Ordered implementation tasks

**T6-0 Carry owner residuals and D-32 evidence** — objective: confirm residuals do not block G9 structure; keep D-32 route tests green. Deps: none. Files: handover log, `apps/web/tests/static-scan.test.mjs`. Validation: no secret values; scan still asserts `/papership`. State: `pending` (route rename already landed in the planning turn).

**T6-1 Entitlement / allowance schema** — objective: versioned entitlement + allowance records; feature flag still ≠ grant; no published numeric rates in API responses consumed by UI. Deps: T6-0. Files: `store.py`, `main.py`, `test_phase6.py`. Validation: pytest for create/list/deny; existing `test_entitlement_is_not_permission` still passes; response fixtures contain no currency amounts. State: `pending`.

**T6-2 Reservation and limit enforcement (test mode)** — objective: reserve before chargeable dispatch; reconcile; fail-closed when over band; pause new chargeable work only; records/export/decisions remain. Deps: T6-1. Files: store + API + usage event names `usage.budget.reserved` / `usage.budget.reconciled`. Validation: four model cases including duplicate-reserve refused; no charge side effect. State: `pending`.

**T6-3 Settings / Plan tier UI** — objective: D-29 labels; remaining-allowance and action-cost **bands**; honest pause copy; no “most popular”, countdowns, or pre-selected upgrades (roadmap §4). Deps: T6-1. Files: `papership.js`, blueprint-2 Settings. Validation: browser or overlay test; price scan clean. State: `pending`.

**T6-4 Stripe test-mode wiring** — objective: carry env **names**; default `billing_charges_enabled=false`; no Elements charge, no live webhook paid-invoice. Deps: T6-2. Files: API config, optional unused client stub behind the flag. Validation: boot without Stripe secrets; charge route 403/404; no secret values in repo. State: `pending`.

**T6-5 Licensing-state / ERA-17** — objective: in-product hook reading existing LICENSE/NOTICE/inventory/Hermes pin evidence; `configured` only with citations. Deps: T6-0. Files: Settings row + registry. Validation: D-02 evidence column filled or row stays `planned`. State: `pending`.

**T6-6 Security** — objective: CA-4 reconciliation review; tenant isolation of billing rows; no secret material; D-25 residual unchanged. Deps: T6-2, T6-4. Files: `security-engineer-subagent/phase-6-*`. Validation: PASS or CONDITIONAL with residuals; no write/external Hermes lift. State: `pending`.

**T6-7 Growth** — objective: CA-1…CA-10 evidence checklist; first-baseline still `not_captured` if zero events; price scan of UI/docs. Deps: T6-3, T6-6. Files: `growth-marketing-subagent/phase-6-*`. Validation: no invented baselines; CA-10 remains owner-only. State: `pending`.

**T6-8 PL G9** — objective: reconcile roles; issue G9; do **not** generate Phase 7 until G9 and this plan’s §22. Deps: T6-6, T6-7. Files: `project-lead-subagent/phase-6-handoff.md`. Validation: G9 verdict + skipped-role reasons (none expected). State: `pending`.

## 13. Adaptive role and delegation map

Tier 3 + commercial/security/growth triggers. All six roles required. Charters are written when implementation starts. Same workstream id.

| Role ID | Required or skipped | Reason | Predecessor | Owned paths | Gate evidence | Status |
|---|---|---|---|---|---|---|
| product-manager-subagent | required | R4 commercial ACC for entitlements, allowances, test-mode limits, D-29 chrome; no prices | D-33 / this plan | `.../product-manager-subagent/phase-6-*` | ACC vs PRD-G / CA-1…10 | planned |
| ui-ux-developer-subagent | required | Settings/Plan labels, band copy, pause/export-accessible states; a11y | PM | `.../ui-ux-developer-subagent/phase-6-*` | §4 tier principles; contrast | planned |
| software-engineer-subagent | required | T6-1…T6-5 | UI/UX | `services/api`, `apps/web/src/blueprint2`, tests | pytest + overlay | planned |
| security-engineer-subagent | required | T6-6; CA-4; billing isolation | SE | `.../security-engineer-subagent/phase-6-*` | PASS/CONDITIONAL | planned |
| growth-marketing-subagent | required | T6-7; CA checklist; no invented baselines; no prices | Security | `.../growth-marketing-subagent/phase-6-*` | CA-1…10 scan | planned |
| project-lead-subagent | required | T6-8 G9 | Growth | `.../project-lead-subagent/phase-6-*` | G9 verdict | planned |

## 14. Test and validation matrix

| Requirement | Validation method | Expected evidence | Status |
|---|---|---|---|
| D-32 canonical route | static scan of `App.jsx` | `/papership` mount; `/cc-org-dash` redirects | pass (planning turn) |
| Storage key migrate | static scan + manual sign-in | `papership-auth`/`theme`; legacy copy-once | pass (planning turn) |
| Entitlement ≠ grant | existing authz test + new rows | 403 on privileged route | pending |
| Allowance schema | pytest | no published currency in JSON | pending |
| PRD-G.4 / G.12 limits | four test-mode models; duplicate reserve refused | pause copy; records still readable | pending |
| PRD-G.6 bands | UI overlay / screenshot | labels only; no prices | pending |
| Stripe inert | boot without secrets; charge path denied | `billing_charges_enabled=false` | pending |
| ERA-17 | registry evidence or planned | D-02 citation | pending |
| CA-4 | Security handoff | reconciliation review | pending |
| D-25 residual | catalog scan | no write/external `accepted` | pending |
| D-29 / CA-10 | price scan UI/docs | clean; no invented rates | pending |
| First-baseline | `GET /usage/baseline` at zero events | `not_captured` | inherited |

## 15. Security, privacy, reliability, accessibility, and performance checks

- Billing rows are tenant-scoped; founder/billing.admin only for writes; entitlements never grant extra AUTH classes.
- No Stripe secret values in repo, chat, or plans. Test-mode publishable name may be wired; live-mode is not required this phase.
- D-14: users own records; billing metadata is tenant operational data, not a third-party analytics destination.
- PRD-A.14: Operator chrome has no prompts, schemas, runtime config, or raw rate-card numbers.
- Reliability: reservation is idempotent; reconcile cannot double-charge even in test mode (CA-4).
- Accessibility: Settings/Plan uses existing D-06 / D-21 tokens; pause and remaining-band text meets contrast; no new motion that ignores `prefers-reduced-motion`.
- Performance: allowance reads are keyed; no unbounded fixture arrays.

## 16. Environment-variable registry

Names only. No values. Do not add live-charge activation keys as required.

| Variable name | Purpose | Scope/environment | Required by phase | Source/provider | Status |
|---|---|---|---|---|---|
| HERMES_API_BASE_URL | API probe | API | carried | existing | wired |
| HERMES_VERSION_PIN | pin | API/worker | carried | existing | wired |
| HERMES_API_SERVER_KEY | Hermes transport | worker only | carried | VPS | must not reach API |
| GITHUB_APP_* | repo connector | API | carried | existing | wired |
| GMAIL_OAUTH_CLIENT_ID | future B12 live | API | not required for G9 | owner | missing |
| GMAIL_OAUTH_REDIRECT_URL | future B12 live | API | not required for G9 | owner | missing |
| SLACK_CLIENT_ID | future B12 live | API | not required for G9 | owner | missing |
| ENGINE_STORE_PATH | local store | API/worker | carried | existing | wired |
| ENGINE_USAGE_EMIT | usage insert flag | API | carried | existing | wired default off |
| STRIPE_TEST_PUBLISHABLE_KEY | future test-mode Elements (not charged) | web/API | T6-4 names only | Stripe test | not wired |
| STRIPE_TEST_SECRET_KEY | future test-mode server (must not charge) | API host only | T6-4 names only | Stripe test | not wired; never in repo |
| STRIPE_TEST_WEBHOOK_SECRET | future test webhook signature | API host only | T6-4 names only | Stripe test | not wired; never in repo |
| ENGINE_BILLING_CHARGES_ENABLED | hard off switch for any charge path | API | T6-4 | existing/new | must default false |

Do not add `STRIPE_LIVE_*` or live webhook names in this phase.

## 17. Deferred human-action queue

| Action | Why agent cannot perform it | Earliest required phase | Blocking now? | Final-checklist destination |
|---|---|---|---|---|
| Live `POST /settings/oq-g2` | live tenant | before second human | no for G9 fixtures | yes |
| Gmail/Slack developer apps + three env names | owner accounts | live B12 | no | yes |
| Rename GitHub/App/Vercel; sync `GITHUB_APP_REPO` | provider dashboards | operator hygiene | no | yes |
| Mailbox creds off systemd `Environment=` | VPS owner | now recommended | no | yes |
| Hermes GET `/health` hang | Hermes ops | ops | no | yes |
| Apple signing / DigitalOcean / backup restore | accounts | R1 residual | no | yes |
| `execute_release` | owner | publication | no | yes |
| Live write/external Hermes `accepted` | new Security PASS | before those tools | no — do not treat D-25 as licence | yes |
| Public build-log | D-30 | later publish decision | no | yes |
| CA-1 measured infra/model/support cost | live concurrency data | before publish rates | no for G9 structure | Phase 6 / checklist |
| CA-2 first-baseline cost per outcome | no events yet | before publish rates | no — stay `not_captured` | Phase 6 / checklist |
| CA-10 publish rates | owner commercial gate | before any public number | no | Phase 6 |
| CA-10 activate charges | owner commercial gate | before any charge | no | Phase 6 |
| Create Stripe test-mode account / set test env names | owner Stripe account | T6-4 live test only | no for wiring | yes |
| Approve any GTM draft | owner | publication | no | yes |
| ERA-15 decommissioning drill | owner/ops | R4 close | no | Phase 7 / checklist |

## 18. Rollback and recovery

Default `ENGINE_BILLING_CHARGES_ENABLED=false` and refuse charge routes. Drop or ignore new allowance/reservation tables via a settings flag if needed; entitlements remain non-grants. Settings/Plan can hide the pane behind a feature flag. Stripe packages unused is already the safe state — T6-4 must preserve “boot without keys”. Invalid rate-card documents are rejected, not applied. No production DNS to roll back. D-32 route change rolls back by restoring `/cc-org-dash` as the mount (aliases already redirect).

## 19. Acceptance criteria (G9)

- Entitlement, allowance, and reservation records exist with tests; entitlement is still not a permission.
- Limit enforcement in test mode pauses new chargeable work only; records, exports, and pending decisions remain; duplicate charges/reserves refused.
- Settings/Plan shows D-29 labels and bands only — no prices, seat counts, or unpublished quantities.
- Stripe test-mode names may be wired; charges stay disabled; no live-mode keys required.
- ERA-17 is `configured` with evidence or remains `planned` with an honest row.
- R4 domain rows B14/B19/B20/B21/B24/P19 stay `planned` (or deny-by-default shells only).
- No prices; no write/external Hermes `accepted`; no marketing-site edits.
- Every required role has an evidence-backed verdict; skipped roles (none expected) would need a reason.
- Lead moves only evidence-backed rows to `configured`.
- CA-10 remains two explicit owner decisions. G9 does **not** publish rates or activate charges.

## 20. Completion evidence

Planning turn only (2026-09-12):

- Plan written at this path (`draft`).
- D-32: `apps/web/src/App.jsx` mounts `/papership`; leftover `/cc-org-dash` redirects; keys `papership-auth` / `papership-theme` with legacy migrate.
- D-33: this file authorized; T6-1…T6-8 not started.
- Product click-through: recorded in `.cursor/memory/memories/2026-09-12-continuation.md` and §6. Implementation evidence (pytest, registry, G9 handoff) is empty until the owner asks to implement.

## 21. Deviations and follow-ups

- Route rename (D-32) landed in the **planning** turn because the owner authorized retiring `/cc-org-dash` as leftover inspiration. It is not Phase 6 commercial scope.
- Browser click-through of the live product was not done in Phase 5; it is done as a precondition of this plan.
- Phase 7 is not generated from this file. One execution phase plan remains after G9.

## 22. Next Plan Generation Prompt

Read `/AGENTS.md`, the complete core agent context, `/instructions/PROJECT_PLANNING.md`, `/instructions/ROLES.md`, `docs/plans/phase_0_foundations_plan.md`, this completed plan, the Phase 5 plan, workstream handoffs, `docs/roadmap.md`, `docs/verification.md`, and `docs/handover/outstanding-actions-and-decisions.md`. Confirm G9 and every required role gate. Then generate exactly one next plan: `docs/plans/phase_7_ecosystem_mobile_plan.md` (R4 / intake 12). Do not generate the final checklist from that step. Do not implement Phase 7 until that file exists and the owner asks.
