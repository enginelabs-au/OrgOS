---
document: evidence
task_id: 20260910-engine-labs-company-os
role_id: security-engineer-subagent
schema_version: 1
revision: 1
created_at: 2026-09-10T17:25:00Z
updated_at: 2026-09-10T17:58:00Z
environment: macOS darwin 25.6.0, zsh, Cursor sandbox (read-only filesystem for this role, network allowlist), repository `/Users/camdouglas/OrgOS`, branch `master`, zero commits, control plane and `docs/` untracked
---

# Security evidence — T0-9 Security gate (Tier 3)

Produced read-only by the role on 2026-09-10 (UTC); materialized verbatim by the orchestrating lead. Evidence states follow `.cursor/instructions/ROLES.md` §3.11: `VERIFIED` (direct observation or executed command), `PARTIAL` (observed in part, remainder inferred or design-stage), `UNVERIFIED` (claimed, not observed). Every record cites the file and section that supports the claim. No secret values appear in this file; environment variables are named only.

Timestamp anchor: `date -u` executed in the same shell as the hygiene scan returned `Thu Sep 10 17:26:24 UTC 2026` (EV-SEC-08). Other timestamps in this file are relative to that anchor and are estimates within ±35 minutes.

## EV-SEC-01 — Context and predecessor inputs loaded

- Requirement: charter §3 read list; plan §6 task 0 (context).
- Claim: All inputs required by the charter were read in full before analysis.
- State: VERIFIED.
- Method: `Read` tool on each file; `Glob` to resolve template names.
- Artefacts read: `.cursor/AGENTS.md`; `.cursor/USER.md`; `.cursor/STATE.md`; `.cursor/INSTRUCTIONS.md`; `.cursor/SKILLS.md`; `.cursor/TOOLS.md`; `.cursor/memory/MEMORY.md`; `.cursor/instructions/ROLES.md` (§3.11–§3.14, §7); `.cursor/instructions/SUBAGENTS.md`; `.cursor/templates/role-evidence-template.md`; `.cursor/templates/role-handoff-template.md`; `docs/workstreams/20260910-engine-labs-company-os/manifest.md`; `.../security-engineer-subagent/charter.md` (r1); `.../security-engineer-subagent/plan.md` (r1); `.../software-engineer-subagent/handoff.md` and `evidence.md` (EV-S01–EV-S16); `.../product-manager-subagent/handoff.md`; `.../ui-ux-developer-subagent/handoff.md`; `docs/plans/phase_0_foundations_plan.md` (§15, §16, §17, §22); `docs/architecture.md` (§1–§14); `docs/capabilities.md`; `docs/product.md` (PRD-A…G, NFR-1…10, §9, §10, §12); `docs/ui-blueprint.md` (§0.4, §0.5, §B, §C, §D, §H); `docs/decisions/2026-09-10-hermes-adapter-contract.md` (D-04); `docs/decisions/2026-09-10-monorepo-layout.md` (D-01); `docs/decisions/2026-08-18-agent-role-pipeline.md`; `docs/Company_Agent_System_Blueprint.md` (Phase 03 L114–155, Phase 04 L156–214, Phase 05 L215–265, Phase 06 L266–301, Phase 07/08 L304–323, Phases 13–18 L358–412); `.cursor/hooks/policy.mjs`; `.cursor/hooks.json`; `.cursor/cli.json`; `.cursor/sandbox.json`; `.cursor/permissions.json`; `.cursorignore`; `.gitignore`; `.github/workflows/agent-governance.yml`; Hermes API server documentation capture at `/Users/camdouglas/.cursor/projects/Users-camdouglas-Papership/agent-tools/0b49ebff-27af-4c6e-912e-4830b104b523.txt`.
- Result: All files present and read. One error: `Read` of `.cursor/templates/role-evidence.md` and `.cursor/templates/role-handoff.md` returned "File not found"; `Glob .cursor/templates/*` showed the real names `role-evidence-template.md` and `role-handoff-template.md`, which were then read. Exit: n/a (tool reads).
- Timestamp: 2026-09-10T17:25:00Z (approx., before anchor).
- Limitations: `docs/verification.md` was read by `rg` for security-relevant rows only (V13-7, V14-3, V14-5, V15-4, V15-5, V16-1, V17-6, V18-2, Security row "pending (T0-9)"), not in full.
- Follow-up: none.

