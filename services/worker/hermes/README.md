# Hermes pin placeholder

Phase 1 does not install or run Hermes.

- Pin name only: `HERMES_VERSION_PIN` (value supplied by the owner at phase 2; never commit the value).
- No API keys, no provider credentials, no image digest secrets belong in this directory.
- The worker adapter interfaces exist; no Hermes client is wired.
