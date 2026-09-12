---
plan: phase_7_ecosystem_mobile
status: complete
created: 2026-09-12
updated: 2026-09-12
owner: lead-agent
source_phase: docs/plans/phase_6_commercial_delivery_plan.md
predecessor_gate: G9 PASS (2026-09-12); D-22…D-34
workstream: docs/workstreams/20260910-engine-labs-company-os/manifest.md
blueprint: docs/blueprints/2026-09-10_engine_labs.md
intake: docs/blueprints/company_agent_system_blueprint.md (Phase 12)
release: R4 ecosystem/mobile slice (accepted D-28); gate G11 implementation / G12 owner
risk_tier: tier_3
---

# Phase 7: Ecosystem and mobile — Engine Labs / Papership

Generated after Phase 6 G9 PASS with residuals. Owner authorized the plan (D-34) and then implementation (2026-09-12). Papership UI remains `docs/ui-blueprint/blueprint-2` at **`/papership`**. Live web already ships R4 compressed chrome at `max-width: 767px` (D-21 item 5). Do not edit `www.enginelabs.com.au`. G11 PASS with residuals.

## 1. Objective

Build intake Phase 12 (ecosystem and mobile) for the remaining R4 slice: a connector SDK and domain-pack contract (P19), deny-by-default shells for the six R4-bucketed market domains (B14, B19, B20, B21, B24), and iOS/Android clients that use the same authenticated cloud API and the same blueprint-2 interface contracts as the live web app. Mobile navigation, notifications, secure authentication, and **explicit** offline behaviour are in scope. Cloud execution and authorisation stay on the server across devices.

This phase closes the last execution plan in the phase-0 map. After G11, generate `docs/plans/final_implementation_checklist.md`. Do not generate that checklist from this planning turn.

## 2. Relation to the project end-state

Phases 0–6 closed foundations, the development loop, R1 verification, R2 seats/connections, R3 company operations, and R4 commercial **structure**. R4 is split (D-28): Phase 6 was intake **11**; this phase is intake **12** only. Commercial activation (CA-10 publish rates; CA-10 activate charges) remains two owner decisions and is **not** a G11 requirement. Verification phases 13–18 re-run at R4 close against the enabled ecosystem/mobile scope; they are not extra build phases. After this phase is verified, no further execution phase plan remains — only the final checklist.

## 3. Entry criteria and inherited evidence

- Phase 6 `complete`. G9 PASS 2026-09-12 (`project-lead-subagent/phase-6-handoff.md`). Every required role had an evidence-backed verdict. Residuals: CA-10, D-25, Stripe test account, OQ-G2 live notice.
- Decisions D-22…D-33 stand; D-34 authorizes this plan only.
- Canonical route `/papership` (D-32). Storage keys `papership-auth` / `papership-theme`.
- Live web at `max-width: 767px` already uses `OrgOS Mobile.dc.html` compressed chrome: compact header, bottom tabs Today / Work / Inbox / Hey Engine, rail sheet, full-screen Hey Engine sheet, 2×2 health, 44px Approve/Reject/Stop. Face ID / fingerprint controls are **offered** on the auth card; the browser still signs in with email/password.
- Prism-head mark is app/tab icon only (D-21 item 6). Canonical master `brand/papership-icon.png`; PWA icons and `apple-touch-icon` exist.
- PWA `apps/web/public/manifest.json` exists (`display: standalone`) but `start_url` is `/` (should become `/papership`). No service worker. No iOS/Android app trees (zero `.swift` / `.kt` sources).
- Desktop is Tauri 2 + React/TS at `apps/desktop` (P15.01 `configured` for the desktop shell). It does not wrap blueprint-2 and is not the mobile client.
- Capability rows B14.01, B19.01, B20.01, B21.01, B24.01, P19.01 are `planned`. No pack-manifest schema, plugin-trust store, or `install_pack` route.
- Commercial structure from Phase 6 stands: allowances/reservations in test mode; `ENGINE_BILLING_CHARGES_ENABLED` defaults false; Settings → Plan shows D-29 labels and bands only.
- Live write/external Hermes stay gated (D-25).
- Outstanding owner residuals: `docs/handover/outstanding-actions-and-decisions.md`. None block this **plan**.

## 4. Scope

