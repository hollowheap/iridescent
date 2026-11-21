# Slice Boundaries

## Definitions

- A slice is one user-observable outcome with one end-to-end verification.
- A sub-slice is an independently verifiable part of the same module boundary.
- A deep module owns one narrow public seam and hides its sub-slices.

## Chain

- `Dxx` states the accepted decision.
- `Rxx [Dxx]` states the observable requirement.
- `Sxx [Rxx]` states the public invariant.
- `Cxx` proves one observable behavior of its `Sxx`.
- `Txx [Sxx] [Cxx...] [Txx...]` delivers cases and names blockers.

## Cardinality

- One `Dxx` may have many `Rxx`.
- One `Rxx` may have many `Sxx`.
- One `Sxx` may have many `Cxx`.
- One `Cxx` belongs to one `Sxx` and one `Txx`.
- One `Txx` may cover many `Cxx` under one `Sxx`.

## Split Rules

- Split when rollback units, owners, or public seams differ.
- Keep private helper work inside the parent slice.
- Create one `Sxx` per public seam, not per decision.
- Let one `Txx` cover many cases when they share a seam and verify command.
