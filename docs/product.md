---
document: product
title: Engine Labs — Product Contract (PRD)
status: accepted_conditional
revision: 1
created: 2026-09-10
updated: 2026-09-10
owner_role: product-manager-subagent (read-only; materialized by orchestrating lead)
task_id: 20260910-engine-labs-company-os
intake: docs/Company_Agent_System_Blueprint.md
blueprint: docs/blueprints/2026-09-10_engine_labs.md
phase_plan: docs/plans/phase_0_foundations_plan.md
manifest: docs/workstreams/20260910-engine-labs-company-os/manifest.md
role_handoff: docs/workstreams/20260910-engine-labs-company-os/product-manager-subagent/handoff.md
role_evidence: docs/workstreams/20260910-engine-labs-company-os/product-manager-subagent/evidence.md
release_1_scope: intake implementation phases 07 (Foundation) + 08 (Development loop)
---

# Engine Labs — Product Contract

This document is the single traceable product contract for Engine Labs. It converts the canonical intake, [`docs/Company_Agent_System_Blueprint.md`](Company_Agent_System_Blueprint.md), into uniquely identified, testable requirements. It does not restate the intake; every requirement cites the intake heading it comes from. Anything not present in the intake is marked `proposal` and may be overturned by the owner without invalidating the rest of the contract.

Downstream roles (`ui-ux-developer-subagent`, `software-engineer-subagent`, `security-engineer-subagent`, `growth-marketing-subagent`, `project-lead-subagent`) may refine *how* a requirement is met; they may not reinterpret *what* a requirement says, change a release bucket, alter a status transition rule, or add prices.

## 0. How to read this document

### 0.1 Citation keys

Every requirement carries one or more citation keys. Each key quotes the exact intake heading it refers to.

| Key | Intake heading (quoted) |
|---|---|
| I-01 | `### Phase 01 — Launch from the supplied blueprint` |
| I-02 | `### Phase 02 — Plan the product and its complete capability registry` |
| I-02B | `#### Business domains` (under Phase 02) |
| I-02P | `#### Agent and platform domains` (under Phase 02) |
| I-03 | `### Phase 03 — Plan the member experience and authority model` |
| I-04 | `### Phase 04 — Plan cloud architecture and connections` |
| I-05 | `### Phase 05 — Plan agents, memory, lifecycle and commercial controls` |
| I-06 | `### Phase 06 — Plan release scope, dependencies and acceptance gates` |
| I-07 | `### Phase 07 — Build the foundation` |
| I-08 | `### Phase 08 — Build the development loop` |
| I-09 | `### Phase 09 — Build collaboration and connections` |
| I-10 | `### Phase 10 — Expand company operations` |
| I-11 | `### Phase 11 — Build commercial delivery` |
| I-12 | `### Phase 12 — Expand the ecosystem and mobile clients` |
| I-13 | `### Phase 13 — Verify functional and domain coverage` |
| I-14 | `### Phase 14 — Verify authority, memory and data lifecycle` |
| I-15 | `### Phase 15 — Verify integrations, recovery and backups` |
| I-16 | `### Phase 16 — Verify the desktop and adaptive experience` |
| I-17 | `### Phase 17 — Verify usage, deployment and commercial operations` |
| I-18 | `### Phase 18 — Verify release readiness and complete the owner handoff` |

### 0.2 Requirement record format

Each requirement row has: **ID** · **Requirement** · **Acceptance criterion** (observable; states the evidence that proves it) · **Release** (R1–R4; see §4) · **Cite**. `R1` means required for the release-1 acceptance definition in §9. Rows marked `proposal` are not in the intake.

### 0.3 Labels

- `verified` — supported by the intake text or repository evidence.
- `proposal` — added by this role to make the contract executable; not in the intake; owner may overturn.
- `provisional` — an assumption with a recorded validation point.

### 0.4 Primary user and outcome (release 1)

- Primary user: the founder of Engine Labs, holding the Founder / organisation owner seat, building Engine Labs itself (I-01: "whose first user is its founder and whose first project is the creation and management of Engine Labs itself").
- Job to be done: turn a product request into a reviewed, evidenced change to Engine Labs' own software through agents under bounded authority, from a desktop that can be closed without losing the job (I-02, I-04, I-07, I-08).
- Later users: Project Lead and Operator seats (R2), then customer organisations (R3–R4) (I-03, I-09, I-11).

## 1. PRD-A — Framework and member experience

| ID | Requirement | Acceptance criterion | Release | Cite |
|---|---|---|---|---|
| PRD-A.1 | Engine Labs is one modular product giving every member a shared operating framework with a workspace tailored to their responsibilities. | Signing in with each enabled seat template yields a workspace whose visible capabilities and default views differ according to that seat's responsibility scope. R1 evidence: Founder seat only. R2 evidence: all three seats compared side by side. | R1 (Founder), R2 (all seats) | I-02 |
| PRD-A.2 | Native capabilities are: identity, responsibility scopes, work coordination, conversations, agent supervision, memory governance, approvals, audit, connector administration, adaptive views, product entitlements. | Each of the eleven capabilities appears in the capability registry with `native` owner and at least one row. R1 target status: identity, responsibility scopes, work coordination, conversations, agent supervision, approvals, audit = `working`; memory governance = `working` (minimal, see PRD-F.3); connector administration, adaptive views, entitlements = `planned`/`configured`. | R1 partial | I-02 |
| PRD-A.3 | Specialist business records and calculations remain in connected systems; Engine Labs keeps a minimal native work ledger for plans, assignments, dependencies, decisions and execution evidence. | The data model contains ledger record types for exactly these five concepts plus source references; no native specialist record table (e.g., invoices, payroll) exists in release 1. A ledger record can link to a source-system record by stable source ID. | R1 | I-02 |
| PRD-A.4 | The disconnected framework (zero connectors) is usable for organisation setup, work planning, configuration and document intake, and it explains which outcomes need a connection. | With no connector configured, the founder completes: create organisation record, create a plan with assignments, change a configuration setting, upload a document. Any action that requires a connection shows the required connection by name and does not fail silently. | R1 | I-02 |
| PRD-A.5 | Customers connect their own tools and accounts; contextual handoffs are used whenever a source application is required. | An authorised owner can start connection setup from the product; an unsupported action offers a source-app handoff (link or instruction) instead of a dead end. | R2 | I-02, I-04, I-09 |
| PRD-A.6 | Connected accounts are registered independently of member identities; connecting an administrator's account must not expose its data to every seat. | `ProviderAccount` is a distinct entity from `Member`; data reached through a connected account is visible only to seats holding an explicit grant for that account scope (test: second seat without grant cannot read it). | R2 | I-04 |
| PRD-A.7 | Priority connections and their required treatment: development repository and CI (bind supplied repository; scope branches, changes, checks and release operations separately); Gmail (supported OAuth; separate read/draft/send; validate production scope requirements); Telegram (authorised bot with verified member/conversation mappings); Slack (workspace installation, channel membership, message scope, delegated actions); WhatsApp (official business integration path via the Hermes Cloud API adapter); web research and browsing (configured Hermes tools within source/network/credential/action limits); additional capabilities through the same contract. | Each priority connection is a registry row set with truthful status. R1: repository/CI = `working` (see PRD-B.2), web research = `working` within limits or `configured`; Gmail, Telegram, Slack, WhatsApp = `planned`. | R1 (repo, research), R2 (messaging) | I-04 |
| PRD-A.8 | A channel used to talk to an agent is distinct from permission to read all of a user's conversations; each provider's actual coverage is preserved. | Connecting a messaging channel creates grants only for the mapped conversation scope; the registry row states actual read/write coverage per provider. | R2 | I-04 |
| PRD-A.9 | Connector behaviours visible to members: revocation/refresh handling, freshness, outcome verification and ordinary-language operator recovery. | Revoking a connector credential moves its rows to `unavailable` and the affected view shows a plain-language recovery instruction; stale data is labelled with its last-sync time. | R2 | I-04, I-09 |
| PRD-A.10 | Members customise personal views, filters and notifications; leads configure their delegated domain; owners set organisation-wide defaults; shared configuration is versioned and personal overrides survive upgrades. | A personal filter set persists across sign-out/sign-in and across an application upgrade; a shared configuration change creates a new version record; the personal override remains applied after the shared change. | R1 (personal, owner defaults), R2 (lead scope) | I-03 |
| PRD-A.11 | Adaptive views: layout, visible capabilities and information density adapt to explicit intent, role, task and available connections; views are validated declarative definitions rendered by trusted components; navigation, active scope, evidence, approval targets, spending and destructive controls stay stable; pinning, undo, reset, keyboard access and a usable fallback exist. | A declarative view definition failing schema validation renders the fallback, not a broken view; pinned elements persist; undo reverts the last adaptation; the listed stable controls are in the same position across adaptations (screenshot comparison). | R3 | I-03, I-10, I-16 |
| PRD-A.12 | Preference learning stays within the member's scope with settings to inspect, disable and reset personalisation; optimise for task completion and error reduction. | Settings expose inspect/disable/reset; with personalisation disabled no adaptation occurs; comparison against fixed seat templates is recorded before promotion (I-10). | R3 | I-03, I-10 |
| PRD-A.13 | Home view fits system health, active priorities, running work, required decisions and a universal assistant asking "What would you like to do?" into the Papership layout. | Home renders the five regions with live data (not fixtures): health from real checks, priorities and running work from the ledger/runs, decisions from approvals, assistant prompt text present. | R1 | I-03 |
| PRD-A.14 | Role-appropriate detail without exposing prompts, API schemas or runtime configuration to normal operators. | Operator seat UI contains no prompt text, schema, or runtime configuration; Founder sees such detail only in designated technical views. R1 evidence: Founder views checked; R2 evidence: Operator seat checked. | R1 (Founder), R2 (Operator) | I-03, I-16 |
| PRD-A.15 | Design specification for seven views — home, work item, assistant, agent run, connection setup, memory manager, permissions editor — each mapped to Papership components or a documented extension; reusable code, adaptations and departures recorded in `docs/ui-blueprint.md`. | A specification exists per view with loading/empty/failure/permission states and component mapping. `proposal`: R1 implements home, work item, assistant, agent run and a minimal permissions editor (owner grants); connection setup and memory manager are implemented in R2/R3 but specified in phase 0. | Spec: phase 0. Build: R1 (4+1 views), R2/R3 (remaining) | I-03, I-07, I-08 |
| PRD-A.16 | Every screen maps to authenticated contracts with real loading, empty, failure and permission states; reference fixtures, synthetic charts and simulated agent responses are isolated as labelled demo data and never counted as implemented capabilities. | No production screen reads `src/api/entities.js` localStorage or `data.jsx` fixtures; demo data is behind an explicit label/flag; registry status is never derived from a reference screen. | R1 | I-04, I-07 |
| PRD-A.17 | Unconfigured functions remain discoverable without crowding daily work. | The registry/discovery surface lists `planned`/`unavailable` capabilities separately from the default work views. | R3 (R1 `proposal`: read-only registry view) | I-10, I-13 |

