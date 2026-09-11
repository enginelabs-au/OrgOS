---
schema_version: 1
task_id: 20260910-engine-labs-company-os
role_id: security-engineer-subagent
status: complete
revision: 1
verdict: CONDITIONAL
started_at: 2026-09-11T11:34:00Z
completed_at: 2026-09-11T11:40:00Z
downstream_role: software-engineer-subagent
risk_tier: 3
---

# Security Engineer handoff — phase 2 T2-1 re-review

## Verdict

**CONDITIONAL.** D-16 (restricted toolsets) is an allowed D-04 item 9 choice. AUTH-25 is **not** cleared for enablement.

- T2-2 `start_run` **must stay refuse-closed**.
- `interception_verified` **must stay false**.
- No side-effecting Hermes toolset may be enabled.
- F-SEC-01 enablement clause remains **OPEN**.

Not PASS (SP-2 unproven; several SPs partial). Not BLOCKED (fail-closed holds; no high/critical exploitable defect while runs stay closed).

## SP-1…SP-7

| ID | Security | Note |
|---|---|---|
| SP-1 | PARTIAL | Live 302; no tool JSON; unknown names were fail-open |
| SP-2 | NOT PROVEN | No API server; do not enable tools to prove it |
| SP-3 | PARTIAL | Persist-before-forward unit; never-forward is a mock |
| SP-4 | PARTIAL | Yaml + library refuse mapped names; not Hermes-server-side |
| SP-5 | PARTIAL | Prompt ignored in-process; not a live injection run |
| SP-6 | PARTIAL | Unit deny only; no Compose |
| SP-7 | PARTIAL | Hashes match; flag false; no image digest |

## Binding conditions for T2-2

1. `start_run` / `subscribe` / `stop` / `forward_approval` keep raising.
2. Artefact path/hash stay empty; flag stays false.
3. Do not send customer content or `HERMES_API_SERVER_KEY` from Papership.
4. Before any later run or flag flip: close F-T21-SEC-01 and F-T21-SEC-02; live API server or Hermes-side disable; live SP-6; digest; new Security PASS.

## Findings (none high/critical now)

F-T21-SEC-01 unknown tools fail-open (medium) · F-T21-SEC-02 hooks unwired (medium) · F-T21-SEC-03 egress unit-only (medium) · F-T21-SEC-04 registry not `unavailable` (low) · F-T21-SEC-05 no digest (low) · F-T21-SEC-06 VPS serve UI outside Papership policy (medium) · F-T21-SEC-07 YAML string truthiness (low) · F-T21-SEC-08/09 mocks (low).

If a toolset is enabled or the flag is set true without a new Security PASS, this verdict **reverts to BLOCKED**.
