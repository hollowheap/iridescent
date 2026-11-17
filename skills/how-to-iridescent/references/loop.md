# Iridescent Loop

## Entrypoints

- New workspace without `AGENTS.md`: `init` skill
- Broken layout, legacy `artifacts/`, or failed graph checks: `doctor-iridescent` skill
- Single-file reversible edit: `implement` skill (`Quick change`)

## Delivery Loop

Structured questions run before design records are written.
The loop requires red cases before tasks.

1. `brainstorm` skill — frame destination, research primary sources, compare 2-3 archetypes, emit `.artifacts/BRAINSTORM.md`.
2. `design` skill — convert outcomes to `Rxx`, resolve unknowns via the question tool, record accepted `Dxx`, update `.artifacts/ARCHITECTURE.md`.
3. `specify` skill — turn accepted `Dxx` into boundary invariants `Sxx` in `.artifacts/SPECS.md`.
4. `draw` skill — turn one `Sxx` into red cases in `.artifacts/tests/<Sxx>.md`.
5. `plan` skill — break `Sxx` cases into atomic vertical tasks `Txx` in `.artifacts/TASKS.md`.
6. `implement` skill — turn assigned red cases green and hand off review.
7. `review` skill — run `diff`, `slice`, `seam`, or `robust` review after implementation.
8. `update` skill — reconcile RDST artifacts and `.artifacts/CONTEXT.md` with current code.
