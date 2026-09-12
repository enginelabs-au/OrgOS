# security-engineer-subagent evidence — Phase 7

- Install ≠ grant: unpriv still 403 on `/records`.
- Activate 403 with execution flag default off and after trust accept.
- Approve payment 401 without `reauth_at`; 403 without designated authority; `payout` always false.
- Dispatch 403 unavailable.
- SW ignores non-GET; does not claim API POST cache.
- Sign-out calls `wipeOfflineQueue`.
- D-25: no write/external Hermes `accepted` added.
- Residual: PWA token still in web storage (TB-14). Native keychain not exercised on a device.
