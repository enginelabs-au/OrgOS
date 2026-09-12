# Decision D-35: Trial rate card

## Status

`accepted` — owner-directed 2026-09-13. Trial publication only. Charges stay off.

## Decision

1. Public tier labels are **Free / Pro / Max / Enterprise** (supersedes D-29 Basic / Professional for display).
2. Trial list prices and included tokens are published in Settings → Plan and `GET /billing/rate-card`.
3. Token pools step about **4×** between Free → Pro → Max (mid of the 2–5× industry band). Max is the 5× seat-price analogue.
4. Enterprise is **US$32 / seat / month**, **5 seat minimum**, **400,000 tokens / seat / month pooled**.
5. Paid plans sell **US$10 usage-credit packs** at the plan overage rate when the included pool is exhausted. Free has no overage.
6. **Usage 1–5** raise the monthly overage ceiling (1× → 16×), same shape as OpenAI / Google spend unlocks.
7. `ENGINE_BILLING_CHARGES_ENABLED` stays `0`. `/billing/charge` stays 403.

## Numbers

| Plan | USD / month | Tokens / month | Overage / 100k |
|---|---|---|---|
| Free | 0 (1 seat) | 50,000 org | none |
| Pro | 24 / seat | 200,000 / seat | US$8 |
| Max | 120 / seat | 800,000 / seat | US$6 |
| Enterprise | 32 / seat (min 5) | 400,000 / seat pooled | US$5 |

AUD display uses 1.5 × USD for operator chrome only.
