---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: security-engineer-subagent
status: complete
revision: 1
verdict: CONDITIONAL
started_at: 2026-09-10T17:25:00Z
completed_at: 2026-09-10T17:58:00Z
downstream_role: growth-marketing-subagent
risk_tier: 3
charter: docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/charter.md (r1)
plan: docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/plan.md (r1)
evidence: docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/evidence.md
---

# Security Engineer handoff — T0-9 Security gate

Produced read-only by the role; materialized verbatim by the orchestrating lead on 2026-09-10. Policy drafts referenced in §4 are materialized at `docs/policies/`.

## 1. Outcome

The T0-9 Security gate for the Engine Labs Company OS release-1 foundations is **CONDITIONAL**. The phase-0 documentation set (`docs/architecture.md`, `docs/product.md`, `docs/capabilities.md`, `docs/ui-blueprint.md`, D-01, D-04) establishes a sound trust-boundary structure, a server-side authority model, a persist-before-accept action lifecycle, retention defaults and a backup design. No secret values, private keys or provider tokens exist in the repository (EV-SEC-08). The repository control plane (hooks, permissions, sandbox, CI) is present and fail-closed (EV-SEC-10).

The gate is not PASS because three high-impact controls are design-stage and unverified: (1) enforceable interception of Hermes side-effecting tools, including the finding that Hermes `/v1/runs/{id}/approval` cannot be the sole approval path and must be wrapped by the Engine Labs action service (F-SEC-01); (2) restriction of public exposure to the Engine Labs API and Supabase Auth only, since RLS as designed does not protect against direct PostgREST/Storage access (F-SEC-02, F-SEC-03); (3) approval authority modelled as an explicit grant class that agent principals can never hold (F-SEC-04). Each has a phase-1 gate. The gate is not BLOCKED because nothing is exploitable today (no code exists), the fail-closed fallback for interception is already a decision (D-04 decision 9), and no downstream Growth work depends on these controls.

## 2. Scope completed / not completed

Completed (plan §6):
1. Component, data-store, trust-boundary and destination enumeration with gaps (EV-SEC-02).
2. STRIDE threat model for TB-1…TB-10 plus TB-11 (desktop update/signing), TB-12 (repository automation), TB-13 (memory/retrieval store) — §5 below.
3. Authority-model review with gap list (EV-SEC-04; §9 F-SEC-03…F-SEC-06).
4. Agent execution control review, approval-path decision and spike requirement (EV-SEC-05; §9 F-SEC-01).
5. Data lifecycle review including Growth consent/data-minimisation constraints (EV-SEC-06; §11).
6. Secrets and supply-chain review including F-S3 disposition and `npm ci` stance (EV-SEC-07, EV-SEC-11).
7. Repository hygiene scan and `.gitignore` review (EV-SEC-08, EV-SEC-09).
8. Findings register F-SEC-01…F-SEC-19 with severity, owner, remediation, re-verification and phase gate (§9).
9. Five policy drafts (materialized under `docs/policies/`).
10. Evidence and this handoff.

Not completed / out of scope:
- No dynamic testing: no code, no running stack, no Hermes instance (charter: read-only; no reference execution).
- Hermes licence terms and image digest not verified (LIC-05, LIC-07 assign this to phase 1).
- DigitalOcean volume encryption-at-rest not verified (DRR-15).
- F-S3 advisories not itemised (not shipped; EV-SEC-11).

## 3. Charter, plan and predecessor references

- Charter r1 and plan r1 (paths in front matter). Charter §5 assumptions: "hooks live" — confirmed VERIFIED (EV-SEC-10); "Hermes auth transport-only" — confirmed and strengthened: `API_SERVER_KEY` grants full toolset including terminal, therefore it is a transport credential with root-equivalent consequence and must never be treated as authorization (AUTH-22, T-18).
- Predecessors: PM handoff (CONDITIONAL, OQ-1…OQ-6), UI/UX handoff (CONDITIONAL, F-U3 simulated behaviours "high if shipped"), SE handoff (CONDITIONAL; F-S1…F-S7; §11 instructions to Security followed: TB-1…TB-10, §6, §7, §9, §10, §12 reviewed; capabilities authority columns reviewed; `.gitignore` reviewed per EV-S02; D-04 decisions 3, 6, 7, 9, 11 reviewed; `cc-org-dash-auth` localStorage stub recorded as a must-not-survive pattern AUTH-27).
- Manifest §4 Tier 3 rationale accepted; §6 REQ-03/04/05 addressed in §5 (coverage table).

## 4. Outputs, changed paths and external effects

- Changed paths by the role: none (read-only). Materialized by the lead:
  - `docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/evidence.md`
  - `docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/handoff.md` (this file)
  - `docs/policies/authority-model.md`, `docs/policies/data-residency-and-retention.md`, `docs/policies/memory-governance.md`, `docs/policies/erasure-and-offboarding.md`, `docs/policies/licensing.md`
