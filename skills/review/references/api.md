# API Lens

## Territory

HTTP/RPC endpoints, queue consumers, schedulers, and external transport boundaries.

## Triggers

- The diff adds or changes a handler, RPC method, consumer, or scheduler entrypoint.
- The diff changes a request/response schema, status code, error envelope, timeout, or retry policy.

## Checks

- Define and validate all request, query, path, and payload schemas at the transport edge.
- Keep handlers thin: validate input, invoke a domain service, and map the result.
- Map domain errors to semantic status codes using one uniform error envelope.
- Make external-call timeouts, retries, idempotency keys, and cancellation explicit.

## Evidence

- Cite `file:line` for the schema, handler, error mapping, and timeout/retry configuration.

## Verify

Boundary tests cover valid payloads, invalid inputs (400/422), domain error mapping, and timeout/retry behavior.