- **P19 connector SDK / domain packs:** versioned pack-manifest schema, list/read APIs, owner `install_pack` behind a trust-review record, custom-field definitions, compatibility fixtures, and deny-by-default executable-plugin activation. Declarative extensions may be configured by authorised roles within their grants. Executable extensions require review before activation (intake Phase 12).
- **Remaining market domains as shells, not live source systems:** B14 treasury/payments (payment proposals + designated authority + step-up reauth), B19 inventory/facilities, B20 field/dispatch/offline capture, B21 quality/BOM/inspections, B24 sector packs via P19. Follow the Phase 4/5 pattern: native records and deny-by-default catalogue rows. Live bank, MES, inventory, or sector connectors stay `planned` unless the owner supplies credentials **and** a new Security PASS.
- **Mobile clients against the same API:** iOS and Android shells that load the live blueprint-2 contracts (`apps/web` / `/papership`), plus an installable PWA with explicit offline behaviour. Shared UI contracts stay in `packages/ui` and `packages/contracts`. Cloud jobs never run on-device; disconnect never cancels a cloud run (PRD-E.4).
- **Explicit offline:** queued approvals and B20 on-site evidence persist locally, show an honest offline banner, and sync on reconnect under the same grants. No local authorisation elevation.
- **Secure authentication on native shells:** biometric unlock may gate an already-issued session on-device. It does not replace server JWT verification and does not mint grants.
- **Registry discipline (D-02):** lead moves a row from `planned` only when the evidence column cites a verified artifact. Expected G11 targets: P19.01 and P15.01 (mobile subset) to `configured` if evidenced; B14/B19/B20/B21/B24 to `configured` only for native/deny-by-default shells, not live source connectors.
- Security review of plugin trust, mobile token storage, offline cache, and B14 reauth as a Phase 7 **gate**, not a waiver.
- Growth scan: no prices, no invented pack-marketplace metrics, no App Store / Play Store claims without a store listing.

## 5. Non-goals

- Re-doing the already-shipped web compressed chrome as the main mobile deliverable.
- From-scratch SwiftUI / Jetpack Compose apps that fork the product UI.
- App Store / Play Store submission, Apple Developer / Google Play accounts, or paid signing certificates (owner / checklist).
- Publishing prices or activating charges (CA-10).
- Inventing allowance quantities, seat counts, rates, stock levels, inspection scores, or sector KPIs.
- Live bank transfers, live MES/QMS writes, live inventory source writes, or live sector-system writes.
- Marketing site / Vercel `enginelabs-au-site`.
- Live write or external Hermes `accepted` (D-25 is not that licence).
- Org-wide erasure (PRD-F.8) and ERA-15 decommissioning as completed G11 evidence — record them; do not treat an owner drill as done unless already evidenced.
- Putting the prism-head mark back inside product chrome.
- Generating the final implementation checklist from this file.
- Renaming GitHub / Vercel / App remotes.

## 6. Current-state audit

| Area | Reality |
|---|---|
| Web mobile chrome | Live at `/papership` ≤767px. Bottom tabs, rail sheet, Hey Engine sheet. Not a native client. |
| Auth biometrics | Presentational Face ID / fingerprint on narrow viewports only. |
| PWA | `manifest.json` + apple-touch + icon-192/512/maskable. `start_url` is `/`. No service worker. No `beforeinstallprompt` handling required for G11 if installability is otherwise evidenced. |
| Native mobile | No `apps/ios`, `apps/android`, or `apps/mobile`. Zero Swift/Kotlin sources. |
| Desktop | Tauri 2 macOS-first shell at `apps/desktop`. Separate React/TS views; not blueprint-2. Packaged store builds are owner-signed. |
| P19 / packs | Registry row `planned`. `packages/contracts` has the 43 capability ids only. No pack schema, trust table, or Connections → Available packs pane. |
| B14 / B19 / B20 / B21 / B24 | `planned`. Today registry copy lists the labels. No payment-proposal store, stock movements, field evidence, inspections, or sector-pack install. |
| Commercial | Structure only. Charges disabled. No published rates. |
| Hermes | Catalogued read `accepted` only. |
| Icons | Inset-squircle master applied to brand, web, desktop, PWA, apple-touch. |

## 7. Assumptions, constraints, risks, and decisions