- External effects: none. No network calls other than the tool sandbox's own operation; no MCP calls.

## 5. Requirement and horizontal coverage

### 5.1 Requirement coverage

| Requirement | Source | Coverage | Evidence |
|---|---|---|---|
| REQ-03 Authority enforced server-side | manifest §6; PRD-D.5 | Reviewed; gaps F-SEC-03/04/06; policy AUTH-08…AUTH-14 | EV-SEC-04 |
| REQ-04 Side effects only via action lifecycle | manifest §6; PRD-E.10 | Reviewed; F-SEC-01 (interception), F-SEC-19 (idempotency retention) | EV-SEC-05 |
| REQ-05 Data lifecycle governed | manifest §6; PRD-F | Reviewed; F-SEC-07/08/14/16; policies DRR, MEM, ERA | EV-SEC-06 |
| NFR security/privacy (NFR-1…10) | `docs/product.md` | Mapped in §5.2 | EV-SEC-03 |
| Phase plan §15 checks | `docs/plans/phase_0_foundations_plan.md` | Hygiene clean; `.gitignore` gaps low; `npm ci` stance recorded | EV-SEC-08/09/07 |
| Charter §9 gate criteria | charter | All criteria met; see §14 | EV-SEC-14 |

### 5.2 STRIDE threat model (horizontal coverage)

Legend: S spoofing, T tampering, R repudiation, I information disclosure, D denial of service, E elevation of privilege. Owner: SE = software engineer, SEC = security, OWN = owner (human-only), PL = project lead. Phase = phase in which the control is verified with evidence. "Now" = verified in phase 0 by this review.

**TB-1 Desktop ↔ Engine Labs API (Tauri webview, TLS, JWT)**

| ID | STRIDE | Threat | Control (release 1) | Owner | Phase |
|---|---|---|---|---|---|
| T-01 | S | Stolen or replayed access token | Access tokens ≤ 15 min; GoTrue refresh-token rotation with reuse detection; sign-out revokes refresh token; tokens stored only in OS keychain (AUTH-26, AUTH-27) | SE | 1 |
| T-02 | T | Man-in-the-middle or request tampering | TLS 1.2+ only, HSTS at proxy, no plaintext fallback; `ENGINE_API_BASE_URL` pinned per build | SE | 1 |
| T-03 | R | Actor denies an approval or change | Audit event per authorization decision with actor, approver, target id and version, policy version (AUTH-15) | SE | 1 |
| T-04 | I | XSS via SSE or markdown content rendered in webview | Strict Tauri CSP (no `unsafe-inline`, no remote scripts), sanitised markdown, no raw HTML, SSE payloads treated as untrusted (F-SEC-13) | SE | 1 |
| T-05 | I | Token or secret in web storage | Keychain plugin only; static scan forbids `localStorage`/`sessionStorage` writes with auth-shaped keys; reference `cc-org-dash-auth` pattern removed (AUTH-27) | SE | 1 |
| T-06 | D | API flooding, run-creation abuse | Per-principal and per-IP rate limits; run-creation quota per seat; 429 with retry-after | SE | 1 |
| T-07 | E | Over-granted Tauri capability (fs, shell, http) | Minimal capability set; `shell:allow-open` restricted to `https?` scheme with user confirmation; no `fs` scope; Security review of `src-tauri/capabilities/*` (F-SEC-17) | SE, SEC | 1 |
| T-08 | I | Desktop cache retains data after revocation or sign-out | Cache holds preferences and last-known view state only; purged on sign-out and on grant-version change (AUTH-14, DRR-13) | SE | 1 |

**TB-2 API ↔ Supabase (Auth, Postgres, Storage)**

| ID | STRIDE | Threat | Control | Owner | Phase |
|---|---|---|---|---|---|
| T-09 | S/E | Anon key + user JWT used directly against PostgREST/Storage/Realtime, bypassing API authorization | Only `/auth/v1/*` and the Engine Labs API are reachable from `edge`; PostgREST, Realtime, Storage, Studio, Supavisor bound to `data` network only; external port scan and Compose config test (F-SEC-02) | SE | 1 |
| T-10 | T | SQL injection | Parameterised queries only; Pydantic validation; no dynamic SQL from user input | SE | 1 |
| T-11 | I/E | Service-role or superuser DB role makes RLS void; API compromise = full DB | API connects with least-privilege role lacking `BYPASSRLS`; per-request `SET LOCAL app.tenant_id, app.principal_id`; RLS policies on tenant and principal; `SUPABASE_SERVICE_ROLE_KEY` restricted to admin jobs (F-SEC-03) | SE | 1 |
| T-12 | I | Studio exposed | Not published; SSH tunnel only; basic auth in addition (architecture §9) | SE | 1 |
| T-13 | D | Connection exhaustion | Supavisor pooling; statement and idle timeouts | SE | 1 |
| T-14 | E | Worker or Hermes reaches Postgres or DBOS system DB | Worker has no DB credentials and no `data` network membership (architecture §14 adopted; AUTH-24); env-exclusion test (PRD-B.10) | SE | 1 |
| T-15 | T | Audit table mutated | App role has INSERT only on audit tables; no UPDATE/DELETE grant; optional hash chain (F-SEC-15) | SE | 1 |