## EV-SEC-02 — Component, data-store, trust-boundary and destination enumeration

- Requirement: plan §6 task 1; charter §4.1.
- Claim: `docs/architecture.md` defines seven components (§2), an entity retention table (§4), trust boundaries TB-1…TB-10 (§5), a data-destination map (§6), the adapter contract (§7), DBOS usage (§8), the Supabase boundary (§9), Compose topology with networks `edge`/`app`/`data`/`worker` (§10), backup/restore (§11) and open items (§14). Enumeration is complete for the release-1 system as designed, with the gaps listed below.
- State: VERIFIED (enumeration by direct inspection); gaps are findings, not evidence failures.
- Method: `Read docs/architecture.md` (263 lines) and cross-reference to `docs/capabilities.md` §5 and `docs/plans/phase_0_foundations_plan.md` §16.
- Result — gaps found (mapped to F-SEC-07 and F-SEC-08 unless noted):
  - G-1: Desktop update distribution channel (artefact host, updater endpoint) is referenced in TB-1 ("signed updates") but is not a component, destination or boundary. No location for update artefacts is defined.
  - G-2: GitHub Actions is a data destination and trust boundary for CI secrets (`TAURI_SIGNING_PRIVATE_KEY`, `TAURI_SIGNING_PRIVATE_KEY_PASSWORD`, `APPLE_ID`, `APPLE_TEAM_ID`, `APPLE_APP_SPECIFIC_PASSWORD`, `DIGITALOCEAN_API_TOKEN` per phase plan §16) but is absent from §6.
  - G-3: Supabase Auth (GoTrue) requires an outbound email provider for password reset and factor enrolment; the SMTP/email provider receives member identities and is not in §6.
  - G-4: `docs/capabilities.md` §5 references a "Honcho-class" memory provider for Hermes. If enabled, it is an external destination for conversation-derived content; §6 lists only local gateway state (SQLite transcripts, stored responses LRU 100).
  - G-5: The desktop→Supabase Storage download path is undefined. Architecture §2/§9 state the desktop talks only to the API; if Storage signed URLs are used the authorization point must be the API.
  - G-6: The "secret store" referenced in the §4 entity table ("credentials as references to the secret store") is not a component. Release 1 uses environment variables and file mounts (phase plan §16); release 2 connectors need a decision.
  - G-7: ACME/TLS certificate issuance is an external egress from the reverse proxy; minor, not mapped.
  - G-8: Worker database access is an open item (§14, proposal "none"); this review adopts "none" as a requirement (F-SEC-09, AUTH-24).
- Timestamp: 2026-09-10T17:26:00Z (approx.).
- Limitations: Enumeration is documentation-based; no running system exists (`.cursor/STATE.md`: no dev server; repository zero commits).
- Follow-up: SE to revise `docs/architecture.md` §5/§6 in phase 1 (F-SEC-07).

## EV-SEC-03 — STRIDE threat model per boundary

- Requirement: plan §6 task 2; charter §4.2.
- Claim: A STRIDE model exists for every listed boundary — TB-1…TB-10 plus three boundaries added by this review (TB-11 desktop update/signing, TB-12 repository automation hooks/CI, TB-13 memory/retrieval store) — with a named control, owner and verification phase for each threat.
- State: VERIFIED for existence and coverage of the model (handoff §5 and §9, table T-01…T-58); UNVERIFIED for effectiveness of every control except TB-12 (repository hooks), which is VERIFIED by EV-SEC-10.
- Method: Analysis against `docs/architecture.md` §5 controls and threats, `docs/product.md` PRD-B/D/E/F, intake Phase 04–06, Hermes API documentation capture.
- Result: 58 threats recorded; 0 without a control; 0 without a phase; controls verified now: hooks (TB-12) only.
- Timestamp: 2026-09-10T17:35:00Z (approx.).
- Limitations: Controls on TB-3…TB-7 depend on the unresolved tool-interception mechanism (D-04 decision 9; F-S5; F-SEC-01).
- Follow-up: SE phase-1 contract tests; Security re-review at phase-1 and phase-2 gates.

