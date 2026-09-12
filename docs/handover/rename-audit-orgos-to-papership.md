# Rename audit: leftover OrgOS / cc-org → Papership

Read-only inventory, 2026-09-12. **No rename performed.** Do not treat this file as authorization.

Target (already accepted D-20 / D-26 / D-32): slug `papership`, UI **Papership**. Old tokens: `orgos`, `OrgOS`, `ORGOS`, `org-os`, `org_os`, `cc-org`, `ccorg`, `cc_org`, and close product variants. A previous file, `docs/handover/rename-audit-orgos-to-paperclip.md`, audited the **wrong** target (competitor Paperclip). Ignore that target. This file is the Papership audit.

## Verdict

**NO-GO** for a single, swift, complete wipe — including the GitHub repo, GitHub App, Vercel project, git history, and every historical filename — with zero leftover old names and no issues.

**GO** for a sequenced leftover sweep into **Papership**, in the passes in §4, after you accept the concerns and solutions in §1. In-repo live code can move quickly. Provider slugs cannot move from this agent.

Phase 6 stays unimplemented until you ask.

## 1. Concerns and solutions (read before any swap)

### 1.1 I cannot rename GitHub, the App, or Vercel from here

| Surface | Current (verified 2026-09-12) | Who can change it |
|---|---|---|
| GitHub repo | `enginelabs-au/OrgOS` (id `1364169617`; only product repo in the org; homepage `https://orgos-ivory.vercel.app`) | You, GitHub Settings → Rename. This agent has no repo-rename tool. `gh` is read-only. |
| `origin` URL | `https://github.com/enginelabs-au/orgos` (GitHub treats it as OrgOS) | Follows a GitHub rename via redirect. |
| GitHub App | `orgos-dev` (id `4908453`, installation `160851156`) | You. App **slugs are often immutable**; a new App may be required if you want the bot name gone. |
| Vercel project | `orgos` (`prj_S74JOIky7KugVTrfu652NhJYOL8l`), host `orgos-ivory.vercel.app` | You, Vercel dashboard. Never touch `enginelabs-au-site`. |
| Host env | `GITHUB_APP_REPO=OrgOS`, paths under `~/.config/orgos/` | You, then the agent updates repo defaults. |
| This VM folder | `/workspace` (already not OrgOS) | N/A |
| Your Mac folder | historically `~/OrgOS` | You, after reopen. Remotes are URL-based. |

**Solution:** you rename GitHub `OrgOS` → `Papership` first (GitHub keeps a redirect). Then point the App’s selected repos and the Vercel Git link at the same repo id. Then set host `GITHUB_APP_REPO=Papership`. Then I change `.env.example`, `scripts/dev-local.sh`, and tests. **Not the reverse** — flipping the default while the live App still looks up `OrgOS` by name breaks `open_pull`.

### 1.2 Live GitHub-App contract is still OrgOS-shaped

These are the sharp dependents. Changing them before §1.1 breaks the live loop:

| Location | Contract |
|---|---|
| `.env.example` | `GITHUB_APP_REPO=OrgOS` |
| `scripts/dev-local.sh` | default repo `OrgOS`; store `/tmp/orgos-api-store.sqlite`; reads `~/.config/orgos/github-app.paths` |
| `services/api/app/github_app.py` | receipt `.orgos/loop/{slug}.md`; fallback slug `orgos-loop`; commit `orgos: {title}` |
| `services/api/app/main.py` | grants payload still includes key `"orgos"` beside `"papership"` |
| `services/api/tests/test_github_*.py`, `test_loop.py`, `test_env.py` | hard-coded `OrgOS`, `orgos/…`, `.orgos/loop/…` |

**Solution:** after the GitHub repo name matches, write new receipts to `.papership/loop/`, commit prefix `papership:`, drop the `"orgos"` grants alias, and dual-read old `.orgos/loop/` files so existing PR #1 receipts stay findable. Do not rewrite published receipts.

### 1.3 “No old name anywhere ever again” cannot include history

You already allowed historical references. These **must** keep the old tokens or we destroy evidence / break pins:

| Residual | Why it stays |
|---|---|
| Git history, old SHAs, PR titles, commit `orgos: …` | Immutable. Do not rewrite history. |
| Decision files `docs/decisions/2026-09-11-orgos-*.md`, D-10, D-20 residual lists | Historical decisions |
| `docs/ui-blueprint/blueprint-1/**` and `docs/ui-blueprint/blueprint-2/OrgOS*.html` | Pinned visual source |
| Unused `apps/web/src/components/cc-org-dash/` | Leftover blueprint-1 components; live chrome is blueprint-2 |
| Workstream id `20260910-engine-labs-company-os` | Frozen task id; hundreds of links |
| Published `.orgos/loop/*.md` on GitHub | Already shipped |
| Competitor name Paperclip in strategy | Different product; must stay |

**Solution:** define “gone” as *live product surfaces and new writing*. Add a scan that fails new OrgOS/cc-org **product** strings in `apps/` (except the unused historical folder and the `/cc-org-dash` redirect), `services/`, `scripts/`, and `NOTICE`. Do not scan `docs/decisions/`, blueprint-1, or `OrgOS.dc.html`.

### 1.4 A bookmark redirect is not a product name

`/cc-org-dash` already redirects to `/papership` (D-32). `/EcoOS` does too. Legacy localStorage keys migrate once.

**Solution I recommend:** keep the redirect and migrate keys as **historical aliases** so old bookmarks do not 404. That is one intentional leftover URL, not live branding. Drop the redirect later if you confirm nobody uses it.

