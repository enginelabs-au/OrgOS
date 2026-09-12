# Resume after provider rename — exhaustive kickstart

Use this file as the kickstart for the next chat after the owner renames GitHub / the GitHub App / Vercel / the local folder. Pair it with the saved transcript. Do not store secrets here.

This document is the durable replacement for the chat that will be lost when the GitHub remote and local folder are renamed. Read it before changing any locked file and before implementing Phase 6.

---

## 0. First message to the next agent (copy)

```
Resume Papership from docs/handover/resume-after-provider-rename.md and the saved transcript.

I have renamed the GitHub repo (and will confirm App + Vercel + GITHUB_APP_REPO + optional ~/.config/papership).

Do this in order:
1. Read .cursor/AGENTS.md, .cursor/USER.md, .cursor/STATE.md, this handover, docs/handover/rename-owner-first-providers.md, docs/handover/outstanding-actions-and-decisions.md, docs/plans/phase_6_commercial_delivery_plan.md.
2. Confirm providers now match Papership. If any of §5 is still OrgOS-shaped, stop and say which.
3. Update the provider-locked files listed in §6 so live defaults match Papership. Dual-read old receipt files. Do not rewrite git history or published .orgos/loop/ receipts.
4. Re-run GitHub/loop tests and apps/web/tests/static-scan.test.mjs.
5. Do not implement Phase 6 until I explicitly ask. When I ask, execute docs/plans/phase_6_commercial_delivery_plan.md (T6-0…T6-8, G9). Do not generate Phase 7 until G9.
6. Never edit www.enginelabs.com.au or Vercel enginelabs-au-site.
7. No prices, no live Stripe charges, no write/external Hermes accepted (D-25).
8. Do not restore named-competitor comparison tables.
```

If the owner has **not** finished the provider rename yet, stop after reading and say which of §5 is still OrgOS-shaped. Do not flip locked files early.

---

## 1. Identity (do not re-ask)

| Thing | Value | Never do |
|---|---|---|
| Product | **Papership** (UI wordmark, in-repo slug `papership`) | Treat any other product name as current |
| Company | **Engine Labs** | Replace Engine Labs with Papership in company/legal copy |
| Marketing site | `www.enginelabs.com.au` / Vercel `enginelabs-au-site` | Edit, redirect, or deploy that project from this repo |
| Live web UI | `docs/ui-blueprint/blueprint-2` exactly (D-21 / D-22) | Hybridise with blueprint-1 or invent a `/` marketing landing |
| Canonical route | **`/papership`** (D-32) | Remount leftover `/cc-org-dash` as live chrome |
| Bookmark aliases | `/`, `/cc-org-dash`, `/EcoOS`, `/ecoos`, `/Dashboard`, `/Dashboard_new` → `/papership` | Delete aliases without owner ask (bookmarks still work) |
| App / tab icon | Prism-head mark only | Put the prism-head **inside** product chrome |
| Desktop | Tauri, already named Papership (`au.enginelabs.desktop`) | Rebuild the desktop shell as part of rename or Phase 6 |
| Workstream folder | `docs/workstreams/20260910-engine-labs-company-os/` | Rename this folder (frozen task id) |
| Risk tier | Tier 3 | Skip roles on Phase 6 |

D-10 (`docs/decisions/2026-09-11-orgos-product-identity.md`) is historical. Display name is D-20. Route is D-32. Live provider slugs stay on the owner-first wait list until this rename.

---

## 2. Control-plane contract the next agent must honour

Paths below use the repo-root `.cursor/` prefix.

**Every new session:** read `.cursor/AGENTS.md` and `.cursor/BOOTSTRAP.md`; run read-only `node .cursor/skills/launch-pipeline/scripts/preflight.mjs`; do **not** run `bash .cursor/scripts/bootstrap.sh` unless preflight says `bootstrap_required` **and** the mode is Agent implementation.

**Every substantive turn:** `.cursor/AGENTS.md`, `.cursor/USER.md`, `.cursor/STATE.md`, `.cursor/INSTRUCTIONS.md`, `.cursor/SKILLS.md`, `.cursor/TOOLS.md`, `.cursor/memory/MEMORY.md`, every file in `.cursor/memory/blockers/` (currently empty), then the files STATE lists as active.