## EV-SEC-04 — Authority-model review (D-03 candidate)

- Requirement: plan §6 task 3; charter §4.3; PRD-D.1–D.13; intake Phase 03 (L114–155).
- Claim: The product and architecture documents define seats (Founder, Project Lead, Operator — `docs/product.md` §5.1), hierarchy owner→lead→member (PRD-D.2), delegation subset (D.3), eight distinct entities (D.4), server-side checks on five surfaces (D.5), source-permission intersection (D.6, marked R2), reauthentication (D.7), provisioning/handover (D.8, R2), designated authority (D.9), approval binding to action+target version (D.10), no agent self-grant (D.11), mid-run recheck (D.12) and desktop posture (D.13). Grant identifiers are listed in `docs/capabilities.md` (17 identifiers).
- State: VERIFIED for review completion; gaps recorded as F-SEC-03, F-SEC-04, F-SEC-05, F-SEC-06, F-SEC-08.
- Method: Document inspection; cross-check of `docs/capabilities.md` `required_grants` column against PRD-D and against `docs/ui-blueprint.md` §B seat visibility rows.
- Result — gaps:
  - No grant class exists for approving actions; approvals are described by seat ("designated authority", PRD-D.9) rather than by grant. Agents are not stated to be excluded from approver principals by data model (only by D.11 prose).
  - Agent effective authority is not defined as an intersection of sponsor grants, toolset ceiling and mode set.
  - Source-permission intersection is deferred to R2 while GitHub (a permissioned source) is an R1 binding (`docs/capabilities.md` B08.01 "∥ GitHub App installation scopes").
  - Revocation propagation latency, access-token lifetime and desktop cache purge on revocation are not specified.
  - `docs/architecture.md` §9 describes RLS as defence in depth, but the API uses `SUPABASE_SERVICE_ROLE_KEY` and a `DATABASE_URL` role that bypasses RLS; the stated control does not hold as written.
- Timestamp: 2026-09-10T17:38:00Z (approx.).
- Limitations: No schema exists yet; review is of intent.
- Follow-up: D-03 decision record to adopt `policies/authority-model.md` requirements.

## EV-SEC-05 — Agent execution controls and Hermes approval semantics

- Requirement: plan §6 task 4; charter §5 open question ("`/v1/runs/{id}/approval` sole path vs wrap"); PRD-E.1–E.12; D-04 decisions 1–12; F-S5.
- Claim: The Hermes API documentation capture confirms: bearer `API_SERVER_KEY` mandatory and grants "full access to hermes-agent's toolset, including terminal commands"; `POST /v1/runs` with `Idempotency-Key` (replay → 202 `Idempotency-Replayed: true`; conflict → 409 `idempotency_key_conflict`; keys retained 24 h, isolated per credential); `GET /v1/runs/{id}`; SSE `/events` (free text passes forced secret redaction; buffers expire after 5 min; transport only); `/stop`; `/approval` described as "Resolve a pending approval for a run that is waiting on a human decision (for example, a tool call gated behind an approval policy)" and advertised as capability `run_approval`; `GET /v1/capabilities`; `X-Hermes-Session-Key` (≤256 chars) for memory scoping; multi-profile `/p/<profile>/` with per-profile keys; `max_concurrent_runs` default 10 → 429; browser-extension control disabled by default; no file upload; stored responses max 100 LRU; per-request `model`/`provider`/`model_options`; a `steer` route is mentioned alongside `stop` and `approval` without its own specification.
- Claim (analysis): The documentation does not specify which tools are gated, how the gating policy is configured, the approval-request payload, whether unapproved tool calls are hard-blocked server-side or model-mediated, or whether the pause is enforced before execution. Therefore `/v1/runs/{id}/approval` cannot be the sole approval path; Engine Labs must own the approval record (PRD-D.10 binding to action + target version, seat authority, audit) and the adapter may only forward a decision already recorded by the Engine Labs API (D-04 decision 6). See handoff §9 F-SEC-01 for the spike requirement.
- State: PARTIAL — endpoint existence and semantics as documented are VERIFIED from the capture; gating semantics and enforceability are UNVERIFIED and can only be established by the phase-2 spike against the pinned version (`HERMES_VERSION_PIN`).
- Method: `Read` of the documentation capture file; comparison with D-04 decisions 3, 6, 7, 9, 11.
- Result: Decision recorded: **wrap, do not rely**. Spike requirement SP-1…SP-7 defined in handoff §9 (F-SEC-01).
- Timestamp: 2026-09-10T17:42:00Z (approx.).
- Limitations: Documentation is a point-in-time capture (fetched 2026-09-10); behaviour of the pinned version may differ. Hermes was not executed (charter: read-only, no reference execution).
- Follow-up: SE phase-2 spike with Security re-review before any run with a side-effecting toolset enabled.

