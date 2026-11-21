---
name: draw
description: Draw failing test cases from accepted seams and invariants.
disable-model-invocation: true
---

## Scope

- Covers: converting one accepted `Sxx` into red test cases in the repository test suite.
- Excludes: production code, task planning, review verdicts, design changes, and archived records.

## Workflow

1. Run `<skill-dir>/scripts/iridescent-artifacts undrawn-specs`; if NONE, stop.
2. Read the first listed `Sxx`, its parent `Rxx`, its architecture seam, and the existing test layout.
3. Grill ambiguous seams, assertions, or red commands with the host's structured question tool before writing cases.
4. Enumerate cases at the public seam with explicit coverage for happy, boundary, failure, and shared-seam paths.
5. Write failing tests at the public seam with stable case IDs in test names; keep the exact Red command with each test.
6. Add `Tests: <path>` to the `Sxx` and run `<skill-dir>/scripts/iridescent-artifacts verify-links`.

## Rules

- Write mode: snapshot; rewrite in place with no retired IDs or markers.
- Use stable `Cxx` IDs in test names.
- Process one `Sxx` at a time; write its tests and `Tests:` link atomically.
- Assert observable behavior at the public seam; never mirror internal calls or add production test hooks.
- Cover happy, boundary, failure, provider, consumer, and cross-seam paths when the seam requires them.
- At shared seams, add provider and consumer cases.
- Require one case focused on one observable behavior per Red command.
- Use the host's structured question tool only for blocking case clarification.
- Give 2-4 concrete options, one recommended answer, and a one-line consequence per answer.
- block before writing a case when a clarification fork stays unanswered.
- Require at least one case per recorded failure, plus provider and consumer cases at shared seams.
- Keep mocks and stubs honest.
- Keep every test red for the expected reason; never weaken assertions or skip tests.
- Never edit production source, specs beyond the test link, or task records.

## Verify

- Verify: `verify-links` outputs OK, every case has a Red command, and every case exercises a public seam.
