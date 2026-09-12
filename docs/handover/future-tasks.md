# Future tasks

Parked work that is not current priority. Do not store secret values here.
Do not treat these as live closeout blockers. The daily list is `docs/handover/outstanding-tasks.md`.

| ID | When | Task |
|---|---|---|
| OT-06 | Later, only if a production Compose/VPS store is in use | Encrypted off-VPS backup: set `BACKUP_TARGET_URL` and customer-owned `BACKUP_ENCRYPTION_KEY_PATH`, then restore once onto a disposable target and keep a receipt. A copy on the same Droplet is not disaster recovery. Not needed for today’s Vercel site or the local Mac SQLite store. |
| OT-07 | Optional, ignore unless you want GitHub hygiene | Branch protection on `main`, Dependabot, pin Actions by SHA. Not required for local Papership or Vercel. |
| OT-08 | Later, when you want real charges | Flip `ENGINE_BILLING_CHARGES_ENABLED`. Trial prices are already published (D-35). |
| OT-09 | Later, when you want store listing | Apple Developer / Google Play accounts and store submit. Same family as OT-12. |
| OT-10 | Later, only after Engineering remediates the five D-25 gaps | Live write / external Hermes `accepted`. Two Security passes (2026-09-12 and 2026-09-13) are CONDITIONAL. `lift_authorized: false`. See `docs/workstreams/20260913-d25-repass/security-engineer-subagent/handoff.md`. Do not treat intercept tests as a lift. |
| OT-11 | Later, only if you want WhatsApp/Telegram inside Papership Inbox | Hermes gateway chat is already live (owner 2026-09-13). That is not a Papership Integration. A later Papership connector would show those threads in Inbox and send via approval-then-receipt, using new Papership secrets — do not copy Hermes env. |
| OT-12 | Later, with OT-09 | Signed desktop / store binaries (Apple notarization, Play App Signing). Unsigned Tauri/PWA already run locally. |
| OT-13 | Do not do this | Org-wide erase / real Droplet destroy. Recorded only so nobody treats ERA-15 as a live action. |
| OT-14 | Cosmetic leftover | Today priorities / runs / decisions can still show blueprint demo rows. People, Inbox, Memory, Integrations already use the live API. Not a product or security defect. |

Owner asked 2026-09-13 to park OT-06…OT-14 and stop treating them as current work. Remind later only if asked.
