# Slice Boundaries

## Definitions

- A slice is one user-observable outcome with one end-to-end verification.
- A sub-slice is an independently verifiable outcome inside the same module boundary.
- A sub-slice does not create a new public contract unless it has an independent observable seam.
- A deep module owns one narrow public interface and hides its sub-slices behind it.

## Cardinality

- One `Rxx` is one slice or sub-slice outcome.
- One `Rxx` may have many `Dxx`.
- One `Dxx` may yield many `Sxx`.
- One `Sxx` may cite many `Dxx`.
- Create `Sxx` per public seam, never one per decision by default.
- One `Sxx` may yield many `Cxx`.
- One `Txx` may cover many `Cxx` when they share a seam, module, and verify command.
- Split `Txx` when outcomes, owners, or rollback units differ.

## Size Gates

- A slice is too big when it needs multiple rollback units, multiple seams without a shared invariant, or no single end-to-end verification.
- A slice is too small when it changes only a private helper with no observable outcome.
- Promote an outcome to a sub-slice when it has independent verification but shares the parent module boundary.
- Keep a sub-slice private when it only decomposes implementation within the parent seam.

## Coupling

- Each skill writes child records and parent links in one invocation.
- `design` writes `Rxx`, `Dxx`, and architecture together.
- `specify` writes `Sxx` and its parent IDs together.
- `draw` writes the ledger and `Ledger:` link together.
- `plan` writes `Txx`, detail file, `Cases:` links, and blockers together.
- `implement` changes only the active `Txx` checkbox after verification and review.

## Supersession

- Supersede immutable IDs; never silently rewrite them.
- One `Rxx` or `Sxx` may declare `Supersedes: <old-id>`.
- A superseded record stays in its live root file; its replacement names it with `Supersedes:`.
- Agents skip superseded entries; the active graph references non-superseded IDs only.
- Retire `Sold` only after `Snew` covers each `Sold` case with `Covers:` and fresh red proof.
- Migrate or recreate active `Txx` records before marking `Sold` superseded.

## Target State

- Doctor emits the canonical target state from this contract and `references/artifacts.md`.
- Current workspace state is evidence of drift, not authority.
- Required end state: every in-scope `Rxx` has `Dxx`; every `Dxx` has `Sxx` or an accepted explicit no-spec outcome; every `Sxx` has a ledger; every `Cxx` has a `Txx`; every `Txx` has detail and case links.
- Each gap names the owning lifecycle skill.
- Lifecycle skills resolve gaps; doctor never treats current files as truth.
- Superseded records remain in live root files as unidirectional `Supersedes` targets.
