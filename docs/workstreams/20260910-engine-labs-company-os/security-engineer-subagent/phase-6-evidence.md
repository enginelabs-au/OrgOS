# Security Engineer evidence — Phase 6

| Control | Verdict | Evidence |
|---|---|---|
| Allowance create is org.admin | PASS | `test_unpriv_cannot_create_allowance` |
| Entitlement/allowance ≠ grant | PASS | `test_allowance_is_not_permission` |
| Duplicate reserve refused | PASS | 409 |
| Charge path disabled | PASS | `/billing/charge` 403; `charges_enabled` false |
| Rate card unpublished | PASS | `entries: []` |
| Licenses: identifiers only | PASS | no pin value, no prices |
| Stripe secrets in repo | PASS | names in `.env.example` only |
| Write/external Hermes `accepted` | residual | D-25 still binding |
| CA-4 live provider reconcile | residual | no Stripe webhook; test-mode structure only |