- `accepted` (D-28): this phase is intake 12 / R4 ecosystem+mobile only.
- `accepted` (D-21 item 5): live web already ships compressed chrome; Phase 7 must not treat that as the native-client done state.
- `accepted` (D-21 item 6): prism mark stays app/tab only, including on home-screen and store icons.
- `accepted` (D-25): no write/external Hermes lift.
- `accepted` (D-29 / CA-10): no prices or unpublished quantities.
- `accepted` (D-34): plan now; do not implement in the planning turn.
- `provisional`: native clients wrap `apps/web` blueprint-2 via a **Tauri 2 mobile** project at `apps/mobile` (iOS + Android) so they share the live UI contracts and `GET`/`POST` Papership API. If the Tauri mobile spike fails on this toolchain, fall back to Capacitor wrapping the same Vite build. Do not start a third UI stack.
- `provisional`: PWA installability plus simulator/emulator launch of both shells is sufficient G11 evidence. Store submission is G12 / checklist.
- `provisional`: biometric unlock stores only a session unlock flag in the OS keychain/keystore; refresh still hits the API. Browser PWA cannot claim Face ID success.
- `provisional`: B14 “approve_payment” in this phase creates a **proposal + reauth challenge** only. No money moves. Provider connector stays `connector:tbd`.
- `provisional`: B20 offline evidence is an encrypted-at-rest device queue of attachments + metadata, uploaded on reconnect, tenant-scoped, never a second source of truth after sync.
- `provisional`: B24 ships **one** example sector-pack fixture (declarative, no executable code) plus the install/trust path. Additional sectors stay catalogue rows.
- `provisional`: ERA-15 and PRD-F.8 remain owner/later. They do not block writing or implementing this plan.
- Constraint: plugin trust is fail-closed. Unknown pack ids denied. Executable packs cannot run until a trust-review row is `accepted` by `org.admin`.
- Constraint: D-12 / D-14 — offline caches and pack config are user/tenant-owned; wipe on sign-out and on erasure request.
- Constraint: entitlement is not a grant. Installing a pack must not grant `org.admin` or bypass AUTH.
- Constraint: no secrets in repo; no live Stripe; fail-closed hooks apply.
- Risk: wrapping the web app twice (PWA + native) can drift. One build of `apps/web` must feed both.
- Risk: offline queues can replay side effects. Uploads must be idempotent and re-checked against current grants.
- Risk: Tauri mobile / Xcode / Android SDK absence. Record the spike; do not fake a store binary. Simulator evidence or an honest toolchain residual is required.
- D-12, D-14, D-21, D-22, D-25, D-26, D-29, D-30, D-32 stand.

## 8. Dependencies

T7-0 (document residuals + confirm web chrome is not the deliverable) → T7-1 P19 pack-manifest schema + trust store + tests → T7-2 remaining-domain deny-by-default shells → T7-3 B14 payment-proposal + designated-authority reauth (structure) → T7-4 PWA / shared mobile contracts / explicit offline API → T7-5 native iOS/Android shells (`apps/mobile` spike + wrap) → T7-6 B20 field evidence queue on the mobile client → T7-7 Security → T7-8 Growth → T7-9 PL G11.

T7-2 may start after T7-1 (shells consume pack ids). T7-3 may start after T7-1 (proposals are native, not a bank connector). T7-4 may start in parallel with T7-1. T7-5 depends on T7-4 (same web build). T7-6 depends on T7-4 and T7-5. T7-7 depends on T7-1, T7-3, T7-5, T7-6. Owner Apple/Google accounts, ERA-15, and CA-10 stay off the critical path for G11 **structure**.

## 9. Architecture and affected systems

Keep D-01 monorepo and D-04 adapter. Packs, payment proposals, and field evidence live in `services/api` store + HTTP. The worker/Hermes catalog is unchanged; do not add write/external `accepted` tools. Mobile shells are thin authenticating WebViews / Tauri mobile windows over the same origin or bundled web build; they hold tokens in OS storage and open OAuth in the system browser (no embedded OAuth webview — same rule as desktop). Offline queues are device-local and sync through existing authenticated routes. Plugin execution, if any, runs server-side after trust review — never as injected client script. Stripe and billing flags are untouched.