**TB-3 API/DBOS ↔ worker (Hermes adapter)**

| ID | STRIDE | Threat | Control | Owner | Phase |
|---|---|---|---|---|---|
| T-16 | S | Rogue caller submits jobs to adapter | Adapter accepts jobs only from the `api` service via `app` network plus per-deployment shared header secret or mTLS; `HERMES_API_SERVER_KEY` present only in worker | SE | 2 |
| T-17 | T | Event stream tampering or loss | Adapter is sole subscriber; events checkpointed to Job record; status reconciled with `GET /v1/runs/{id}` on gap or reconnect (D-04 decision 7) | SE | 2 |
| T-18 | I/E | Lateral movement to Hermes = full terminal access | Hermes bound to `worker` network only; port 8642 not published; per-profile keys; `/health/detailed` internal only | SE | 2 |
| T-19 | D | `max_concurrent_runs` 429 storms | DBOS queue concurrency below Hermes cap; exponential backoff; budget deadline | SE | 2 |
| T-20 | R | Duplicate runs on retry | `Idempotency-Key` derived from persisted Job id; replay test; adapter checks own Job state before calling because Hermes retains keys 24 h only (F-SEC-19) | SE | 2 |
| T-21 | I | SSE free text carries secrets | Do not rely on Hermes forced redaction; adapter applies Engine Labs redaction before persistence; secrets never in prompts (MEM-14) | SE | 2 |

**TB-4 Worker/Hermes ↔ execution sandbox (worktrees, shell)**

| ID | STRIDE | Threat | Control | Owner | Phase |
|---|---|---|---|---|---|
| T-22 | E | Prompt-injected shell/file actions escape scope | Per-run worktree mounts only; non-root; `no-new-privileges`; read-only root FS; seccomp default; no Docker socket; no credential or orchestration DB mounts (PRD-E.6) | SE | 2 |
| T-23 | I | Data exfiltration via network | Egress allowlist (GitHub, model providers, package registries as needed) enforced at firewall/proxy; DNS restricted; egress test to non-allowlisted host must fail | SE | 2 |
| T-24 | I | Credential discovery in env or files | Worker/Hermes env contains only `HERMES_API_BASE_URL`, `HERMES_API_SERVER_KEY`, `MODEL_PROVIDER_API_KEY`, `HERMES_VERSION_PIN`; assertion test for absence of `GITHUB_APP_*`, `SUPABASE_SERVICE_ROLE_KEY`, `DATABASE_URL`, `DBOS_SYSTEM_DATABASE_URL`, `SUPABASE_JWT_SECRET`, `POSTGRES_PASSWORD`, `BACKUP_*`, `DIGITALOCEAN_API_TOKEN`, `TAURI_SIGNING_*`, `APPLE_*` | SE | 1 (compose) / 2 (runtime) |
| T-25 | T | Worktree state persists across runs | Ephemeral volume purged at run close; purge receipt in Job | SE | 2 |
| T-26 | D | Runaway resource use | CPU/memory/pids limits per container; budget deadline cancels run | SE | 2 |

**TB-5 Hermes tools ↔ Engine Labs action service**

| ID | STRIDE | Threat | Control | Owner | Phase |
|---|---|---|---|---|---|
| T-27 | E | Side effect executed by a Hermes tool without action lifecycle | Interception mechanism proven by spike SP-1…SP-7; until proven, side-effecting toolsets disabled and registry rows `unavailable` (D-04 decision 9; F-SEC-01) | SE, SEC | 1 (fail-closed) / 2 (spike) |
| T-28 | R/T | Duplicate or unrecorded external effects | Receipt persisted before completion; idempotency key per action; reconciliation on timeout-after-write (PRD-E.8) | SE | 2 |
| T-29 | S/E | Agent approves its own action | Approval requires human principal with `approval.<class>` grant; agent principals cannot hold approval grants (AUTH-09, AUTH-11; F-SEC-04) | SE | 1 |
| T-30 | T | Approval reused for a different target version | Approval record stores hash of action type, parameters, target id, target version, policy version; executor recomputes and refuses on mismatch (AUTH-10) | SE | 1 |
| T-31 | E | Budget overrun by child runs | Reservation before dispatch; child spend debits parent; ceiling refusal recorded (PRD-E.3) | SE | 2 |

**TB-6 Action service ↔ GitHub**

