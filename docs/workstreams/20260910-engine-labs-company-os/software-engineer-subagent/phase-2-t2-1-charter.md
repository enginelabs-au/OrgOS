# Charter: T2-1 interception spike (phase 2)

- Role: `software-engineer-subagent`
- Risk: Tier 3
- Status: ready to start
- Non-goals: enable side-effecting Hermes toolsets; collect secrets; edit `.cursor/` governance

## Objective

Prove Engine Labs API owns every side effect (SP-1…SP-7) before any Hermes tool that can write, network, or mutate git is enabled.

## Owned paths

- `services/worker/adapter/`
- `services/worker/policy_hooks/`
- `services/worker/config/toolsets.yaml`
- `services/worker/tests/`
- evidence under this directory (`phase-2-*`)

## Validation

- Worker still refuses to start if a side-effecting toolset is enabled without artefact+hash.
- Security re-review required before T2-2 enables tools.
- No `working` registry rows.

## First deliverable

A spike note listing SP-1…SP-7, the interception mechanism choice, and failing-closed tests. Implementation of the chosen mechanism may follow in the same phase after the note exists.
