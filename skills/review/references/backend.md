# Backend Lens

## Territory

Endpoints, services, transport, and persistence boundaries.

## Triggers

- The diff adds or changes an HTTP handler, RPC method, queue consumer, scheduler, or persistence call.
- The diff changes a request or response schema, error envelope, timeout, retry, or pool lifecycle.
- The diff moves logic across a transport or service seam.

## Checks

- Request and response schemas are defined at the transport boundary.
- Handlers stay thin: validate input, invoke a domain service, map the result.
- Business logic and queries live in pure service functions decoupled from `Request` and `Response`.
- Every input is validated at the edge, including query and path parameters.
- Domain errors map to semantic status codes with one uniform error envelope.
- Stack traces, database errors, and credentials stay out of client responses.
- Timeouts, idempotency, retries, and pool shutdown are explicit.
- Tests exercise the seam rather than HTTP mocks of the implementation.

## Evidence

- Cite `file:line` for the schema, handler, service, and error mapping.
- Cite the test command and the failing branch it covers.

## Verify

Endpoint tests cover valid input, invalid payloads (400/422), expected domain errors, timeout behavior, and clean shutdown.

## Skip

Skip when the diff reaches no endpoint, service, transport, or persistence boundary.
