---
document: policy
title: Licensing and Supply Chain
status: proposed
revision: 1
created: 2026-09-10
updated: 2026-09-10
owner_role: security-engineer-subagent
task_id: 20260910-engine-labs-company-os
sources:
  - docs/product.md (PRD-G.9 licensing; PRD-G.7)
  - docs/decisions/2026-09-10-monorepo-layout.md (D-01)
  - docs/plans/phase_0_foundations_plan.md (§15, §16)
  - docs/verification.md (V17-6 licence inventory)
  - docs/ui-blueprint.md (§0.5 fonts; §F keep list)
  - docs/workstreams/20260910-engine-labs-company-os/software-engineer-subagent/evidence.md (EV-S04 `npm ci`; F-S3)
  - docs/workstreams/20260910-engine-labs-company-os/security-engineer-subagent/handoff.md (EV-SEC-07, EV-SEC-11; F-SEC-10, F-SEC-12; T-44, T-47)
---

# Licensing and Supply Chain

Drafted read-only by `security-engineer-subagent` (T0-9); materialized by the orchestrating lead. Status `proposed` until adopted by decision record. Contains no prices.

## 1. Purpose

Set the licence position of Engine Labs Company OS, the obligations toward upstream components, and the controls over dependencies, images, lifecycle scripts and automation that make the shipped artefacts trustworthy.

## 2. Scope

All first-party code in the monorepo (D-01: `apps/desktop`, `services/api`, `services/worker`, `packages/contracts`, `packages/ui`, `infra/`), third-party dependencies across npm, PyPI and crates, container images (including Hermes), fonts and assets, the reference clone `.reference/orgos/`, GitHub Actions workflows, and future SDK distribution.

## 3. Definitions

- Proprietary licence: Engine Labs' commercial licence for the product (PRD-G.9); no price terms appear in this policy.
- Licence inventory: the machine-generated list of dependencies with licence identifiers, versions and sources, plus manual entries for images, fonts and reference material.
- Pin: an immutable reference (exact version in a lockfile, image digest, commit SHA).
- Lifecycle script: any script executed by a package manager during install.

## 4. Normative requirements

### 4.1 Product licence and notices

- LIC-01. First-party code MUST be released under the Engine Labs proprietary licence; each package MUST declare `license: "SEE LICENSE IN LICENSE"` (npm), the equivalent in `pyproject.toml` and `Cargo.toml`, and the repository MUST contain `LICENSE` and `NOTICE` files (PRD-G.9).
- LIC-02. Upstream notices MUST be preserved: the desktop build MUST embed a third-party notices document generated from the licence inventory; the API MUST expose `/licenses` or ship the same document in the image.
- LIC-03. The SDK (`packages/contracts` when published) MUST be independently licensable; its licence MUST be decided by decision record before first external publication (PRD-G.9).
- LIC-04. No dependency under a licence incompatible with proprietary distribution (GPL-family strong copyleft for linked code, SSPL, non-commercial or field-of-use restricted licences) MAY be included in shipped artefacts without a decision record. AGPL components MAY run only as separate network services (e.g. Supabase stack components) with their licences recorded and unmodified sources noted.
- LIC-05. The Hermes agent licence MUST be verified for commercial self-hosted use and recorded in the inventory before phase-2 spike work begins (owner action H-5). If verification fails, D-04 is reopened.
- LIC-06. Fonts MUST be vendored (Inter, JetBrains Mono under SIL OFL 1.1 as recorded in `docs/ui-blueprint.md` §0.5 once verified) and MUST NOT be fetched from external font services at runtime.

### 4.2 Inventory

- LIC-07. A licence inventory MUST be generated in CI for every release using `license-checker` (npm), `pip-licenses` (Python) and `cargo-license` (Rust) (V17-6), with manual entries for container images (Supabase components, Postgres, Hermes, reverse proxy), fonts and any copied code. The inventory MUST be an artefact of the release and MUST include the reference-clone attribution if any design element is derived from `.reference/orgos/`.
- LIC-08. Container images MUST be pinned by digest in `infra/digests.lock`; `HERMES_VERSION_PIN` MUST resolve to a recorded digest, not a mutable tag.
- LIC-09. Lockfiles MUST be committed for every package manager (`package-lock.json`, `uv.lock` or equivalent, `Cargo.lock`) and CI MUST fail on lockfile drift.

