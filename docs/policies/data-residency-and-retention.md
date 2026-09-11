---
document: policy
title: Data Residency and Retention
status: proposed
revision: 1
created: 2026-09-10
updated: 2026-09-10
owner_role: security-engineer-subagent
task_id: 20260910-engine-labs-company-os
sources:
  - docs/product.md (PRD-F.1, F.4, F.5, F.6, PRD-G.7, PRD-G.11, §10)
  - docs/architecture.md (§4 entity table; §6 data-destination map; §8 DBOS; §10 Compose; §11 backup)
  - docs/plans/phase_0_foundations_plan.md (§16 environment-variable registry)
  - docs/Company_Agent_System_Blueprint.md Phases 13–18 (L358–412)
  - docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/handoff.md (EV-SEC-06; F-SEC-07, F-SEC-14, F-SEC-16; GM-1…GM-12)
---

# Data Residency and Retention

Drafted read-only by `security-engineer-subagent` (T0-9); materialized by the orchestrating lead. Status `proposed` until adopted by decision record.

## 1. Purpose

Classify data handled by a deployment, fix where each class may reside, set retention defaults and backup requirements, and constrain usage measurement so that Growth and Engineering share one set of rules.

## 2. Scope

All data created or processed by the desktop, API, DBOS, worker, Hermes, Supabase services, backups, CI and any external destination. Applies from release 1.

## 3. Definitions

- Classification levels: C0 public (marketing content); C1 internal (configuration without secrets, schema); C2 confidential (company records, conversations, memory items, files, audit events, usage events, DBOS workflow state); C3 restricted (credentials, tokens, private keys, backup encryption keys, JWT secrets, recovery codes). A personal-data flag applies orthogonally to any record containing information about an identifiable person.
- Residency: the set of physical locations and providers where a class may be stored or processed.
- Tenant: one customer organisation on one deployment (architecture §10: one Droplet per customer).
- Retention default: the maximum age before automatic deletion or aggregation absent a legal hold.

## 4. Normative requirements

### 4.1 Classification

- DRR-01. Every entity in `docs/architecture.md` §4 MUST carry a classification and personal-data flag in the schema documentation. Default: C2 with personal-data flag true for conversations, memory items, notifications and audit events.
- DRR-02. C3 data MUST never be stored in the tenant database, memory store, logs, prompts, SSE events, DBOS workflow state, usage events or backups other than the encrypted backup key holder's own custody. Connector credentials in release 2 MUST be stored as references to a secret store decided by decision record before release 2 (F-SEC-09).
- DRR-03. C2 data MUST NOT appear in logs beyond identifiers; log lines MUST be scrubbed of content fields by construction.

### 4.2 Residency

- DRR-04. Each row of architecture §6 MUST state: destination, classes permitted, provider, region, controller (customer or Engine Labs), retention, erasure path. Release-1 destinations: tenant Postgres and Storage (C2, customer region); Supabase Auth (C2 identities); Hermes gateway state on the worker volume (C2 transcripts, stored responses, runtime memory); model providers (C2 content in flight only); GitHub (code, C2); off-VPS backup target (`BACKUP_TARGET_URL`, encrypted C2); Engine Labs licensing service (R4, C1 licence state only); optional telemetry (`SENTRY_DSN`, scrubbed); desktop cache (C2 preferences and last-known view state); GitHub Actions (C3 CI secrets, Engine Labs controller); Auth email provider (C2 identities); update artefact host (C0/C1 signed binaries) (F-SEC-07 additions).
- DRR-05. The tenant database, Storage and Hermes state MUST reside on the customer's deployment in the customer-selected region. No cross-tenant storage.
- DRR-06. Before any real customer content is sent to a model provider, a decision record MUST record the provider's data-use terms (training, retention, region); fixtures MUST be used until then (PRD-E.12; T-36). Marketing MUST NOT claim provider guarantees beyond the recorded terms.
- DRR-07. Hermes long-term memory providers external to the deployment (Honcho-class) MUST be disabled in release 1 or replaced by a local provider on the worker volume (F-SEC-07, MEM-17).
- DRR-08. Telemetry MUST be off by default, opt-in per organisation, scrubbed of C2 content and direct identifiers before transmission, and evidenced by payload inspection (R1-ACC-14).

### 4.3 Retention defaults