**Instruction precedence:** current user request → `.cursor/AGENTS.md` → activated instructions → `.cursor/USER.md` → STATE + active plan → MEMORY / blockers / runbooks / skills / tools → repository conventions.

**Active instructions while Phase 6 is the live plan:** `.cursor/instructions/LAUCH.md`, `.cursor/instructions/PROJECT_PLANNING.md`, `.cursor/instructions/SUBAGENTS.md`, `.cursor/instructions/ROLES.md`. Load `ROLES.md` in full when implementing Phase 6, selecting roles, or running a gate.

**Do not store secrets** in markdown, plans, memory, logs, examples, or chat. Env **names** only.

Ask the owner only for: credentials / account ownership; irreversible product decisions; destructive work beyond scope; safety / privacy approval; incompatible implementations with materially different outcomes. Everything else: choose the safest assumption, record it, continue.

---

## 3. Where we are in the lifecycle

| Phase | Plan | Status |
|---|---|---|
| 0 Foundations | `docs/plans/phase_0_foundations_plan.md` | complete_conditional |
| 1 Foundation | `docs/plans/phase_1_foundation_plan.md` | complete_conditional |
| 2 Development loop | `docs/plans/phase_2_development_loop_plan.md` | complete_conditional |
| 3 Release verification | `docs/plans/phase_3_release_verification_plan.md` | complete (G3 PASS-with-residuals; V18-5 owner APPROVE recorded) |
| 4 Collaboration / connections (R2 / intake 09) | `docs/plans/phase_4_collaboration_connections_plan.md` | complete; **G5 PASS 2026-09-12** |
| 5 Company operations (R3 / intake 10) | `docs/plans/phase_5_company_operations_plan.md` | complete; **G7 PASS 2026-09-12** |
| **6 Commercial delivery (R4 / intake 11)** | `docs/plans/phase_6_commercial_delivery_plan.md` | **draft only. Not implemented.** |
| 7 Ecosystem / mobile (R4 / intake 12) | `docs/plans/phase_7_ecosystem_mobile_plan.md` | **Do not write until G9** |
| Final checklist | `docs/plans/final_implementation_checklist.md` | R1 checklist exists; do not regenerate from Phase 6 or this rename |

Release map (D-28): R2 = intake 09, R3 = 10, R4 = 11+12. Gates: Phase 4 = G5/G6, Phase 5 = G7/G8, Phase 6 = **G9 implementation / G10 owner**.

Workstream: `docs/workstreams/20260910-engine-labs-company-os/manifest.md` — `status: phase_6_plan_draft`, `current_gate: G7 PASS; Phase 6 plan drafted; G9 not started`. All six roles required for phase gates. Role artifacts live under that folder (`<role-id>/{charter,plan,evidence,handoff}.md` plus later `phase-5-*` / future `phase-6-*`).

**Next product work after the locked-file follow-up:** implement Phase 6 when the owner asks. One execution plan remains after that (Phase 7).

---

## 4. What the last session already did (2026-09-12, this chat)

This is the work the transcript covers. Do not redo it. Do not treat it as Phase 6 implementation.

### 4.1 Product click-through (Vite `127.0.0.1:5173`)

- `/` and `/cc-org-dash` both end at `/papership`.
- Sign-in title: Papership / Engine Labs.
- Tabs exercised: Today (Overview / Decisions / Running / Registry), Work (Issues / Board), Inbox, People / Teams, Data, Files, Integrations, Settings.
- Avatar → Memory; Hey Engine docked composer accepted typed text (not submitted); Company rail Decisions + a priority; theme Light / Dark / Dimmed.
- Inbox / People / Memory honest-empty without JWT.
- No leftover `/cc-org-dash` chrome. No currency prices. Data cost band says “no published prices”.
- **Fixture leak for T6-3:** Today compose still shows `Remaining allowance: 184640` (unpublished quantity; D-29). Settings → Plan is still appearance/theme, not Free / Basic / Professional / Enterprise. Data still has blueprint fixture counts (Traces 128). Those are leftover chrome, not a rename regression.

### 4.2 Phase 6 planned, not implemented

- Owner authorized planning after the leftover `/cc-org-dash` click-through (D-33).
- Plan: `docs/plans/phase_6_commercial_delivery_plan.md` (R4 / intake 11, draft).
- Tasks T6-0…T6-8 exist as text only. No commercial schema, no Stripe wiring, no Settings/Plan tier UI, no G9.
- Phase 7 was **not** generated.

