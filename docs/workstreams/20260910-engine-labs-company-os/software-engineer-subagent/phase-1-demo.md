# T1-19 Demonstration evidence (development level)

Recorded 2026-09-11. No GUI quit/reopen walkthrough (Cloud/local limitation). Substitutes are automated tests.

| R1-ACC | Demo step | Evidence | Gap |
|---|---|---|---|
| 1 | Sign in with strong factor | `SignInForm` + JWT tests; Founder seat seed | Live IdP / TOTP not run |
| 2 | Create priority and plan | `services/api/tests/test_ledger.py` | Desktop create flow not driven in browser |
| 3 | Start background job | `test_jobs.py` persist-before-202 + SSE | No packaged window |
| 4 | Unprivileged refused | `test_authz.py` five surfaces | Second human not used |
| 5 | Restart / reconnect | store reopen + SSE `last_event_id`; cancel ≠ disconnect | No desktop quit |

Screenshots: not captured this pass. Ordinary-language empty states exist on all five desktop views.