- DRR-09. Defaults (PRD-F.4; architecture §4): conversations 365 days; application and access logs 30 days; notifications 90 days; backups 30 days; approved knowledge until superseded; inferred memory 180 days unless promoted; usage events 365 days then aggregated; DBOS workflow state pruned 30 days after workflow completion; Hermes stored responses and sessions pruned 30 days after run close; audit events retained for the life of the organisation then anonymised on erasure.
- DRR-10. Retention MUST be configurable per organisation within [7 days, default] for conversations and logs; extensions beyond default require a decision record and legal-hold flag.
- DRR-11. The retention job MUST support dry-run, MUST honour legal-hold flags, MUST write an audit event per deletion batch and MUST report counts to the owner (T-58). Design is a phase-1–2 item (architecture §14).
- DRR-12. Retention MUST cover every destination in DRR-04 including Hermes gateway state, DBOS system tables, Storage objects and desktop cache (F-SEC-14).
- DRR-13. Desktop cache MUST hold only preferences and last-known view state; it MUST be purged on sign-out and on grant-version change (AUTH-14).

### 4.4 Backups

- DRR-14. Nightly `pg_dump` and Storage snapshots MUST be encrypted with a customer-owned key referenced by `BACKUP_ENCRYPTION_KEY_PATH` before leaving the host; the key MUST NOT be stored at `BACKUP_TARGET_URL` or with the backup provider (T-39).
- DRR-15. Backups MUST be stored with a different provider or region from the deployment; retained 30 days; integrity MUST be verified by checksum and signed manifest before restore (T-40). Volume encryption at rest for the worker/Hermes volume MUST be verified for the hosting provider or applied at the application layer (A-4).
- DRR-16. A restore dry run MUST be performed in phase 3 and a full restore drill before release 4 (V15-5); results are evidence.
- DRR-17. Backup jobs MUST run with a dedicated service identity holding only the credentials named `BACKUP_TARGET_URL` and `BACKUP_ENCRYPTION_KEY_PATH` plus read access to the database; never `SUPABASE_SERVICE_ROLE_KEY` beyond what `pg_dump` requires.

### 4.5 Environment and secrets residency

- DRR-18. Secrets are named in phase plan §16 and MUST reside only as environment variables or file mounts on the deployment host, in the CI protected environment (signing and hosting tokens), or in the desktop OS keychain (session tokens). `.env` files MUST be git-ignored; `.env.example` files MUST contain names only. `DBOS_CONDUCTOR_KEY` MUST NOT be used.
- DRR-19. Per-service environment allowlists MUST be declared in Compose and asserted by test (T-24): worker receives `HERMES_API_BASE_URL`, `HERMES_API_SERVER_KEY`, `MODEL_PROVIDER_API_KEY`, `HERMES_VERSION_PIN` only.

### 4.6 Usage measurement and consent (binding on Growth)

- DRR-20. UsageEvent MUST contain only: tenant id, pseudonymous member id, run id, mode, model band, token counts, tool-call counts by class, duration, estimated cost band, outcome code, timestamp. Content fields MUST be excluded by schema (GM-1).
- DRR-21. Provider usage MUST be de-duplicated by provider event id; missing data MUST be reported as missing, never interpolated (GM-2; PRD-G.11).
- DRR-22. No third-party analytics SDK, pixel, session replay or fingerprinting in release 1 (GM-4).
- DRR-23. No cross-tenant learning, benchmarking or aggregation without an adopted decision record (GM-5).
- DRR-24. Preference learning stays in the tenant and MUST NOT be used for segmentation or marketing (GM-6).
- DRR-25. Marketing and lifecycle communications MUST use consented first-party channels and identifiers only; connected-source contacts MUST NOT be harvested (GM-7, GM-10).
- DRR-26. Any new measurement destination or event type MUST be added to DRR-04 and reviewed by Security before implementation (GM-11, GM-12).
- DRR-27. Experiments MUST NOT vary authorization, approval, retention, safety or pricing-disclosure behaviour (GM-9).

## 5. Verification

- Phase 1: classification column in schema docs (DRR-01); log scrubbing test (DRR-03); architecture §6 revision (DRR-04); telemetry payload inspection when enabled (DRR-08); Compose env allowlist assertion (DRR-19); UsageEvent schema review (DRR-20).
- Phase 2: retention job dry run with counts (DRR-11, DRR-12); Hermes memory provider configuration check (DRR-07).
- Phase 3: backup encryption, separation and restore dry run (DRR-14…DRR-16).
- Release 4: full restore drill.

## 6. Exceptions

Owner-approved decision record with compensating control and expiry ≤ 90 days. No exception may store C3 data in C2 locations (DRR-02) or send C2 content to a provider without recorded terms (DRR-06).

## 7. Related decisions and requirements

D-01; D-04 decisions 8, 10, 12; PRD-F.1, F.4–F.6; PRD-G.7, G.11; NFR privacy items; R1-ACC-14; V15-4, V15-5; findings F-SEC-07, F-SEC-09, F-SEC-14, F-SEC-16.
