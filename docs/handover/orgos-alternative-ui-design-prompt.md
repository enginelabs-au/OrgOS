# Papership — alternative UI layout brief (Claude Design / Minimax Design)

Copy everything below the line into Claude Design or Minimax Design. Attach `brand/papership-icon.png` plus 2–4 screenshots of the current `/papership` shell (light and dark) if the tool accepts images.

---

## Role

You are a senior product designer. Redesign **Papership**, a company operating system for a founder who runs agents under real authority. Produce an **alternative visual layout** of the **same product**, not a new information architecture and not a marketing website.

## What this is

**Papership** is the product. **Engine Labs** is the company that builds it. The UI is a dense authenticated desktop/web app — a command centre, not a landing page.

Do **not** design:

- A public marketing site, hero, pricing page, or “book a demo”
- A replacement for `www.enginelabs.com.au`
- A generic AI-chat landing, Notion clone, Linear clone, or Salesforce CRM
- Invented revenue, dollar prices, ARR, MRR, invoices-as-product-metrics, or “Upgrade to Pro $49”
- Fake customers (Acme, Salesforce, EcoAdmin). The only person is **Cam Douglas**, founder of Engine Labs. The only repo is **Papership**. The bound source is **GitHub**. The runtime is **Hermes**.

## Design goal

Keep the **current shell geometry and navigation model**. Change density, grouping, typography rhythm, card vs table balance, and visual polish so it feels like a refined alternative of *this* app — not a different product.

Think: same rooms, better furniture. A founder should still find Today, Work, Inbox, the left Company rail, and Hey Engine without relearning the product.

## Current layout (preserve this skeleton)

Desktop width **1440×900** and **1280×800**. Mobile **390×844** as a compressed version of the same chrome, not a separate mobile app (mobile clients are a later release).

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ TOP BAR  60px                                                                │
│ [rail ▤] [prism icon] Papership / Engine Labs  [Search anything  ⌘K]            │
│          [sun/moon] [+] [bell•] [avatar] [Hey Engine  rainbow]               │
├──────────────────────────────────────────────────────────────────────────────┤
│ PRIMARY TABS  notched, under the top bar                                     │
│ Today · Work · Inbox · People · Data · Files · Integrations · Settings       │
├────────────┬──────────────────────────────────────────────┬──────────────────┤
│ COMPANY    │ MAIN COLUMN  max-width ~1280, pad 24/28      │ HEY ENGINE       │
│ RAIL 264   │ Page header + SubNav pills + content          │ PANEL 420        │
│ (54 closed)│                                              │ (optional, right)│
│            │                                              │                  │
├────────────┴──────────────────────────────────────────────┴──────────────────┤
│ PLATFORM STATUS BAR  32px collapsed · live audit chip · expand upward        │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Z-order (keep):** top nav 520 > Hey Engine 500 > command palette 400 > modal 300 > slide-over 200 > status bar 10050 (always on top of content, never covering the top bar).

**Motion:** `cubic-bezier(0.32, 0.72, 0, 1)`. No gratuitous parallax. Respect `prefers-reduced-motion`.

**Overlays that already exist and must stay:**

- Command palette ⌘K (width 520): groups Jump to / Work items / Runs / Actions
- Slide-over 460 from the right for rail-row detail and list peek
- Notification drawer 360
- Centred modal max 520
- Auth is a separate full-page card (max 400), not inside the shell

## Visual system (must use)

**Mark:** low-poly prism head. Use the attached `papership-icon.png`. Do not invent a new logo.

**Type:** Inter for UI. JetBrains Mono only for IDs, SHAs, keys, timestamps, allowance, issue keys (`CCO-245`), run ids.

**Primary:** blue `#2563eb` / `#3b82f6` for chrome, buttons, links, selected states.

**Secondary:** fractured purple `#6d28d9` light / `#16082e` dark for nav field and secondary surfaces.

**Rainbow (accent only):** `linear-gradient(135deg, #2563eb, #22d3ee, #4ade80, #fbbf24, #f472b6, #a78bfa)` — **Hey Engine button and similar highlights only**. Never rainbow-wash the whole UI.