### 4.3 Canonical route (D-32)

- `apps/web/src/App.jsx`: `/papership` mounts blueprint-2; leftover aliases redirect.
- `apps/web/src/pages/papership.jsx` re-exports blueprint-2; `cc-org-dash.jsx` is a compatibility re-export.
- Storage keys `papership-auth` / `papership-theme` with one-time migrate from `cc-org-dash-*`.
- Static scan: `apps/web/tests/static-scan.test.mjs` (title, route, keys, live API client has no OrgOS / cc-org).

### 4.4 Leftover-name Pass A (safe current-tree sweep)

Authorized: sweep `orgos` / `OrgOS` / `cc-org` leftovers in the **current tree** to Papership. Historical git commits stay. Owner does GitHub / App / Vercel / local folder **after** this pack is final.

Already changed:

- `NOTICE` → Engine Labs (Papership)
- `services/api/app/main.py` dropped extra `"orgos"` grants JSON key (kept `"papership"`)
- `apps/web/src/api/papership.js` token key `papership-token` (copies once from `engine-os-token`); OrgOS copy removed
- `scripts/dev-local.sh` store `/tmp/papership-api-store.sqlite` (the `~/.config/orgos` GitHub App path is still locked)
- Vercel runbook: `.cursor/memory/runbooks/vercel-papership-single-site.md` (old `vercel-orgos-single-site.md` deleted)

**Mistaken leftover-name audit files were deleted** (do not recreate them). A prior audit wrongly targeted another product name. That was a mistake. The only remaining leftover-name work is the provider-locked set in §6.

### 4.5 Named-competitor comparison tables withdrawn

Owner asked those tables gone too. Removed from:

- `docs/blueprints/2026-09-10_engine_labs.md` §5 (gap statement only) and §16 (no longer cites competitor prices)
- `docs/roadmap.md` GTM trust-assets line
- Growth charter / plan / handoff / evidence (Papership-only capability table remains)
- Project Lead notes / evidence (named third-party products and price-point claims stripped)

Attach-icon export renamed to `Attach` in `packages/ui/src/icons.tsx`, leftover `apps/web/src/components/cc-org-dash/`, and pinned `docs/ui-blueprint/blueprint-1/` copies. Working-tree grep for the withdrawn product name must stay empty. Do not restore those tables unless the owner asks.

### 4.6 What this session deliberately did **not** do

- Did not implement Phase 6 (T6-1…T6-8).
- Did not generate Phase 7 or a new final checklist.
- Did not change provider-locked files (§6).
- Did not rewrite git history or published `.orgos/loop/` receipts.
- Did not rename the workstream folder, decision filenames, or pinned blueprint HTML.
- Did not publish prices or enable Stripe charges.
- Did not treat D-25 as write/external Hermes `accepted`.
- Did not edit the Engine Labs marketing site.

Branch before the owner rename: `cursor/phase-6-planning-cc89`. Draft PR: https://github.com/enginelabs-au/OrgOS/pull/5 (URL will redirect after the GitHub repo rename). Base branch is `main`.

---

## 5. Owner actions before the next agent touches locked files

Do these on the dashboards. Then paste §0 into a new chat with this file and the saved transcript.

1. **GitHub repository.** Settings → rename `enginelabs-au/OrgOS` → `enginelabs-au/Papership`. Confirm `https://github.com/enginelabs-au/OrgOS` redirects. Live record (2026-09-12): repo id `1364169617`, homepage `https://orgos-ivory.vercel.app`. `origin` is `https://github.com/enginelabs-au/orgos` (GitHub treats it as OrgOS).
2. **GitHub App** `orgos-dev` (id `4908453`, installation `160851156`): selected repos must include the renamed repo. If the bot slug must also go, create a **new** App (slugs are often immutable), copy the PEM, update IDs. Never paste the PEM into chat or repo files.
3. **Vercel** project `orgos` (`prj_S74JOIky7KugVTrfu652NhJYOL8l`): relink Git if the connection breaks; rename the project if you want the dashboard slug gone. Preview host `orgos-ivory.vercel.app` may persist. **Never** touch `enginelabs-au-site`.
4. **Host / VPS env:** `GITHUB_APP_REPO=Papership`. Optional: `cp -a ~/.config/orgos ~/.config/papership` and point `github-app.paths`. Do not commit those files.
5. **Local folder:** `~/OrgOS` → `~/Papership` is safe after reopen (this cloud VM is already `/workspace`). Git remotes are URL-based.
6. Save this file + the transcript into the new chat.

