---
name: plan
description: Turn specs into atomic verified tasks.
disable-model-invocation: true
---

## Workflow

1. Run `scripts/artifacts.sh unconverted-specs`; if NONE, run `unconverted-decs`.
2. Derive `Txx` from `Sxx`. If a spec has no contract, architecture section, or verify command, stop.
3. Route any missing contract or design fork back to `{{skill:specify}}` or `{{skill:design}}`; use the question tool only when task splitting, dependency ordering, or verification command choice is genuinely ambiguous.
4. Run `scripts/artifacts.sh next-id t` to obtain sequential `Txx` IDs.
5. Append atomic vertical tasks to `.artifacts/tasks.md` under the slice H3 heading (see `references/examples.md` only if the format is unclear); keep the task record minimal.
6. Run `scripts/artifacts.sh check` and `scripts/artifacts.sh frontier`.

## Rules

- Every task references its parent `Sxx`. Put blockers in a trailing `[Txx, Tyy]`; omit the bracket when unblocked.
- Keep tasks minimal: outcome, verify, files, notes, risk. Do not add requirements, design, spec, or review breakdowns.
- No stubs. A task must have a verifiable outcome and command from the start.
- Keep tasks atomic; split a task that satisfies unrelated specs.
- Ask questions only when task granularity, dependency ordering, or verification command selection is ambiguous; never re-litigate accepted specs or decisions.
- Never mark parent specs or decisions complete; conversion is derived from references.
- Verify: `scripts/artifacts.sh check` outputs OK and `frontier` lists ready tasks.