## EV-SEC-06 — Data lifecycle review

- Requirement: plan §6 task 5; charter §4.5; PRD-F.1–F.9; intake Phases 13–18 (L358–412); architecture §4, §6, §11.
- Claim: Retention defaults (conversations 365 d; logs 30 d; backups 30 d; approved knowledge until superseded; Notification 90 d `proposal`), erasure semantics (AuditEvent anonymised; UsageEvent aggregated; MemoryItem never holds credentials), residency map (tenant PG, Storage, Auth, Hermes gateway state, model providers, GitHub, off-VPS backup, shared licensing R4, optional scrubbed telemetry, desktop cache) and backup design (nightly `pg_dump`, client-key encryption, separate provider/region, 30 d, restore drill R4, dry run phase 3) are documented.
- State: VERIFIED for documentation; UNVERIFIED for implementation (none exists).
- Method: Document inspection.
- Result — gaps and constraints: destinations missing (EV-SEC-02 G-1…G-7); Hermes gateway state (SQLite sessions, stored responses, memory files) holds conversation content and is not in the erasure inventory as an explicit step (F-SEC-14); DBOS system database stores workflow inputs/outputs which may contain content and must be classified C2 and pruned (DRR-09); telemetry (`SENTRY_DSN`) scrubbing needs payload-inspection evidence (R1-ACC-14); usage measurement constraints for Growth defined in handoff §11 (GM-1…GM-12) and `policies/data-residency-and-retention.md` DRR-20…DRR-27.
- Timestamp: 2026-09-10T17:45:00Z (approx.).
- Limitations: Whether DigitalOcean block storage encrypts volumes at rest was not verified; recorded as a phase-2 verification item (DRR-15).
- Follow-up: SE phase 1 architecture revision; retention job design phase 1–2 (architecture §14).

## EV-SEC-07 — Secrets and supply-chain posture

- Requirement: plan §6 task 6; charter §4.6; phase plan §15/§16; SE F-S3; EV-S04.
- Claim: The environment-variable registry (phase plan §16) names all release-1 secrets; `DBOS_CONDUCTOR_KEY` is explicitly not used; `SUPABASE_ANON_KEY` is public by design on the desktop; `SUPABASE_SERVICE_ROLE_KEY` is API-only. No product lockfiles exist yet (repository has no `package.json`, `uv.lock` or `Cargo.lock` outside `.reference/`). `.reference/orgos/` dependency install ran lifecycle scripts (EV-S04, exit 0) and `npm audit` reported 24 advisories (F-S3: 2 low, 10 moderate, 11 high, 1 critical). `.reference/` is git-ignored and D-01 forbids importing reference code as a package.
- State: PARTIAL — registry and reference facts VERIFIED; no scanner output exists for product code (nothing to scan); Hermes licence and image digest not verified.
- Method: `Read` of phase plan §16; SE evidence EV-S04; `.gitignore`; D-01.
- Result: Requirements recorded in `policies/licensing.md` and handoff §9 (F-SEC-10, F-SEC-12): `npm ci --ignore-scripts` default with an allowlist for packages that require scripts; `npm audit`, `pip-audit`, `cargo audit` in CI; `HERMES_VERSION_PIN` resolved to an image digest recorded in `infra/digests.lock`; licence inventory via `license-checker`, `pip-licenses`, `cargo-license` (verification row V17-6); GitHub Actions pinned by commit SHA (currently `actions/checkout@v4` tag in the protected workflow — owner action).
- Timestamp: 2026-09-10T17:48:00Z (approx.).
- Limitations: F-S3 advisory identifiers were not itemised by SE and were not re-run by this role (read-only; reference not shipped).
- Follow-up: Phase-1 CI gate.

