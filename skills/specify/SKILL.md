---
name: specify
description: Turn accepted requirements into live public-boundary specs.
disable-model-invocation: true
---

## Scope

- Covers: converting accepted requirements into live public-boundary specs in `.artifacts/SPECS.md`.
- Excludes: design decisions, task planning, implementation, review, and archived snapshots.

## Workflow

1. Run `<skill-dir>/scripts/iridescent-artifacts unconverted-reqs`; if output is NONE, stop immediately.
2. Derive `Sxx` from accepted `Rxx` and architecture using `references/slicing.md`; reach `Dxx` through that requirement.
3. Resolve facts from the repository directly, then grill ambiguous seams with the host's structured question tool:
   - Never ask unresolved questions as plain chat text.
   - Give 2-4 concrete options, one recommended answer, and a one-line consequence per answer.
   - Block until answered; return to `design` if an answer changes design.
4. Run `<skill-dir>/scripts/iridescent-artifacts next-id s` to obtain sequential `Sxx` IDs.
5. Append public invariants with template from `references/SPECS.md` under the owning module-seam H3.
6. Run `<skill-dir>/scripts/iridescent-artifacts check` to verify trace links and graph shape.

## Rules

- Write mode: snapshot; rewrite in place with no retired IDs or markers.
- Keep seam names stable across live snapshots.
- Specify strictly public seams and external invariants, including failure paths.
- Write zero stubs; resolve missing verification via `design` before writing `Sxx`.
- Use the host's structured question tool only for blocking seam clarification.
- Give 2-4 concrete options, one recommended answer, and a one-line consequence per answer.
- block before writing a spec when a clarification fork stays unanswered.
- Keep `.artifacts/SPECS.md` as a live snapshot; never write retirement fields here.
- Route retired specs to `update` for archive migration; never plan against archived IDs.

## Verify

- Verify: `<skill-dir>/scripts/iridescent-artifacts check` outputs OK and `unconverted-specs` lists the new items.
