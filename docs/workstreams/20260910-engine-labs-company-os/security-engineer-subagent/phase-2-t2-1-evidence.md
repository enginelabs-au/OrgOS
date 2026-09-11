# T2-1 Security evidence

Reviewer: security-engineer-subagent ([T2-1 Security re-review](c0785649-3b53-4d9e-9bc4-4d1f449c76a4))  
Time: 2026-09-11T11:36Z

| EV | Claim | Result |
|---|---|---|
| EV-T21-SEC-02 | `interception_verified` false; five toolsets disabled | VERIFIED |
| EV-T21-SEC-03 | Artefact hashes match | VERIFIED |
| EV-T21-SEC-04 | `:9119` `/health`, `/v1/capabilities`, `/v1/toolsets` → 302 login | VERIFIED |
| EV-T21-SEC-05 | Both adapters refuse `start_run` | VERIFIED |
| EV-T21-SEC-06 | Startup refuses enabled toolset without artefact | VERIFIED |
| EV-T21-SEC-08 | persist-before-forward unit only | PARTIAL |
| EV-T21-SEC-11 | Registry `unavailable` | OPEN |

Findings F-T21-SEC-01…09 in the handoff. No high/critical in refuse-closed posture.
