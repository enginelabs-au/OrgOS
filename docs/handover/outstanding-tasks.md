# Outstanding tasks

Canonical live list. The lead agent updates this file every substantive turn and repeats the **open** rows at the end of the reply, even when the owner did not mention them.

Do not store secret values here. Charges stay off until a later owner flip.

| ID | Status | Owner | Task |
|---|---|---|---|
| OT-01 | done | — | Leftover feature branches are gone from git. This tree has only `main` @ `63a3e3a` and `origin/main`. GitHub has no leftover branches; PRs 1–5 are closed. If Cursor still lists the old names, that is a stale picker / closed-PR label, not a live branch. |
| OT-02 | done | — | OQ-G2 recorded on local API store 2026-09-12T15:20Z (`oq_g2_recorded: true` at `/tmp/papership-api-store.sqlite`). Vercel still cannot hold this flag. |
| OT-03 | done | — | Public Gmail/Slack client IDs and Gmail redirect are set in `~/.config/papership/connectors.env`. Hermes env was not copied. |
| OT-04 | done | — | Gmail/Slack OAuth start, callback, and sealed token exchange shipped. Tests: `services/api/tests/test_oauth.py` 7 passed. Live connect waits on OT-20 secrets. |
| OT-05 | done | — | Hermes user systemd has no `Environment=EMAIL_*`. Live `hermes-gateway.service` only has PATH / VIRTUAL_ENV / HERMES_HOME / HERMES_SUPERVISED_CHILD. Serve already uses `EnvironmentFile`. Values were not printed. |
| OT-06 | later | — | Parked. Off-VPS backup + restore drill is not current work. Logged in `docs/handover/future-tasks.md`. |
| OT-07 | later | — | Parked. Optional GitHub branch protection / Dependabot / pin Actions by SHA. Owner said ignore. |
| OT-08 | later | — | Parked. Flip `ENGINE_BILLING_CHARGES_ENABLED` later. Remind on request. |
| OT-09 | later | — | Parked. Apple / Google store accounts and submit. Remind on request. |
| OT-10 | later | — | Parked. Two Security passes (2026-09-12 and 2026-09-13) are CONDITIONAL. Write/external Hermes `accepted` stays unauthorized. Five architectural gaps remain. See `docs/workstreams/20260913-d25-repass/security-engineer-subagent/handoff.md`. |
| OT-11 | later | — | Parked. Hermes WhatsApp/Telegram chat is already live. Papership Integrations rows stay planned unless you later want Inbox/send-with-approval inside Papership. Do not copy Hermes env. |
| OT-12 | later | — | Parked. Signed desktop / store binaries. Same family as OT-09. Unsigned Tauri/PWA already run. |
| OT-13 | later | — | Parked. Org-wide erase / Droplet destroy is not recommended and is not tracked as live work. |
| OT-14 | later | — | Parked. Today decorative fixture rows are leftover blueprint chrome. Insignificant. |
| OT-15 | done | — | Founder JWT no longer persists in `localStorage`. Session is in-memory + `sessionStorage`; leftover `localStorage` keys are cleared; sign-out wipes the token. Residual: XSS can still read `sessionStorage`. httpOnly cookies need same-origin (Vite is `localhost:5173` → API `127.0.0.1:8000`). |
| OT-16 | done | — | Live Hermes `GET /health` on `127.0.0.1:8642` returned 200 in ~1ms (HEAD 405). Gateway and serve were active. Papership probe stays HEAD-first. |
| OT-17 | done | — | Trial rate card Free / Pro / Max / Enterprise published in Settings → Plan. Charges off. |
| OT-18 | done | — | Desktop Tauri loads current `/papership` web chrome. |
| OT-19 | done | — | `main` pushed as Cursor Agent; production `/papership` READY (`63a3e3a`). |
| OT-20 | done | — | `connectors.env` has Gmail and Slack client IDs, secrets, and redirect URLs. Live `/health` `oauth.gmail` and `oauth.slack` are `ready`. Values were not printed. |
| OT-21 | done | — | Local `/papership` Continue accepts blank or any email/password. There is no real password. Use `http://localhost:5173/papership`, not Vercel, for API-backed work. |
| OT-22 | done | — | Local API CORS now allows `http://localhost:5173` as well as `http://127.0.0.1:5173`. Connect fetch from Vite localhost no longer looks like a dead API. |
| OT-23 | done | — | Local API calls mint `/auth/local-session` when `papership-token` is missing, so Integrations connect no longer fails with missing bearer after a chrome-only sign-in. |
| OT-24 | done | — | Local API no longer segfaults (exit 139) on the overlay burst. SQLite access is serialized; uvicorn uses `--loop asyncio --http h11`. Concurrent `/people` `/teams` `/inbox` `/connections` `/memory` `/strategy` now stay 200. |
| OT-25 | done | — | Local Gmail OAuth completed. `/connections` shows `gmail` `configured`, `enabled`, `has_token`. Send stays approval-then-receipt. Token values were not printed. |
| OT-26 | done | — | Local Slack OAuth completed. `/connections` shows `slack` `configured`, `enabled`, `has_token` after `GET /oauth/slack/callback` 302 at 16:30Z. Send stays approval-then-receipt. Token values were not printed. |
| OT-27 | done | — | Integrations Set up now preselects that row’s provider. Slack Set up no longer starts Gmail. OAuth return opens the Integrations tab. |
| OT-28 | done | — | Local founder JWT is reminted when expired or within 90s of expiry. A 401 retries once so Slack Set up no longer dies with `invalid token: Signature has expired`. |
| OT-29 | done | — | Hermes desktop/droplet inference pinned to OpenRouter. Stale Nous `active_provider` and an exhausted OpenRouter pool flag were cleared. Free OpenRouter fallbacks (`poolside/laguna-xs-2.1:free`, `thinkingmachines/inkling:free`) stay. |
| OT-30 | done | — | Hermes status chip “Gateway · inference unavailable” was a false negative: `setup.runtime_check` saw OpenRouter configured but the serve process had no router key. Key is now in the serve EnvironmentFile; serve restarted; runtime resolve is usable. |
| OT-31 | done | — | OpenRouter Settings picker now lists the live tool-capable catalog (377). Cap is 999 / uncapped, not None. |
| OT-32 | done | — | Hermes Desktop chat model selector no longer hangs on the live 377-id OpenRouter catalog. Featured is the curated shortlist (~48) plus the current pick (`openai/gpt-5.6-luna-pro` in featured). Capability lookups skip the long tail. Serve restarted; reconnect Desktop once. |

## Standing rules for this list

- Never drop an `open` / `in_progress` / `held` row because a later message ignored it.
- Move a row to `done` only with evidence.
- Owner-requested stop-tracking moves a row to `later` (`docs/handover/future-tasks.md`) and is not repeated every turn.
- `later` is parked future work and is not repeated every turn.
