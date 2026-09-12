# Decision D-22–D-30: Phase 4 owner closeout

## Status

`accepted` — owner-directed 2026-09-12. Numbered answers map to the Phase 4 status-review sections, not to individual components.

## Decisions

### D-22 Visual review (section 1)

The blueprint-2 port at `/cc-org-dash` is **approved**. Chrome stays `docs/ui-blueprint/blueprint-2` exactly (D-21).

### D-23 OQ-G2 (section 2)

The measurement notice and legal basis for a second seat are **accepted**. Product still requires an explicit `POST /settings/oq-g2` before a non-founder seat or guest is created. Default remains fail-closed (`oq_g2_recorded=false`).

### D-24 Gmail / Slack (section 3)

Proceed with the B12 contract and connection wizard. Live OAuth stays owner-gated. Connectors other than GitHub remain `planned` / `enabled: false` until `GMAIL_OAUTH_CLIENT_ID`, `GMAIL_OAUTH_REDIRECT_URL`, and `SLACK_CLIENT_ID` are supplied. Send/message = approval then receipt.

### D-25 Security pass (section 4)

The Phase 4 security pass is **accepted and proceed** for seats, the wizard, destination classes, and grant ∩ source-permission intersection. It does **not** authorise live write or external Hermes tools as `accepted`. Write/external remain intercept + approval + receipt.

### D-26 In-repo product slug (section 5)

In this repository, the product slug is **papership** and UI copy is **Papership**. Engine Labs remains the company. Do not edit `www.enginelabs.com.au` or Vercel project `enginelabs-au-site`.

Provider residuals until the owner renames them on each dashboard:

- GitHub repository `enginelabs-au/OrgOS` (do not rename the remote from this workstream)
- GitHub App `orgos-dev`
- Vercel project `orgos`
- local config `~/.config/orgos/`
- `GITHUB_APP_REPO` must keep matching the live GitHub repository name
- receipt path `.orgos/loop/` (live App convention)
- historical decision filenames (`2026-09-11-orgos-*.md`)
- blueprint HTML filenames (`OrgOS.dc.html`)

### D-27 OQ-2 first R3 domains

Accept the existing `docs/product.md` §4.3 proposal: B01 strategy/governance and B03 people/capacity are first R3 business domains. Memory manager and adaptive views remain R3 core (PRD-A.15 B.6 / §D).

### D-28 OQ-3 phase-to-release map

Accept R2 = intake 09, R3 = intake 10, R4 = intake 11 + 12. The alternative (R3 = 10+11, R4 = 12) is withdrawn.

### D-29 OQ-4 tier labels

Accept public labels **Free / Basic / Professional / Enterprise** for intake Tier 1–4. **No prices**, allowances, seat counts, or rates appear until the two R4 CA-10 decisions.

### D-30 OQ-G1 public build-log

No public build-log until a later explicit publish decision. Record only.

## Consequences

- Phase 4 implementation may finish T4-2…T4-11 and issue G5.
- Do not generate `docs/plans/phase_5_company_operations_plan.md` until G5 exists.
- Do not fire live write/external Hermes tools from this decision.