## 2. PRD-B — Development loop (first complete workflow)

| ID | Requirement | Acceptance criterion | Release | Cite |
|---|---|---|---|---|
| PRD-B.1 | The first complete workflow is: product request → research → specification → plan → work assignment → isolated code change → tests → review → approved release → monitoring → retained knowledge. | One real Engine Labs change traverses all eleven stages; each stage produces a ledger record or artifact linked to the exact revision; the chain is navigable from the work item. | R1 | I-02, I-08 |
| PRD-B.2 | The founder's actual repository is bound; branch, change, check and release operations are scoped separately. | Repository binding record exists; four distinct grant classes (branch, change, check, release); a release operation without the release grant is refused and logged. | R1 | I-02, I-04, I-08 |
| PRD-B.3 | Changes are developed in isolated branches/worktrees within approved scope; relevant checks run; review evidence is attached to the exact revision; a release proposal is produced. | The change is on a non-default branch/worktree; check results and review evidence records reference the commit SHA; a release proposal record exists in state `proposed`, not executed. | R1 | I-06, I-08 |
| PRD-B.4 | Release executes only within its authorised policy; source-control publication and releases go through the protocol's authorisation gates. | Attempting release execution without the designated authority is refused with an audit record; with authority it proceeds and records the approver, action and target version. | R1 | I-06, I-08 |
| PRD-B.5 | `GlobalAgentPanel` is connected to authenticated, backend-mediated Hermes sessions with streamed events; the simulated reply handler is replaced; conversations persist in the customer's cloud environment; granted scope is enforced on every operation; provider credentials stay outside the frontend. | Desktop bundle contains no provider credential (static scan); desktop network calls target only the Engine Labs API; a conversation started before restart is visible after restart; an out-of-scope operation is refused server-side. | R1 | I-08 |
| PRD-B.6 | Run status, scope, sources, model/tool usage, budget, pause/cancel and recovery are exposed to the member. | The agent-run view shows all eight elements with live values; pause and cancel change the run state within the streamed events; a recovery event is shown when it occurs. | R1 | I-08 |
| PRD-B.7 | Thin contract tests exist at the runtime, source-control and action boundaries; restarting a worker or desktop does not duplicate an external effect. | Three contract test suites pass on the release revision; an interruption test (worker kill and desktop close, before and after a potential external write) shows zero duplicated external effects. | R1 | I-08, I-15 |
| PRD-B.8 | Capability status is updated using observed results. | Each registry status change to `working` references the run/test/evidence record that demonstrated it. | R1 | I-08 |
| PRD-B.9 | Cursor's delivery roles, product seats and Hermes runtime identities are kept separate. | Three identity namespaces are distinct in the data model and no credential is shared across them. | R1 | I-06 |
| PRD-B.10 | Production deployment credentials stay outside development workers. | Worker environment inventory contains no production deployment credential name; policy test confirms denial. | R1 | I-08 |
| PRD-B.11 | Engine Labs manages its own development without granting its agents unrestricted control over production. | Agents can propose releases; production execution requires owner/CI authority (external to agent runtime). | R1 | I-06, I-18 |

## 3. PRD-C — Capability registry

| ID | Requirement | Acceptance criterion | Release | Cite |
|---|---|---|---|---|
| PRD-C.1 | A versioned capability registry covers every domain group B01–B24 and P01–P19 (43 groups). | Registry has a version identifier and exactly 43 domain groups, each with at least one capability row; no group removed at any release. | R1 | I-02, I-02B, I-02P, I-13 |
| PRD-C.2 | Each row records the columns in §3.1. | Every row has every column populated or an explicit `n/a` with reason. | R1 | I-02 |
| PRD-C.3 | Statuses `planned`, `configured`, `working`, `unavailable` are tracked distinctly under the transition rules in §3.2. | No status value outside the vocabulary; each transition to `working` cites evidence; `unavailable` rows are visibly distinct in the product and the document. | R1 | I-02, I-08, I-13 |
| PRD-C.4 | The installed Hermes version's tools, profiles, sessions, skills, memory, scheduling, delegation, browser, research, code/file execution, document handling and media capabilities are inventoried and mapped into the registry with actual dependencies and permissions; the inventory is extended as Hermes and connectors evolve. | Inventory records the pinned Hermes version string; each inventoried item maps to a registry row with dependency and permission columns filled. | R1 (pinned version), ongoing | I-02, I-04 |
| PRD-C.5 | Full domain scope is retained through phased delivery; deferred capabilities remain planned, not completed or hidden. | Registry diff between releases shows no removed group; deferred rows remain `planned`. | R1→R4 | I-02, I-06, I-13 |
| PRD-C.6 | Acceptance is defined at two levels: a working first development loop, then increasing verified coverage across the registry. | R1 `working` rows are limited to those demonstrated by the development loop and foundation (§4 table, "R1 target"); coverage metric = count of `working` rows per release, reported in `docs/verification.md`. | R1→R4 | I-02 |
| PRD-C.7 | The registry is a product surface (phase 07 deliverable), readable by the owner, and drives the "which outcomes need a connection" explanation. | Owner can view the registry in-product with status per row; PRD-A.4's explanation is derived from registry dependency and status columns. | R1 | I-07, I-02 |