## 10. Files and paths in scope

- `services/api/app/store.py`, `services/api/app/main.py`, new helpers as needed (`packs.py` / `payments.py` / `field_evidence.py` — only if existing modules cannot hold the schema)
- `services/api/tests/` (new `test_phase7.py`; keep Phase 6 billing tests green)
- `packages/contracts/src/` (pack-manifest types + fixtures)
- `packages/ui/src/` only if a shared mobile primitive is missing (offline banner, biometric affordance)
- `apps/web/public/manifest.json`, `apps/web/index.html`, new service-worker only if required for explicit offline
- `apps/web/src/api/papership.js`
- `apps/web/src/blueprint2/App.jsx`, `screens.jsx`, `blueprint2.css` (Connections → Available packs; B14/B19/B20/B21/B24 shells; offline banner honesty). Do not redesign shipped compressed chrome.
- New `apps/mobile/` (Tauri 2 mobile or Capacitor wrapper) plus README for simulator launch
- `apps/web/tests/static-scan.test.mjs` (start_url, no prices, no in-chrome prism mark)
- `docs/capabilities.md` (lead only, evidence-linked)
- `docs/verification.md` (V16 mobile / V15 recovery residuals as they apply)
- `docs/architecture.md` (mobile client + pack-trust boundaries)
- Workstream `docs/workstreams/20260910-engine-labs-company-os/<role>/phase-7-*` when implementation starts

No Engine Labs marketing project. No live `.orgos/loop/` path change. No `STRIPE_LIVE_*`.

## 11. Supporting documents to create or update

- This plan (canonical).
- D-34 (done this planning turn).
- `docs/handover/outstanding-actions-and-decisions.md` (this turn; update again if residuals change).
- Role charters/plans/evidence/handoffs `phase-7-*` when implementation starts — not in the planning turn.
- Registry rows move from `planned` only with evidence (D-02).
- `docs/verification.md` mobile/P19 rows updated at G11.
- Next file after G11: `docs/plans/final_implementation_checklist.md` (do not write it now).

## 12. Ordered implementation tasks

**T7-0 Carry residuals and separate web chrome from native clients** — objective: confirm G9 residuals do not block G11 structure; record that D-21 item 5 web chrome is already shipped. Deps: none. Files: handover log, this plan §6. Validation: no secret values; scan still asserts `/papership`. State: `done` (this planning turn).

**T7-1 P19 pack contract and plugin trust** — objective: versioned pack-manifest schema; `GET /packs`, `GET /packs/:id`, `POST /packs/install` (owner; creates a trust-review row; does not execute code); custom-field definitions scoped to tenant; unknown packs denied; entitlement still ≠ grant. Deps: T7-0. Files: `store.py`, `main.py`, `packages/contracts`, `test_phase7.py`. Validation: pytest install/deny/unknown-id; fixture pack is declarative JSON only; no executable eval. State: `done`.

**T7-2 Remaining-domain deny-by-default shells** — objective: B19 / B21 / B24 (and B14/B20 placeholders until T7-3/T7-6) appear as honest registry + Connections catalogue rows; actions that need a missing source return `unavailable` / `not_captured`, never fixture stock or inspection numbers. Deps: T7-1. Files: blueprint-2 Data/Integrations/Registry, capabilities evidence later. Validation: browser or overlay; price/quantity scan clean. State: `done`.

**T7-3 B14 payment proposals + designated-authority reauth** — objective: create/list payment proposals; `approve_payment` requires designated authority **and** a fresh reauth step; `change_bank_details` requires reauth; no provider payout; no amounts invented for display beyond user-entered proposal fields. Deps: T7-1. Files: API store + Settings/Approvals + tests. Validation: pytest refuse without reauth; refuse without designated grant; no charge side effect. State: `done`.

**T7-4 Shared mobile contracts, PWA, explicit offline** — objective: `manifest.json` `start_url` `/papership`; installable standalone; service worker or equivalent that caches shell + queues T7-6 uploads; offline banner already in chrome must stay honest; sign-out wipes the queue. Deps: T7-0. Files: `apps/web/public`, `index.html`, `papership.js`, tests. Validation: static scan; offline/online toggle in browser; no cloud job started from cache. State: `done`.

