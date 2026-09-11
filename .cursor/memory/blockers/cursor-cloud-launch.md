# Blocker: Cursor Cloud cannot open `enginelabs-au/OrgOS`

## Symptoms

1. Early: `environment: "cloud" requires exactly one known git remote; found 0` even though `git remote -v` showed `origin https://github.com/enginelabs-au/OrgOS.git`.
2. After `6306a6c` on `origin/main`: `No GitHub access token found with access to repository enginelabs-au/orgos` (cloud subagent `bc-51c02bcc-5917-412e-b24c-1ec765576ce3`).

The Mac repo is fine. Cloud runs on a Cursor VM that clones via **Cursor’s GitHub App**, not your local `git`.

## What you need to do

1. GitHub → organization **enginelabs-au** → Settings → GitHub Apps (or Third-party access) → **Cursor**.
2. Grant the Cursor GitHub App access to repository **OrgOS** (not only personal repos).
3. If the org uses SAML SSO: **Authorize** the Cursor app for `enginelabs-au`.
4. In Cursor: Settings → Account / Integrations → GitHub → confirm `enginelabs-au/OrgOS` is listed.
5. On [cursor.com](https://cursor.com) start a Cloud agent on `enginelabs-au/OrgOS` `main` once.

I cannot complete those org-admin clicks from this agent.

## Local fallback

T2-1 plan is in `docs/workstreams/20260910-engine-labs-company-os/software-engineer-subagent/phase-2-t2-1-plan.md`. Phase 2 implementation can continue locally after owner H-4/H-5/GitHub App/model key (see `docs/handover/phase-2-owner-actions.md`).

## Resolution criteria

A Cloud Task starts and can read this repo, **or** you accept local-only phase 2.
