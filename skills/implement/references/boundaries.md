# Implementation Boundaries

Load when changes touch APIs, persistence, auth, hot paths, or rendered UI.

## API & Transport

- Validate edge input; use one error envelope with semantic status code mapping.
- Make timeout, retries, idempotency, and cancellation explicit.

## Data & Persistence

- Prefer expand-and-contract changes; bound lock and backfill work.
- Use transactions or idempotency for partial failure; close connections on every path.

## Security

- Validate untrusted input and authorize at the operation with least privilege.
- Keep secrets and stack traces out of outputs; avoid new exposure.
- Preserve every safety check when simplifying.

## Performance

- Measure before optimizing; keep blocking work and startup bounded.
- Remove N+1 calls and unbounded loops.

## UI

- Use semantic markup, keyboard order, contrast, touch target sizing, and reduced-motion support.