### 3.1 Registry row schema

Column names are taken from the intake sentence "For each capability record its user outcome, native or connector owner, read/write actions, data authority, required grants, dependencies, interface components, release phase, implementation status and acceptance evidence" (I-02). Identifier and version columns are `proposal` additions required for a versioned registry.

| Column | Source | Type / allowed values | Notes |
|---|---|---|---|
| `domain_id` | I-02B / I-02P (row identifiers) | `B01`–`B24`, `P01`–`P19` | Group the capability belongs to. |
| `capability_id` | `proposal` | `<domain_id>.<nn>` | Stable across releases. |
| `user_outcome` | I-02 | free text | What the member can achieve. |
| `owner` | I-02 ("native or connector owner") | `native` or `connector:<provider>` | |
| `read_actions` | I-02 ("read/write actions") | list | Typed read operations. |
| `write_actions` | I-02 | list | Typed write operations; each must route through the action lifecycle (PRD-E.3). |
| `data_authority` | I-02 | `native` / `source:<system>` / `shared` | Which system is authoritative. |
| `required_grants` | I-02 | list of grant identifiers | Engine Labs grants; source scopes named separately. |
| `dependencies` | I-02 | list of capability IDs, connections, runtime features | |
| `interface_components` | I-02 | list of view/component names | Mapped to `docs/ui-blueprint.md`. |
| `release_phase` | I-02 | implementation phase `07`–`12` and release `R1`–`R4` | Per §4. |
| `implementation_status` | I-02 | `planned` / `configured` / `working` / `unavailable` | §3.2. |
| `acceptance_evidence` | I-02 | link(s) to evidence records | Required for `working`. |
| `registry_version` | `proposal` ("versioned capability registry") | semver or date-revision | Whole-registry version. |
| `status_changed_at` / `status_evidence` | `proposal` | timestamp / link | Required by PRD-B.8. |

### 3.2 Status vocabulary and transition rules

| Status | Meaning (intake-derived) |
|---|---|
| `planned` | In the registry with owner, dependencies and phase; no implementation, configuration, or demonstrated workflow yet (I-02, I-06 "Deferred roadmap capabilities remain planned"). |
| `configured` | Implementation and/or configuration exists (code, schema, connection, hook, measurement) but no complete user workflow has been demonstrated and verified (I-06 "Introduce access controls, durable state, data lifecycle hooks and usage measurement in phase 07; deepen them as capabilities arrive"). |
| `working` | A complete workflow has been demonstrated with verified integration behaviour and linked acceptance evidence on the current revision (I-02 "Require demonstrated workflows and verified integration behaviour before marking capabilities complete"; I-08 "Update capability status using observed results"). |
| `unavailable` | A required dependency, connection, credential, grant, provider capability, or platform check is missing, revoked, failed, or unsupported; shown distinctly, never hidden (I-02 "Track planned, configured, working and unavailable capabilities distinctly"; I-13 "Report unsupported integrations and untested paths accurately"). |

Transition rules:

1. `planned → configured`: implementation or configuration merged/applied; evidence: revision or configuration record. No user-workflow claim.
2. `configured → working`: only with (a) a demonstrated end-to-end workflow, (b) verified integration behaviour against the real dependency (mocks, reference screens, sample data, or a visible control do not qualify — I-04, I-13), and (c) a linked acceptance evidence record on the release revision.
3. `any → unavailable`: on missing/revoked credential, failed health or contract check, unsupported provider route, or a blocked platform check; the row records the reason and the member-facing recovery instruction (PRD-A.9).
4. `unavailable → configured | working`: after the dependency is restored and the relevant check is re-run; return to `working` requires re-verification, not the prior evidence.
5. `working → configured`: when a verification invalidates the prior evidence (regression, changed dependency, changed environment — I-18 "Reuse valid evidence only when the relevant code, dependencies and environment remain unchanged").
6. No transition may skip evidence; every change records `status_changed_at` and `status_evidence`. `project-lead-subagent` rejects unsupported `working` statuses at each gate (blueprint §15 risk control).

## 4. Release map and domain bucket table

### 4.1 Release definition

| Release | Intake implementation phases | Basis |
|---|---|---|
| R1 | 07 Foundation, 08 Development loop | I-06 "Set the first release around implementation phases 07–08 and their required controls." `verified` |
| R2 | 09 Collaboration and connections | `accepted` (D-28 / OQ-3, 2026-09-12). |
| R3 | 10 Company operations | `accepted` (D-28 / OQ-3, 2026-09-12). |
| R4 | 11 Commercial delivery, 12 Ecosystem and mobile | `accepted` (D-28 / OQ-3, 2026-09-12). Alternative R3 = 10+11 withdrawn. |

Verification phases 13–18 apply to every release's enabled scope (I-06, I-13).

### 4.2 Bucket rule

A domain group's **release bucket** is the release in which its first capability is targeted to reach `working` (or `configured` where the intake introduces only hooks/measurement). Bucketing does not remove any group from the registry; groups bucketed later remain `planned` and visible (PRD-C.5). "R1 target" is the maximum status any row in the group may reach in release 1. The R3/R4 split of business domains is `proposal`, since the intake selects "the next highest-value domain capability" iteratively (I-10) and reserves "remaining market domains" for phase 12 (I-12) without naming them.

### 4.3 Business domains (B01–B24)

| ID | Domain (intake name) | Bucket | R1 target | R1 capability (if any) / rationale | Cite |
|---|---|---|---|---|---|
| B01 | Strategy and governance | R3 | `planned` | Goals/KPIs/board reporting are domain modules (I-10). | I-02B, I-10 |
| B02 | Organisation structure | R2 | `planned` (R1 `configured` `proposal`: single organisation record for the founder) | Seats/hierarchy/delegated administration land in phase 09. | I-02B, I-03, I-09 |
| B03 | People and capacity | R3 | `planned` | Domain module. | I-02B, I-10 |
| B04 | Customers and CRM | R3 | `planned` | Domain module. | I-02B, I-10 |
| B05 | Sales and commercial scope | R3 | `planned` | Domain module. | I-02B, I-10 |
| B06 | Projects and programmes | R1 | `working` (partial) | Work ledger: plans, dependencies, delivery evidence, acceptance ("basic work ledger"; "plan work"). Budgets/resources later. | I-02B, I-02, I-07 |
| B07 | Tasks and personal work | R1 | `working` (partial) | Assignments, priorities, blockers ("priority creation, work planning"). Recurring work/checklists later. | I-02B, I-07 |
| B08 | Software and product delivery | R1 | `working` (partial) | Requirements, repositories, branches, PRs, tests, releases via the development loop; feature flags/incidents later. | I-02B, I-08 |
| B09 | Service delivery and operations | R3 | `planned` | Domain module (support/service ops relevant to customer delivery). `proposal` R3. | I-02B, I-10 |
| B10 | Customer support and success | R3 | `planned` | Domain module. `proposal` R3. | I-02B, I-10 |
| B11 | Knowledge and documents | R1 | `working` (partial) | Decisions, evidence, versions and "retained knowledge" from the loop; document intake (PRD-A.4). Policies/SOP search later. | I-02B, I-02 |
| B12 | Communications and meetings | R2 | `planned` | Communication connectors (Gmail, Slack, Telegram, WhatsApp) in phase 09. | I-02B, I-04, I-09 |
| B13 | Finance and accounting | R3 | `planned` | Domain module. `proposal` R3. | I-02B, I-10 |
| B14 | Treasury and payments | R4 | `planned` | Payments require designated authority and full commercial/lifecycle controls; `proposal` R4 (remaining domains, I-12). | I-02B, I-05, I-12 |
| B15 | Procurement and vendors | R3 | `planned` | Domain module. `proposal` R3. | I-02B, I-10 |
| B16 | Marketing and content | R3 | `planned` | Domain module. `proposal` R3. | I-02B, I-10 |
| B17 | Legal and risk | R3 | `planned` | Domain module. `proposal` R3. | I-02B, I-10 |
| B18 | IT and internal systems | R3 | `planned` | Domain module (accounts/devices/licences); platform provisioning is P10. `proposal` R3. | I-02B, I-10 |
| B19 | Inventory and physical assets | R4 | `planned` | Remaining market domain. `proposal` R4. | I-02B, I-12 |
| B20 | Supply chain and field work | R4 | `planned` | Remaining market domain; offline capture implies mobile (phase 12). `proposal` R4. | I-02B, I-12 |
| B21 | Manufacturing and quality | R4 | `planned` | Remaining market domain. `proposal` R4. | I-02B, I-12 |
| B22 | Research and innovation | R3 | `planned` | Domain module (experiments, datasets, model runs). `proposal` R3. | I-02B, I-10 |
| B23 | Stakeholders and external portals | R2 | `planned` | Guest assignments and scoped collaboration in phase 09. | I-02B, I-03, I-09 |
| B24 | Sector-specific operations | R4 | `planned` | Remaining market domain. `proposal` R4. | I-02B, I-12 |

