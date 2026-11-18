---
name: plan
description: Turn specs into atomic verified tasks.
disable-model-invocation: true
---

## Scope

- Covers: converting accepted specs into atomic, verified tasks in `.artifacts/TASKS.md`.
- Excludes: specs, design decisions, implementation, and review.

## Workflow

1. Run `scripts/iridescent-artifacts undrawn-specs`; if undrawn specs remain, return to the `draw` skill; then run `unconverted-specs` and `unconverted-decs` as needed.
2. Derive `Txx` from `Sxx` and its ledger. If a spec has no contract, ledger, architecture section, or verify command, stop.
3. Route any missing contract or design fork back to the `specify` or `design` skill; use the host's structured question tool only when task splitting, dependency ordering, or verification command choice is genuinely ambiguous, never ask unresolved questions as plain chat text, give 2-4 concrete options, one recommended answer, and a one-line consequence per answer, and block until answered.
4. Run `scripts/iridescent-artifacts next-id t` to obtain sequential `Txx` IDs.
5. Append atomic vertical tasks to `.artifacts/TASKS.md` under the slice H3 heading with `Detail: tasks/<Txx>.md` and `Cases: Cxx` lines (see `references/examples.md` only if the format is unclear); keep the task record minimal.
6. Run `scripts/iridescent-artifacts check`, `verify-links`, and `frontier`.

## Rules

- Every task references its parent `Sxx`. Include a trailing `[Txx, Tyy]` blocker bracket only when blocked; omit it when unblocked.
- Include strictly `outcome`, `verify`, `files`, `notes`, `risk`, `detail`, and `cases`; never add requirements, design, spec, or review breakdowns.
- The detail fields are contract: keep `detail` before `cases` and preserve exact field names.
- Require a concrete verifiable outcome and command from the start; write zero stubs.
- Active `Txx` records must reference live `Sxx` IDs; never plan against superseded IDs.
- Group cases by seam, module, and verify command; one `Txx` may cover many cases when they share all three.
- Split a task that satisfies unrelated specs, owners, or rollback units.
- Write each `Txx`, its detail file, its `Cases:` links, and its blockers in the same invocation.
- Ask questions strictly when task granularity, dependency ordering, or verification command selection is ambiguous; use the host's structured question tool with 2-4 options, a recommendation, and answer consequences, and never re-litigate accepted specs or decisions.
- Edit only `.artifacts/TASKS.md`; never mark parent specs or decisions complete (conversion is derived strictly from child references).
- Verify: `scripts/iridescent-artifacts check` and `verify-links` output OK, undrawn-specs output is `NONE`, and `frontier` lists ready tasks.
