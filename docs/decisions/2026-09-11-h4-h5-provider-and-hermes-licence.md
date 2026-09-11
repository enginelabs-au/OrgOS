# Decision D-11: H-4 provider terms and H-5 Hermes commercial use

## Status

`accepted` — owner-directed 2026-09-11.

Workstream: `docs/workstreams/20260910-engine-labs-company-os/manifest.md`.

## Context

H-4 (DRR-06) requires a recorded provider and owner acceptance of that provider’s data-use terms before Papership sends real company prompts or context to a model. H-5 (LIC-05) requires confirmation that Hermes may be used commercially for Papership self-host.

Health probes do not send customer content. Live T2-2 runs will.

## Decision

1. **H-4 provider:** OpenRouter. That is the model gateway already wired on the existing Hermes VPS (not a second Papership key). OpenRouter may route to an upstream model; those calls still leave the tenant.
2. **H-4 acceptance:** superseded in part by D-12. The owner accepts that **OpenRouter** (and any later integration) handles data under **that vendor’s** terms. Engine Labs does not take responsibility for integration-held data.
3. **H-5:** Hermes Agent **v0.21.1** may be used commercially for Papership self-host. Pin name: `HERMES_VERSION_PIN=v0.21.1`.
4. Papership does not store a `MODEL_PROVIDER_API_KEY`. Credentials stay on the VPS Hermes install.

## Assumption

If the droplet was later switched off OpenRouter to a native Anthropic or OpenAI key, replace the provider name in a follow-up decision. Do not paste keys into chat.

## Consequences

- Fixtures are no longer required solely for missing H-4/H-5.
- T2-1 (interception spike) may start on owner “go”.
- Real customer content still waits until T2-2 after SP-1…SP-7 and Security re-review.