Wait-list detail: `docs/handover/rename-owner-first-providers.md`.

---

## 6. Files the next agent must update after §5 (locked until then)

Changing these while the live repo is still `enginelabs-au/OrgOS` breaks `open_pull` and deploys. That is why they were left.

| File | Current contract | Change to |
|---|---|---|
| `.env.example` | `GITHUB_APP_REPO=OrgOS` | `GITHUB_APP_REPO=Papership` |
| `scripts/dev-local.sh` | default `GITHUB_APP_REPO=OrgOS`; reads `~/.config/orgos/github-app.paths` | default `Papership`; read `~/.config/papership/github-app.paths` if that dir exists, else keep reading the old path once |
| `services/api/app/github_app.py` | receipts `.orgos/loop/{slug}.md`; fallback `orgos-loop`; commit `orgos: {title}` | receipts `.papership/loop/{slug}.md`; fallback `papership-loop`; commit `papership: {title}`; **still read** existing `.orgos/loop/*.md` |
| `services/api/tests/test_github_app.py` | asserts the live path/prefix | assert the new path/prefix; keep a dual-read case |
| `services/api/tests/test_github_pulls.py` | fixtures `repo: OrgOS`, heads `orgos/…` | `repo: Papership`, heads `papership/…` |
| `services/api/tests/test_loop.py` | same live contract | same as pulls |

Do not rewrite published receipts already on GitHub under `.orgos/loop/`. After the follow-up, new receipts go to `.papership/loop/` and old files remain readable.

After those edits: re-run GitHub / loop pytest and `apps/web/tests/static-scan.test.mjs`. Update `.cursor/STATE.md` and append `.cursor/memory/memories/YYYY-MM-DD-continuation.md`.

---

## 7. Historical leftovers that stay on purpose

“Gone” means live product surfaces and new writing, not these pins.

- Workstream folder name `20260910-engine-labs-company-os`
- Decision filenames `docs/decisions/2026-09-11-orgos-*.md` (D-10, D-13, etc.)
- Pinned visual source `docs/ui-blueprint/blueprint-2/OrgOS*.html` and `docs/ui-blueprint/blueprint-1/**`
- Unused `apps/web/src/components/cc-org-dash/` (not the live mount; live chrome is `apps/web/src/blueprint2/`)
- `/cc-org-dash` **redirect** (bookmark alias)
- Git history and old PR titles (do not rewrite)
- Published `.orgos/loop/` receipts
- Asset filename `orgos-icon.png` until a later owner-asked rename
- D-20 still lists some historical slugs; D-32 supersedes the live route clause

---

## 8. Phase 6 when the owner asks (do not start from this file alone)

Canonical plan: `docs/plans/phase_6_commercial_delivery_plan.md` (all 22 sections). Authorization: `docs/decisions/2026-09-12-phase-6-planning-authorized.md` (D-33).

### In

- Entitlements, allowances, reservations, fail-closed limit checks in **billing test mode**.
- Settings / Plan D-29 labels only: Free / Basic / Professional / Enterprise.
- Remaining-allowance and action-cost **bands** only. Prefer band enums until CA-10. Tests must assert unpublished numerics never serialize to UI or public docs.
- Stripe **environment-variable names** only. Packages `@stripe/stripe-js` and `@stripe/react-stripe-js` exist in `apps/web/package.json` and are unused. `ENGINE_BILLING_CHARGES_ENABLED` must default false. No live-mode keys. No webhook that records a paid invoice.
- ERA-17 licensing-state hook as `configured` only with evidence; otherwise stay `planned` with an honest Settings row.
- Security CA-4 reconciliation review. Four entitlement/usage models in test mode, including no duplicate charges (PRD-G.12).
- Growth CA-1…CA-10 checklist. First-baseline stays `not_captured` if `event_count=0`. Price scan remains clean.
- Replace Today `Remaining allowance: 184640` with a band or `not_captured`.

### Out

