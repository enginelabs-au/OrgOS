---
document: policy
title: Authority Model
status: proposed
revision: 1
created: 2026-09-10
updated: 2026-09-10
owner_role: security-engineer-subagent
task_id: 20260910-engine-labs-company-os
sources:
  - docs/product.md (PRD-D.1–D.13, PRD-E.2, PRD-E.10, §5.1, §9 R1-ACC-1..15)
  - docs/architecture.md (§5 TB-1, TB-2, TB-5, TB-10; §9; §14)
  - docs/capabilities.md (grant identifiers; required_grants; data_authority)
  - docs/ui-blueprint.md (§B, §B.7, §C, §D, §H D-8)
  - docs/decisions/2026-09-10-hermes-adapter-contract.md (D-04 decisions 3, 6, 7, 9, 11)
  - docs/Company_Agent_System_Blueprint.md Phase 03 (L114–155), Phase 04 (L156–214)
  - docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/handoff.md (F-SEC-01…06, F-SEC-08, F-SEC-15)
---

# Authority Model

Drafted read-only by `security-engineer-subagent` (T0-9); materialized by the orchestrating lead. Status `proposed` until the owner adopts it via decision record D-03.

## 1. Purpose

Define who and what may read, change, approve and execute within an Engine Labs Company OS deployment, and where those decisions are enforced. This policy is the normative basis for decision record D-03 and for acceptance criteria R1-ACC-1, R1-ACC-4, R1-ACC-6, R1-ACC-7.

## 2. Scope

Applies to every principal (member, agent, service identity), every surface (desktop, API, worker, generated views), every data-bearing operation (records, search, aggregates, attachments, notifications, memory, runs, actions) and every environment. Applies from release 1. Repository delivery roles (Cursor agents, CI) are out of scope: they hold no product authority (AGENTS.md security boundary).

## 3. Definitions

- Principal: an authenticated identity of type member, agent or service identity (PRD-D.4; TB-10).
- Seat: a human member's commercial entitlement (Founder, Project Lead, Operator — `docs/product.md` §5.1). Seats are not grants.
- Grant: an atomic permission identifier (e.g. `ledger.write`) attached to a principal for a scope (organisation, project, repository).
- Template: a named default set of grants applied at provisioning; editable afterwards without changing the template.
- Title: a display label with no authority.
- Sponsor: the human principal who started a run and whose grants bound the run (PRD-E.2).
- Acting identity: the agent principal executing a run.
- Designated authority: the set of human principals holding an `approval.<class>` grant for an action class (PRD-D.9).
- Action: a side-effecting operation moving through the eight-step lifecycle (PRD-E.4).
- Target version: the immutable identifier of the state an action applies to (record version, commit SHA, run revision).
- Grant version: a monotonically increasing per-principal counter incremented on any grant, seat or session change.

## 4. Normative requirements

### 4.1 Structure

- AUTH-01. Seats, titles, templates and grants MUST be four distinct entities; authority MUST derive from grants only (PRD-D.4). Seat templates in §5.1 of `docs/product.md` are defaults, not enforcement inputs.
- AUTH-02. The hierarchy owner → lead → member MUST be represented as scoped grants; a lead's authority over a project MUST be a subset of the owner's (PRD-D.2).
- AUTH-03. Delegation MUST only assign a subset of the delegator's current grants within the delegator's scope (PRD-D.3). Delegated grants MUST record the delegator and MUST be revoked when the delegator loses the grant.
- AUTH-04. Grant identifiers MUST come from a versioned registry (initially the 17 identifiers in `docs/capabilities.md` plus `approval.<class>` from AUTH-09). Unknown identifiers MUST be refused at assignment and evaluation.
- AUTH-05. Members, agents and service identities MUST be distinct principal types. Agents MUST NOT have interactive credentials. Service identities MUST be per-service with separate secrets (TB-10).

### 4.2 Agents

