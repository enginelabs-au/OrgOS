---
schema_version: 1
task_id: 20260913-d25-repass
role_id: security-engineer-subagent
revision: 1
---

# Evidence — D-25 re-pass

Environment: local repo read, HEAD `63a3e3a`. No secrets. Tests cited, not treated as a lift.

| ID | Claim | Cite | State |
|---|---|---|---|
| EV-01 | Only `start_run` → `accepted` is `memory_read` | `services/worker/tests/test_runtime.py` | VERIFIED |
| EV-02 | Hermes POST is unscoped to `tool=` | `interfaces.py` `start_run`; `hermes_client.py`; `toolsets.yaml` | VERIFIED |
| EV-03 | Subscribe intercepts after SSE | `interfaces.py` `subscribe` | VERIFIED |
| EV-04 | Job consumer has no `persist_approval` | `services/worker/jobs.py` | VERIFIED |
| EV-05 | API `POST /runs` never calls adapter `start_run` | `services/api/app/main.py` | VERIFIED |
| EV-06 | Intercept units are not a lift | `test_interception.py` | VERIFIED |
| EV-07 | Catalog/artefact hashes still match yaml | `toolsets.yaml` | VERIFIED |
| EV-08 | Papership Gmail/Slack send is not Hermes `accepted` | `main.py` `send_via_provider` | VERIFIED |