| ID | STRIDE | Threat | Control | Owner | Phase |
|---|---|---|---|---|---|
| T-32 | E | Over-scoped installation token | GitHub App with minimal permissions; installation token minted per action narrowed by `repositories` and `permissions`; release grant class separate and default off (PRD-B.4) | SE | 2 |
| T-33 | I | App private key exposure | `GITHUB_APP_PRIVATE_KEY_PATH` mounted read-only into `api` only; never in worker (T-24) | SE | 1 |
| T-34 | T | Push to protected branch or release without approval | Branch protection on the customer repository (owner action); server-side grant check; source-permission intersection for repo grants in R1 (F-SEC-05, AUTH-12) | SE, OWN | 2 |
| T-35 | R | Unattributed commits | Commits attributed to the App identity with `Engine-Run-Id` trailer; audit link to Job | SE | 2 |

**TB-7 Hermes ↔ model providers**

| ID | STRIDE | Threat | Control | Owner | Phase |
|---|---|---|---|---|---|
| T-36 | I | Customer content leaves tenant to provider | Provider policy record per tenant (no-training terms recorded, DRR-06); context minimised to permitted knowledge (PRD-E.12); fixtures until permission granted | SE, OWN | 2 |
| T-37 | S | Provider key misuse | `MODEL_PROVIDER_API_KEY` only in worker; rotation runbook; spend ceilings via budget reservation | SE | 2 |
| T-38 | D | Provider outage or throttling | Circuit breaker per provider; incident record; no recursive recovery (PRD-E.9) | SE | 2 |

**TB-8 Backups**

| ID | STRIDE | Threat | Control | Owner | Phase |
|---|---|---|---|---|---|
| T-39 | I | Unencrypted or provider-readable export | Encrypt with client-owned key (`BACKUP_ENCRYPTION_KEY_PATH`) before upload; key never stored at `BACKUP_TARGET_URL` (DRR-14) | SE | 3 |
| T-40 | T | Tampered archive restored | Checksum and signed manifest verified before restore | SE | 3 |
| T-41 | D | Backup unusable | Restore dry run phase 3; full drill R4 (V15-5) | SE | 3 |
| T-42 | R | Erasure receipt misreports backup copies | Receipt lists pending backup copies with expiry ≤ 30 d (ERA-12) | SE | 3 |

**TB-9 / TB-12 Repository automation (hooks, CI, protected paths)**

| ID | STRIDE | Threat | Control | Owner | Phase |
|---|---|---|---|---|---|
| T-43 | E | Agent modifies enforcement files | `isProtectedPath` deny in `policy.mjs`; owner-only edits; CI validators | OWN | Now (EV-SEC-10) |
| T-44 | T | CI supply chain (mutable action tags) | Pin Actions to commit SHA; `permissions: contents: read` present; Dependabot for actions | OWN | 1 |
| T-45 | I | Secrets committed | Hygiene scan clean (EV-SEC-08); `.gitignore` plus gaps (F-SEC-11); hook denies secret-path reads; CI secret scanner (LIC-14) | SE, OWN | Now / 1 |
| T-46 | D | Governance CI never runs | Workflow targets `main`; branch is `master` — owner decision (manifest §13) | OWN | 1 |
| T-47 | E | Agent executes untrusted reference code | `.reference/` git-ignored; D-01 forbids import; no further reference execution by agents (EV-SEC-11) | PL | Now |

**TB-10 Identity namespaces**

| ID | STRIDE | Threat | Control | Owner | Phase |
|---|---|---|---|---|---|
| T-48 | S | Credential or identity reuse across member, agent and service identities | Distinct principal types in data model; agents have no interactive credentials; service identities are per-service with separate secrets (AUTH-05) | SE | 1 |
| T-49 | E | Cursor delivery role treated as product authority | No production authority inferred from repository roles (AGENTS.md security boundary); release actions owner-only | OWN | Now |

**TB-11 Desktop update and signing (added)**

| ID | STRIDE | Threat | Control | Owner | Phase |
|---|---|---|---|---|---|
| T-50 | T | Tampered update artefact | Tauri updater signature with embedded public key; notarisation; `TAURI_SIGNING_*` and `APPLE_*` only in CI protected environment | SE, OWN | 3 |
| T-51 | S | Rogue update endpoint | Pinned HTTPS endpoint; signature required regardless of endpoint | SE | 3 |
| T-52 | I | Signing key theft | CI secret scoping, environment protection rules, rotation runbook, revocation plan | OWN | 3 |

**TB-13 Memory and retrieval store (added)**