- AUTH-06. Every run MUST record the nine fields of PRD-E.2 (sponsor, acting identity, purpose, scope, policy version, model configuration, budget, deadline, owner) as NOT NULL.
- AUTH-07. An agent's effective grants for a run MUST equal the intersection of the sponsor's current grants, the agent's toolset ceiling and the grants permitted by the run mode. The intersection MUST be recomputed at every action step (PRD-D.12).
- AUTH-08. An agent principal MUST NOT assign, delegate or request grants for itself or any other principal (PRD-D.11). Attempts MUST be refused and audited.

### 4.3 Approvals

- AUTH-09. Approval authority MUST be a grant class `approval.<action-class>` (initial classes: `repo.change`, `repo.release`, `data.export`, `data.erase`, `org.admin`, `billing.admin`, `connector.admin`). Agent principals MUST NOT be assignable any `approval.*` grant, enforced by a database constraint and an API check.
- AUTH-10. An approval record MUST bind to a single action id and a hash of (action type, canonical parameters, target id, target version, policy version). The executor MUST recompute the hash immediately before execution and MUST refuse on mismatch (PRD-D.10; T-30).
- AUTH-11. For classes `repo.release`, `data.erase`, `billing.admin`, `org.admin` the approver MUST NOT be the sponsor of the action. Other classes MAY permit sponsor approval when the sponsor holds the grant; the choice MUST be recorded per class in the policy version.
- AUTH-11a. Hermes `/v1/runs/{id}/approval` MUST NOT be used as the approval authority. The Engine Labs API MUST record the approval first; the adapter MAY forward the decision to Hermes afterwards (D-04 decision 6; handoff F-SEC-01, D-S1).

### 4.4 Enforcement points

- AUTH-12. Every authorization decision MUST be made server-side in the Engine Labs API for records, search results, aggregates and counts, attachments, notifications and memory retrieval (PRD-D.5). The desktop MUST NOT be trusted for any decision; hidden UI is not authorization. For permissioned sources bound in release 1 (GitHub), the effective authority MUST be the intersection of the Engine Labs grant and the source permission, checked before any token is minted (PRD-D.6 brought forward for GitHub; F-SEC-05).
- AUTH-13. Access tokens MUST expire within 15 minutes; refresh tokens MUST rotate with reuse detection; every API request and every action step MUST verify the principal's grant version; revocation MUST take effect within 60 seconds (F-SEC-06).
- AUTH-14. On sign-out or grant-version change the desktop MUST purge cached data beyond preferences and layout state (T-08).
- AUTH-15. Every authorization decision that grants, refuses or approves MUST produce an audit event with actor, approver (if any), target id and version, grant version, policy version, outcome and timestamp. Audit tables MUST be INSERT-only for the application role (F-SEC-15).
- AUTH-16. Strong authentication (second factor) MUST be required for Founder and Project Lead seats and for any principal holding `org.admin`, `approval.*`, `data.erase`, `billing.admin` or `connector.admin`. Reauthentication no older than 5 minutes MUST be required for `data.erase`, `billing.admin`, `org.admin` grant changes and `repo.release` approvals (PRD-D.7).
- AUTH-17. Search, aggregate and notification results MUST be computed over the authorized subset only; counts MUST NOT reveal the existence of unauthorized records (R1-ACC-4).
- AUTH-18. Attachments MUST be served by the API or by API-minted signed URLs with TTL ≤ 5 minutes issued only after an authorization check; storage services MUST NOT be reachable from the public edge (F-SEC-02, F-SEC-08).

### 4.5 Data layer

- AUTH-19. The API MUST connect to Postgres with a role that is neither superuser nor `BYPASSRLS`; each request MUST set tenant and principal context with `SET LOCAL`; row-level security policies MUST exist on every tenant-scoped table. `SUPABASE_SERVICE_ROLE_KEY` MUST be used only by administrative jobs (migrations, retention, backup) (F-SEC-03).
- AUTH-20. Only the Engine Labs API and Supabase Auth endpoints MAY be published on the `edge` network. PostgREST, Realtime, Storage API, Studio and the pooler MUST be internal only (F-SEC-02).

