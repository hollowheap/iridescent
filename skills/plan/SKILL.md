---
name: plan
description: Turn live specs into atomic verified tasks.
disable-model-invocation: true
---

## Scope

- Covers: converting accepted specs into atomic, verified tasks in `.artifacts/TASKS.md`.
- Excludes: specs, design decisions, clarification, implementation, review, and archived tasks.

## Workflow

1. Run `<skill-dir>/scripts/iridescent-artifacts undrawn-specs`; return to `draw` if any remain, then run `unconverted-specs` and `unconverted-decs`.
2. Derive `Txx` from `Sxx` and its test file; stop if a contract, test file, architecture section, or verify command is missing.
3. Resolve facts from the repository directly; route ambiguous contracts to `specify`, `design`, or `draw`.
4. Run `<skill-dir>/scripts/iridescent-artifacts next-id t` to obtain sequential `Txx` IDs.
5. Append tasks and details with templates from `references/TASKS.md` and `references/task-detail.md`, respectively.
6. Run `<skill-dir>/scripts/iridescent-artifacts check`, `verify-links`, and `frontier`.

## Rules

- Write mode: snapshot; rewrite in place with no retired IDs or markers.
- Treat `TASKS.md` as the single verification source.
- Sharpen every `Verify` field to a non-human executable command from the start; write zero stubs.
- Reference live `Sxx` IDs only; never plan against archived IDs.
- Split refactor work from feature work.
- Write each task, its detail file, and its blockers in the same invocation.
- Never grill during planning; route clarification to `specify`, `design`, or `draw`.
- Edit strictly `.artifacts/TASKS.md` and `.artifacts/tasks/<Txx>.md`; never mark parent specs or decisions complete.

## Verify

- Verify: `<skill-dir>/scripts/iridescent-artifacts check` and `verify-links` output OK, `undrawn-specs` outputs `NONE`, and `frontier` lists ready tasks.
