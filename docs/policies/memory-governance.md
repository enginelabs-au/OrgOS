---
document: policy
title: Memory Governance
status: proposed
revision: 1
created: 2026-09-10
updated: 2026-09-10
owner_role: security-engineer-subagent
task_id: 20260910-engine-labs-company-os
sources:
  - docs/product.md (PRD-F.1–F.3, PRD-E.12, PRD-D.5)
  - docs/architecture.md (§4 MemoryItem; §5 TB-10; §6 Hermes gateway state; §7 adapter contract)
  - docs/capabilities.md (§5 Hermes inventory; memory.read/memory.write grants)
  - Hermes API documentation capture (X-Hermes-Session-Key; sessions API; stored responses)
  - docs/blueprints/company_agent_system_blueprint.md Phase 13–15 (L358–390)
  - docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/handoff.md (TB-13 T-53…T-58; F-SEC-07, F-SEC-13, F-SEC-14)
---

# Memory Governance

Drafted read-only by `security-engineer-subagent` (T0-9); materialized by the orchestrating lead. Status `proposed` until adopted by decision record.

## 1. Purpose

Govern what agents and the system may remember, how memory is classified, attributed, retrieved and forgotten, and how Hermes runtime memory is scoped so that memory never widens authority or leaks across principals or tenants.

## 2. Scope

Engine Labs memory items (six kinds in PRD-F.1), derived summaries and embeddings, retrieval services, Hermes session state and runtime memory files, DBOS workflow state carrying content, and desktop caches. Applies from release 1.

## 3. Definitions

- Memory item: a stored unit of one of six kinds (PRD-F.1) with class `source`, `approved` or `inferred`.
- Provenance: the seven fields in PRD-F.2 (origin, author or agent, run id, source reference, source permission snapshot, created at, policy version).
- Source permission snapshot: the permission set on the origin record at capture time.
- Session key: the value sent as `X-Hermes-Session-Key` to scope Hermes long-term memory.

## 4. Normative requirements

### 4.1 Classification and provenance

- MEM-01. Every memory item MUST carry kind, class and all seven provenance fields; writes lacking any field MUST be refused.
- MEM-02. Class `source` MUST be an immutable reference to an existing record and MUST inherit that record's permissions dynamically.
- MEM-03. Class `approved` MUST record the approving human principal and approval time; approved items are the only class eligible for default retrieval in production runs.
- MEM-04. Class `inferred` MUST be retrievable only when the run mode permits inferred memory and the sponsor holds `memory.read`; inferred items expire per DRR-09.
- MEM-05. Promotion `inferred → approved` MUST require review by a human principal holding `memory.write` in scope; no automatic promotion (T-54).
- MEM-06. Content originating from untrusted inputs (tool output, fetched web content, external messages, model output) MUST be marked untrusted in provenance and MUST NOT be promoted without a human reading the content.

### 4.2 Retrieval and authority

- MEM-07. Memory MUST NOT widen authority: retrieval results MUST be filtered by the requesting principal's current effective grants (AUTH-07) at query time, not at write time (PRD-D.5).
- MEM-08. Derived summaries and embeddings MUST inherit the most restrictive permission of all sources; if any source becomes unavailable to a principal, the derivative MUST be excluded for that principal (T-53).
- MEM-09. Source-permission snapshots MUST be re-validated against current source permissions before retrieval for class `source`; stale snapshots MUST fail closed.
- MEM-10. Retrieval MUST be logged as an audit event with principal, run id, item ids and policy version.
- MEM-11. Search and inspection (PRD-F operation R1 search/inspect) MUST respect AUTH-17: no counts or existence leakage.

### 4.3 Prohibited content

- MEM-12. Credentials, tokens, keys, recovery codes and secret-shaped strings MUST never be stored in memory; a credential-shaped scan MUST run before every write and refuse matches with an audit event (T-55; architecture §4).
- MEM-13. Personal data about external individuals MUST NOT be stored as inferred memory; only source references to records the organisation lawfully holds.
- MEM-14. Prompts and SSE payloads MUST NOT contain secrets; the adapter MUST apply Engine Labs redaction before persisting any event text and MUST NOT rely on Hermes forced redaction (T-21).

### 4.4 Tenancy and cross-principal isolation

- MEM-15. No memory, embedding or summary MAY be shared across tenants; no cross-tenant learning (DRR-23).
- MEM-16. Within a tenant, memory scope MUST be organisation, project or principal; principal-scoped preference memory MUST be readable only by that principal and by agents acting on that principal's behalf.
- MEM-17. Hermes `X-Hermes-Session-Key` MUST be derived deterministically from (tenant id, sponsor principal id, purpose class) with a keyed hash so that runs for different principals or purposes never share Hermes long-term memory; the key MUST be ≤ 256 characters with no control characters. External Hermes memory providers MUST be disabled or local in release 1 (DRR-07; T-56).
- MEM-18. Hermes session transcripts, stored responses (LRU 100) and runtime memory files are C2 data on the worker volume; they MUST be included in retention (DRR-12) and erasure (ERA-08) and MUST NOT be treated as the record of truth — the Engine Labs Job and Conversation records are canonical (D-04).

### 4.5 Measurement and learning

- MEM-19. Preference and behavioural learning MUST stay within the tenant and MUST NOT feed marketing segmentation, growth experiments or cross-customer features (DRR-24).
- MEM-20. Memory statistics exposed for measurement MUST be counts by kind and class only, never content.

### 4.6 Injection posture

- MEM-21. Policy and permissions MUST live outside prompts (PRD-E.6); memory content MUST be presented to models as data, labelled untrusted where MEM-06 applies, and MUST NOT be able to alter tool allowlists, budgets or approvals (F-SEC-13).
- MEM-22. A prompt-injection fixture suite MUST include memory-borne instructions attempting to invoke side-effecting tools or to promote inferred memory; all MUST be refused by policy (SP-5).

## 5. Verification

- Phase 1: schema constraints (MEM-01…MEM-04); two-principal retrieval tests (MEM-07…MEM-11); credential scan test (MEM-12); log/redaction test (MEM-14).
- Phase 2: session-key derivation test and Hermes memory provider configuration check (MEM-17, MEM-18); injection fixtures (MEM-21, MEM-22).
- Each release: audit sampling of promotions (MEM-05).

## 6. Exceptions

Owner-approved decision record with expiry ≤ 90 days. No exception may permit credentials in memory (MEM-12), cross-tenant sharing (MEM-15) or automatic promotion (MEM-05).

## 7. Related decisions and requirements

D-04 decisions 3, 8, 12; PRD-F.1–F.3; PRD-E.6, E.12; PRD-D.5, D.12; R1-ACC-4; findings F-SEC-07, F-SEC-13, F-SEC-14; threats T-53…T-58.