### 4.3 Vulnerability management

- LIC-10. CI MUST run `npm audit --audit-level=high`, `pip-audit` and `cargo audit` on every pull request and weekly on the default branch; open high or critical advisories block release unless a decision record accepts the risk with expiry ≤ 30 days (F-SEC-10).
- LIC-11. Dependabot or Renovate MUST be enabled for npm, pip, cargo, GitHub Actions and Docker digests (owner action H-2).
- LIC-12. Product installs MUST use `npm ci --ignore-scripts` by default in CI and developer bootstrap. Packages that require lifecycle scripts (for example native binaries) MUST be allowlisted in `infra/install-scripts-allowlist.json` with a justification and executed in a second explicit step; the allowlist is reviewed by Security at each phase gate. The reference clone install that ran scripts (EV-S04) is accepted as a one-time local action and MUST NOT be repeated by agents (phase plan §15; D-S2).
- LIC-13. The reference clone `.reference/orgos/` MUST remain git-ignored, MUST NOT be imported as a package or copied wholesale (D-01), and its 24 advisories (F-S3) are out of scope for the product; product lockfiles MUST be created fresh from the keep list (F-SEC-12).
- LIC-14. A secret scanner (`gitleaks` or equivalent) MUST run in CI on every pull request; the phase-0 baseline is the clean `rg` scan (EV-SEC-08).

### 4.4 Automation integrity

- LIC-15. GitHub Actions MUST be pinned to full commit SHAs with a version comment; workflow `permissions` MUST be least privilege (`contents: read` default, elevated per job only) (T-44).
- LIC-16. Release signing keys (`TAURI_SIGNING_PRIVATE_KEY`, `TAURI_SIGNING_PRIVATE_KEY_PASSWORD`, `APPLE_*`) and hosting tokens (`DIGITALOCEAN_API_TOKEN`) MUST live only in a protected CI environment with required reviewers; they MUST NOT exist on developer machines used by agents or in any repository file (T-50, T-52).
- LIC-17. Build provenance (SLSA-style attestation or at minimum a signed manifest of artefact digests) SHOULD be produced for desktop and image releases from phase 3.
- LIC-18. The repository control plane (`.cursor/hooks/*`, `.cursor/*.json`, `.github/workflows/*`) remains owner-only; agents MUST NOT modify it (T-43).

### 4.5 Review cadence

- LIC-19. Security reviews the inventory, advisories, allowlist and pins at every phase gate and every release; changes in licence of any dependency MUST be flagged by the inventory diff.
- LIC-20. Any new external service, SDK or model provider MUST be added to the inventory and to DRR-04 before use.

## 5. Verification

- Phase 1: `LICENSE`/`NOTICE` present (LIC-01); inventory job runs (LIC-07); lockfiles committed and drift check (LIC-09); audits in CI (LIC-10); `--ignore-scripts` default with allowlist (LIC-12); secret scanner (LIC-14); Actions pinned (LIC-15, owner); fonts vendored (LIC-06).
- Phase 2: Hermes digest and licence recorded (LIC-05, LIC-08).
- Phase 3: signing key placement and provenance (LIC-16, LIC-17).

## 6. Exceptions

Decision record with named component, reason, compensating control and expiry ≤ 30 days for advisories or ≤ 90 days for licence questions. No exception may ship strong-copyleft linked code under the proprietary licence (LIC-04) or place signing keys outside the protected CI environment (LIC-16).

## 7. In-product licensing-state hook (ERA-17 / Phase 6)

`GET /licenses` returns identifiers and presence flags only (LICENSE, NOTICE, policy path). It does not return secret values, pin strings, or prices. Settings → Docs shows the same identifiers. Policy status remains `proposed` until an owner decision adopts it. After erasure, retain only those identifiers and dates (ERA-17).

## 8. Related decisions and requirements

D-01, D-04; PRD-G.7, G.9; phase plan §15, §16, §17; V17-6; SE F-S3, EV-S04; findings F-SEC-10, F-SEC-11, F-SEC-12; threats T-43…T-47, T-50…T-52.