## EV-SEC-08 — Repository hygiene scan for secret-shaped strings

- Requirement: plan §6 task 7; phase plan §15 ("no secrets in any file").
- Claim: No private-key blocks, AWS access key IDs, `sk-` style provider keys or Slack tokens exist in tracked-eligible files outside `node_modules` and `.reference`.
- State: VERIFIED.
- Method: Shell (read-only).
- Command: `cd /Users/camdouglas/OrgOS && date -u && rg -n "(BEGIN (RSA|OPENSSH|EC) PRIVATE KEY|AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9]{20,}|xox[baprs]-)" --glob '!**/node_modules/**' --glob '!.reference/**' . ; echo "rg-exit=$?"`
- Result: `Thu Sep 10 17:26:24 UTC 2026` then `rg-exit=1` (ripgrep exit 1 = no matches). No hook denial occurred (command contains no secret-file tokens).
- Timestamp: 2026-09-10T17:26:24Z (exact).
- Limitations: Pattern set is a baseline, not a full secret scanner; `.reference/` excluded deliberately (untrusted third-party code, not shipped). Recommend `gitleaks` or `trufflehog` in CI (phase 1, LIC-14).
- Follow-up: Repeat on every PR in CI.
- `[lead]` Independently re-run by the orchestrating lead on 2026-09-10 after materialization (same command, `docs/ui-blueprint/*.png` binaries present) — see the continuation log entry for the recorded exit status.

## EV-SEC-09 — `.gitignore` coverage review

- Requirement: plan §6 task 7; phase plan §15 ("`.gitignore` covers `.env*`"); SE §11 pointer to EV-S02.
- Claim: `.gitignore` (52 lines) ignores `.reference/`, `node_modules/`, `.venv/`, `__pycache__/`, `dist/`, `build/`, `target/`, `.vite/`, `.env`, `.env.*` with `!.env.example` and `!.env.*.example`, coverage directories, `.DS_Store`, `*.log`, `src-tauri/target/`, `src-tauri/gen/schemas/`, `*.pem`, `*.key`, `*.p12`.
- State: VERIFIED (direct read).
- Method: `Read .gitignore`; comparison with `.cursorignore`.
- Result: Gaps relative to `.cursorignore`: `*.pfx`, `credentials.json`, `secrets.json`, `.netrc`, `.npmrc`, `.pypirc`, `.aws/credentials`, gcloud ADC path, `.docker/config.json` are not git-ignored. `.cursorignore` and the hook's `isSecretPath` cover agent reads but not `git add`. Recorded as F-SEC-11 (low).
- Timestamp: 2026-09-10T17:27:00Z (approx.).
- Limitations: none.
- Follow-up: SE phase 1 adds patterns; verify with `git check-ignore`.

## EV-SEC-10 — Repository control-plane enforcement inspection

- Requirement: charter §5 assumption "hooks live" (marked `verified` in charter); manifest §9.
- Claim: `.cursor/hooks.json` routes all five events to `node .cursor/hooks/policy.mjs` with `failClosed: true`; `policy.mjs` implements `isSecretPath`, `isProtectedPath`, `shellReferencesSecret`, `isDestructiveGit`, `isProductionMutation`, `shellMutatesProtectedPath`, `stateChangingMcp` and `evaluate`, and denies on malformed input; `.cursor/sandbox.json` sets `workspace_readwrite` with network default deny and an allowlist (GitHub, npm, Vercel, Supabase); `.cursor/permissions.json` defines allow/deny lists; `.cursorignore` covers secret file names; `.github/workflows/agent-governance.yml` runs policy tests, validators and bootstrap idempotence with `permissions: contents: read` on Node 22, triggered on `pull_request` and `push` to `main` only.
- State: VERIFIED (file contents read; enforcement behaviour corroborated by SE EV-S02 and EV-S14 denials in the predecessor run, and by lead-observed denials recorded in the continuation log).
- Method: `Read` of each file.
- Result: Controls present. Observations: workflow triggers `main` while the branch is `master` (manifest §10, owner decision §13); Actions referenced by tag not SHA. Both recorded as owner items (handoff §12).
- Timestamp: 2026-09-10T17:30:00Z (approx.).
- Limitations: This role did not trigger a hook denial; enforcement is corroborated by predecessor evidence, not reproduced.
- Follow-up: none for phase 0.