| ID | STRIDE | Threat | Control | Owner | Phase |
|---|---|---|---|---|---|
| T-53 | I | Retrieval crosses a permission boundary | Permission recheck at retrieval time against current grants and source-permission snapshot; derived summaries inherit most restrictive source (MEM-08, MEM-09) | SE | 1 |
| T-54 | T | Memory poisoning via untrusted content | Class `inferred` never auto-promoted; promotion to `approved` requires human review with provenance (MEM-05, MEM-06) | SE | 1 / 2 |
| T-55 | I | Credentials written to memory | Credential-shaped scan and refusal before write (MEM-12) | SE | 1 |
| T-56 | I | Hermes runtime memory crosses tenants or principals | `X-Hermes-Session-Key` derived from tenant + principal + purpose; Honcho-class provider disabled or local in R1 (F-SEC-07, MEM-17) | SE | 2 |
| T-57 | R | Memory change unattributed | Seven provenance fields mandatory (PRD-F.2) | SE | 1 |
| T-58 | D | Retention job deletes required records | Retention job dry-run mode, legal-hold flag, audit of deletions (DRR-11) | SE | 2 |

## 6. Validation and evidence

All evidence records EV-SEC-01…EV-SEC-14 are in `evidence.md`. Executed commands: `date -u`, `rg` hygiene scan (exit 1 = clean), `git status --porcelain`, `ls docs/policies` (absent), `rg` over `docs/verification.md`. All other validation is document inspection. No hook denials occurred for this role. No tests, builds or type checks were run because no product code exists; SE's EV-S01–EV-S16 were relied upon for repository facts.

## 7. Tools, skills and MCP used

- Tools: `Read`, `Glob`, `Grep`, read-only `Shell`.
- Skills: none invoked.
- MCP: none.
- No `.reference/orgos/` code executed.

## 8. Assumptions, decisions and deviations

- A-1 (recorded): Severity in §9 denotes impact if the control is absent at the named gate; nothing is exploitable at phase 0 because no implementation exists. This is how ROLES §7's distinction between "exploitable defects" and "missing evidence / design requirements" is applied to a documentation-only phase.
- A-2 (recorded): Architecture §14 open item "worker DB access" is adopted as "none" (AUTH-24). If SE needs worker DB access, a new Security review is required.
- A-3 (recorded): Hermes documentation capture of 2026-09-10 reflects current upstream behaviour; the pinned version may differ; the spike validates against the pin.
- A-4 (recorded): DigitalOcean volume encryption at rest is not assumed; DRR-15 requires verification or application-level encryption of the Hermes profile volume.
- Decision D-S1: Hermes `/v1/runs/{id}/approval` is **not** an acceptable sole approval path (EV-SEC-05; F-SEC-01).
- Decision D-S2: `npm ci --ignore-scripts` is the default for product installs; exceptions are allowlisted with justification (LIC-12).
- Deviation: none from charter or plan.

## 9. Findings, severity and risks

Exploitable now: **No** for all findings (phase 0, no code). Re-verification is by the named phase gate with evidence from SE and re-review by Security.

