# Phase 3 owner actions

Human-only leftovers after Phase 3 implementation (2026-09-11). No secret values.

| Action | Blocking? |
|---|---|
| Confirm you want live Hermes **tool** runs (`accepted`) after Security PASS — Papership `queued` only means the API listener is there | yes for tools |
| Keep `HERMES_API_SERVER_KEY` on the worker/VPS only; never put it on the API or desktop | always |
| Move mailbox credentials off the gateway unit `Environment=` line (they appear in process listings) | recommended |
| Live GitHub PR: `dry_run: false` + reauth + non-empty installation permissions | yes for publication |
| Record V18-5 `APPROVE` / `REQUEST_CHANGES` / `DO_NOT_PROCEED` on the owner handoff | yes for R1 release |
| Accept or keep F-G1 usage emit off as a product decision | no |
| Docker Compose live + backup target for V15-5 | no for code |
| Apple signing / DigitalOcean production | no |
| Wake-word vendor | no |
| Hermes `GET /health` hangs — readiness is not usable; HEAD works | no |