**Light (“Observatory cream”):**
- canvas `#faf8f4`, surface `#ffffff`, raised `#f1eee6`
- text `#1a1224` / `#63738a` / `#617083` (t3 must stay `#617083` for WCAG AA)
- page wash `linear-gradient(180deg, #f7f4ee, #f3efe6, #faf8f4)`

**Dark (near-black purple):**
- canvas `#0b0614`, surface `#16101f`, raised `#1c1528`
- text `#f2eef8` / `#9fb0cc` / `#7c8ca8`
- page wash `linear-gradient(180deg, #0b0614, #12081e, #0a0e22)`

**Dimmed** (Settings only, optional third theme): canvas `#1e2438`, surface `#232840`.

**Semantic:** green `#059669` / `#4ade80`, red `#e11d48` / `#fb7185`, amber `#d97706` / `#fbbf24`. Status is **never colour-only** — always pair with a label or icon.

**Primitives to keep recognisable:** Surface radius 10, Btn radius 6, Badge pill h20, SubNav capsule pills on a raised bar, Primary tabs notched (active tab fills with canvas), Dot + text, Progress h6, Table with 12/600 headers.

**Contrast:** body and UI text ≥ 4.5:1 on canvas/surface. Do not use the decorative t4 greys for text.

**Tone:** quiet, precise, operator-grade. Cream paper + deep purple night. Not neon SaaS. Not skeuomorphic observatory chrome beyond the colour story.

## Product thesis (so the UI stays honest)

Papership is a **company OS that treats authority, provenance, and recovery as the product**.

- Every agent run has a **sponsor, scope, budget, and receipt**.
- Closing the window **never cancels** cloud work. **Cancel** is an explicit red action with confirm.
- Prompts are not a security boundary. The UI must never imply the assistant can bypass grants.
- Specialist records (invoices, payroll, CRM) live in **connected systems**. Papership keeps a thin native **work ledger**: plans, assignments, dependencies, decisions, execution evidence.
- Users own their data. Engine Labs does not own user content. No invented billing numbers.
- Unconfigured capabilities stay **visible as planned/unavailable**, never hidden, never crowding Today.

**Seats (show in chrome, do not design three separate apps):**

| Seat | When | What they see |
|---|---|---|
| Founder (Cam Douglas) | Release 1 now | Org-wide. Technical details only behind a “Technical details” link. |
| Project Lead | Release 2 | Delegated projects. No host/DB detail. No org defaults. |
| Operator | Release 2 | Own assignments and runs. Ask / Analyse / Draft. No permissions editor. |

**Assistant modes (chips, not menus):** Ask · Analyse · Plan · Draft · Execute · Review. **Automate** is visible but disabled: “Coming later”.

## Global chrome — design every piece

### Top bar
Left: rail toggle (36×36, purple-tinted border) · prism icon · wordmark **Papership** (Inter 15/700) with **Engine Labs** as a quieter subtitle.
Centre: search button “Search anything” + ⌘K, max 400.
Right, stable order that **must not move under any adaptation**: sun/moon · **+** create · bell with unread count · avatar · **Hey Engine** rainbow control.

**+ create menu items:** New priority · New plan · New request · New run. Later: New issue, Invite person, Upload document.

Avatar menu: Profile (opens Account) · Settings · Sign out.

### Primary tabs
Keep **notched** active geometry and 16px stroke icons.

**Full product (web, this is the layout to redesign):**
Today · Work · Inbox · People · Data · Files · Integrations · Settings
Account is **not** a tab — only via avatar.

**Release-1 desktop subset** (same chrome, fewer tabs — design as a variant, not a different app):
Today · Work · Runs · Connections · Settings
Badge on **Runs** / **Inbox** = waiting-approval or unread count.

Later tabs without inventing a new nav model: **Memory** (R3) can appear after Settings or as a Settings subsection. Do not add a tenth mystery tab.

### Company command rail (left, 264 / 54)
Header: **Company** · “Health · work · decisions”
Sections, in this order:

