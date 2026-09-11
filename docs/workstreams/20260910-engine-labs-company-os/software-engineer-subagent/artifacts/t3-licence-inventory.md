# V17-6 licence inventory (Phase 3)

Date: 2026-09-11  
Method: lockfile + first-party LICENSE read. `license-checker` not installed. `pip-licenses` not used (avoid inventing a full tree).

| Component | Licence / note | Pin source |
|---|---|---|
| First-party Papership | Engine Labs proprietary (`LICENSE`) | repo |
| Hermes Agent | commercial self-host (D-11) | `v0.21.1` / git `20f7ef4d` |
| FastAPI | MIT (upstream) | `services/api/pyproject.toml` `>=0.115,<0.120` |
| Uvicorn | BSD-3 (upstream) | same |
| PyJWT | MIT (upstream) | same |
| Pydantic | MIT (upstream) | same |
| Worker / API Python | `uv.lock` present | `services/*/uv.lock` |
| Web / desktop npm | `package-lock.json` present | workspace |
| Papership ui-blueprint clone | LIC-12/13 — do not re-run reference server | `docs/ui-blueprint/` |
| Marketing site `enginelabs.com.au` | out of scope | — |

Full SPDX dump is an owner/CI action if required before publication.
