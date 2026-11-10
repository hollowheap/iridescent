# Review Profiles

Profiles set scope and persistence. Lenses add territory-specific checks. Simplicity is an always-on check.

## Profile matrix

| Profile | Inputs | Persistent? | Vxx | Review record | Q writes |
|---|---|---|---|---|---|
| diff | parent task/spec, changed hunks, one verification | no | only if durable Qxx | none | only by promoting to Vxx |
| slice | `R/D/S/T`, relevant architecture section, diff | only if durable | only if durable | findings only | real design unknowns only |
| robust | full relevant design/architecture/evidence | yes | always | findings only | may write |

## Review IDs

- Stable IDs are `Vxx`.
- Only persistent reviews receive one: robustness, architecture/workspace audit, durable slice review.
- Diff reviews are ephemeral and receive `Vxx` only if they emit a durable `Qxx`.
- `artifacts/reviews.md` maps `Vxx` to file, mode, and scope.

## Q-write rules

- Review may write `Qxx` to `artifacts/questions.md` under `### Review Vxx — <slice>`.
- Review never creates `Dxx`, `Sxx`, or `Txx`.
- No local review resolution IDs; resolution remains `Qxx -> Dxx`.

## Lenses

Lenses add checks for the territory the change reaches. They do not change scope, persistence, or review IDs. Every lens has the same shape: Territory, Triggers, Checks, Evidence, Verify, Skip.

- Backend: transport and service boundaries.
- Security: trust boundaries, auth, secrets, exposure, persistence.
- Performance: hot paths, large data, startup, repeated work, measured regressions.
- UI: rendered markup, styles, components, layout, focus, motion, tokens.

Simplicity is an always-on check, not a lens; see `references/simplicity.md`.

## Lens ledger

Every review records one row per lens. Diff reviews include the table in the response. Persistent reviews write it under `## Lens ledger` in the review document.

| Lens | Status | Reason |
|---|---|---|
| backend | `considered` / `loaded` / `skipped` | Trigger result or skip reason |
| security | `considered` / `loaded` / `skipped` | Trigger result or skip reason |
| performance | `considered` / `loaded` / `skipped` | Trigger result or skip reason |
| ui | `considered` / `loaded` / `skipped` | Trigger result or skip reason |
| simplicity | `loaded` | Always on |

Status meanings:

- `loaded`: triggers matched and the checks ran.
- `considered`: triggers were absent; no checks were needed.
- `skipped`: triggers matched but the checks did not run. The reason is mandatory.

Do not omit a row. A skipped lens without a row is an unreported gap.

## Token budget

- diff: no full architecture or review-history reads; no review document; stop at no high/medium findings; low notes one line or omitted.
- slice/robust: read only the relevant architecture section and review scope; persist `Vxx` and findings only when durable or required.

## Simplicity checks

See `references/simplicity.md`. Always on for every profile; lenses change breadth and depth, not whether the check exists.