| ID | Sev | Title | Owner | Remediation | Re-verification | Gate |
|---|---|---|---|---|---|---|
| F-SEC-01 | High | Enforceable interception of Hermes side-effecting tools unproven; Hermes `/approval` cannot be sole approval path | SE (impl), SEC (review) | Engine Labs API owns approval record bound to action + target version (AUTH-10); adapter forwards decision only (D-04 decision 6). Phase 1: encode fail-closed default — worker refuses to start with any side-effecting toolset enabled unless config flag `interception_verified` is backed by a committed contract-test artefact; registry rows for side-effecting Hermes tools `unavailable`. Phase 2: spike SP-1…SP-7 as the first phase-2 task. | Phase 1: config test + startup refusal test. Phase 2: spike evidence with pass on SP-1…SP-7, Security re-review before any run with side-effecting tools. | Phase 1 (fail-closed) + Phase 2 (spike) |
| F-SEC-02 | High | Public exposure of Supabase services other than Auth would bypass API authorization | SE | Reverse proxy publishes only Engine Labs API and `/auth/v1/*`; PostgREST, Realtime, Storage API, Studio, Supavisor on internal networks; remove unneeded services from Compose (architecture §9). | Compose config assertion test; external port scan of dev stack; unauthenticated and anon-JWT requests to `/rest/v1/*`, `/storage/v1/*`, `/realtime/v1/*` unreachable from `edge`. | Phase 1 |
| F-SEC-03 | Medium | RLS described as defence in depth but API uses service-role/superuser credentials, so RLS is void | SE | API DB role without `BYPASSRLS`; per-request `SET LOCAL` tenant/principal; RLS policies; service-role key restricted to admin jobs. Or: remove the RLS claim from architecture and rely on API tests alone (weaker; not recommended for Tier 3). | Role inventory (`\du`) shows no `BYPASSRLS`/superuser for app role; two-principal RLS test. | Phase 1 |
| F-SEC-04 | High | Approval authority not modelled as grant; agents not structurally excluded from approving; agent effective authority undefined | SE | Grant classes `approval.<action-class>` (AUTH-09); approver must be a human principal holding the grant and not the sponsor of the action unless policy allows self-approval for that class (default: not allowed for release, erasure, billing, `org.admin`); agent effective grants = sponsor grants ∩ toolset ceiling ∩ mode set (AUTH-07). | Tests: agent principal cannot be assigned any `approval.*` grant; self-grant refused (PRD-D.11); approval by sponsor refused for restricted classes. | Phase 1 |
| F-SEC-05 | Medium | Source-permission intersection deferred to R2 while GitHub is an R1 source | SE | Apply intersection for repo grants in R1: server checks installation permissions ⊇ requested operation before minting a narrowed token (AUTH-12). | Contract test with an installation lacking `contents:write` → refusal recorded. | Phase 1 (schema) / Phase 2 (test) |
| F-SEC-06 | Medium | Revocation propagation, token lifetime, mid-run recheck and cache purge unspecified | SE | Access token ≤ 15 min; per-principal `grant_version` checked per request and per action step (PRD-D.12); desktop purges cache on grant-version change; revocation effective ≤ 60 s (AUTH-13, AUTH-14). | Test: revoke grant mid-run → next step refused; token still valid but request refused. | Phase 1 |
| F-SEC-07 | Medium | Data-destination map incomplete (update channel, CI secrets, Auth email provider, Hermes memory provider, ACME) | SE | Add rows to architecture §6 and boundaries TB-11/TB-13 to §5; decide Hermes memory provider = disabled or local for R1. | Architecture revision reviewed by Security. | Phase 1 |
| F-SEC-08 | Medium | Desktop file download path via Storage undefined | SE | Files served via API or API-minted signed URLs with TTL ≤ 5 min after authorization check; Storage never directly reachable from `edge` (F-SEC-02). | Test: signed URL for unauthorized principal refused; expired URL refused. | Phase 1 |
| F-SEC-09 | Medium | Secret store for R2 connector credentials undecided; R1 relies on env/file mounts | SE, OWN | R1: env-exclusion assertion test (T-24); secrets via Compose `.env` or file mounts with 0400 permissions; R2: decision record for secret store before connectors. | Env assertion test; decision record exists before R2 work. | Phase 1 |
| F-SEC-10 | Medium | Supply-chain baseline absent (no scanners, no licence inventory, Hermes licence/digest unverified, Actions by tag) | SE, OWN | CI: `npm audit --audit-level=high`, `pip-audit`, `cargo audit`, licence inventory (LIC-06…LIC-09); `infra/digests.lock` with Hermes image digest; Actions pinned by SHA (owner, protected file). | CI run artefacts in phase 1. | Phase 1 |
| F-SEC-11 | Low | `.gitignore` lacks `*.pfx`, `credentials.json`, `secrets.json`, `.netrc`, `.npmrc`, `.pypirc`, `id_rsa*` | SE | Add patterns; keep `!.env.example` exceptions. | `git check-ignore -v` on each pattern. | Phase 1 |
| F-SEC-12 | Low | F-S3: 24 advisories in `.reference/orgos/` | SE | Accepted for reference (not shipped, git-ignored, not imported per D-01). Product lockfiles built fresh; no reference lockfile inheritance; agents must not run the reference dev server again. | `npm audit` on product lockfiles: no open high/critical. | Phase 1 |
| F-SEC-13 | Medium | Prompt-injection and output-handling posture not consolidated | SE | Untrusted-content labelling in adapter (PRD-E.6); policy outside prompts; per-mode tool allowlist; egress allowlist (T-23); desktop renders SSE/markdown as untrusted with strict CSP (T-04); external links require confirmation; injection fixture suite. | Phase 1: CSP and sanitiser tests. Phase 2: fixture suite — injected instruction to invoke side-effecting tool refused by policy. | Phase 1 / Phase 2 |
| F-SEC-14 | Medium | Hermes gateway state (SQLite sessions, stored responses, memory files) holds content outside backup and erasure inventory | SE | Add to erasure inventory (ERA-08): delete sessions via Hermes sessions API and purge profile volume paths; retention job covers stored responses; volume encryption verified or applied (DRR-15). | Erasure test: after org erasure, Hermes session lookup → 404 and volume paths empty. | Phase 2 |
| F-SEC-15 | Low | Audit log append-only not enforced at DB level | SE | App role INSERT-only on audit tables; migration test attempts UPDATE/DELETE → permission denied. | Migration test. | Phase 1 |
| F-SEC-16 | Medium | Usage-measurement consent and data-minimisation constraints undefined for Growth | Growth (adopt), SE (schema) | Adopt GM-1…GM-12 (§11); UsageEvent schema excludes content fields by construction. | Schema review by Security in phase 1; Growth handoff cites GM constraints. | Phase 1 |
| F-SEC-17 | Low | Tauri webview posture (CSP, capabilities, updater) unspecified | SE, SEC | CSP; minimal capabilities; `shell:allow-open` https only; updater config with pubkey (T-07, T-50). | Capability file review; CSP header test. | Phase 1 (capabilities) / Phase 3 (signing) |
| F-SEC-18 | Low | Undocumented Hermes `steer` route referenced in docs | SE | Adapter uses only documented endpoints advertised in `GET /v1/capabilities` for the pin; unknown capabilities ignored. | Adapter capability check test. | Phase 2 |
| F-SEC-19 | Low | Hermes idempotency keys retained 24 h only; adapter must not depend on Hermes for de-duplication | SE | Adapter persists `hermes_run_id` in Job before dispatch and checks it before any retry; Hermes key is secondary. | Retry-after-25h simulation test. | Phase 2 |