1. **SIGNALS** — Health (n degraded) · Decisions (n) · Notifications (n)
2. **PRIORITIES** — top ledger items with health dots
3. **PLANS & MILESTONES** — collapsible; % and dates
4. **BLOCKERS** — red-tint rows, impact + team
5. **DECISIONS** pinboard — recent decision records

Row click → 460 slide-over with title, body, footer **Open** / **Close**.
Collapsed 54px rail = **icon strip** (not empty). Persist open/closed.

### Hey Engine panel (right, 420)
Browser-style **session tabs** + “+”. Message log. Footer:

- Mode chips (Ask / Analyse / Plan / Draft / Execute / Review)
- Scope pill (Organisation / Project: X / Item: KEY) — read-only unless the seat may widen
- Allowance line in mono: `Remaining allowance: N · This action ≈ est.` — **no currency, no fake $**
- Composer: Enter sends, Shift+Enter newline; send becomes **Stop** while streaming

Do **not** put model pickers, temperature, max tokens, tenant_id, or API keys in the default footer. Founder-only “Technical details” opens a slide-over (session id, model band, policy version).

Inline cards inside the thread: run status, approval (action + target + version), “Closing this panel won’t stop the work”.

Wake-word “Hey Engine” is specified, not shipped — a mic affordance may exist but must look **off / unavailable** unless labelled as a future entitlement.

### Status bar (bottom, 32px)
Collapsed: activity icon · relative age · latest audit line · live chip · chevron.
Expanded (max 40vh): last ~80 events with absolute time.
Event kinds: created, modified, deleted, connected, failed, warning, released, rotated, exported, signed in/out, **approved, refused, run started, run completed, recovered**.
Offline: red “Offline · Reconnecting…”. Cloud work continues.

### Notifications drawer
Severity + text. Types: run completed, approval requested/decided, connection unavailable, incident/escalation. Row deep-links. Mark all read.

## Screen inventory — design all of these

Every screen needs **loading / empty / error / disconnected / pending-approval / running / completed / restricted** thinking, even if you only fully render the happy + empty + disconnected states. Use Australian English (en-AU). Plain language. No prompt text, JSON schemas, or env vars on operator surfaces.

---

### 0. Auth (full page, before the shell)

Card max 400. Prism + Papership + Engine Labs. Email/password. Strong-factor as a **second card state** (not a third-party marketing SSO wall). No Google button in R1. No sign-up (invite later). Footer: language + theme. Errors in plain words. Demo person if needed: Cam Douglas / founder@enginelabs.com.au — never pre-filled passwords.

---

### 1. Today (Home)

Purpose: “what needs me now”.

**SubNav:** Overview · Decisions (count) · Running (count) · Registry

**Regions (this order on desktop):**

1. Full-width assistant strip: **“What would you like to do?”** + input + mode chips. Submit opens Hey Engine pre-filled.
2. **System health** — four KPI cards: API · Workers/Hermes · Database · Bound repository. Each: Dot + label + last check time. Never empty.
3. Two-column: **Active priorities** (progress) + **Required decisions** (Approve / Reject, showing action + target + version). If the target changed since request: “Changed — review again”.
4. **Running work** — runs with status, elapsed, estimated cost band (no $), Open run.

Disconnected banner: “Can’t reach Papership cloud. Showing last known state from HH:MM. Work already started continues in the cloud.”

Empty copy examples: “No priorities yet. Create one or ask the assistant.” / “Nothing running.” / “No decisions waiting.”

---

### 2. Work

**SubNav (full product):** Projects · Issues · Board · Roadmap · Workflows · Wiki  
**R1 subset to also show:** Priorities · Plans · Assignments · Board

- **Projects / Plans table:** name, department, owner, status (on_track / at_risk / planning / done), priority, progress, due
- **Issues / Assignments:** grouped ticket rows — checkbox, issue key, dot, title, labels, due, avatar. Sticky bulk bar when selected
- **Board:** 4 columns, todo / in_progress / review / done, drag
- **Roadmap:** list + timeline + cycle (quarters). Burndown as a small chart with a text equivalent
- **Workflows:** node-graph canvas, left rail ~216, inspector ~210, orthogonal connectors, Node/Sequence toggle, Run/Save. “AI assist” is a banner, not a hidden model panel
- **Wiki:** honest empty state until knowledge exists

