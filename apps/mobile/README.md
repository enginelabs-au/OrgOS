# Papership mobile shells

Wraps the live `apps/web` blueprint-2 client (`/papership`) for iOS and Android. Same authenticated cloud API. Cloud jobs never run on-device.

## What this is

- Tauri 2 mobile project at `src-tauri/tauri.conf.json`
- Frontend dist: `apps/web/dist`
- Icons: reused `brand/papership-icon.png` outputs already in `apps/desktop/src-tauri/icons/`
- Tokens belong in the OS keychain/keystore. OAuth opens the system browser.
- Biometric unlock may gate an existing session only. It does not mint grants.

## Simulator / emulator

1. `npm run build --workspace @papership/web`
2. `node apps/mobile/scripts/check-toolchain.mjs`
3. If Xcode is present: `npx tauri ios dev` from this directory (Apple signing is owner-only for device/store).
4. If Android SDK is present: `npx tauri android dev`

G11 accepts this toolchain report when a simulator cannot be launched on the agent host. App Store / Play Store submission is not in this phase.

## Capacitor fallback

Not activated. Use only if the Tauri mobile spike fails on this toolchain. Do not start a third UI stack.
