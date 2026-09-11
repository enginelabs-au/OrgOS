# Phase 2 — remaining owner actions

## Already done

- D-09…D-14, Cloud, emit, Hermes health, GitHub App created and installed on Papership only.
- API GitHub health + PR **plan/open** client is wired. Live open is opt-in (`dry_run: false` + reauth). Hermes write tools still wait for T2-1.

## Owner (if the key is still only in Downloads)

```bash
mkdir -p ~/.config/orgos
cp ~/Downloads/orgos-dev.2026-09-11.private-key.pem ~/.config/orgos/github-app.pem
chmod 600 ~/.config/orgos/github-app.pem
```

Optional: rotate the App client secret if it was pasted in chat.

## Not required for T2-1

Redis, Docker, webhook, second model key, a live (non-dry-run) first PR.

Say **go** to start the interception spike.