**Work item detail** (full page `/work/:id` and a 460 peek slide-over):

- Header: key, title, status, priority, owner, due
- **Loop chain — 11 stages, this exact order:**  
  1 Request → 2 Research → 3 Specification → 4 Plan → 5 Assignment → 6 Isolated change → 7 Tests → 8 Review → 9 Approved release → 10 Monitoring → 11 Retained knowledge  
  Each stage: state dot + link to record/artifact + revision SHA (mono). Horizontal ≥1280, vertical below.
- Details key/values · Dependencies · Runs table · Evidence & decisions · Activity timeline
- Actions: Start a run (opens Hey Engine scoped to this item) · Change status · Link dependency · Add decision · Open branch/PR (external handoff) · Close (danger, confirm)

Release execution is **proposal only** in this UI. Never a one-click “Ship to production” without designated authority.

---

### 3. Runs (tab on desktop; also reachable from Today / Work / Hey Engine)

**SubNav:** Running · Waiting · Completed · Failed

List columns: run · work item · mode · status · started · elapsed · est./actual cost band (no $)

**Detail:**

- Header: purpose, status, sponsor, acting identity, deadline
- Actions: Pause · Resume · **Cancel** (confirm: “Stop this run? Work done so far is kept. This can’t be undone.”) — never conflate with Close
- Left ~2/3: Progress `ol` with checkpoints; plain-language receipts (“Read 3 files”, “Ran tests: 14 passed”); Recovery callout on retry/escalation
- Right ~340: **Scope** (org/project/item + grant classes in words) · **Sources** (dot + last sync) · **Usage** (model band, tool calls, time, tokens as bars) · **Budget** (reserved vs allowance)

Closing the app: optional toast “3 runs continue in the cloud”. Never “stop”.

---

### 4. Inbox (R2 collaboration; keep in the full layout)

Ticketed conversations, not a consumer chat dump.

- Workspace switcher
- **SubNav:** All · Mentions · Starred · Archived
- Filters: status, channel (Email / Slack / Telegram / WhatsApp / in-app), assignee, mine / unassigned
- Thread list + message pane + detail rail
- Compose: public reply vs internal note; reactions
- Channels are **not** permission to read all of a user’s mail. Scope pill must stay visible.

---

### 5. People (R2)

**SubNav:** People · Teams · Pending invites

Table: avatar, name, role, department, email, status. Slide-over person. Invite modal. Seats: Founder / Project Lead / Operator / Guest. Guest sees only assigned scope.

---

### 6. Data (observability + registry metrics)

Left **apps rail** 228/52:

- MY APPS: Metrics Hub · Trace Explorer · (Model Arena / SQL Lab as external handoff, labelled “opens in source”)
- CONNECTED: warehouse/transform as planned connectors, not fake Snowflake logos
- Footer: Documentation · Changelog · Usage · Settings

**SubNav:** Metrics · AI traces · Events · Alerts

Trace table: name, agent, model **band** (not raw prompt), tokens, cost band, latency, status, time. Trace detail slide-over.

This is **run traces and health**, not a BI product and not a cost dashboard with invented $.

---

### 7. Files / documents

Dropbox-style three panes: folder nav 228 · list/grid · detail 240.

Folders: All Files · Plans · Decisions · Loop notes · Handover · Shared · Starred · Trash.

Upload modal. Document intake is a first-class R1 action (disconnected framework must still allow upload). No emoji-only folder icons — use stroke icons.

---

### 8. Integrations / Connections

**SubNav:** Connected · Available · Unavailable  
(Full product may still show Installed / Browse / Webhooks as a more tool-y variant — prefer the status vocabulary.)

Cards: provider glyph or initials, status Dot+Badge (`planned` / `configured` / `working` / `unavailable`), scope summary, last verified time, users if connected.

**R1:** GitHub (bound repository) is the only permissioned source. Web research/browsing is configured-within-limits. Gmail, Slack, Telegram, WhatsApp are **planned** and stay visible.

**Setup wizard (5 steps, modal or slide-over):**  
1 Choose provider → 2 Authorise (external browser handoff — never embed credentials) → 3 Grant scopes (source scopes read-only + Papership grant checkboxes) → 4 Verify → 5 Done

