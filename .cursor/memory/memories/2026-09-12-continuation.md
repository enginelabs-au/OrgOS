# 2026-09-12 continuation

- Owner directed a hybrid of live chrome and `docs/ui-blueprint/blueprint-2`, leaning toward the newer mock, plus a product rename to **Papership**.
- Web shell now uses the purple nav field, centered search, field-chrome icon buttons, Hey Engine rainbow pill, and notched tabs on the field. Home gained the compose strip. Auth card leans toward the mock while keeping Google sign-in.
- D-20 recorded. D-10 kept as historical (display name only superseded). Live slugs left in place: GitHub repo `OrgOS`, App `orgos-dev`, Vercel project `orgos`, `~/.config/orgos/`, `GITHUB_APP_REPO=OrgOS`, asset `papership-icon.png`, route `/cc-org-dash` (alias `/papership`).
- Local folder rename `~/OrgOS` → `~/Papership` is safe after reopen in Cursor. Do not rename GitHub/Vercel/App until those providers are updated.
- Owner reversed the hybrid: use blueprint-2 **exactly**. `/cc-org-dash` now mounts `apps/web/src/blueprint2/App.jsx` (tokens, auth without Google, notched field tabs, Company rail, Today compose/health/priorities/decisions/runs, docked 420px Hey Engine, status bar). D-21 recorded. Desktop Tauri and R4 mobile bottom tabs were not part of this port. Browser Today shell verified on http://127.0.0.1:5173/cc-org-dash; click-through MCP remains policy-blocked.
- Owner: prism-head mark is app icon and browser tab only. Removed in-app `<img>` uses from blueprint-2 (top bar, auth, compose, Hey), leftover cc-org-dash auth/home, and desktop Wordmark/SignInForm. Favicon / PWA / Tauri icons kept. D-21 item 6.