### 4.4 Agent and platform domains (P01–P19)

| ID | Domain (intake name) | Bucket | R1 target | R1 capability (if any) / rationale | Cite |
|---|---|---|---|---|---|
| P01 | Agent workforce | R1 | `working` (partial) | Universal assistant as one agent with sponsor, model, tool access, budget, status ("model/tool usage, budget"). Working hours/retirement later. | I-02P, I-05, I-08 |
| P02 | Profiles and identities | R1 | `working` (partial) | Founder identity, tenant membership, owner seat ("identity, owner seat"). Delegation later. | I-02P, I-07 |
| P03 | Conversations and modes | R1 | `working` (partial) | Persisted assistant conversations; modes per PRD-E.1 (Automate `configured`). Voice later. | I-02P, I-05, I-08 |
| P04 | Agent execution | R1 | `working` (partial) | Runs, steps, checkpoints, cancellation, recovery ("pause/cancel and recovery"). Deadlines/handoffs partial. | I-02P, I-05, I-08 |
| P05 | Workflow orchestration | R1 | `working` (partial) | Durable state, job persistence, retries, approvals ("durable job status"). Schedules `configured` until R3. | I-02P, I-06, I-07 |
| P06 | Tools and connectors | R1 | `working` (partial) | Capability registry, Hermes adapter, repository binding. Connector catalogue R2+. | I-02P, I-07, I-08 |
| P07 | Data ingestion and synchronisation | R2 | `planned` | Sync checkpoints, dedup, lineage arrive with connectors. | I-02P, I-04, I-09 |
| P08 | Business meaning and analytics | R3 | `planned` | Canonical references/metrics/dashboards with domain modules. | I-02P, I-10 |
| P09 | Memory and retrieval | R1 | `working` (minimal) | Retained knowledge written through the governed store with provenance; search/inspect. Full operations (PRD-F.3) R3. | I-02P, I-02, I-05, I-10 |
| P10 | Identity and authorisation | R1 | `working` (partial) | Membership, owner seat, grant checks ("grant checks"; "Verify access boundaries"). SSO/offboarding later. | I-02P, I-07, I-14 |
| P11 | Privacy and lifecycle | R1 | `configured` | Data lifecycle hooks and retention settings present ("data lifecycle hooks ... in phase 07"); erasure/offboarding workflows R4. | I-02P, I-05, I-06, I-11 |
| P12 | Secrets and boundaries | R1 | `working` (partial) | Provider credentials off desktop, isolation, restricted egress ("Keep provider credentials outside the frontend"). Rotation later. | I-02P, I-04, I-08 |
| P13 | Audit and provenance | R1 | `working` (partial) | Actor, intent, policy, approvals, tool receipts, record changes ("linked evidence"; receipts). | I-02P, I-04, I-05, I-08 |
| P14 | Evaluation and improvement | R1 | `configured` | Capture of the six outcome metrics for the loop (§10); regression cases/promotion R3. | I-02P, I-02, I-10 |
| P15 | Member experience | R1 | `working` (partial) | Founder template, desktop layout, search, notifications. Mobile/localisation later. | I-02P, I-03, I-07 |
| P16 | UI composition and adaptation | R3 | `planned` | Declarative intent-based views, pinning, undo, fallback in phase 10. | I-02P, I-03, I-10 |
| P17 | Reliability and operations | R1 | `working` (partial) | Health checks, streamed status, restart recovery ("restart recovery"). Backups/restore verified R4. | I-02P, I-04, I-07, I-11 |
| P18 | Product commercial operations | R1 | `configured` | Usage measurement records ("usage measurement in phase 07"); no plans, billing or entitlement enforcement until R4. | I-02P, I-05, I-06, I-11 |
| P19 | Extensibility and distribution | R4 | `planned` | Connector SDK, domain packs, plugin trust in phase 12. | I-02P, I-12 |

Bucket totals: R1 = 19 (B06, B07, B08, B11, P01–P06, P09–P15, P17, P18), R2 = 4 (B02, B12, B23, P07), R3 = 14 (B01, B03, B04, B05, B09, B10, B13, B15, B16, B17, B18, B22, P08, P16), R4 = 6 (B14, B19, B20, B21, B24, P19). Total 43.

## 5. PRD-D — Authority model and seat templates

