---
name: how-to-iridescent
description: Explain the iridescent lifecycle and current workspace state.
disable-model-invocation: true
---

## Scope

- Covers: read-only onboarding explanation of the lifecycle and current workspace state.
- Excludes: routing, workspace repair, artifact edits, and implementation.

## Workflow

1. Inspect the workspace for `AGENTS.md` and `.artifacts/`; locate the CLI at `<skill-dir>/scripts/iridescent-artifacts`.
2. Run `<skill-dir>/scripts/iridescent-artifacts status` when the CLI is available.
3. Explain the lifecycle and current workspace state using `references/loop.md`.

## Rules

- Remain strictly read-only.
- Explain; do not assign the next skill.
- Keep the explanation concise: workspace state, lifecycle stage, and relevant records.
- Resolve the CLI from `<skill-dir>/scripts/iridescent-artifacts`; never assume the workspace root.

## Verify

- Verify: response states current workspace readiness and lifecycle stage.
