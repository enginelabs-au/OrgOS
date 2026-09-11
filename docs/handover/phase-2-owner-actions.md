# Phase 2 — what the owner must supply

No secret values belong in git. Put values only in a local `.env` or a secrets manager.

## Already done

- H-6: D-01…D-08 accepted (D-09).
- Product identity: OrgOS (D-10). Engine Labs site left alone.

## H-4 — provider data-use terms

Before OrgOS sends **real company content** to a model provider, record which provider you will use and that you accept their data-use terms (no training on your data, or you accept training).

What I need from you (one line each, no keys):

1. Provider name (for example OpenAI, Anthropic, or OpenRouter).
2. Confirmation: “I accept that provider’s data-use terms for OrgOS prompts and context.”

Until that exists, the worker may only use fixtures. I cannot invent a legal acceptance.

## H-5 — Hermes licence

Hermes is the agent runtime OrgOS wraps. Commercial self-hosted use needs a licence check.

What I need from you:

1. The Hermes version string you want pinned (example: a release tag). I will store only the name `HERMES_VERSION_PIN`.
2. Confirmation: “Hermes may be used commercially for OrgOS self-host.”

Without 1–2 I can write the interception **plan** (already done) but I cannot run a live Hermes spike.

## GitHub App

OrgOS needs a GitHub App installed on `enginelabs-au/OrgOS` so the development loop can open branches and PRs.

What I need from you:

1. Create a GitHub App (GitHub → Settings → Developer settings → GitHub Apps) with repository permissions: Contents read/write, Pull requests read/write, Checks read/write, Metadata read.
2. Install it on `enginelabs-au/OrgOS` only.
3. Put these **names** in local env (values never committed):

| Name | What it is |
|---|---|
| `GITHUB_APP_ID` | App id number |
| `GITHUB_APP_INSTALLATION_ID` | Installation id on this repo |
| `GITHUB_APP_PRIVATE_KEY` | Path to the downloaded `.pem` on your machine |
| `GITHUB_APP_WEBHOOK_SECRET` | Webhook secret if you enable webhooks |

I will wire the names into allowlists in phase 2 T2-3. I cannot create the App under your GitHub org from here without those values.

## Model provider key

| Name | Where it lives | What I need |
|---|---|---|
| `MODEL_PROVIDER_API_KEY` | worker env only, never the browser | Create the key in the provider dashboard and put it in local `.env`. Tell me only that the name is set — do not paste the key into chat. |

## F-G1 usage emit — recommendation

`ENGINE_USAGE_EMIT` is still `0`.

- **On:** OrgOS writes first-party usage rows (identifier/enum only) when jobs run. Useful once the loop is live. Risk: empty or noisy ledger before Hermes exists.
- **Off:** no usage rows. Safer until T2-2 produces real runs.

Recommendation: **leave off** until the first real Hermes run. Say “turn emit on” if you want it earlier.

## Cursor Cloud

See `.cursor/memory/blockers/cursor-cloud-launch.md`. The failure is GitHub access from Cursor Cloud to `enginelabs-au/OrgOS`, not a missing remote on disk.
