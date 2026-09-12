# Rename audit: OrgOS / cc-org → Paperclip

Read-only inventory, 2026-09-12. **No rename performed.** Do not treat this file as authorization.

Target requested: slug `paperclip`, UI **Paperclip**. Old tokens in scope: `orgos`, `OrgOS`, `ORGOS`, `org-os`, `org_os`, `cc-org`, `ccorg`, `cc_org`, and close variants.

## Verdict

**NO-GO** for a single, swift, complete swap — including the GitHub repo — with zero leftover old names and no issues.

**CONDITIONAL GO** only after the owner answers the blocking questions in §1 and accepts the lockstep in §4. In-repo live-code leftovers can be swept in one or two passes *after* that. Provider slugs cannot.

## 1. Blocking concerns (must answer before any swap)

### 1.1 Paperclip is already the named competitor

This repo’s own strategy treats **Paperclip** as the closest alternative (`github.com/paperclipai/paperclip`, re-verified 80,404 stars). Blueprint and Growth handoffs say Engine Labs must be measurably better than Paperclip. The UI already exports a Lucide-style `Paperclip` attach icon in `packages/ui/src/icons.tsx` and leftover `apps/web/src/components/cc-org-dash/icons.jsx`.

Using **Paperclip** as *this* product’s public name collides with that competitor, the attach icon export, and later GTM copy. That is a consequential naming decision (AGENTS.md §4), not a mechanical string replace.

**Solution if you still want Paperclip:** record a new decision that supersedes D-20; rewrite competitor rows as “Paperclip AI (`paperclipai/paperclip`)”; rename the icon export to `Attach`; accept trademark/confusion risk yourself. I will not invent a legal opinion.

**Solution I recommend:** do **not** adopt Paperclip. Finish the leftover OrgOS / cc-org sweep into the already-accepted name **Papership** (D-20, D-26, D-32). Rename the GitHub repo to `Papership` when you are ready on the provider dashboards.

### 1.2 Papership is already the live product name

Accepted and shipped:

| Surface | Current |
|---|---|
| UI / tab title | Papership |
| Route | `/papership` (D-32); `/cc-org-dash` redirects |
| npm | `@papership/web` |
| Desktop | `productName: Papership`, identifier `au.enginelabs.desktop` |
| In-repo slug | `papership` (D-26) |

Your ask listed only OrgOS / cc-org → Paperclip. It did not say what happens to **Papership**. A sweep that leaves Papership in the UI and Paperclip in slugs creates a third name. A sweep that also replaces Papership is a second product rename in two days.

**Need from you:** (A) replace only OrgOS/cc-org leftovers, keep Papership, or (B) replace Papership as well with Paperclip.

### 1.3 The GitHub repo cannot be renamed from this agent

- Canonical GitHub name: `enginelabs-au/OrgOS` (confirmed via GitHub API; only product repo in the org).
- `origin` URL: `https://github.com/enginelabs-au/orgos` (GitHub treats this as OrgOS).
- This VM’s working tree is `/workspace`, not `~/OrgOS`. Local folder rename here is a no-op. On your Mac, `~/OrgOS` → a new folder name is safe after reopen (remotes are URL-based).
- `gh` in this environment is read-only. There is no repo-rename tool on the agent. **You** rename it in GitHub Settings.

Renaming `GITHUB_APP_REPO` in code or env **before** the GitHub repo and App installation match **breaks** live `open_pull` (App `orgos-dev`, receipts under `.orgos/loop/`, commit prefix `orgos:`).

**Solution:** owner renames GitHub repo → updates GitHub App selected repos + any webhook/homepage → updates Vercel Git link → then set `GITHUB_APP_REPO` to the new name → then the agent changes defaults/tests. Not the reverse.

### 1.4 “No old name anywhere ever again” is not possible

You allowed historical references. Even then, these cannot be erased by a repo sweep:

| Residual | Why it stays |
|---|---|
| Git history / old SHAs / PR titles | Immutable unless you rewrite history (do not) |
| GitHub App slug `orgos-dev` | App slugs are sticky; often need a **new** App, not a rename |
| Vercel project id `orgos` / host `orgos-ivory.vercel.app` | Project rename is dashboard-only; URL slugs may persist |
| Existing `.orgos/loop/*.md` on GitHub | Already published receipts |
| Workstream id `20260910-engine-labs-company-os` | Frozen task id; hundreds of links |
| Decision filenames `2026-09-11-orgos-*.md` | Historical, as you allowed |
| `docs/ui-blueprint/blueprint-1/**` and `OrgOS.dc.html` | Pinned reference captures |
| Competitor name “Paperclip” in strategy | Must stay if that product still exists |

**Solution:** define “gone” as *live product surfaces and new writing*. Keep historical files. Do not rewrite git history.

## 2. Inventory (exhaustive by class)

Roughly **90 files** contain an in-scope token. Most are docs/history. Runtime dependents are few and sharp.

### 2.1 Live code (must change in lockstep with providers)

