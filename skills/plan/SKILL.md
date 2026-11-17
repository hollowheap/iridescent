---
name: plan
description: Turn specs into atomic verified tasks.
disable-model-invocation: true
---

## Scope

- Covers: converting accepted specs into atomic, verified tasks in `.artifacts/TASKS.md`.
- Excludes: specs, design decisions, implementation, and review.

## Workflow

1. Run `scripts/iridescent-artifacts unconverted-specs`; if NONE, run `unconverted-decs`.
2. Derive `Txx` from `Sxx`. If a spec has no contract, architecture section, or verify command, stop.
3. Route any missing contract or design fork back to the `specify` or `design` skill; use the question tool only when task splitting, dependency ordering, or verification command choice is genuinely ambiguous.
4. Run `scripts/iridescent-artifacts next-id t` to obtain sequential `Txx` IDs.
5. Append atomic vertical tasks to `.artifacts/TASKS.md` under the slice H3 heading (see `references/examples.md` only if the format is unclear); keep the task record minimal.
6. Run `scripts/iridescent-artifacts check` and `scripts/iridescent-artifacts frontier`.

## Rules

- Every task references its parent `Sxx`. Include a trailing `[Txx, Tyy]` blocker bracket only when blocked; omit it when unblocked.
- Include strictly `outcome`, `verify`, `files`, `notes`, and `risk`; never add requirements, design, spec, or review breakdowns.
- Require a concrete verifiable outcome and command from the start; write zero stubs.
- Keep tasks atomic; split a task that satisfies unrelated specs.
- Ask questions strictly when task granularity, dependency ordering, or verification command selection is ambiguous; never re-litigate accepted specs or decisions.
- Edit only `.artifacts/TASKS.md`; never mark parent specs or decisions complete (conversion is derived strictly from child references).
- Verify: `scripts/iridescent-artifacts check` outputs OK and `frontier` lists ready tasks.