**T7-5 Native iOS and Android shells** — objective: `apps/mobile` wraps the T7-4 web build; both platforms launch on simulator/emulator against the same API; tokens in keychain/keystore; system-browser OAuth; biometric unlock of an existing session only; icons from `brand/papership-icon.png`. Deps: T7-4. Files: `apps/mobile/**`, desktop icon generator reuse. Validation: documented simulator commands + screenshot or toolchain residual recorded. State: `done` (toolchain report; simulator screenshots not captured).

**T7-6 B20 field / offline capture** — objective: capture on-site evidence while offline; queue is tenant+user scoped; sync is idempotent and rechecks grants; dispatch/return actions that need a live logistics connector stay `unavailable`. Deps: T7-4, T7-5. Files: API + mobile/web capture UI + tests. Validation: pytest replay-safe upload; browser/simulator offline then reconnect. State: `done`.

**T7-7 Security** — objective: plugin-trust review; mobile token/offline-cache review; B14 reauth; D-25 residual unchanged; D-14 wipe-on-sign-out. Deps: T7-1, T7-3, T7-5, T7-6. Files: `security-engineer-subagent/phase-7-*`. Validation: PASS or CONDITIONAL with residuals; no write/external Hermes lift. State: `done` (PASS with residuals).

**T7-8 Growth** — objective: no prices; no invented store/install counts; no App Store claim without a listing; CA-10 still owner-only. Deps: T7-2, T7-7. Files: `growth-marketing-subagent/phase-7-*`. Validation: price scan of UI/docs; no fabricated baselines. State: `done`.

**T7-9 PL G11** — objective: reconcile roles; issue G11; do **not** generate the final checklist until G11 and this plan’s §22. Deps: T7-7, T7-8. Files: `project-lead-subagent/phase-7-handoff.md`. Validation: G11 verdict + skipped-role reasons (none expected). State: `done` (G11 PASS with residuals).

## 13. Adaptive role and delegation map

Tier 3 + mobile auth, plugin trust, and remaining-domain triggers. All six roles required. Charters are written when implementation starts. Same workstream id `20260910-engine-labs-company-os`.

| Role ID | Required or skipped | Reason | Predecessor | Owned paths | Gate evidence | Status |
|---|---|---|---|---|---|---|
| product-manager-subagent | required | R4 ecosystem/mobile ACC for P19, B14/B19/B20/B21/B24 shells, mobile clients, offline; no prices | D-34 / this plan | `.../product-manager-subagent/phase-7-*` | ACC vs I-12 / NFR-1 / PRD-E.4 | PASS |
| ui-ux-developer-subagent | required | Native/PWA navigation, offline/permission/biometric states; do not redesign shipped web chrome | PM | `.../ui-ux-developer-subagent/phase-7-*` | D-21; NFR-1 shared contracts | PASS |
| software-engineer-subagent | required | T7-1…T7-6 | UI/UX | `services/api`, `apps/web`, `apps/mobile`, `packages/contracts` | pytest + simulator/PWA | PASS |
| security-engineer-subagent | required | T7-7; plugin trust; mobile token/offline; B14 reauth | SE | `.../security-engineer-subagent/phase-7-*` | PASS/CONDITIONAL | PASS (residuals) |
| growth-marketing-subagent | required | T7-8; no store claims; no prices | Security | `.../growth-marketing-subagent/phase-7-*` | CA-10 residual; price scan | PASS |
| project-lead-subagent | required | T7-9 G11 | Growth | `.../project-lead-subagent/phase-7-*` | G11 verdict | PASS |

## 14. Test and validation matrix

| Requirement | Validation method | Expected evidence | Status |
|---|---|---|---|
| D-32 canonical route | static scan | `/papership` mount; PWA `start_url` `/papership` | pass |
| Web chrome ≠ native done | plan + STATE | D-21 item 5 recorded as shipped; T7-5 still required | pass |
| P19 manifest + deny unknown | pytest | install creates trust row; unknown id 404/403; no eval | pass |
| Executable pack gated | pytest + Security | no activation without trust-review `accepted` | pass |
| B14 reauth | pytest | approve without reauth refused; no payout | pass |
| B19/B21/B24 shells | UI overlay / scan | honest `unavailable` / `not_captured`; no invented qty | pass |
| B20 offline queue | pytest + offline toggle | idempotent sync; wiped on sign-out | pass |
| iOS + Android shells | simulator/emulator or toolchain residual | both platforms launched or residual recorded | pass (toolchain residual) |
| Same API / same contracts | contract tests + wrap config | no second auth stack; no local grants | pass |
| D-25 residual | catalog scan | no write/external Hermes `accepted` | pass |
| D-29 / CA-10 | price scan UI/docs | clean; no invented rates | pass |
| Entitlement ≠ grant | existing authz test | pack install does not grant `org.admin` | pass |
| ERA-15 | owner drill | queued to checklist unless already evidenced | inherited |