### 4.6 Provisioning, handover, revocation

- AUTH-21. Provisioning MUST apply a template then record resulting grants individually. Handover of an owner seat MUST require the outgoing owner's reauthenticated approval or a documented recovery procedure executed by Engine Labs with the customer's written instruction; support access MUST be time-boxed, logged and visible to the customer (PRD-D.8).
- AUTH-22. Bearer credentials to infrastructure (`HERMES_API_SERVER_KEY`, `SUPABASE_SERVICE_ROLE_KEY`, `DATABASE_URL`, `GITHUB_APP_PRIVATE_KEY_PATH`) are transport credentials and MUST NOT be treated as authorization for any principal. Possession of `HERMES_API_SERVER_KEY` grants the full Hermes toolset including terminal execution; it MUST exist only in the worker service and MUST NOT be exposed to the desktop, the API process, logs or prompts (TB-3, T-18).
- AUTH-23. Offboarding a member MUST revoke all grants, sessions and delegated grants within 60 seconds and MUST follow `docs/policies/erasure-and-offboarding.md`.

### 4.7 Runtime boundaries

- AUTH-24. The worker and Hermes containers MUST have no database credentials and no membership of the `data` network (architecture §14 resolved).
- AUTH-25. Side-effecting Hermes toolsets MUST remain disabled and their registry rows `unavailable` until the interception spike (handoff §9 SP-1…SP-7) passes Security re-review; the worker MUST refuse to start otherwise (F-SEC-01).

### 4.8 Desktop posture

- AUTH-26. Authentication tokens MUST be stored only in the operating system keychain via the Tauri secure-storage plugin; never in `localStorage`, `sessionStorage`, IndexedDB or files (PRD-D.13).
- AUTH-27. The reference patterns `cc-org-dash-auth` (localStorage session), Settings "AI & Agents" provider key in `localStorage`, Security tab API keys, demo credentials and Google sign-in MUST NOT exist in the product (`docs/ui-blueprint.md` §C, §H D-8; SE handoff §11).
- AUTH-28. No simulated authorization, approval or permission control MAY ship; every control either performs the server-side operation or is absent (UI/UX F-U3).
- AUTH-29. Generated or adaptive views MUST be schema-validated view definitions composed from trusted components; they MUST NOT access filesystem, shell, database or credentials and MUST use the same API read contracts as static views (`docs/ui-blueprint.md` §D).
- AUTH-30. Tauri capability files MUST grant the minimum: no `fs`, `shell:allow-open` limited to `https?` URLs with confirmation, updater and secure-storage only; Security reviews capability files in phase 1 (F-SEC-17).

## 5. Verification

- Phase 1: schema constraints (AUTH-01, 04, 05, 06, 09); tests for AUTH-07/08/10/11/12/13/14/17/18/19/20; migration test for AUTH-15; env-exclusion test for AUTH-22/24; startup refusal test for AUTH-25; static scan for AUTH-26/27; capability review AUTH-30.
- Phase 2: intersection test with GitHub (AUTH-12); spike SP-1…SP-7 (AUTH-25).
- Every release: re-run tests; Security re-review of any grant registry change.

## 6. Exceptions

Exceptions require an owner-approved decision record naming the requirement, scope, compensating control and expiry ≤ 90 days. Tier 3 gates cannot be waived by any role (ROLES §7). No exception may permit agent approval grants (AUTH-09) or desktop-side authorization (AUTH-12).

## 7. Related decisions and requirements

D-01, D-03 (candidate), D-04 decisions 3, 6, 7, 9, 11; PRD-D.1–D.13, PRD-E.2, PRD-E.10; NFR security items; R1-ACC-1, 4, 6, 7; findings F-SEC-01…F-SEC-06, F-SEC-08, F-SEC-15, F-SEC-17.
