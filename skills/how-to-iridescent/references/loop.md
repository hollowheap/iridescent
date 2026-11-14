# Iridescent Loop

## Entrypoints

- New workspace without `AGENTS.md`: `init` skill
- Broken layout, legacy `artifacts/`, or failed graph checks: `doctor-iridescent` skill
- Single-file reversible edit: `implement` skill (`Quick change`)

## Delivery Loop

1. `brainstorm` skill — frame destination, research primary sources, compare 2-3 archetypes, emit `.artifacts/BRAINSTORM.md`.
2. `design` skill — convert outcomes to `Rxx`, resolve unknowns via the question tool, record accepted `Dxx`, update `.artifacts/ARCHITECTURE.md`.
3. `specify` skill — turn accepted `Dxx` into boundary invariants `Sxx` in `.artifacts/SPECS.md`.
4. `plan` skill — break `Sxx` into atomic vertical tasks `Txx` in `.artifacts/TASKS.md`.
5. `implement` skill — execute `Txx` test-first and hand off review.
6. `review` skill — run `diff`, `slice`, `seam`, or `robust` review after implementation.
7. `update` skill — reconcile RDST artifacts and `.artifacts/CONTEXT.md` with current code.