**Spike requirement for F-SEC-01 (phase 2, first task):**
- SP-1: Enumerate `GET /v1/toolsets` and `GET /v1/capabilities` for the pinned version; record every side-effecting tool (terminal, file write, browser, web fetch, subagent spawn, any MCP tool).
- SP-2: Determine whether Hermes provides a server-enforced tool-approval policy hook that (i) pauses before execution of a named tool, (ii) emits an SSE event containing tool name and full arguments, (iii) blocks until `/approval` receives a decision, (iv) refuses execution on deny or timeout. Evidence: transcript of a gated run with a deliberately targeted tool and the raw SSE events.
- SP-3: If SP-2 holds, verify the adapter can bind the Hermes approval request to an Engine Labs action (create action, run lifecycle steps 1–5, record approval, then forward) and that Hermes refuses when the adapter never forwards.
- SP-4: If SP-2 does not hold, verify that disabling side-effecting toolsets is enforced server-side (a run instructed to call the terminal tool fails with a policy error, not a model refusal), and that Engine Labs-owned tools (worktree git operations via the action service) provide the R1 development loop instead.
- SP-5: Injection bypass test: a prompt-injection fixture instructing the agent to execute a side-effecting tool directly must be refused by policy in both SP-3 and SP-4 configurations.
- SP-6: Egress test from the sandbox to a non-allowlisted host must fail.
- SP-7: Record the pinned image digest, the toolset configuration file hash and the test artefacts; Security re-review before any run with a side-effecting toolset is enabled in any environment.

## 10. Remediation and invalidated gates

- No prior Security gate exists to invalidate.
- SE F-S3 disposition: accepted as low (F-SEC-12); SE handoff row "owner Security" may be closed with this reference.
- SE F-S5 (interception) remains open and is subsumed by F-SEC-01.
- UI/UX F-U3 (simulated behaviours): Security concurs "high if shipped"; AUTH-28 forbids shipping simulated authorization or approval controls.
- PM OQ-1…OQ-6: no Security blocker; OQ items touching authority should reference AUTH-09 (approval grants) when resolved.

## 11. Downstream instructions

### 11.1 Next role: `growth-marketing-subagent`

Required inputs: this handoff §11.1; `docs/product.md` §10 metric taxonomy and PRD-G.11; `docs/policies/data-residency-and-retention.md` DRR-20…DRR-27; `docs/policies/memory-governance.md` MEM-19…MEM-20.

Constraints (consent and data minimisation for usage measurement, positioning and lifecycle):
- GM-1: UsageEvent and any measurement event MUST contain no prompt text, no conversation content, no file content, no memory items, no external individual's personal data. Permitted fields: tenant id, pseudonymous member id, run id, mode, model band (not full config), token counts, tool-call counts by class, duration, estimated cost band, outcome code, timestamp.
- GM-2: Provider usage MUST be de-duplicated by provider event id; no fabricated or interpolated baselines; absence of data is reported as absence.
- GM-3: Events are retained 365 d then aggregated; individual events are not individually erasable but MUST be excluded from any export after organisation erasure and MUST be aggregated within 30 d of erasure (ERA-14).
- GM-4: No third-party analytics SDK, pixel, session-replay or fingerprinting in the desktop or API in R1. Any telemetry (`SENTRY_DSN`) is opt-in per organisation, scrubbed of content and identifiers, and its payload inspected as evidence (R1-ACC-14).
- GM-5: No cross-tenant learning, benchmarking or "customers like you" features without an adopted policy; single-tenant deployments do not share data with Engine Labs except licensing state (R4) and opt-in telemetry.
- GM-6: Personal preference learning (PRD-F kind: preference) stays inside the tenant and MUST NOT feed marketing segmentation.
- GM-7: Lifecycle messaging MUST be triggered only by consented channels; no scraping of member contacts from connected sources (GitHub, later Slack/email) for marketing.
- GM-8: Positioning MUST NOT claim security certifications, compliance frameworks, "zero data retention" or provider no-training guarantees unless a decision record with evidence exists (DRR-06). Claims about encryption and isolation must match `docs/architecture.md` as verified.
- GM-9: Experiments MUST NOT vary authorization, approval, retention or safety behaviour; A/B scope is limited to presentation and onboarding copy.
- GM-10: Attribution uses first-party, consented identifiers only; no cross-site tracking.
- GM-11: Event taxonomy additions require Security review of the schema before implementation (F-SEC-16 gate).
- GM-12: Any external destination introduced for measurement becomes a row in architecture §6 and DRR-04 residency classification before use.