| ID | Requirement | Acceptance criterion | Release | Cite |
|---|---|---|---|---|
| PRD-D.1 | Three initial seat templates exist as in §5.1. | Each template is a data record with responsibilities and default authority matching §5.1; R1 instantiates Founder; R2 instantiates all three and demonstrates a delegated workflow across two seats (I-09). | R1 (Founder), R2 | I-03, I-09 |
| PRD-D.2 | Hierarchy is owner → domain/project lead → member; job titles, seat templates and actual grants are separate; one person may hold multiple responsibilities and switch work context. | Data model separates title, template, grant; a member with two responsibilities can switch context and the visible scope changes accordingly. | R2 | I-03 |
| PRD-D.3 | A delegator may grant only a subset of their own authority; assignment never confers unrelated access. | Attempt to delegate a grant the delegator lacks is refused; assigning a task grants no read access outside the task's scope (I-14). | R2 | I-03, I-14 |
| PRD-D.4 | Organisation, legal entity, department, team, location, project, task and provider account are modelled separately; scoped guest participation, agency administration and several accounts with the same provider are supported. | Eight distinct entities exist; two `ProviderAccount` records for one provider coexist with separate grants; a guest sees only assigned scope. | R1 (entities), R2 (guests, agency) | I-03 |
| PRD-D.5 | Server-side role, record, field and action checks apply to everything, including search, aggregates, attachments, notifications and memory. | Authorisation tests cover each of the five listed surfaces; an unauthorised principal receives no rows, no aggregate contribution, no attachment, no notification, no memory item. | R1 | I-03, I-14 |
| PRD-D.6 | Engine Labs permissions intersect with source-system permissions, the connected credential's scope and the active action policy; billing entitlements are separate from data authority. | An action allowed by Engine Labs grant but denied by source ACL is refused; a tier upgrade creates no data permission (I-14). | R2 (source intersection), R1 (entitlement separation) | I-03, I-14 |
| PRD-D.7 | Strong authentication for privileged users; reauthentication for destructive administration. | Owner sign-in requires the configured strong factor; a destructive administrative action prompts reauthentication and is refused without it. | R1 | I-03 |
| PRD-D.8 | Engine Labs staff have explicit provisioning access during setup; at handover, client ownership is verified, setup credentials replaced, temporary application/cloud/SSH grants revoked and resulting access tested; thereafter support access is customer-authorised, logged and time-limited; client-controlled infrastructure ownership precedes handover completion. | Handover checklist record with each step evidenced; post-handover test shows revoked setup access fails (I-09, I-14); support session has an expiry. | R2 | I-03, I-09, I-14 |
| PRD-D.9 | Independent read/research, drafting, sandboxed development and reversible internal actions are allowed within policy; external commitments, production releases, access changes, payments, destructive changes and spending beyond a grant require the designated authority; the same rules apply to direct UI actions, messaging requests, agents and subagents. | Policy matrix exists; each restricted class is exercised once per entry channel and refused without authority. | R1 (UI, agent), R2 (messaging) | I-05 |
| PRD-D.10 | Approval is bound to the actual action and target version and revalidated when either changes. | Changing the target after approval invalidates the approval; re-execution requires new approval. | R1 | I-05, I-14 |
| PRD-D.11 | Agents cannot self-grant permissions or directly modify production code or security controls. | Attempt via agent tool is refused and audited. | R1 | I-05 |
| PRD-D.12 | Running and queued work rechecks authority on revoked credentials, changed assignments, expired approvals and modified targets. | Revoking a grant mid-run stops the affected step at a safe boundary with an audit record. | R1 | I-14, I-05 |
| PRD-D.13 | Desktop security posture: bundled UI, restricted native capabilities, secure token storage, signed releases and updates, narrow authenticated cloud API; provider secrets and privileged execution off the desktop; generated views have no direct filesystem, shell, database or credential access. | Native capability allowlist is minimal and documented; tokens stored in the OS keychain; update signature verified before install (I-16); generated view runtime has no such APIs. | R1 | I-04, I-16 |

### 5.1 Seat templates (product requirements)

Source table: I-03 "Provide three initial seat templates". Default views are `proposal` mapped to PRD-A.15.

| Seat (intake name) | Responsibilities (intake) | Default authority (intake) | Default views (`proposal`) | Allowed action classes | Prohibited exposures |
|---|---|---|---|---|---|
| Founder / organisation owner | Strategy, organisation configuration, budgets, policy, ownership and cross-domain oversight | Administer their organisation and delegate bounded grants | Home, work item, assistant, agent run, permissions editor, connection setup, memory manager, billing view (I-05) | All independent actions; designated authority for external commitments, releases, access changes, payments, destructive changes, spend beyond grant (PRD-D.9); organisation-wide defaults (PRD-A.10); erasure with reauthentication (PRD-F.8) | May see technical detail only in designated technical views; never raw provider credentials (PRD-D.13) |
| Project Lead / domain lead | Scope, planning, dependencies, assignments, delivery review and domain improvements | Manage assigned projects/domains within delegated limits | Home, work item, assistant, agent run; permissions editor limited to delegated scope | Independent actions within domain; delegate subset of own grants (PRD-D.3); configure delegated domain (PRD-A.10); agent configuration within ceiling (PRD-E.2) | No organisation-wide defaults; no grants beyond own; no prompts/schemas/runtime configuration (PRD-A.14) |
| Operator | Execute assigned work, use assistants, maintain relevant records and report exceptions | Access and act on explicitly assigned scope | Home, work item, assistant, agent run (own runs) | Independent actions within assigned scope; report exceptions | No configuration of others' scope; no prompts, API schemas, runtime configuration (PRD-A.14); no data beyond assignment (PRD-D.3) |

Release: Founder seat R1; Project Lead and Operator R2 (I-09 "Implement Founder, Project Lead and Operator templates").

## 6. PRD-E — Runtime, assistant and action lifecycle

| ID | Requirement | Acceptance criterion | Release | Cite |
|---|---|---|---|---|
| PRD-E.1 | A universal assistant backed by essential Hermes capabilities supports Ask, Analyse, Plan, Draft, Execute, Review and Automate modes through backend-enforced tool access; specialist agents are added only when separate context, permissions or parallel work gives a measurable benefit. | Mode is a server-side attribute of the session; a tool outside the mode's set is refused server-side. `proposal`: R1 enables Ask, Analyse, Plan, Draft, Execute, Review; Automate is `configured` until schedules arrive (R3). | R1 (six modes), R3 (Automate) | I-05 |
| PRD-E.2 | Every run has a sponsor, acting identity, purpose, scope, policy version, model configuration, budget, deadline and accountable owner; roles configure agents within their delegated ceiling; aggregate budgets are tracked across parent and child runs. | Run record has all nine fields non-null; a child run's spend counts against the parent's aggregate; configuration above the ceiling is refused. | R1 | I-05 |
| PRD-E.3 | Action lifecycle: retrieve authorised context → prepare a typed action → validate scope and current state → obtain required approval → reserve budget → execute → verify the source outcome → store a receipt. | Each write action produces an audit trail containing the eight steps in order; skipping a step is impossible by construction (test attempts refused). | R1 | I-05 |
| PRD-E.4 | Cloud execution is independent of the desktop connection: accepted background jobs keep running; durable status, streamed progress, reconnect/resume and completion notifications exist; closing the application is distinct from explicitly cancelling work. | Close desktop mid-job → job completes; reopen → status and history stream; explicit cancel → job stops with `cancelled` state; notification delivered on completion. | R1 | I-04, I-07 |
| PRD-E.5 | A job is persisted before an accepted response is returned; one Engine Labs workflow layer owns dispatch, schedules and approvals; Hermes scheduling/delegation is mapped into that ownership; no duplicate independent scheduling of the same obligation. | Kill the API between persist and response → job exists on restart; a scheduled obligation appears once in the workflow layer even when delegated to Hermes. | R1 | I-04 |
| PRD-E.6 | Code and browser work runs in isolated environments with least-privilege filesystem/network access; source documents, messages, tool output and retrieved memory are untrusted inputs; permissions are enforced outside prompts; agent profiles are separate from execution isolation; credentials and orchestration databases are outside agent execution mounts. | Isolation inventory (mounts, network egress) reviewed by Security; a prompt-injection fixture attempting a restricted action is refused by policy, not by prompt. | R1 | I-05 |
| PRD-E.7 | Job, step, claim, checkpoint, approval, cancellation and receipt state persist; recovery resumes at the last verified boundary; external effects use idempotency keys where supported; uncertain outcomes are reconciled before replay; a remote write followed by a timeout is treated as potentially completed. | Interruption tests (I-15) show resume at last verified boundary and zero duplicated effects; timeout-after-write path reconciles source state before retry. | R1 | I-05, I-04, I-15 |
| PRD-E.8 | Internal diagnostic harness: two safe transient retries and one bounded diagnostic attempt within remaining time and budget; backoff, circuit breakers and an incident record; escalation with evidence and a proposed next action when recovery fails or needs new authority, credentials, spending or a consequential change; no recursive recovery loops. | Fault-injection run shows exactly 2 retries + 1 diagnostic attempt, then an incident record and an escalation containing evidence and a proposed next action; budget/deadline never exceeded. | R1 | I-05, I-15 |
| PRD-E.9 | Agents may propose and evaluate improvements to skills, prompts, workflows and views; validated changes promote within owner policy; shared or consequential changes require review; versions, regression cases and rollback exist. | Improvement proposal record → evaluation → review → promotion with version and rollback path demonstrated once. | R3 | I-05, I-10 |
| PRD-E.10 | Side-effecting Hermes tools route through the Engine Labs action service; shell/browser network access has the same boundary; Hermes API authentication is transport access, not per-tool authorisation; company records are independent of Hermes' internal storage format. | Contract test: a side-effecting tool call bypassing the action service is impossible/refused; company records readable with Hermes stopped. | R1 | I-04, I-08 |
| PRD-E.11 | Deterministic code handles amounts, currencies, dates, financial metrics and validation. | No model output is used directly as a financial or date value; tests cover conversion functions. | R1 (rule), R3 (finance) | I-04 |
| PRD-E.12 | Hermes sessions and runtime memory are scoped by tenant and authorised principal/project context; runs are hydrated only with permitted knowledge; durable memory is written back through the governed store; shared runtime memory files or session identifiers never cross permission boundaries. | Two principals in one tenant cannot read each other's session; memory written by a run appears in the governed store with provenance. | R1 | I-05, I-14 |
| PRD-E.13 | Hey Engine is the end-product universal assistant: a persistent button/mic control and the wake phrase "Hey Engine" (plus typed Ask) invoke the same assistant. It may perform any action the signed-in user is allowed to perform in the product — same grants, approval classes, and spend/release/erasure gates. Voice or button never bypasses AUTH-07, F-SEC-04, or restricted approvals. | R1: the shell control is present and opens the assistant; the panel shows an honest `unavailable` state until the runtime exists; no simulated replies (AUTH-28); wake-word listening is specified, not shipped. Phase 2: Hermes-backed execution of user-equivalent actions through the Engine Labs action service. Later: always-on or push-to-talk wake word on desktop, then mobile. A restricted action requested by voice is refused the same as the equivalent UI action. | R1 (control + unavailable), R1/R2 (runtime via PRD-E.1/B.5), later (wake word) | I-03, I-05, owner 2026-09-11 |

