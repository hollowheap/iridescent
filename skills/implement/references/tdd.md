# TDD Rules

Use for non-trivial production changes with an already-drawn failing check.

## Red → green

1. Run the assigned drawn test or reproducible check; if absent, route to `draw`.
2. Confirm the failure is the expected one.
3. Implement the minimum clean production change.
4. Rerun the same check and confirm green.
5. Run the broader suite and the task verify.

## Reproduction

Reproduce the reported failure with a drawn test or command before editing production code. If no test seam exists, record the reproduction command and route the regression test to `draw`.

## Config and eval work

Use the failing `nix eval`, `nix build`, or task verification command directly as the red check when a unit test is not meaningful.

## Mutation check

For high-impact behavioral invariants, temporarily invert one production condition, rerun the task verify to prove a test fails, and restore the file immediately before review handoff.

## Exceptions

Skip test-first strictly when no failing check can be expressed beforehand. Record the reason in task notes and always run the task verification command.
