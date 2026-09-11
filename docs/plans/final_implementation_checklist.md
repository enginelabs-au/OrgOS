---
document: final_implementation_checklist
status: open
created: 2026-09-11
updated: 2026-09-11
release: R1
---

# Final Implementation Checklist

## 1. Completion declaration

- [x] All planned agent-executable Phase 3 work is implemented.
- [x] Available automated validation passes (worker 32, API 52).
- [x] Unverified results are listed below.
- [x] Owner V18-5 decision recorded (`APPROVE`).

## 2. Outstanding defects or unverified items

| Item | Impact | Evidence/status | Required action | Owner |
|---|---|---|---|---|
| Live Hermes `accepted` | tools | CONDITIONAL; catalogued **read** `tool=` only | keep write/external gated | owner + Security |
| R1-ACC-6 live GitHub open | publication | PR #1 opened | `execute_release` still owner | owner |
| Usage first-baseline | measurement | emit on (identifier/enum) | no prices | owner |
| Hermes GET `/health` hang | readiness | inventory r2 | Optional Hermes fix | owner/ops |
| Gateway mailbox `Environment=` | secret hygiene | process listings | Move credentials | owner |
| Desktop signed update / axe gallery | V16-1/4 | PARTIAL | Apple signing; a11y lab | owner |
| Compose live + backup restore | V15-5 / V17-4 | config OK, not brought up | Backup target + drill | owner |
| Web `/cc-org-dash` still uses `data.jsx` | V16-3 | fixture shell | R2 People/Inbox off fixtures | later phase |
| Browser click hook-blocked | V13-4/V16 | Cursor MCP | Owner walk Settings/Work | owner |

## 3. Role and stage-gate closure

| Role ID | Required or skipped | Final verdict or skip reason | Handoff/evidence |
|---|---|---|---|
| software-engineer-subagent | required | CONDITIONAL | `.../phase-3-t3-handoff.md` r2 |
| security-engineer-subagent | required | CONDITIONAL (catalogued-read `accepted`) | `.../phase-3-live-tools-handoff.md` |
| ui-ux-developer-subagent | required | CONDITIONAL | `.../phase-3-t3-6-handoff.md` r2 |
| product-manager-subagent | required | CONDITIONAL (ACC-6…9 PARTIAL) | `.../phase-3-t3-8-handoff.md` r2 |
| growth-marketing-subagent | required | CONDITIONAL (`not_captured`) | `.../phase-3-t3-7-handoff.md` r2 |
| project-lead-subagent | required | G3 close with residuals | `.../phase-3-g3-handoff.md` |

- [x] No `BLOCKED` verdicts.
- [x] Owner handoff links residuals: `docs/workstreams/20260910-engine-labs-company-os/delivery/owner-handoff.md`.

## 4. Environment variables and secrets still required

Never include secret values.

| Variable name | Provider/source | Destination/environment | Why required | Value supplied? | Validation after supply |
|---|---|---|---|---|---|
| `HERMES_API_BASE_URL` | local tunnel / VPS | API + worker | Probe + later runs | yes (local `http://127.0.0.1:8642`) | `/health` hermes reachable |
| `HERMES_VERSION_PIN` | pin | API + worker | Pin | yes `v0.21.1` | `/health` hermes_pin |
| `HERMES_API_SERVER_KEY` | Hermes gateway | **worker/VPS only** | `/v1/*` auth | yes on VPS; never on API/desktop | capabilities without key returns auth error |
| `GITHUB_APP_ID` | GitHub App | API | Bound repo | yes (local paths file) | `/health` github reachable |
| `GITHUB_APP_INSTALLATION_ID` | GitHub App | API | Bound repo | yes | same |
| `GITHUB_APP_PRIVATE_KEY_PATH` | GitHub App | API | Bound repo | yes (path only) | same |
| `ENGINE_USAGE_EMIT` | product flag | API | F-G1 | live `1` after APPROVE | `/health` usage_emit true |
| `SUPABASE_JWT_SECRET` | Auth | API | JWT | local/test | API tests |
| `ENGINE_JWT_ISSUER` / `ENGINE_JWT_AUDIENCE` | Auth | API | JWT | local defaults | API tests |

## 5. Human-only account, permission, billing, or legal actions

| Action | Platform | Reason agent cannot perform | Exact completion evidence |
|---|---|---|---|
| V18-5 recorded `APPROVE` | this handoff | done 2026-09-11 | `delivery/owner-handoff.md` |
| Confirm live Hermes tools | Hermes + Security | done for catalogued read | Security CONDITIONAL |
| Live GitHub open | GitHub App | done | https://github.com/enginelabs-au/OrgOS/pull/1 |
| F-G1 accept emit | product | done (enum only) | `/health` usage_emit |
| Apple signing | Apple | account | signed build |
| DigitalOcean / DNS | DO | account | droplet + health |
| OQ-G2 second-seat notice | legal/product | owner decision | Phase 4 |

## 6. Production integrations and dashboard actions

### Deployment

Local API + tunnel only. Production Compose/VPS deploy is owner/CI.

### DNS and domains

None in this phase. Do not change `enginelabs.com.au`.

### OAuth and identity providers

GitHub App already bound (dry-run default). Extra OAuth (Gmail) is Phase 4.

### Database and storage

Local sqlite store. Hosted Postgres/Supabase remain owner.

### APIs, webhooks, email, payments, analytics, and other providers

No webhooks in R1. No payments. Usage emit off. Hermes gateway mailbox credentials should leave systemd `Environment=`.

## 7. Final smoke tests after manual actions

- [x] Application health (`GET /health` ok, hermes+github reachable, emit false)
- [x] Authorization tests (API 47)
- [x] Data persistence (sqlite jobs/work-items)
- [ ] External live GitHub open
- [ ] Live Hermes tool run
- [ ] Signed desktop update
- [ ] Owner security/privacy/a11y acceptance walk

## 8. Owner decision

- [ ] Owner approved the handoff.
- [ ] Conditions or requested remediation are recorded in the active workstream.

## 9. Final evidence

- `docs/plans/phase_3_release_verification_plan.md`
- `docs/verification.md` revision 3
- Worker `uv run pytest -q` → 30 passed
- API `uv run pytest -q` → 47 passed
- Live `GET http://127.0.0.1:8000/health`
- `docs/workstreams/20260910-engine-labs-company-os/delivery/owner-handoff.md`
- Phase 4 plan exists but is not implemented (D-19)
