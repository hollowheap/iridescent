# Implementation Principles

Always load before writing non-trivial code; self-audit `git diff` against every section before review handoff.

## Simplicity & Anti-Slop

- Inline shallow 1:1 wrappers, single-caller helpers, and single-adapter interfaces with no second consumer or test seam.
- Reject speculative flags, env vars, unread options, duplicate cross-layer validation, and unneeded dependencies when stdlib or workspace tools suffice.
- Apply the deletion test: keep structural depth only for multiple real adapters, an external boundary, a measured bottleneck, or a concurrency or compliance invariant.
- Delete dead code in touched files (unused imports, flags, branches, unreachable helpers) without reformatting or refactoring untouched blocks.
- Apply Chesterton's Fence: prove why an existing guard, invariant, or ordering exists before removing or simplifying it.
- Preserve outputs, errors, side effects, and ordering when simplifying; keep existing tests passing unchanged.
- Separate behavior-preserving refactors from feature changes into distinct steps; use named remedies (inline seam, collapse duplicate branches, replace condition chains with a model or dispatcher, move logic to owner, reuse canonical helper).
- Comment only non-obvious invariants, protocol constraints, or trade-offs; never narrate control flow or restate code.

## Architecture & Seams

- Keep changes inside the owning vertical slice; keep core domain logic free of HTTP transport, DB clients, ORMs, and CLI/framework glue.
- Point dependencies inward: domain defines ports, adapters implement them, and domain logic runs in memory without DB drivers or HTTP servers.
- Read configuration, environment variables, and mutable globals strictly at the composition root; pass dependencies explicitly into domain logic.
- Design deep modules that hide internal state and storage mechanics behind narrow public seams; protect or migrate all existing consumers together.

## Slice Failure & Enforcement

- Validate and reject invalid, missing, or hostile inputs at the boundary; ensure defaults fail safe without undocumented state.
- Guard multi-step or external work against partial failure so half-written or unrecoverable state cannot persist.
- Handle concurrency, ordering, and duplicate delivery explicitly; close connections, cursors, locks, and pools cleanly on success, error, and shutdown.
- Fix recurring mistakes at the highest effective layer (architecture, types, lint/CI naming the replacement, tests, then docs); prove new guards fail on real past mistakes and require a reason, expiry date, and human approval for exceptions.