- Prices, published quantities, seat counts, rates, invented KPI/usage numbers.
- Live Stripe charges or live-mode secret names as required.
- Phase 7 (mobile, SDK / P19 live, remaining market domains).
- Marketing site / `enginelabs-au-site`.
- Write / external Hermes `accepted` (D-25 is not that licence).
- Live treasury / inventory / mobile / SDK as working connectors.
- Public build-log (D-30).
- Generating Phase 7 or a new final checklist from the Phase 6 planning/rename turn.

### Tasks (all `pending` except T6-0 route evidence already landed)

| Task | Objective |
|---|---|
| T6-0 | Residuals + keep D-32 scan green |
| T6-1 | Entitlement / allowance schema; feature flag still ≠ grant |
| T6-2 | Reservation + fail-closed limits in test mode |
| T6-3 | Settings / Plan labels + bands; kill the 184640 fixture |
| T6-4 | Stripe test-mode names; charges stay off |
| T6-5 | ERA-17 hook |
| T6-6 | Security CA-4 |
| T6-7 | Growth CA checklist + price scan |
| T6-8 | PL G9 |

T6-3 may start after T6-1. T6-4 must not enable charges. T6-5 is independent of Stripe. Owner CA-10 / OQ-G2 / provider rename are off the critical path for G9 **structure**. Publishing rates is not a G9 requirement.

### Roles

All six required. Write `phase-6-*` charters when implementation starts, same workstream id. Lead — not an implementing role — moves `docs/capabilities.md` rows from `planned` only with evidence (D-02). Expected Phase 6 status is `configured` for commercial **structure**. R4 rows **B14, B19, B20, B21, B24, P19** stay `planned` unless deny-by-default catalogue shells.

### Env names Phase 6 may wire (values never in repo)

Carried: `HERMES_API_BASE_URL`, `HERMES_VERSION_PIN`, `HERMES_API_SERVER_KEY` (worker only; must not reach API), `GITHUB_APP_*`, `ENGINE_STORE_PATH`, `ENGINE_USAGE_EMIT` (default off).

T6-4 names only: `STRIPE_TEST_PUBLISHABLE_KEY`, `STRIPE_TEST_SECRET_KEY`, `STRIPE_TEST_WEBHOOK_SECRET`, `ENGINE_BILLING_CHARGES_ENABLED` (default false).

Not required for G9: `GMAIL_OAUTH_CLIENT_ID`, `GMAIL_OAUTH_REDIRECT_URL`, `SLACK_CLIENT_ID`. Do **not** add `STRIPE_LIVE_*`.

---

## 9. Standing decisions (do not re-ask)

| ID | File | Meaning |
|---|---|---|
| D-12 / D-14 | `docs/decisions/2026-09-11-data-responsibility-integrations.md`, `docs/decisions/2026-09-11-user-owned-data.md` | Users own their data; Engine Labs does not own user content; keep only generic anonymous usage |
| D-13 | `docs/decisions/2026-09-11-orgos-prism-brand.md` | Prism brand; in-app use later forbidden by D-21 |
| D-16 / D-17 | interception / tool enablement | Hermes catalog; unknown tools denied |
| D-20 / D-26 | `docs/decisions/2026-09-12-papership-product-name.md` | Product Papership; company Engine Labs; no marketing-site edits |
| D-21 / D-22 | `docs/decisions/2026-09-12-blueprint-2-product-ui.md`, Phase 4 closeout | Live chrome is blueprint-2 exactly; visual review approved |
| D-23 | Phase 4 closeout | OQ-G2 accepted; store fail-closed until live `POST /settings/oq-g2` |
| D-24 | Phase 4 closeout | Gmail/Slack = contract + wizard; send = approval then receipt |
| D-25 | Phase 4 closeout | Phase 4 security pass is **not** a licence for write/external Hermes |
| D-27 | Phase 4 closeout | First R3 = B01 + B03 + memory/adaptive views (done in Phase 5) |
| D-28 | Phase 4 closeout | R2=09, R3=10, R4=11+12 |
| D-29 | Phase 4 closeout | Free / Basic / Professional / Enterprise; **no prices** until CA-10 |
| D-30 | Phase 4 closeout | No public build-log |
| D-31 | `docs/decisions/2026-09-12-phase-5-planning-authorized.md` | Phase 5 planning (implemented; G7 PASS) |
| D-32 | `docs/decisions/2026-09-12-papership-canonical-route.md` | Canonical route `/papership` |
| D-33 | `docs/decisions/2026-09-12-phase-6-planning-authorized.md` | Phase 6 planning only until the owner asks to implement |