Detail: View logs · Test · Reconnect · **Revoke** (danger, reauth). `unavailable` rows show a plain-language recovery line.

**Capability registry (read-only surface on this screen or Today → Registry):** all **43 domain groups**, never removed:

**Business B01–B24** (one row each; show as a browsable list with status chips, not a wall of text):

1. Strategy, goals, KPIs, initiatives, board  
2. Organisation, entities, teams, reporting lines  
3. People / HR / leave / payroll references  
4. CRM / accounts / opportunities / consent  
5. Enquiries, proposals, contracts, signatures  
6. Plans, milestones, dependencies, acceptance  
7. Priorities, assignments, blockers, approvals  
8. Development loop (this repo, isolated change, review, release proposal)  
9. Operations / SOPs / work orders / SLAs  
10. Support tickets / adoption / retention  
11. Knowledge, decisions, evidence, document intake  
12. Comms: email, chat, calendar, transcripts  
13. Finance / invoices / budgets (source system; no fake $ in chrome)  
14. Treasury / payments (designated authority + reauth)  
15. Procurement / vendors / subscriptions  
16. Marketing / campaigns / publishing (designated authority)  
17. Legal, risk, compliance, privacy requests  
18. IT / devices / access / cloud  
19. Inventory / facilities  
20. Field / dispatch / offline capture  
21. Quality / BOM / inspections  
22. Research / experiments / IP  
23. Guests / partners / scoped review  
24. Sector packs (care, grants, education, …)

**Platform P01–P19:**

1. Agent record (sponsor, skills, budget, status)  
2. Identity, membership, seats  
3. Hey Engine + modes + persisted sessions  
4. Runs, steps, receipts, pause/cancel/recover  
5. Durable jobs (close ≠ cancel)  
6. Capability registry + connector catalogue  
7. Sync, lineage, freshness  
8. Canonical metrics / deterministic reports  
9. Governed memory  
10. Grants / row-field-action control  
11. Retention, export, erasure  
12. Secrets off desktop; isolated workers  
13. Audit / provenance  
14. Outcome metrics (completion, correctness, recovery, intervention, context-switch, cost/outcome)  
15. Desktop shell / locale en-AU  
16. Adaptive views (pin, undo, reset, fallback)  
17. Health, queues, backups  
18. Usage events (no published prices)  
19. Connector SDK / domain packs  

Status chips only: planned · configured · working · unavailable.

---

### 9. Settings (left pill nav ~220, content ~520–560)

| Nav item | What to show |
|---|---|
| General | Org name Papership / Engine Labs, timezone Australia/Sydney, locale en-AU |
| AI & Agents | Agent ceilings (budget band, allowed modes, deadline). **No API keys in the UI** |
| Notifications | Critical, warnings, digest, deployments, approvals — toggles, not prices |
| Security | Sessions, 2FA, reauth policy. **Remove API-key lists** |
| Permissions / Seats | Seats table; grant matrix; repository grants **branch / change / check / release** as separate toggles (release default off); agent ceilings. Save that widens access → “Confirm it’s you” reauth modal |
| Plan | “Not priced · commercial gate pending”. **No $**, no fake tiers |
| Team | Members + invites (R2). R1 empty: “Only you (Founder) have a seat.” |
| Appearance | Light / Dark / Dimmed. Sun/moon also in the top bar |
| Data & retention | Conversations 365d, logs 30d, backups 30d, approved knowledge until superseded. Usage disclosure: anonymous first-party events only. Export / erasure (erasure = three confirmations, owner) |
| Personalisation (R3) | Inspect / disable / reset adaptations |
| Docs | Three-pane docs is optional; do not turn Settings into a marketing site |

---

### 10. Account (via avatar)

Sidebar: Public profile · Branding · My link · Phone · Login & security · Cookie settings. Delete account modal. Identity: Cam Douglas. Cookie groups: Essential (locked on), Analytics (anonymous usage), Marketing (off).

---

### 11. Memory manager (R3; include as a specified screen)