## 15. Security, privacy, reliability, accessibility, and performance checks

- Pack install and trust-review writes are `org.admin` only; declarative config cannot widen AUTH classes.
- Mobile tokens live in OS keychain/keystore, not `localStorage` on native shells. PWA may keep the existing web session key with the same XSS posture as today; document the residual.
- Offline caches and evidence blobs are tenant+user scoped, encrypted at rest on native if the platform API exists, and deleted on sign-out and erasure.
- B14 reauth is a fresh authentication event, not a cached biometric flag reused across payments.
- OAuth uses the system browser. No embedded OAuth webview.
- D-14: users own evidence and pack config; Papership does not claim sector or field content.
- PRD-A.14: Operator chrome has no prompts, schemas, runtime config, or raw rate-card numbers. Pack manifests shown to operators are identifiers and grants, not executable source.
- Reliability: upload and approve routes are idempotent; disconnect does not cancel cloud work.
- Accessibility: native chrome keeps 44px primary actions already used on narrow web; offline and reauth copy meets contrast; `prefers-reduced-motion` still honoured.
- Performance: service-worker cache is the shell + signed-in static assets, not an unbounded evidence archive.

## 16. Environment-variable registry

Names only. No values. Do not add live-charge or store-publishing keys as required.

| Variable name | Purpose | Scope/environment | Required by phase | Source/provider | Status |
|---|---|---|---|---|---|
| HERMES_API_BASE_URL | API probe | API | carried | existing | wired |
| HERMES_VERSION_PIN | pin | API/worker | carried | existing | wired |
| HERMES_API_SERVER_KEY | Hermes transport | worker only | carried | VPS | must not reach API |
| GITHUB_APP_* | repo connector | API | carried | existing | wired |
| GMAIL_OAUTH_CLIENT_ID | future B12 live | API | not required for G11 | owner | missing |
| GMAIL_OAUTH_REDIRECT_URL | future B12 live | API | not required for G11 | owner | missing |
| SLACK_CLIENT_ID | future B12 live | API | not required for G11 | owner | missing |
| ENGINE_STORE_PATH | local store | API/worker | carried | existing | wired |
| ENGINE_USAGE_EMIT | usage insert flag | API/worker | carried | existing | wired default off |
| ENGINE_BILLING_CHARGES_ENABLED | hard off switch | API | carried | existing | must stay false |
| ENGINE_PACK_EXECUTION_ENABLED | hard off switch for executable packs | API | T7-1 | existing/new | wired default false |
| ENGINE_API_PUBLIC_URL | mobile/PWA origin for the wrapped client | mobile/web | T7-5 | existing/new | names only |
| APPLE_TEAM_ID | signing (store) | CI/owner | not required for G11 | Apple | missing |
| ANDROID_KEYSTORE_* | signing (store) | CI/owner | not required for G11 | Google Play | missing; never in repo |

Do not add `STRIPE_LIVE_*`. Do not require store credentials to issue G11.

## 17. Deferred human-action queue

