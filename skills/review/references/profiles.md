# Review Profiles

Profiles set scope and persistence. Lenses add territory-specific checks. Simplicity is an always-on check.

## Profile matrix

| Profile | Inputs | Persistent? | Vxx | Review record |
|---|---|---|---|---|
| diff | parent task/spec, changed hunks, one verification | no | only if durable debt | none |
| slice | one canonical slice (`R/D/S/T`), architecture section, diff | only if durable | only if durable | findings only |
| seam | cross-cutting contract/port, consumers, architecture section, diff | only if durable | only if durable | findings only |
| robust | canonical slice roster, full relevant architecture/evidence | yes | always | findings only |

## Review IDs and Design Forks

- Stable IDs are `Vxx`.
- Persistent reviews (`robust`, or durable `slice`/`seam` audits) receive `Vxx` and are indexed in `.artifacts/REVIEWS.md`.
- Diff reviews are ephemeral; promote to `Vxx` only when durable debt or a cross-slice gap must be tracked.
- Report unresolved design unknowns as **blocking findings** routed strictly to the `design` skill (`Dxx`) before completion; write only `Vxx` and `.artifacts/review/<slice>.md` (never write `Rxx`, `Dxx`, `Sxx`, or `Txx` during review).

## Lenses

Lenses add checks for the territory the change reaches. Every lens shares the shape: Territory, Triggers, Checks, Evidence, Verify.

- Architecture (`architecture.md`): vertical slices, inward dependencies, ports/adapters, composition roots.
- API (`api.md`): endpoints, RPC, consumers, request/response schemas, edge validation, error envelopes, boundary timeouts/retries.
- Data (`data.md`): persistence, DB schemas, migrations, transactions, queries, connection/pool lifecycles.
- Security (`security.md`): trust boundaries, auth, secrets, error redaction, network exposure, permissions.
- Performance (`performance.md`): hot paths, large data, startup, repeated work, measured regressions.
- Tests (`tests.md`): red-to-green proof, public-seam assertions, edge coverage, honest doubles, gate integrity.
- UI (`ui.md`): rendered markup, styles, components, layout, focus, motion, tokens.

Simplicity is an always-on check, not a lens; see `references/simplicity.md`.

## Lens ledger

Account for every lens without omitting skipped gaps:

- **Diff reviews:** emit one compact line:
  `Lenses: loaded=[simplicity, ...]; skipped=[lens: reason]; considered=[...]`
- **Persistent reviews (`slice`, `seam`, `robust`):** include a `## Lens ledger` table (`Lens | Status | Reason`) with one row per lens (`loaded`, `considered`, or `skipped` with mandatory reason) plus `simplicity | loaded | Always on`.

## Token budget

- `diff`: no full architecture or review-history reads; no review document; stop when zero high/medium findings remain; low notes one line or omitted.
- `slice` / `seam` / `robust`: read only the relevant slice/seam architecture section and scope; persist `Vxx` and findings only when durable or required.