Three panes like Files. Left: Sessions · Preferences · Projects · Domains · Organisation · Skills + class filter Source / Approved / Inferred.  
Table: title, kind, class, owner, verified, expiry, version.  
Detail: 7 provenance fields (source, owner, source permissions, timestamps, verification, expiry, version) + preview.  
Actions: Search, Inspect, Correct (new version), Restrict, Merge, Archive, Export, Delete (gated).

---

### 12. Adaptive layout overlay (R3; one frame)

A small badge “Adapted for: \<intent\>” + Why? (plain explanation, **no prompt**). Pin on regions. Undo / Reset layout.  
**These controls never move or hide:** primary tabs, top bar, rail toggle, Hey Engine, scope pill, evidence links, approval targets, allowance text, Cancel / Revoke / Delete.

---

## Cross-cutting features that must appear in the system

- **Approvals** always show action + target + version. Surfaces: Today decisions, run pinned card, Hey Engine inline card, notification, status bar `approved`/`refused`.
- **Repository grants** are four classes, not one “GitHub access” toggle: branch, change, check, release.
- **Handoffs:** if Papership cannot do it, offer “Open in GitHub / Gmail / Slack” instead of a dead end.
- **Health + last sync** on every connected thing.
- **Restricted state:** “Not in your scope” / “You don’t have access to this item” — no title leak.
- **Discovery:** planned/unavailable capabilities live in Registry / Connections, not as junk widgets on Today.
- **Hey Engine = user-equivalent.** The button must not look like a superuser override.
- **Wake word / mic:** optional control, labelled unavailable until entitlement exists.
- **Desktop window:** macOS-style traffic lights sit *above* this chrome in the Tauri shell; do not redraw OS chrome. The web mock can omit traffic lights or show a thin titlebar.
- **iOS/Android (R4, one frame each):** same visual language, bottom tabs Today / Work / Inbox / Hey Engine, explicit offline banner, biometric sign-in. Cloud execution continues.

## Copy and fixture rules

Allowed fixtures: Cam Douglas, Engine Labs, Papership, Hermes, GitHub, Vercel (as a connection, not a price), Phase 2 development loop, T2-1 interception, dry-run PR, “Not priced”.

Forbidden: $ amounts, seat prices, ARR, “Q2 Revenue $2.4M”, Salesforce, Acme Corp, EcoAdmin, OpenAI keys in inputs, “gpt-4o temperature 0.7” in the main assistant footer.

## What to produce

Generate a **cohesive alternative** of this shell. Same IA. Clearer hierarchy. Better empty/error/offline. Keep cream / purple observatory colour story.

**Required frames (light AND dark unless noted):**

1. Today — Overview, healthy, Hey Engine closed  
2. Today — Decisions waiting, Hey Engine open with a streaming reply + approval card  
3. Work — Issues list + bulk bar  
4. Work item detail — loop chain mid-run (stage 6 Isolated change)  
5. Runs detail — in progress, recovery callout  
6. Inbox — thread selected (light)  
7. People — table (light)  
8. Data — traces (dark)  
9. Files — list + detail (light)  
10. Integrations — Connected/Available/Unavailable + GitHub connected, Gmail planned  
11. Connections registry — 43 groups as a scannable list (dark)  
12. Settings — Permissions / repository grants  
13. Settings — Appearance + Plan “Not priced”  
14. Account — profile  
15. Auth — sign-in  
16. Memory manager (light)  
17. Command palette open over Today  
18. Disconnected Today (banner + stale health)  
19. Mobile 390 Today + Hey Engine (light)  
20. Optional: iOS Today (R4)

Also deliver a one-page **annotation** of the shell (named regions, widths 54/264/420/1280, z-order) so engineers can implement without guessing.

## Quality bar

- Looks like one product, not a moodboard
- Operator can hit Approve, Cancel, Search, Hey Engine, and rail toggle without hunting
- Rainbow only on Hey Engine
- Prism icon used; no new mascot
- Every primary tab exists in the desktop 1440 compositions
- Empty and disconnected are designed, not omitted
- If you must cut frames, cut mobile/R4 first — never cut Today, Work+loop, Runs, Hey Engine, or the shell annotation
