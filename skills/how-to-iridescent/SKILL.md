---
name: how-to-iridescent
description: Explain the iridescent lifecycle loop and recommend the next skill for the current workspace.
disable-model-invocation: true
---

## Workflow

1. Inspect the workspace for `AGENTS.md`, `.artifacts/`, and `scripts/artifacts.sh`.
2. Run `scripts/artifacts.sh status` when `scripts/artifacts.sh` is available.
3. Explain the current stage and name the next skill to invoke using `references/loop.md`.

## Rules

- Read-only guidance; never modify files or artifact state.
- Route missing `AGENTS.md` to `{{skill:init}}` and broken `.artifacts/` layout or legacy `artifacts/` paths to `{{skill:doctor-iridescent}}`.
- Route single-file reversible edits to `{{skill:implement}}` Quick change; route design or multi-slice work through `references/loop.md`.
- Keep the explanation concise: workspace state, recommended next skill, and matching stage flow.
- Verify: Response states current workspace readiness, the next skill, and its entry condition.