## 7. PRD-F — Memory, data, and lifecycle

| ID | Requirement | Acceptance criterion | Release | Cite |
|---|---|---|---|---|
| PRD-F.1 | Memory spans sessions, personal preferences, projects, domains, organisation knowledge and procedural skills; useful history is retained within configured storage/retention limits; source records, approved facts and model-inferred candidates are separated. | Memory item has a `kind` from the six values and a `class` of `source`/`approved`/`inferred`; retrieval can filter by class. | R1 (minimal), R3 | I-05 |
| PRD-F.2 | Substantive memory stores provenance, owner, source permissions, timestamps, verification state, expiry and version. | Every memory item written by the R1 loop has all seven fields. | R1 | I-05 |
| PRD-F.3 | Memory supports searching, inspecting, correcting, merging, restricting, archiving, exporting and deleting; permissions are rechecked before retrieval; contributing source restrictions apply to derived summaries and embeddings. | R1: search and inspect; R3: all eight operations demonstrated; a restriction on a source item hides derived summaries from unauthorised principals (I-14 "correction propagation"). | R1 (search/inspect), R3 | I-05, I-14 |
| PRD-F.4 | Configurable starting retention: conversation history 365 days; execution/debug logs 30 days; rotating backups 30 days; approved organisational knowledge until superseded, deleted or expired by policy; settings visible and overridable by authorised owners; credentials excluded from memory; copied sensitive data minimised. | Retention settings page shows the four defaults; owner change persists; a credential-shaped string is never stored in memory (scan test). | R1 (settings, exclusion), R4 (enforcement verified with backups) | I-05 |
| PRD-F.5 | No cross-customer content learning or training by default; preference learning is personal; operational evaluation stays within the tenant; broader use requires explicit policy; model/data-processing providers are configurable and activated under owner policies, with test fixtures until live-data permissions exist. | Provider configuration is per tenant with a policy record; default policy = no cross-tenant use; fixtures used where no permission recorded. | R1 | I-05 |
| PRD-F.6 | Data residency: primary records, conversations, memory, artifacts, secrets and execution state stay in the assigned data environment; any shared licensing/billing service holds only account, entitlement and usage metadata; customer content stays out of shared telemetry by default; encrypted backups go to a separate client-controlled location with provider, region, retention, key ownership and restore access as deployment settings; provider snapshots tracked separately; external model/tool processing is a separate data destination under its own policy; a local backup on the same VPS is not disaster recovery. | Data-destination map (architecture) lists each destination with policy; telemetry payload inspection shows no customer content; backup settings exist as configuration. | R1 (map, telemetry), R4 (backup restore verified, I-15) | I-04, I-15 |
| PRD-F.7 | Offboarding revokes sessions, grants and personal credentials; stops affected queued/running actions at safe boundaries; archives work and requests an owner's disposition; continues only workflows sponsored by an independent authorised service identity; archived work has a visible owner and decision deadline. | Offboarding test: sessions invalid, grants gone, runs stopped at boundary, archive record with owner and deadline. | R4 (verified R2 for seats `proposal`) | I-05, I-14 |
| PRD-F.8 | Domain erasure is a scoped request with owner approval and dependency/impact preview; organisation-wide erasure requires owner reauthentication, explicit scope confirmation and an additional final confirmation; erasure suspends runs, revokes credentials, clears primary content, artifacts, summaries, indexes, caches and replicas; backups, snapshots and external deletions follow their actual retention capabilities with pending copies and exceptions disclosed; a deletion receipt is produced; deletion in connected source systems is a separately scoped action. | Erasure test on disposable fixtures (I-14) shows preview, the three confirmations, cleared surfaces, disclosed pending copies, and a receipt. | R4 | I-05, I-11, I-14 |
| PRD-F.9 | Data export is available across tiers. | Owner can export tenant data in a documented format at any tier. | R4 (R1 `proposal`: developer export of ledger and memory) | I-05 |

## 8. PRD-G — Commercial controls (structure only; no prices)

| ID | Requirement | Acceptance criterion | Release | Cite |
|---|---|---|---|---|
| PRD-G.1 | Four configurable commercial tiers exist per §8.1. | Tier records exist with the entitlement/usage model fields; configurable, not hard-coded. | R4 (design R1) | I-05 |
| PRD-G.2 | Tiers 1–3 use model-band token allowances and a monetary budget, shown separately as actual tokens and monetary usage; Tier 4 applies published graduated usage rates, configurable spending ceilings, alerts and concurrency limits. | Billing view shows tokens and money as separate figures; Tier 4 ceiling breach pauses new chargeable work and raises an alert. | R4 | I-05, I-17 |
| PRD-G.3 | Cost accounting includes retries, cached input, output, tool calls and execution costs without double-counting provider events. | Ledger sum equals provider-reported usage for a test run; repeated provider event does not duplicate a ledger entry (I-17). | R1 (measurement), R4 (reconciliation) | I-05, I-17 |
| PRD-G.4 | Estimated cost is reserved before dispatch, actual usage reconciled, and new chargeable work paused when a limit is reached, while records, exports and pending decisions remain accessible. | Reservation record precedes dispatch; exhausted allowance blocks new runs but not viewing, export or approvals (I-17). | R4 | I-05, I-17 |
| PRD-G.5 | Provider billing is separated from customer charges through a versioned rate card and an auditable usage ledger. | Rate card has version; every charge references a rate-card version and a ledger entry. | R4 | I-05 |
| PRD-G.6 | Members see a simple remaining allowance and estimated action cost; detailed model, token and rate accounting lives in the billing view. | Non-billing views show only remaining allowance and estimated cost; billing view shows detail. | R4 (R1 `proposal`: estimated cost and usage per run shown in the run view per PRD-B.6) | I-05, I-08 |
| PRD-G.7 | Tenant isolation, permissions, essential audit, data export and deletion are available across all tiers. | Each tier definition includes these as non-removable entitlements. | R4 | I-05, I-17 |
| PRD-G.8 | Hosted capacity, backup storage and support are priced explicitly; customer tool subscriptions are separate unless commercially authorised. | Rate card has distinct line items for these; no bundled implicit pricing. No prices in this contract. | R4 | I-05 |
| PRD-G.9 | Proprietary commercial licensing; upstream notices preserved; dependency licence inventory maintained; connector SDK independently licensable. | Licence file, notices, inventory exist; SDK has its own licence artifact. | R1 (licence, notices, inventory), R4 (SDK) | I-05, I-17 |
| PRD-G.10 | Prices and allowances are calculated from measured infrastructure, model/tool and support costs before billing customers; publication and charge activation are a commercial decision gate. | No price published or charge activated in R1–R3; a measured-cost record precedes any price proposal (I-11). | R4 | I-05, I-11 |
| PRD-G.11 | Usage measurement begins in phase 07 in skeletal form and deepens later. | R1: each run records tokens (by model band), tool calls, execution time and estimated monetary cost. | R1 | I-06, I-08 |
| PRD-G.12 | Commercial operations: tenant provisioning, plans, seat/usage billing, quotas, entitlements, onboarding, support, exports and deletion; all four entitlement/usage models validated in test mode before activation. | Phase 11 test-mode validation of rate cards, limits, reservations and reconciliation recorded (I-11, I-17). | R4 | I-02P, I-11, I-17 |

