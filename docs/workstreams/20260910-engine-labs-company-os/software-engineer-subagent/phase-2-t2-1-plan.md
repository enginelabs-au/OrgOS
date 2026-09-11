# T2-1 plan: interception spike SP-1…SP-7

Status: `planned` (Cloud venue blocked; written locally 2026-09-11).  
Source: Security phase-0 handoff §9.  
Charter: `phase-2-t2-1-charter.md`.  
Do not enable `side_effecting_toolsets` until Security re-review of this spike.

## Current substrate

- `services/worker/config/toolsets.yaml`: `interception_verified: false`; all five named toolsets disabled.
- `policy_hooks/startup.py`: refuse start if any toolset is enabled without artefact path + sha256 match.
- `adapter/interfaces.py`: `UnwiredAdapter` — no Hermes client.
- Worker has no DB credentials (D-08).

## Mechanism choice (provisional)

Until a pinned Hermes version is available (owner: `HERMES_VERSION_PIN` value, H-5):

1. Prefer a **server-enforced approval hook** (SP-2/SP-3) if the pin exposes pause + SSE args + block-until-`/approval`.
2. Else **disable side-effecting toolsets server-side** and implement R1 git/worktree effects only through the Engine Labs API action service (SP-4).
3. Do not treat model refusal as policy.

This remains `provisional` until SP-1 inventory exists against the pin.

## SP coverage

| ID | Proof | How | Blocked on |
|---|---|---|---|
| SP-1 | Inventory of side-effecting tools | Call `GET /v1/toolsets` and `GET /v1/capabilities` on the pin; write `phase-2-t2-1-inventory.md` | Hermes pin + licence (H-5) |
| SP-2 | Server-enforced approval hook | One gated run; raw SSE; pause before named tool; deny/timeout refuses | Pin + model key name |
| SP-3 | API owns the approval | Adapter creates Engine Labs action, records approval, then forwards; never-forward ⇒ Hermes refuses | SP-2 true |
| SP-4 | Disable path if no hook | Terminal/browser/github/files_write/email_send stay disabled; run that asks for terminal fails with policy error | SP-2 false |
| SP-5 | Injection | Fixture in `services/worker/tests/` (and MEM-22) must be refused by policy, not the model | SP-3 or SP-4 |
| SP-6 | Egress | Sandbox to a non-allowlisted host fails; record in compose/network test | Live Compose + Docker |
| SP-7 | Artefact | Commit digest + toolsets.yaml hash + transcripts; set `interception_artefact` only after Security PASS | SP-1…SP-6 |

## Tests to add when the pin exists

- Existing: startup refusal (keep).
- New: inventory snapshot; never-forward approval; policy error (not model) on disabled terminal; injection fixture; egress deny.

## Non-goals

Hermes install, GitHub App, Hey Engine runtime, usage emit, enabling any toolset.

## Cloud venue

`Task(environment=cloud)` failed 2026-09-11: no GitHub access token for `enginelabs-au/OrgOS`. Owner: grant Cursor Cloud GitHub access to that org/repo, then relaunch. Local planning is this file.
