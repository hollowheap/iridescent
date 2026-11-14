# Seam Review Profile

Use when reviewing or refactoring a cross-cutting boundary, shared port, schema, CLI contract, or module interface spanning multiple slices.

## Checks

- Does the public boundary invariant hold for every consumer slice?
- Do dependencies point inward (`.artifacts/ARCHITECTURE.md`) without hidden globals or back-channel coupling?
- Are existing consumers protected against silent breaking changes (or migrated together)?
- Is the abstraction justified by multiple real adapters or a true external boundary (`simplicity.md`)?
- Are error semantics, validation responsibilities, and edge-case failure behavior unambiguous on both sides of the seam?

## Evidence

- Cite `file:line` for the seam definition and each consumer boundary.
- Cite consumer or contract tests exercising both valid and failure paths across the seam.

## Verify

Contract and consumer checks pass without bypassing seam invariants or leaking internal types.