### 8.1 Tier structure (no prices)

Intake names are `Tier 1`–`Tier 4` (I-05 "Implement four configurable commercial tiers"). The labels Free / Basic / Professional / Enterprise were supplied by the orchestrating lead and are `proposal` (open question OQ-4). No monetary value, allowance quantity, seat count or rate appears here by requirement (PRD-G.10).

| Intake tier | Proposed label (`proposal`) | Entitlement and usage model (intake) | Allowance mechanism (intake) | Budget semantics (intake) |
|---|---|---|---|---|
| Tier 1 | Free | Individual operation, core workspace and basic connectors, with a capped monthly model allowance and concurrency | Model-band token allowance + monetary budget; tokens and money shown separately | Reserve before dispatch; reconcile; pause new chargeable work at limit; keep records/exports/decisions accessible |
| Tier 2 | Basic | Higher allowances, scheduled workflows and broader connector capacity | Same as Tier 1 | Same |
| Tier 3 | Professional | Higher allowances, coordinated agents, advanced workflows and adaptive workspace capabilities | Same as Tier 1 | Same |
| Tier 4 | Enterprise | Organisation subscription with paid seats and metered model usage; no included token quota as the limiting mechanism | Published graduated usage rates; configurable spending ceilings; alerts; concurrency limits | Same reservation/reconciliation; ceilings instead of quota |

Cross-tier guarantees: PRD-G.7. Rate card and usage ledger: PRD-G.5. Explicit line items for hosted capacity, backup storage and support: PRD-G.8.

## 9. Release-1 acceptance definition

The intake has no section titled "Final result". Release-1 acceptance is derived from the phase 06 required-evidence rows for phases 07 and 08, the demonstration sentences of phases 07 and 08, and the registry-preservation rule of phase 13 (evidence record EV-05). Release 1 is accepted when every row below is `VERIFIED` on the exact release revision (I-18) or explicitly waived by the owner.

| ID | Acceptance criterion (observable) | Evidence type | Cite |
|---|---|---|---|
| R1-ACC-1 | Founder signs in to the packaged desktop client with real identity (no development stub); token stored in secure OS storage. | Native platform run; screenshot; keychain inspection | I-06 ("Founder can sign in"), I-07, I-04 |
| R1-ACC-2 | Founder creates a priority and a plan with assignments and dependencies; records persist server-side and are visible after desktop restart. | Ledger records; API query; restart screenshot | I-07 ("priority creation, work planning") |
| R1-ACC-3 | Founder starts a background job, closes the desktop, the job continues and completes; on reopening, status and progress history stream and a completion notification is shown. | Job log with timestamps spanning the disconnect; event stream capture | I-06 ("reconnect to a persisted cloud job"), I-07, I-04 |
| R1-ACC-4 | Access boundaries hold: a second identity or a request lacking a grant is refused server-side on records, search, aggregates, attachments, notifications and memory. | Authorisation test results | I-07 ("Verify access boundaries"), I-03, I-14 |
| R1-ACC-5 | API and worker restart during a job resumes at the last verified boundary with no duplicated external effect. | Interruption test log (before/after potential write) | I-07 ("restart recovery"), I-08, I-15 |
| R1-ACC-6 | One real Engine Labs change completes the full loop (PRD-B.1) with linked evidence and bounded authority; a release proposal exists; release execution occurs only with authorised policy. | Work item chain; branch/PR; test and review records; release proposal record; audit entries | I-06 ("Complete a real Engine Labs change with linked evidence and bounded authority"), I-08 |
| R1-ACC-7 | The assistant panel uses backend-mediated, streamed Hermes sessions; conversation persists across restart; no simulated replies; no provider credential in the desktop bundle. | Static scan; network capture; restart check | I-08 |
| R1-ACC-8 | The agent-run view shows status, scope, sources, model/tool usage, budget, pause/cancel and recovery. | Screenshot with live run | I-08 |
| R1-ACC-9 | Contract tests at runtime, source-control and action boundaries pass on the release revision. | Test output with exit codes | I-08 |
| R1-ACC-10 | Registry shows all 43 groups; statuses reflect observed results; `working` rows are only those demonstrated; no reference screen counted. | Registry file/service diff; status evidence links | I-02, I-08, I-13 |
| R1-ACC-11 | The six outcome metrics (§10) are captured for the R1 loop and recorded as the first baseline (no target asserted). | Metric records | I-02 |
| R1-ACC-12 | No commercial activation: no price published, no charge, no customer deployment; usage measurement records exist per run. | Configuration inspection; ledger sample | I-05, I-06 |
| R1-ACC-13 | Disconnected usefulness: with no connector other than the bound repository, organisation setup, planning, configuration and document intake complete; connection-requiring outcomes are explained. | Walkthrough evidence | I-02 |
| R1-ACC-14 | Verification phases 13–18 are applied to the enabled scope; future-feature checks are `NOT_APPLICABLE`; no missing credential, policy or platform evidence is recorded as passed. | `docs/verification.md` index | I-13, I-18 |
| R1-ACC-15 | Owner handoff prepared and the owner's `APPROVE` / `REQUEST_CHANGES` / `DO_NOT_PROCEED` is recorded (not inferred). | `delivery/owner-handoff.md` | I-18 |

## 10. Success-metric taxonomy inputs

Inputs for `growth-marketing-subagent` and `project-lead-subagent`. No baseline exists; no analytics source is authenticated (`.cursor/TOOLS.md` treats analytics as unavailable until verified); every value in release 1 is a first measurement (blueprint §7 V4). Targets are not set here (I-06: "Define measurable recovery, performance and usability targets from the pilot baseline before testing them").

| Metric (intake term) | Definition input | Event/data need | Baseline | Target | Cite |
|---|---|---|---|---|---|
| Task completion | Share of loop stages reached and completed per work item; loop completed end-to-end yes/no | Ledger stage transitions with timestamps | none (first measurement R1) | not set | I-02 |
| Correctness | Review outcome and check results per change; defects found after review | Review records; check results; post-release incident links | none | not set | I-02, I-13 |
| Recovery | Count and outcome of retries/diagnostic attempts; time from failure to resumed progress; duplicated effects (must be zero) | Incident records; run events; receipt reconciliation | none | zero duplicates is a hard requirement (PRD-B.7), not a metric target | I-02, I-05, I-15 |
| Operator intervention | Approvals, manual edits, escalations answered per completed outcome | Approval and escalation records | none | not set | I-02 |
| Context switching | Source-app handoffs and view changes per work item; distinct surfaces used | UI navigation events; handoff records | none | not set | I-02 |
| Cost per completed outcome | Tokens by model band, tool calls, execution cost per completed work item, without double counting | Usage ledger (PRD-G.3, G.11) | none | not set | I-02, I-05 |
| Guardrail: authority violations | Refused unauthorised attempts; any successful unauthorised action (must be zero) | Audit records | none | zero successful violations (requirement) | I-03, I-14 |
| Usability (R3+) | Completion time and errors: adaptive vs fixed views; routine work without technical traces | Task timing; error counts | none | set from pilot baseline | I-06, I-10, I-16 |
| Recovery/performance targets (infra) | Recovery time and potential data loss on restore; resource headroom | Restore drill; resource measurement | none | set from pilot baseline before testing | I-06, I-15, I-04 |

