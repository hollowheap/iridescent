# Implementation Principles

## Simplicity & Minimal Surface

- Inline single-caller logic; do not add 1:1 pass-through helpers, single-adapter interfaces, or speculative options.
- Use the standard library or existing workspace dependencies before introducing a new package.
- Keep diffs surgical; do not refactor unrelated code or reformat untouched blocks.
- Comment only non-obvious invariants, protocol constraints, or trade-offs; never narrate control flow.

## Architecture & Seams

- Keep changes inside the owning vertical slice and respect inward dependency direction.
- Keep core domain logic free of HTTP transport, database clients, ORMs, and CLI/framework glue.
- Wire configuration and external clients at the composition root; never read environment variables or mutable globals inside domain logic.
- Hide internal data structures and storage mechanics behind narrow module boundaries.

## Boundaries, Data & Operations

- **API & Transport**: Validate schemas at the edge, keep handlers thin, map domain errors to a uniform error envelope, and set explicit timeouts, retries, and cancellation on outbound calls.
- **Data & Persistence**: Wrap multi-step writes in a transaction or make them idempotent on retry; use expand-and-contract steps for schema or state changes; close connections, cursors, and pools on error and shutdown.
- **Security**: Enforce authz and input validation at trust boundaries; never hardcode or log secrets, tokens, or raw credentials.
- **Performance**: Bound batch sizes, pagination, and in-memory buffers; avoid N+1 queries and unnecessary allocations on hot paths.
- **UI**: Use semantic elements, preserve keyboard focus and ARIA state, and use existing design tokens.