### 1.5 Related leftover that is not OrgOS but the same class

| Token | Where | Solution |
|---|---|---|
| `engine-os-token` | `apps/web/src/api/papership.js` | Migrate to `papership-token` (copy-once, like D-32). |
| `EcoOS` / `ecoos` | `App.jsx` redirects | Keep as aliases or drop with `/cc-org-dash`. |

### 1.6 Do not touch the marketing site

`www.enginelabs.com.au` and Vercel `enginelabs-au-site` stay as-is (D-20).

### 1.7 Do not mix this with Phase 6

Commercial entitlements are a different change set. Sweep first or after; not in the same commit as T6-1.

## 2. Inventory (re-verified this turn)

Roughly **90 files** still contain an in-scope token. Most are docs/history. Desktop (`apps/desktop`) and `packages/` have **zero**. `infra/` has **zero**. `.github/` has **zero**.

### 2.1 Live code (must change; some only after §1.1)

| Location | Notes |
|---|---|
| `NOTICE` | `Engine Labs (OrgOS)` — display/legal; safe now |
| `apps/web/src/api/papership.js` | Copy still says provider project may be named OrgOS; `engine-os-token` |
| `apps/web/src/App.jsx` | Historical redirects only |
| `apps/web/src/blueprint2/App.jsx` | Legacy storage keys only |
| `apps/web/src/blueprint2/blueprint2.css` | Comment cites `OrgOS.dc.html` (historical pin; keep) |
| `apps/web/src/pages/cc-org-dash.jsx` | Compatibility re-export |
| `apps/web/src/components/cc-org-dash/` | Unused live; historical folder — keep |
| `services/api/app/main.py` | `"orgos"` grants alias |
| `services/api/app/github_app.py` | Receipt path / commit prefix / fallback slug |
| `services/api/tests/test_github_*.py`, `test_loop.py`, `test_env.py` | Fixtures |
| `scripts/dev-local.sh`, `.env.example` | Defaults + `~/.config/orgos` |

### 2.2 Provider / machine (owner-only)

GitHub `enginelabs-au/OrgOS`, App `orgos-dev`, Vercel `orgos` / `orgos-ivory.vercel.app`, `~/.config/orgos/`, live `GITHUB_APP_REPO`, receipt dir `.orgos/loop/`.

### 2.3 Historical (do not rewrite)

Decisions `2026-09-11-orgos-*`, D-20 residual list, blueprint-1, `OrgOS.dc.html` + Mobile/Annotation, workstream `20260910-engine-labs-company-os`, closed handoffs, `docs/ui-blueprint.md` capture notes, runbooks `vercel-orgos-single-site.md` / `orgos-hermes-tunnel.md` (update the **live** rule text in those runbooks, keep the filename).

## 3. What “swift” actually is

| Pass | Agent can do? | After you… | Risk |
|---|---|---|---|
| **A — live copy, NOTICE, grants alias, `engine-os-token`, comments** | Yes | Accept this audit | Low. No provider flip. |
| **B — GitHub repo → Papership** | **No** | You rename in Settings | GitHub redirect keeps old URLs working |
| **C — App + Vercel Git + host `GITHUB_APP_REPO`** | **No** | You update dashboards + env | Breaks `open_pull` if skipped |
| **D — receipt path, commit prefix, tests, `.env.example`, `dev-local.sh`** | Yes | B + C done | Medium; dual-read old receipts |
| **E — scan test for new live-code leftovers** | Yes | After D | Low |
| Unused `components/cc-org-dash/` directory rename | Optional; I recommend **keep** as historical | — | None if kept |
| Blueprint-1 / `OrgOS.dc.html` filenames | Must **not** | — | Breaks pinned source |
| GitHub App slug `orgos-dev` | Often never | New App + new PEM if you insist | High if forced |
| Vercel project id + `*.vercel.app` | Dashboard only | Optional custom domain | Ivory URL may persist |
| Wipe git history | Must not | — | Destroys evidence |
| Local `/workspace` | Already not OrgOS | Mac folder is yours | None |

## 4. Safe sequence (the “GO” path)

1. You accept: target is **Papership** (already D-20); historical files stay; `/cc-org-dash` may remain a redirect; Phase 6 is separate.
2. You say go for **Pass A**. I sweep live copy/NOTICE/token/grants alias only. I do **not** touch `GITHUB_APP_REPO` or `.orgos/loop/`.
3. You rename GitHub `enginelabs-au/OrgOS` → `enginelabs-au/Papership`. Confirm `https://github.com/enginelabs-au/OrgOS` redirects.
4. You update GitHub App selected repos (and homepage if you want), Vercel Git link, and host `GITHUB_APP_REPO=Papership`. Optional: copy `~/.config/orgos` → `~/.config/papership` and point `github-app.paths`.
5. You say go for **Pass D**. I update `github_app.py`, tests, `.env.example`, `dev-local.sh`, receipt path (dual-read), commit prefix.
6. Pass E scan. Then you may implement Phase 6.

## 5. Go / no-go line

| Ask | Verdict |
|---|---|
| Full wipe this session, including GitHub/App/Vercel, zero leftovers in history | **NO-GO** |
| Agent-only live leftover sweep to Papership **without** flipping `GITHUB_APP_REPO` / receipt path (Pass A) | **GO** when you say so |
| Complete live infra rename including GitHub repo name (Passes B–E) | **GO after you finish B+C** |
| Rename to anything other than Papership (e.g. Paperclip) | **NO-GO** — D-20 stands; Paperclip is the documented competitor |

I have not changed product strings in this turn.
