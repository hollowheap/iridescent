# Slice Review Profile

Use when reviewing one canonical vertical slice defined in `.artifacts/requirements.md` and `.artifacts/architecture.md`.

## Scope test

A slice is vertical only when it:

- corresponds to a single user-visible outcome;
- includes every layer needed to deliver it;
- has one end-to-end verification command.

Reject layer-only slices (`all config`, `all packages`), unrelated tool lists, and service inventories. Use `references/seam.md` for cross-cutting boundaries instead of bundling them here.

## Checks

- Does the slice preserve its public boundary invariants end-to-end?
- Does the end-to-end command exercise the claimed outcome?
- Are unrelated tools or services bundled into the slice?

## Failure checks

- Invalid, missing, or hostile inputs are rejected at the boundary.
- Timeouts, retries, idempotency, and cancellation are explicit on external work.
- Partial failures cannot leave half-written or unrecoverable state.
- Concurrency, ordering, and duplicate delivery are handled safely.
- Resources and locks close cleanly on success, error, and shutdown.
- Defaults fail safe; recovery cannot depend on undocumented state.

Report findings at `file:line`; do not convert every finding into a new knob.