| Action | Why agent cannot perform it | Earliest required phase | Blocking now? | Final-checklist destination |
|---|---|---|---|---|
| Live `POST /settings/oq-g2` | live tenant | before second human | no for G11 fixtures | yes |
| Gmail/Slack developer apps + three env names | owner accounts | live B12 | no | yes |
| Apple Developer + signing + App Store listing | owner account / paid enrolment | store publish | no for simulator G11 | yes |
| Google Play console + keystore | owner account | store publish | no for emulator G11 | yes |
| Xcode / Android SDK on the agent host if absent | toolchain install | T7-5 binaries | no — record residual | yes |
| Live bank / MES / inventory / sector connectors | owner provider apps + new Security PASS | live source writes | no | yes |
| CA-10 publish rates | owner commercial gate | before any public number | no | yes |
| CA-10 activate charges | owner commercial gate | before any charge | no | yes |
| ERA-15 decommissioning drill | owner/ops | R4 close | no | yes |
| PRD-F.8 org-wide erasure drill | owner/ops + disposable tenant | R4 close | no | yes |
| Live write/external Hermes `accepted` | new Security PASS | before those tools | no — D-25 is not that licence | yes |
| Create Stripe test-mode account | owner Stripe | leftover Phase 6 | no | yes |
| `execute_release` / public build-log | owner / D-30 | publication | no | yes |
| GitHub org/App dashboard avatars | owner | hygiene | no | yes |

## 18. Rollback and recovery

Default `ENGINE_PACK_EXECUTION_ENABLED=false` and refuse executable activation. Installed declarative packs can be disabled by a settings flag without dropping the trust-review audit. Payment proposals remain records; there is no payout to reverse. Offline queues stay on-device until the user signs out or erases. `apps/mobile` can be unpublished from the tree without affecting `/papership`. PWA `start_url` rolls back to `/` (redirect still works). No production DNS to roll back. Billing flags stay as Phase 6 left them.

## 19. Acceptance criteria (G11)

- P19 pack-manifest schema, list/read/install, and plugin-trust review exist with tests; executable packs default off; entitlement is still not a permission.
- B14 payment proposals require designated authority and reauth; no money moves; no live bank connector required.
- B19, B21, B24 (and B20 source-connector actions) are honest shells or one declarative sector-pack fixture — not live source systems.
- B20 offline evidence queues, syncs idempotently, and wipes on sign-out.
- PWA `start_url` is `/papership`; explicit offline behaviour is evidenced in the browser.
- iOS and Android shells launch against the same API, or the exact toolchain limitation is recorded and is not hidden as “native done”.
- Web compressed chrome is unchanged in intent (D-21 item 5) and is not counted as T7-5.
- No prices; no write/external Hermes `accepted`; no marketing-site edits; prism mark stays app/tab only.
- Every required role has an evidence-backed verdict; skipped roles (none expected) would need a reason.
- Lead moves only evidence-backed rows to `configured`.
- CA-10 remains two explicit owner decisions. G11 does **not** publish rates, activate charges, or submit store listings.
- Final checklist is **not** generated until G11 and §22.

## 20. Completion evidence

Implementation turn (2026-09-12):

- T7-1…T7-9 done. G11 PASS with residuals (`project-lead-subagent/phase-7-handoff.md`).
- pytest: `test_phase7.py` + Phase 5/6/env = 30 passed.
- Web static scan 7 passed; contracts packs/capabilities passed.
- `apps/mobile/toolchain-report.json`: rustc, Xcode, adb, tauri-cli present; simulator screenshots not captured.
- Registry: B14/B19/B20/B21/B24/P19 `configured` (native/shells only). Final checklist not generated.

## 21. Deviations and follow-ups

- Web R4 compressed chrome shipped in the Phase 6 closeout window, before this plan existed. Phase 7 treats that as inherited UI, not as intake-12 completion.
- ERA-15 remains an R4 close drill on the owner queue, not a G11 structure task.
- Roadmap §2.4 still lists CA-1…CA-10 as R4 entry. Verified reality: G9 shipped commercial **structure** without CA-10. This plan does not reopen billing.
- After G11, do not invent a Phase 8 execution plan.

## 22. Next Plan Generation Prompt

Read `/AGENTS.md`, the complete core agent context, `/instructions/PROJECT_PLANNING.md`, `/instructions/ROLES.md`, `docs/plans/phase_0_foundations_plan.md`, this completed plan, the Phase 6 plan, workstream handoffs, `docs/roadmap.md`, `docs/verification.md`, and `docs/handover/outstanding-actions-and-decisions.md`. Confirm G11 and every required role gate. Then generate exactly one next file: `docs/plans/final_implementation_checklist.md` from `/templates/final-implementation-checklist-template.md`. Do **not** generate another execution phase plan. Do not implement leftover owner-only actions. Consolidate remaining human-only actions and environment-variable **names** only.
