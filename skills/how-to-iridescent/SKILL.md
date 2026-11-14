---
name: how-to-iridescent
description: Explain the iridescent lifecycle loop and recommend the next skill for the current workspace.
disable-model-invocation: true
---

## Workflow

1. Inspect the workspace for `AGENTS.md`, `.artifacts/`, and `scripts/iridescent-artifacts`.
2. Run `scripts/iridescent-artifacts status` when `scripts/iridescent-artifacts` is available.
3. Explain the current stage and name the next skill to invoke using `references/loop.md`.

## Rules

- Remain strictly read-only: inspect workspace state and report the next skill without modifying files or artifact state.
- Route missing `AGENTS.md` to the `init` skill and broken `.artifacts/` layout or legacy `artifacts/` paths to the `doctor-iridescent` skill.
- Route single-file reversible edits to the `implement` skill (`Quick change`); route design or multi-slice work through `references/loop.md`.
- Keep the explanation concise: workspace state, recommended next skill, and matching stage flow.
- Verify: Response states current workspace readiness, the next skill, and its entry condition.
