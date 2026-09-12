---
document: policy
title: Erasure and Offboarding
status: proposed
revision: 1
created: 2026-09-10
updated: 2026-09-10
owner_role: security-engineer-subagent
task_id: 20260910-engine-labs-company-os
sources:
  - docs/product.md (PRD-F.7 offboarding, PRD-F.8 erasure, PRD-F.9 export, PRD-D.8)
  - docs/architecture.md (§4 deletion semantics; §6 destinations; §11 backup)
  - Hermes API documentation capture (sessions API)
  - docs/blueprints/company_agent_system_blueprint.md Phase 16–17 (L391–405)
  - docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/handoff.md (ERA references; F-SEC-06, F-SEC-14; T-42)
---

# Erasure and Offboarding

Drafted read-only by `security-engineer-subagent` (T0-9); materialized by the orchestrating lead. Status `proposed` until adopted by decision record.

## 1. Purpose

Define how members, agents, connectors and whole organisations are removed, what is deleted, anonymised or retained, and how the customer receives verifiable receipts.

## 2. Scope

Member offboarding, agent retirement, connector removal, organisation erasure, data export preceding erasure, and the handling of backups, Hermes state, provider-side data and desktop caches.

## 3. Definitions

- Offboarding: removal of a principal's access and delegated authority while the organisation continues.
- Erasure: irreversible deletion of an organisation's or a member's data across all destinations, subject to retention of anonymised audit and aggregated usage records.
- Receipt: a signed record listing what was deleted, anonymised, retained (with reason) and pending (with expiry).
- Pending copy: data that persists temporarily after erasure (encrypted backups within retention).

## 4. Normative requirements

### 4.1 Member offboarding

- ERA-01. Offboarding MUST revoke all grants, active sessions, refresh tokens and delegated grants of the member within 60 seconds and MUST terminate or reassign runs the member sponsors (AUTH-23; PRD-D.12).
- ERA-02. Grants the member delegated MUST be revoked from delegates unless re-granted by a remaining authority (AUTH-03).
- ERA-03. Records authored by the member MUST remain organisation property; the author reference MUST persist as an identifier until organisation erasure. Personal preference memory MUST be deleted at offboarding.
- ERA-04. Owner-seat handover MUST follow AUTH-21; an organisation MUST always retain at least one owner or a recorded recovery path.
- ERA-05. Offboarding MUST produce an audit event and a receipt to the remaining owner.

### 4.2 Agent and connector retirement

- ERA-06. Retiring an agent MUST cancel or close its runs per PRD-E lifecycle (close ≠ cancel), release budget reservations and revoke its principal; its runs, receipts and audit events MUST remain.
- ERA-07. Removing a connector MUST revoke or delete the source credential reference, invalidate source-permission snapshots for that source (MEM-09 fails closed) and record which memory items became unreadable.

### 4.3 Organisation erasure

- ERA-08. Erasure MUST cover every destination in DRR-04: tenant Postgres (including DBOS system tables), Storage objects, Supabase Auth identities, Hermes sessions (deleted through the Hermes sessions API for the tenant profile) and the Hermes profile volume paths for transcripts, stored responses and runtime memory, desktop caches (remote sign-out and purge on next launch), usage events (aggregated within 30 days), and optional telemetry (deletion request to the telemetry provider recorded) (F-SEC-14).
- ERA-09. Erasure MUST require three confirmations from a human principal holding `data.erase` with reauthentication ≤ 5 minutes: organisation name typed, explicit acknowledgement of pending backup copies, and a second owner's approval where one exists (PRD-F.8; AUTH-11, AUTH-16).
- ERA-10. Export MUST be offered before erasure and MUST complete or be declined explicitly (PRD-F.9). Export bundles MUST be encrypted to a customer-provided key or delivered over an authenticated short-lived link ≤ 24 hours.
- ERA-11. Audit events MUST be anonymised (actor identifiers replaced by irreversible pseudonyms, content fields removed) and retained; usage events MUST be aggregated and individual rows deleted (architecture §4).
- ERA-12. The receipt MUST list: deleted destinations with counts, anonymised sets, retained sets with legal basis, pending backup copies with expiry dates (≤ 30 days), provider-side deletion requests with request identifiers, and the policy version. Receipts MUST be signed by the API service identity and delivered to the owner (T-42).
- ERA-13. Backups created before erasure MUST expire on schedule and MUST NOT be restored except to fulfil a documented legal obligation; any restore of a pre-erasure backup MUST trigger re-erasure and a new receipt.
- ERA-14. Usage events for the erased organisation MUST be excluded from any export and aggregated within 30 days (GM-3).
- ERA-15. Deployment decommissioning MUST destroy the Droplet and attached volumes after the receipt is issued and MUST record provider deletion confirmation. Hosting-provider deletion behaviour for volumes MUST be verified (A-4).

### 4.4 Provider and third-party data

- ERA-16. For each external destination with a deletion API (model providers where offered, telemetry, GitHub App installation), erasure MUST issue the request and record the identifier; where no API exists, the receipt MUST state the provider's documented retention period from the DRR-06 record.
- ERA-17. Engine Labs licensing state (release 4) MUST retain only licence identifiers and dates after erasure.

### 4.5 Timing and evidence

- ERA-18. Online erasure steps MUST complete within 24 hours; backup expiry within 30 days; the receipt MUST be issued when online steps complete and updated when the last pending copy expires.
- ERA-19. Erasure MUST be executed by a DBOS workflow with persisted steps so that partial failure resumes rather than repeats destructive steps; each step MUST be idempotent.
- ERA-20. Erasure MUST be tested against a fixture tenant in phase 2 with verification that Hermes session lookups return 404, Storage buckets are empty, Auth identities are gone and audit rows are anonymised.

### 4.6 Prohibitions

- ERA-21. No agent principal MAY initiate offboarding or erasure; these are human actions with `org.admin` or `data.erase` grants (AUTH-08, AUTH-09).
- ERA-22. Erasure MUST NOT be simulated in the UI (AUTH-28).
- ERA-23. Erasure and offboarding MUST NOT be subject to growth experiments or retention-flow dark patterns; the flow MUST be completable without contacting Engine Labs.
- ERA-24. Support access granted during offboarding MUST be time-boxed and logged (AUTH-21).

## 5. Verification

- Phase 1: revocation latency and delegation tests (ERA-01, ERA-02); grant checks (ERA-21).
- Phase 2: fixture-tenant erasure test (ERA-08, ERA-20); receipt format review (ERA-12); workflow resumption test (ERA-19).
- Phase 3: backup expiry and pre-erasure restore procedure (ERA-13).
- Release 4: decommissioning drill (ERA-15).

## 6. Exceptions

Legal-hold flag set by an owner with a decision record suspends deletion for named record sets only; the receipt MUST disclose the hold. No exception may permit agent-initiated erasure or unlisted retention.

## 7. Related decisions and requirements

PRD-D.8, D.12; PRD-E lifecycle (close vs cancel); PRD-F.7–F.9; NFR privacy items; findings F-SEC-06, F-SEC-14; threats T-42, T-58.