Also standing: AUTH-25 catalog; AUTH-29 adaptive views are schema-validated trusted components with no filesystem / shell / database / credential access. Closed owner questions (do not re-ask): OQ-2, OQ-3, OQ-4, OQ-G1, OQ-G2.

Capability registry: a `docs/capabilities.md` row moves from `planned` only when the evidence column cites a verified artifact. Usage measurement (Growth GM-1…12): first-party, in-tenant, identifier/enum payloads only; every threshold without data is labelled `first-baseline`.

---

## 10. Architecture snapshot the next agent will touch

Monorepo (D-01). Adapter pattern (D-04). Do not invent a second product shell.

| Area | Path / fact |
|---|---|
| Live web chrome | `apps/web/src/blueprint2/` mounted by `apps/web/src/App.jsx` at `/papership` |
| Live API client | `apps/web/src/api/papership.js` |
| Unused leftover screens | `apps/web/src/components/cc-org-dash/` |
| API | `services/api/app/main.py`, `store.py`, `github_app.py`, `usage.py` |
| Entitlements today | `entitlements(id, tenant_id, principal_id, feature)` + `POST /entitlements` / `GET /entitlements/me`. Feature flag ≠ permission (`test_entitlement_is_not_permission`). No allowance / reservation / limit rows |
| Usage | Events exist; `ENGINE_USAGE_EMIT` defaults off; `GET /usage/baseline` is `not_captured` at zero events; budget reserved/reconciled event names are not enforced |
| Local API | `bash scripts/dev-local.sh` → `http://127.0.0.1:8000/health`; store `/tmp/papership-api-store.sqlite` |
| Hermes tunnel | `bash scripts/hermes-tunnel.sh` to Host `hermes-vps`. HTTP API `:8642` (HEAD `/health` 405 = reachable; GET may hang). `hermes serve` on `:9119` is login UI. Do not copy VPS `auth.json` or start a second Hermes |
| Worker | May hold `HERMES_API_SERVER_KEY` (transport only). Live `accepted` only for catalogued **read** `tool=` after intercept. `start_run` without `tool=` is refused |
| Desktop | `apps/desktop/` Tauri; already Papership; not part of Phase 6 chrome work unless Settings already mirrors web |
| Marketing | Separate. Never this repo |

People / Inbox / Memory overlay via `papership.js`; unauthenticated = honest empty.

---

## 11. Owner residuals (none block Phase 6 **planning**; some block live seats)

Canonical log: `docs/handover/outstanding-actions-and-decisions.md`. Also `docs/handover/phase-4-owner-actions.md` and `docs/handover/phase-2-owner-actions.md` for older queues.

| Residual | Blocks G9 structure? | Blocks live second seat / connector / charge? |
|---|---|---|
| Live `POST /settings/oq-g2` | no | yes for a real second human or guest |
| Gmail/Slack OAuth: `GMAIL_OAUTH_CLIENT_ID`, `GMAIL_OAUTH_REDIRECT_URL`, `SLACK_CLIENT_ID` (names wired, values missing) | no | yes for live Gmail/Slack |
| This provider rename (§5) then locked-file follow-up (§6) | no | no (hygiene; breaks `open_pull` if half-done) |
| Mailbox creds off systemd `Environment=` | no | hygiene |
| Hermes GET `/health` hang (use HEAD first) | no | ops |
| Apple signing, DigitalOcean, backup restore, `execute_release` | no | R1 residual / publication |
| Fire live write/external Hermes tools | no — needs a **new** Security PASS | do not treat D-25 as that licence |
| Public build-log | no (D-30) | later explicit publish decision |
| Local folder `~/OrgOS` → `~/Papership` | no | safe after reopen |
| CA-10 publish rates; CA-10 activate charges (**two** decisions) | no for G9 structure | yes for any public number or charge |
| Stripe test-mode account / test env names | no for wiring | needed only if owner wants a live test checkout later |

---

## 12. Validation already on record, and what to re-run

Already recorded:

- Phase 5: API pytest 77 passed; worker 33; web `<title>Papership</title>`
- Pass A sweep: `apps/web/tests/static-scan.test.mjs`; API `test_env`, `test_github_grants`, `test_phase4`, `test_authz` after the grants-alias drop
- Click-through: continuation log 2026-09-12; screenshots historically under `/tmp/computer-use/` (ephemeral)

After the locked-file follow-up:

```bash
node .cursor/skills/launch-pipeline/scripts/preflight.mjs
# from services/api, the GitHub / loop / env tests
# from apps/web
node --test tests/static-scan.test.mjs
```

Do not claim Phase 6 complete without T6-1…T6-8 evidence, all six role handoffs, and G9.

When implementing UI, verify in the browser (or closest substitute) end-to-end: click, type, navigate; check routes that share state; check empty/error/theme variants. A single screenshot is not verification.

---

## 13. File index for the next chat

Read first:

- This file
- `docs/handover/rename-owner-first-providers.md`
- `docs/handover/outstanding-actions-and-decisions.md`
- `docs/plans/phase_6_commercial_delivery_plan.md`
- `.cursor/STATE.md`
- `.cursor/memory/MEMORY.md`
- `.cursor/memory/memories/2026-09-12-continuation.md` (and the UTC-day file for the new session)

Then as needed:

- Decisions: `docs/decisions/2026-09-12-phase-4-closeout.md` (D-22…D-30), `2026-09-12-papership-product-name.md`, `2026-09-12-blueprint-2-product-ui.md`, `2026-09-12-papership-canonical-route.md`, `2026-09-12-phase-5-planning-authorized.md`, `2026-09-12-phase-6-planning-authorized.md`
- Closed phase plans: `docs/plans/phase_4_collaboration_connections_plan.md`, `docs/plans/phase_5_company_operations_plan.md`
- Workstream: `docs/workstreams/20260910-engine-labs-company-os/manifest.md`; Phase 5 G7 `project-lead-subagent/phase-5-handoff.md`; Security Phase 5 `security-engineer-subagent/phase-5-handoff.md`
- Product contracts: `docs/product.md`, `docs/capabilities.md`, `docs/architecture.md`, `docs/roadmap.md`, `docs/verification.md`, `docs/blueprints/2026-09-10_engine_labs.md`
- R1 owner handoff: `docs/workstreams/20260910-engine-labs-company-os/delivery/owner-handoff.md`
- Vercel (Papership project only): `.cursor/memory/runbooks/vercel-papership-single-site.md`
- Dev env: `.cursor/memory/runbooks/engine-labs-dev-environment.md`
- GitHub App / model key (names, not values): `docs/handover/github-app-and-model-key.md`

---

## 14. Common pitfalls from this session (do not repeat)

1. **Wrong leftover-name target.** A prior audit treated another product name as the destination. That was a mistake. Destination is **Papership**. Deleted audit files must stay deleted.
2. **Flipping locked files before the GitHub repo matches.** Breaks `open_pull` and deploys. Confirm §5 first.
3. **Implementing Phase 6 because a plan exists.** D-33 is plan-only. Wait for an explicit implement request.
4. **Generating Phase 7 early.** One plan at a time. Phase 7 only after G9.
5. **Restoring competitor tables** while “researching positioning.” Owner withdrew them.
6. **Showing unpublished quantities.** The 184640 allowance is the known leak; do not add more.
7. **Editing `enginelabs-au-site`.** Different product.
8. **Rewriting git history** or published `.orgos/loop/` receipts to chase leftover names.
9. **Renaming the workstream folder** to match Papership. Frozen task id.
10. **Putting secrets in the resume chat.** Paste this file and the transcript; not PEMs, tokens, or `.env` values.
11. **Treating D-25 as write/external Hermes licence.** It is not.
12. **Inventing prices or first-baseline numbers** to make CA-10 look ready.

---

## 15. What not to do (standing)

- Do not implement Phase 6 until the owner says implement
- Do not generate Phase 7 or a new final checklist from a Phase 6 planning/rename turn
- Do not publish prices or enable Stripe charges
- Do not treat D-25 as write/external Hermes `accepted`
- Do not invent KPI, usage, or allowance numbers
- Do not restore named-competitor comparison tables unless the owner asks
- Do not edit the Engine Labs marketing site
- Do not store secret values in agent files
- Do not claim completion without evidence