## 11. Non-functional requirements

| ID | Requirement | Acceptance criterion | Release | Cite |
|---|---|---|---|---|
| NFR-1 | Desktop client with cloud execution; macOS first; shared UI contracts for later Windows, Linux, iOS and Android. | Packaged macOS app passes R1-ACC-1..3; UI contracts documented for reuse. | R1 | I-04, I-12 |
| NFR-2 | Accessibility: keyboard navigation, focus management, accessible labels, contrast, responsive layout, readable empty/error states; an operator completes routine work without technical traces or special prompting. | Accessibility checklist passes on the R1 views; routine-task walkthrough recorded. | R1 | I-16, I-03 |
| NFR-3 | Visual fidelity to the recorded Papership `/cc-org-dash` reference: THEMES, Inter/JetBrains Mono typography, spacing, primary tabs, command rail, assistant panel and overlay behaviour preserved; Engine Labs branding replaces prototype branding; departures are recorded and material aesthetic departures are asked about before implementation. | Screenshot comparison at matching viewport and theme; `docs/ui-blueprint.md` lists departures. | R1 | I-03, I-16 |
| NFR-4 | Measurable recovery, performance and usability targets are defined from the pilot baseline before being tested; none are asserted in advance. | Targets recorded after R1 baseline, before R2 tests. | R1 (baseline), R2 (targets) | I-06 |
| NFR-5 | Operations: structured logs, run traces, health checks, cost metrics, alerting, encrypted backups and tested restore procedures. | Each exists and is exercised; restore drill R4 (I-15). | R1 (logs, traces, health, cost), R4 (backups verified) | I-04 |
| NFR-6 | Database, browser and worker resource consumption are measured before selecting production VPS capacity. | Measurement report precedes sizing decision. | R1→R4 | I-04, I-11 |
| NFR-7 | Signed releases and updates; secure token storage. | Update signature verified; keychain storage confirmed. | R1 | I-04, I-16 |
| NFR-8 | Seeded development environment and ordinary-language empty/error states. | Fresh environment seeds; every R1 view's empty and error states use plain language. | R1 | I-07 |
| NFR-9 | Every enabled capability is traceable to a requirement, implementation, configuration and acceptance check; evidence states `VERIFIED` / `PARTIAL` / `UNVERIFIED` / `NOT_APPLICABLE` are distinct from role gate verdicts. | `docs/verification.md` rows link PRD ID → registry row → implementation → check. | R1 | I-13, I-06 |
| NFR-10 | Compatible releases and image digests pinned after a compatibility spike; backend modular; first worker count small; unneeded services disabled. | Lockfiles and digests recorded in architecture. | R1 | I-04 |

## 12. Open owner questions

Recorded, not blocking (charter §5). The lead routes these at the gate where they matter.

| ID | Question | Why it matters | Needed by |
|---|---|---|---|
| OQ-1 | Confirm the founder development repository bound in phase 08 (current assumption: this repository). | PRD-B.2; phase 2 plan. | Before `phase_2_development_loop_plan.md` |
| OQ-2 | Which domain groups should be first in R3 (phase 10 "next highest-value domain capability")? | Sequencing of R3 modules and connectors. | **Accepted 2026-09-12 (D-27):** §4.3 proposal — B01 strategy/governance, B03 people/capacity first; memory manager / adaptive views are R3 core. |
| OQ-3 | Confirm phase-to-release mapping for 09–12 (proposal: R2 = 09, R3 = 10, R4 = 11 + 12; alternative R3 = 10 + 11, R4 = 12). | Bucket table §4; roadmap. | **Accepted 2026-09-12 (D-28):** R2=09, R3=10, R4=11+12. |
| OQ-4 | Confirm public tier labels (proposal: Free / Basic / Professional / Enterprise for intake Tier 1–4). | Growth tier communication (T0-10); no pricing implied. | **Accepted 2026-09-12 (D-29):** Free / Basic / Professional / Enterprise. No prices. |
| OQ-5 | Confirm which of the seven views are implemented in R1 (proposal: home, work item, assistant, agent run, minimal permissions editor). | UI/UX scope; phase 1/2 plans. | Before `phase_1_foundation_plan.md` |
| OQ-6 | Confirm the assistant modes enabled in R1 (proposal: six; Automate deferred to R3). | Runtime scope. | Before `phase_2_development_loop_plan.md` |

## 13. Provisional assumptions

| ID | Assumption | Label | Validation point |
|---|---|---|---|
| AS-1 | Release 1 = intake phases 07 + 08 only. | `verified` (I-06; manifest §3) | — |
| AS-2 | Founder is the only R1 user; Project Lead and Operator seats are specified now, activated R2. | `provisional` | R2 plan |
| AS-3 | Prices, allowance quantities, seat counts, rates and model bands are structure-only in R1–R3. | `verified` (I-05 commercial gate) | Phase 11 gate |
| AS-4 | Release bucket rule = first release with a `working`/`configured` target row (§4.2). | `proposal` | PL reconciliation T0-12 |
| AS-5 | R3/R4 split of business domains and R2–R4 numbering (§4.1, §4.3). | `accepted` (D-27, D-28) | — |
| AS-6 | Tier labels Free/Basic/Professional/Enterprise. | `accepted` (D-29); no prices | CA-10 |
| AS-7 | Seven-view implementation timing (PRD-A.15). | `proposal` | OQ-5 |
| AS-8 | Registry `capability_id`, `registry_version`, `status_changed_at`, `status_evidence` columns. | `proposal` | SE registry (T0-8) |
| AS-9 | Release-1 acceptance derived from I-06/I-07/I-08/I-13/I-18 because no "Final result" heading exists in the intake. | `verified` (heading enumeration) | PL gate |
| AS-10 | No analytics baseline exists; all R1 metrics are first measurements. | `verified` (`.cursor/TOOLS.md`; blueprint §16) | — |

## 14. Traceability summary

| Intake heading | PRD coverage |
|---|---|
| I-01 | §0.4; process requirements owned by the lead (REQ-01) |
| I-02, I-02B, I-02P | PRD-A.1–A.5, A.17; PRD-B.1; PRD-C.1–C.7; §4; §10 |
| I-03 | PRD-A.10–A.15; PRD-D.1–D.8, D.13; §5.1; NFR-2, NFR-3 |
| I-04 | PRD-A.5–A.9, A.16; PRD-B.2; PRD-D.13; PRD-E.4, E.5, E.7, E.10, E.11; PRD-F.6; NFR-1, NFR-5–7, NFR-10 |
| I-05 | PRD-D.9–D.12; PRD-E.1–E.3, E.6–E.9, E.12; PRD-F.1–F.9; PRD-G.1–G.10; §8.1 |
| I-06 | §4.1; PRD-B.3, B.4, B.9, B.11; PRD-C.5; PRD-G.11; NFR-4, NFR-9; §9 |
| I-07, I-08 | §9 R1-ACC-1..9; PRD-A.13, A.16; PRD-B.*; PRD-E.4 |
| I-09–I-12 | §4 buckets R2–R4; PRD-A.5, A.9, A.11, A.12; PRD-D.1–D.3, D.8; PRD-E.9; PRD-F.7, F.8; PRD-G.12 |
| I-13–I-18 | §9 R1-ACC-10..15; PRD-C.3; PRD-D.5, D.6, D.12; PRD-E.7, E.8; NFR-2, NFR-9 |
