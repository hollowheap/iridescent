---
name: draw
description: Draw failing tests from accepted seams and invariants.
disable-model-invocation: true
---

## Scope

- Covers: converting one accepted `Sxx` into red test cases and a linked ledger.
- Excludes: production code, task planning, review verdicts, and design changes.

## Workflow

1. Run `scripts/iridescent-artifacts undrawn-specs`; if NONE, stop.
2. Read the first listed `Sxx`, its parent `Rxx` and `Dxx`, its architecture seam, the recorded `Behavior` and `Failures`, and the existing test layout.
3. Enumerate cases for happy path, boundary, failure propagation, provider side, consumer side, and one cross-seam path using `references/cases.md`.
4. Write one failing test per case at the public seam without production changes.
5. Run each case alone; record the exact red command and observed failure in `tests/<Sxx>.md`.
6. Add `Ledger: tests/<Sxx>.md` to the `Sxx` details and run `scripts/iridescent-artifacts verify-links`.

## Rules

- Process one `Sxx` at a time.
- Assert observable behavior only; never mirror internal steps.
- Require one case focused on one observable behavior and a Red command per case.
- Require at least one case for every recorded failure and both sides of a shared seam.
- Keep every test red for the expected reason; never weaken assertions or skip tests.
- Never edit production source, specs beyond the ledger link, or task records.
- Verify: `verify-links` outputs OK, every `Sxx` case has a red command, and no case is written without a public seam.
