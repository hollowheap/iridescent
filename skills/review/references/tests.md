# Tests Lens

## Territory

Automated tests, verification checks, fixtures, and test doubles.

## Triggers

- The diff adds or edits tests, fixtures, or verification scripts.
- The diff claims a bugfix, behavioral invariant, or public contract change.

## Checks

- Assert observable behavior at the public seam rather than mirroring private implementation steps or config literals.
- Bugfixes and behavioral invariants include a check that fails before the fix and passes after.
- Exercise boundary failure paths and edge conditions (empty, invalid, concurrent, error), not only the happy path.
- Keep mocks/stubs honest so they do not mask real schema, serialization, or contract mismatches.
- Never skip tests, weaken assertions, or disable compiler/lint gates to force a pass.

## Evidence

- Cite test `file:line` and the exact verification command and observed output.

## Verify

Target tests and task verification pass cleanly without skipped assertions or relaxed checks.
