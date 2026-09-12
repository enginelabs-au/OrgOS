# Phase 4 — remaining owner actions

Agent-capable Phase 4 work is closed (G5, 2026-09-12). These items cannot be finished from the repository.

## Already done in-repo

- OQ-G2 notice copy and `oq_g2_recorded` gate (D-23). Founder must still `POST /settings/oq-g2` on the live store.
- Gmail/Slack contract + wizard (D-24). Env names wired: `GMAIL_OAUTH_CLIENT_ID`, `GMAIL_OAUTH_REDIRECT_URL`, `SLACK_CLIENT_ID`.
- Security pass accepted for Phase 4 connectors (D-25). Write/external Hermes stay gated.
- In-repo slug is papership / Papership (D-26).
- OQ-2, OQ-3, OQ-4, OQ-G1 closed (D-27…D-30).
- Worker job consumer + AUTH-12 HTTP path + usage first-baseline `not_captured`.
- People/Inbox off fixtures on the product path.

## Owner-only residuals

| Action | Why agent cannot | Blocking Phase 5 planning? |
|---|---|---|
| Rename GitHub repo `enginelabs-au/OrgOS`, App `orgos-dev`, Vercel project `orgos`, and then set `GITHUB_APP_REPO` to the new name | provider dashboards | no |
| Create Google OAuth client and Slack app; set the three env names on the API host | owner accounts | no |
| Call `POST /settings/oq-g2` on the live store before inviting a second human | live tenant | no for planning; yes for a live second seat |
| Move mailbox credentials off systemd `Environment=` | VPS owner | no |
| Hermes GET `/health` hang on the gateway | Hermes ops | no (HEAD-first probe already used) |
| Apple signing / DigitalOcean / backup restore drill | accounts | no |
| `execute_release` | owner | no |
| Fire live write/external Hermes tools | requires a new Security PASS plus approval | no — do not treat D-25 as that licence |
| Public build-log | D-30 says no until a later publish decision | no |

Do not start Phase 5 until you ask for the next plan. Three execution phase plans remain after Phase 4: Phase 5 (R3 company operations), Phase 6 (R4 commercial delivery), Phase 7 (R4 ecosystem/mobile). Verification phases 13–18 re-run per release and are not extra build phases.
