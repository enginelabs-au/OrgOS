---
document: owner-handoff
task_id: 20260910-engine-labs-company-os
release: R1
gate: G4
status: owner_approved
created: 2026-09-11
updated: 2026-09-11
---

# Owner handoff — Papership R1 / Phase 3

Product is **Papership**. Engine Labs is the company. Do not treat this as approval to edit `www.enginelabs.com.au`.

## V18-5 decision

**APPROVE**

Recorded 2026-09-11 from the owner’s instruction to land live tools and a real PR, then approve and proceed to the Phase 4 plan. Not inferred from a role verdict.

## What this APPROVE accepts

- G3 PASS-with-residuals plus the live close-out in this turn.
- Live Hermes `accepted` for **catalogued read** tools only (`tool=` + intercept-before-POST). Security live-tools gate: **CONDITIONAL** (`phase-3-live-tools-handoff.md`).
- Live GitHub PR #1 via Papership App `open_pull` (`dry_run: false`): https://github.com/enginelabs-au/OrgOS/pull/1
- Write / external / destructive tools still need receipt / approval-then-receipt.
- Usage emit on after this turn (identifier/enum payloads only; no prices).
- Phase 4 plan `docs/plans/phase_4_collaboration_connections_plan.md` may start T4-0/T4-1.

## What this APPROVE does not authorize

- `accepted` for write/external/destructive Hermes tools.
- `execute_release` or production deploy.
- Second seats until OQ-G2 (T4-2).
- Extra live connectors until T4-5 + Security PASS.
- Prices, marketing-site edits, wake-word vendor (D-18).
- A second Hermes gateway.

## Residual limitations

| Residual | Owner action |
|---|---|
| Hermes GET `/health` hang | optional |
| Mailbox credentials on gateway `Environment=` | recommended EnvironmentFile move |
| Worker still idles (no job consumer / subscribe) | Phase 4 if assistant turns go live |
| AUTH-12 HTTP route not used for PR #1 (library `open_pull`) | optional: mint founder JWT on the API |
| Docker Compose bring-up + backup target | V15-5 |
| Apple signing / DigitalOcean | packaging |

## Rollback

Set `interception_verified: false` and disable toolsets; worker refuse-start. Close or revert PR #1 if the receipt branch should not stay open.

## Next

Phase 4 T4-0 carry is satisfied by this close-out. Continue T4-1 seat templates.