Checks to repeat: none executable at phase 0; confirm the Growth handoff cites GM-1…GM-12 explicitly.

### 11.2 Project Lead (`project-lead-subagent`)

- Carry F-SEC-01, F-SEC-02, F-SEC-04 phase-1 gates into `docs/plans/phase_1_*.md` as acceptance items; the Security gate reverts to BLOCKED if the phase-1 plan omits any of them.
- Carry medium findings as phase-1 tasks (F-SEC-03, 05, 06, 07, 08, 09, 10, 13, 16) and phase-2 tasks (F-SEC-14, 18, 19).
- Schedule Security re-review at: phase-1 exit (all phase-1 gates), phase-2 spike completion (SP-1…SP-7) before any side-effecting toolset is enabled, phase-3 backup dry run and signing.
- Reconcile D-03 (authority model) with `docs/policies/authority-model.md`; adopt policies via decision records; update `docs/verification.md` Security row from "pending (T0-9)" to CONDITIONAL with this handoff path.
- Owner items in §12 must appear in the human-action queue (phase plan §17).

## 12. Human actions (owner only)

- H-1: Decide CI default branch (`main` vs `master`) so `agent-governance.yml` runs (manifest §13; T-46).
- H-2: Pin GitHub Actions to commit SHAs and enable Dependabot for actions and npm/pip/cargo (protected workflow file; T-44, F-SEC-10).
- H-3: Enable branch protection on the customer/product repositories used by the R1 development loop (T-34).
- H-4: Record model-provider terms (no-training, retention) as a decision before real customer content is sent (T-36, DRR-06).
- H-5: Verify Hermes licence permits commercial self-hosted redistribution and record it in the licence inventory (LIC-05).
- H-6: Adopt policies via decision records; approve D-03.
- H-7: Provision CI secrets `TAURI_SIGNING_PRIVATE_KEY`, `TAURI_SIGNING_PRIVATE_KEY_PASSWORD`, `APPLE_ID`, `APPLE_TEAM_ID`, `APPLE_APP_SPECIFIC_PASSWORD` in a protected environment when phase 3 starts (names only; values never in repository).

## 13. Proposed state and memory updates (for lead materialization)

- `.cursor/STATE.md`: T0-9 Security → complete, verdict CONDITIONAL; add active files `docs/policies/*.md`; blockers: none new (F-SEC-01 tracked as workstream finding, not a repository blocker); next action: Growth role T0-10 then PL reconciliation.
- `docs/workstreams/20260910-engine-labs-company-os/manifest.md` §5: Security row → `complete / CONDITIONAL`, handoff path; §12 gates: add phase-1 Security gates (F-SEC-01 fail-closed config, F-SEC-02 exposure test, F-SEC-04 approval grants) and phase-2 Security re-review (SP-1…SP-7); §13: add H-1…H-7.
- `docs/verification.md`: Security row → CONDITIONAL, evidence path.
- `.cursor/memory/memories/2026-09-10-continuation.md`: append T0-9 completion evidence (hygiene scan exit 1 at 17:26:24Z; 19 findings; 5 policies drafted; approval-path decision D-S1).
- `.cursor/memory/MEMORY.md`: durable directive candidate — "Hermes bearer key is transport only; Engine Labs API owns approvals; side-effecting Hermes toolsets are disabled until spike evidence exists."
- Decision record candidate: `docs/decisions/2026-09-10-authority-model.md` (D-03) referencing AUTH-01…AUTH-30.

## 14. Verdict

**CONDITIONAL.**

Justification against charter §9 and ROLES §7:
- Threat model covers every boundary with control, owner and phase (EV-SEC-03) — met.
- Authority-model gaps recorded as findings with remediation (EV-SEC-04) — met.
- Approval-path question answered: wrap, do not rely; spike requirement defined (EV-SEC-05) — met.
- Data lifecycle, secrets and supply chain reviewed; Growth constraints delivered (EV-SEC-06, EV-SEC-07) — met.
- Repository hygiene clean; `.gitignore` gaps low (EV-SEC-08, EV-SEC-09) — met.
- No critical finding; every high finding has a phase-1 gate (EV-SEC-14) — met.
- Not PASS: three high-impact controls are unverified by construction (no implementation exists).
- Not BLOCKED: no exploitable defect exists; fail-closed fallback for the highest-risk item is already decided (D-04 decision 9); Tier 3 gates are not waived — they are scheduled with named evidence. If the phase-1 plan omits any phase-1 gate in §9, this verdict reverts to BLOCKED without further review.

Conditions: (1) phase-1 plan includes the F-SEC-01, F-SEC-02, F-SEC-04 gates and the medium phase-1 tasks; (2) no side-effecting Hermes toolset is enabled in any environment before SP-1…SP-7 pass Security re-review; (3) policies are materialized as `proposed` and reconciled by PL before the phase-1 plan is written.
