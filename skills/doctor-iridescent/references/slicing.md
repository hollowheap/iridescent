# Slice Boundaries

## Definitions

- A slice is one user-observable outcome with one end-to-end verification.
- A sub-slice is an independently verifiable part of the same module boundary.
- A deep module owns one narrow public seam and hides its sub-slices.

## Chain

- `Dxx` states the accepted decision.
- `Rxx [Dxx]` states the observable requirement.
- `Sxx [Rxx]` states the public invariant and its `Tests:` link.
- `Txx [Sxx] [Txx...]` delivers the invariant and names blockers.

## Cardinality

- One `Dxx` may have many `Rxx`.
- One `Rxx` may have many `Sxx`.
- One `Sxx` may have many `Txx`.
- One `Txx` belongs to one `Sxx`.

## Split Rules

- Split when rollback units, owners, or public seams differ.
- Keep private helper work inside the parent slice.
- Create one `Sxx` per public seam, not per decision.
- Give each `Txx` one seam and one verify command.