## EV-SEC-11 — Disposition of SE finding F-S3 (reference `npm audit` advisories)

- Requirement: charter §4.6; SE handoff §9 F-S3 (owner Security).
- Claim: The 24 advisories belong to `.reference/orgos/` dependencies, which are git-ignored, never imported as a package (D-01 decision; rejected alternative 2), and executed only locally for screenshot capture (ui-blueprint §0.4). They do not affect shipped code.
- State: VERIFIED for non-shipment (`.gitignore`, D-01); advisory content UNVERIFIED (not itemised).
- Method: Document inspection.
- Result: Severity for product: low (F-SEC-12). Condition: product lockfiles must be created fresh from the keep list (ui-blueprint §F) and pass `npm audit` with no open high/critical at the phase-1 gate; the reference dev server must not be run again by agents (local compromise risk of executing unaudited third-party code).
- Timestamp: 2026-09-10T17:49:00Z (approx.).
- Limitations: none.
- Follow-up: Phase-1 CI gate.

## EV-SEC-12 — Policy drafts produced

- Requirement: plan §6 task 9; charter §6 outputs.
- Claim: Five policies drafted with front matter, purpose, scope, definitions, numbered MUST/SHOULD requirements, verification, exceptions and related IDs: `authority-model.md` (AUTH-01…AUTH-30), `data-residency-and-retention.md` (DRR-01…DRR-27), `memory-governance.md` (MEM-01…MEM-22), `erasure-and-offboarding.md` (ERA-01…ERA-24), `licensing.md` (LIC-01…LIC-20).
- State: VERIFIED for content; materialization at `docs/policies/` performed by the lead (see handoff §4 and the continuation log).
- Method: Authoring; `Glob`; shell `ls` (`docs/policies` absent at 2026-09-10T17:52:00Z approx.).
- Result: Content delivered verbatim.
- Timestamp: 2026-09-10T17:55:00Z (approx.).
- Limitations: Policies are `proposed`; the owner adopts via D-03 and follow-on decision records.
- Follow-up: Lead materializes; PL reconciles; owner adopts.

## EV-SEC-13 — Constraint compliance (read-only role)

- Requirement: charter §7 constraints; SUBAGENTS.md read-only role rules; ROLES §3.13.
- Claim: This role created, edited or deleted no file, called no MCP write tool and executed no code from `.reference/orgos/`.
- State: VERIFIED.
- Method: `git status --porcelain | head -20` (only the pre-existing untracked roots `.cursor/`, `.cursorignore`, `.github/`, `.gitignore`, `AGENTS.md`, `docs/` listed; no new paths); tool log contains only `Read`, `Glob`, `Grep`, read-only `Shell` (`date`, `rg`, `git status`, `ls`).
- Result: Compliant. Sandbox filesystem was read-only for this role.
- Timestamp: 2026-09-10T17:52:00Z (approx.).
- Limitations: none.
- Follow-up: none.

## EV-SEC-14 — Findings register completeness check

- Requirement: plan §6 task 8 ("no critical/high finding may lack a phase-1 gate").
- Claim: 19 findings F-SEC-01…F-SEC-19; 0 critical; 3 high (F-SEC-01, F-SEC-02, F-SEC-04), each with a phase-1 gate; 11 medium; 5 low. No finding is exploitable at phase 0 because no implementation exists; severities denote impact if the control is absent at the named gate.
- State: VERIFIED (register in handoff §9).
- Method: Self-check against charter §9 criteria.
- Result: Criterion satisfied.
- Timestamp: 2026-09-10T17:56:00Z (approx.).
- Limitations: none.
- Follow-up: PL to carry the gates into `docs/plans/phase_1_*.md`.
