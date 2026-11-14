# TDD Rules

Use for non-trivial behavior, bug fixes, and any change where a failing check can be written at the seam.

## Red -> green

1. Write the smallest failing test or reproducible check at the public seam.
2. Run it and confirm it fails for the expected reason.
3. Implement the minimum production change.
4. Rerun the same check and confirm green.
5. Run the broader suite and the task verify.

## Bug fixes

Reproduce the reported failure with a failing test or command before editing. Fix the root cause, then rerun the same reproduction as proof. If no test seam exists, record the reproduction command and add a regression check where possible.

## Config and eval work

Use the failing `nix eval`, `nix build`, or task verification command directly as the red check when a unit test is not meaningful; never invent a test that merely restates the generated config.

## Test quality

- Assert observable behavior strictly at the public seam with one meaningful assertion per behavior; never mirror implementation steps.
- Keep tests deterministic and independent of host state unless the task is explicitly integration-level.
- One small test is enough for a branch, loop, parser, money, security, or data-loss path.
- Trivial one-liners may use the task verify directly.

## Exceptions

Skip test-first strictly when no failing check can be expressed beforehand; record the reason in task notes and always run the task verification command (never use this exception to avoid verification).