| Location | What it does | Risk if changed first |
|---|---|---|
| `.env.example` `GITHUB_APP_REPO=OrgOS` | Default repo for the GitHub App | Live App looks at the wrong repo |
| `scripts/dev-local.sh` | Defaults `GITHUB_APP_REPO=OrgOS`, store `/tmp/orgos-api-store.sqlite`, reads `~/.config/orgos/github-app.paths` | Local + live App break |
| `services/api/app/github_app.py` | Receipt path `.orgos/loop/{slug}.md`; fallback slug `orgos-loop`; commit `orgos: {title}` | New receipts miss the old convention; live tests fail |
| `services/api/app/main.py` | Grants payload still includes key `"orgos"` beside `"papership"` | Clients that still read `orgos` |
| `services/api/tests/test_github_*.py`, `test_loop.py`, `test_env.py` | Hard-coded `OrgOS`, `orgos/…`, `.orgos/loop/…` | Tests fail until updated with the new contract |
| `apps/web/src/App.jsx` | `/cc-org-dash` redirect (keep as alias if you want bookmarks) | Safe to keep as historical redirect |
| `apps/web/src/blueprint2/App.jsx` | Legacy localStorage `cc-org-dash-auth` / `cc-org-dash-theme` | Safe; migrate-only |
| `apps/web/src/api/papership.js` | Copy mentions OrgOS GitHub residual | Copy-only |
| `NOTICE` | `Engine Labs (OrgOS)` | Legal display |
| `apps/web/src/pages/cc-org-dash.jsx` | Compatibility re-export | Safe to keep or delete after redirect-only |

Unused but still in tree: `apps/web/src/components/cc-org-dash/` (20 leftover blueprint-1 files, including `Paperclip` icon and fixture `tenant_id` `cc-org-au`). Live chrome is blueprint-2, not this folder.

Desktop (`apps/desktop`) and `packages/` have **no** OrgOS/cc-org product strings. Desktop is already Papership.

### 2.2 Live providers (owner-only; not in this repo)

| Provider | Current | Notes |
|---|---|---|
| GitHub repo | `enginelabs-au/OrgOS` | Rename in Settings; GitHub keeps a redirect from the old name |
| GitHub App | `orgos-dev` (id `4908453`, installation `160851156`) | Slug may be immutable; homepage was `orgos-ivory.vercel.app` |
| Vercel project | `orgos` (`prj_S74JOIky7KugVTrfu652NhJYOL8l`) | Git-linked; do not touch `enginelabs-au-site` |
| Local secrets dir | `~/.config/orgos/` | PEM + paths; not in git |
| Receipt convention | `.orgos/loop/` | Already on GitHub via PR #1 |
| Icon filename (historical) | `orgos-icon.png` in blueprint-2 HTML / some docs | Live brand path is `papership-icon.png` |

### 2.3 Historical / do-not-rewrite (your exception)

- Decisions `docs/decisions/2026-09-11-orgos-*.md`, D-10, D-20 residual lists
- `docs/ui-blueprint/blueprint-1/**` (pinned `/cc-org-dash` capture, `capture.mjs`)
- `docs/ui-blueprint/blueprint-2/OrgOS*.html` (canonical visual source filenames)
- Workstream `docs/workstreams/20260910-engine-labs-company-os/`
- Continuation logs, closed handoffs, `docs/verification.md` SHA-linked evidence
- Runbooks `vercel-orgos-single-site.md`, `orgos-hermes-tunnel.md`

### 2.4 Related leftovers (not OrgOS/cc-org, but same class)

| Token | Where | Treat as |
|---|---|---|
| `engine-os-token` | `apps/web/src/api/papership.js` | Old session key; migrate if you rename |
| `EcoOS` / `ecoos` | redirects in `App.jsx` | Already aliases |
| `20260910-engine-labs-company-os` | workstream id | Frozen |
| `cco-245` | blueprint fixtures | Ticket id, not a product name |

## 3. What “swift and efficient” actually means

| Pass | Agent can do? | Swift? | Issues |
|---|---|---|---|
| Live in-repo strings + tests + NOTICE + comments | Yes, after §1 | Yes (one PR, two passes: code then scan) | Must not flip `GITHUB_APP_REPO` until GitHub matches |
| Leftover `components/cc-org-dash/` directory rename | Yes | Medium | Unused by live route; optional cleanup |
| Blueprint-1 / `OrgOS.dc.html` filenames | Yes, but should **not** | No value | Breaks pinned visual source; keep as historical |
| GitHub repo name | **No** | Owner Settings | Then update every remote, Vercel, App, env |
| GitHub App slug | **No** / maybe never | New App if slug is frozen | Re-copy PEM to a new `~/.config/…` |
| Vercel project name + `*.vercel.app` | **No** | Dashboard | Custom domain optional |
| Wipe git history | Must not | — | Destroys evidence |
| Local `/workspace` folder | N/A | Already not OrgOS | Your Mac folder is owner-only |

## 4. Safe sequence (only after §1)

1. You confirm target: **Papership** (recommended) or **Paperclip** (after competitor accept).
2. You rename GitHub `OrgOS` → that target (Settings). Confirm the redirect works.
3. You point GitHub App + Vercel Git at the new repo name. Set host `GITHUB_APP_REPO` to the new name.
4. You say go. Agent sweeps live code/tests/defaults, keeps `/cc-org-dash` as a redirect, keeps historical files, adds a scan test that fails on new OrgOS/cc-org *product* strings in `apps/` + `services/` (not `docs/decisions/` / blueprint-1).
5. Owner copies `~/.config/orgos` → the new config dir if you want that gone locally.
6. Do **not** implement Phase 6 in the same turn as the sweep.

## 5. Go / no-go line

- **Full rename to Paperclip, including GitHub, zero leftovers, this session:** **NO-GO.**
- **In-repo leftover OrgOS/cc-org → Papership after you rename the GitHub repo to Papership:** **GO.**
- **In-repo leftover OrgOS/cc-org → Paperclip after you accept §1.1–1.2 and rename GitHub first:** **CONDITIONAL GO.**

I have not changed any product strings. Phase 6 stays unimplemented.
