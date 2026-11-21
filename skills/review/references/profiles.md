# Review Profiles

Profiles set scope and persistence for deeper reviews. The main review workflow handles changed hunks without a profile.

## Profile matrix

| Profile | Inputs | Persistent? | Vxx | Review record |
|---|---|---|---|---|
| slice | one slice, architecture section, changed hunks | only if durable | only if durable | findings only |
| seam | cross-cutting contract or port, consumers, architecture section | only if durable | only if durable | findings only |
| robust | canonical slice roster, relevant architecture and evidence | yes | always | findings only |

## Review IDs and Design Forks

- Stable IDs are `Vxx`.
- Persistent reviews receive `Vxx` and are indexed in `.artifacts/REVIEWS.md`.
- Report unresolved design unknowns as blocking findings routed to `design`.

## Lenses

Lenses add checks for the territory the change reaches. Every lens shares the shape: Territory, Triggers, Checks, Evidence, Verify.

- Architecture (`architecture.md`): slices, inward dependencies, ports, composition roots.
- API (`api.md`): endpoints, schemas, validation, error envelopes, timeouts.
- Data (`data.md`): schemas, migrations, transactions, queries, pool lifecycles.
- Security (`security.md`): trust boundaries, auth, secrets, redaction, exposure.
- Performance (`performance.md`): hot paths, large data, startup, measured regressions.
- Tests (`tests.md`): red-to-green proof, public-seam assertions, honest doubles.
- UI (`ui.md`): rendered markup, styles, layout, focus, motion, tokens.

Simplicity is always on; see `references/simplicity.md`.

## Token budget

- Default changed-hunk review: no full architecture or review-history reads; no review document.
- Persistent profiles: read only the relevant slice, seam, or robust scope.
