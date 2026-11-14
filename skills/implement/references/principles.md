# Implementation Principles

## Simplicity & Minimal Surface

- Inline single-caller logic; introduce helpers, interfaces, or options only when backed by multiple callers, adapters, or requirements.
- Use the standard library or existing workspace dependencies before introducing a new package.
- Keep diffs strictly surgical and scoped to the lines required by the task; never refactor unrelated code or reformat untouched blocks.
- Comment only non-obvious invariants, protocol constraints, or trade-offs, never control-flow narration.

## Architecture & Seams

- Keep changes strictly inside the owning vertical slice and respect inward dependency direction.
- Keep core domain logic free of HTTP transport, database clients, ORMs, and CLI/framework glue.
- Read configuration, environment variables, and mutable globals strictly at the composition root; pass dependencies explicitly into domain logic.
- Hide internal data structures and storage mechanics behind narrow module boundaries.

## Boundaries, Data & Operations

- **API & Transport**: Validate schemas at the edge, keep handlers thin, map domain errors to a uniform error envelope, and set explicit timeouts, retries, and cancellation on outbound calls.
- **Data & Persistence**: Wrap multi-step writes in a transaction or make them idempotent on retry; use expand-and-contract steps for schema or state changes; close connections, cursors, and pools on error and shutdown.
- **Security**: Enforce authz and input validation strictly at trust boundaries; never hardcode or log secrets, tokens, or raw credentials.
- **Performance**: Bound batch sizes, pagination, and in-memory buffers; keep collection queries batched (no N+1 queries) and reuse allocations on hot paths.
- **UI**: Use semantic elements, preserve keyboard focus and ARIA state, and use existing design tokens.
