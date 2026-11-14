---
name: design
description: Define outcomes, decisions, and architecture.
disable-model-invocation: true
---

## Workflow

1. Run `scripts/artifacts.sh status`; read `.artifacts/requirements.md`, `.artifacts/architecture.md`, and `.artifacts/brainstorm.md` when present.
2. Convert observable outcomes into requirements using `references/requirements.md`, grouped by canonical vertical-slice H3 headings; reject any requirement that names a framework, module, file, or API.
3. Grill adaptively with the question tool on architectural and design forks (system shape, vertical slices, module seams, stack choices, data contracts, and operations/security) until every fork is resolved; block before writing `Dxx` if any choice remains unanswered.
4. Record accepted decisions with `references/decision.md`, grouped under the exact architecture H2 heading; omit `Arch` and `Verify` because the H3 and child specs carry them.
5. Update `.artifacts/architecture.md` with `references/architecture.md` for accepted design changes; record vertical slice ownership, inward seams, and composition roots.
6. Stop at accepted design and architecture; never record unresolved open decisions.

## Rules

- Requirements describe observable outcomes, acceptance, constraints, and non-goals; never implementation choices.
- Vertical-slice H3 headings in `.artifacts/requirements.md` define the canonical slice roster for downstream specs, tasks, and reviews.
- Decisions are accepted only; resolve every architectural or design fork via the question tool before writing `Dxx`, and defer seam-level edge cases to `{{skill:specify}}` and task breakdown to `{{skill:plan}}`. An accepted decision may stay `[ ]` until its child specs complete.
- Design covers system shape, vertical slices, module seams, framework and library choices, data contracts, and operations.
- Any behavior-changing decision made in chat becomes an accepted `Dxx` before the next action. If it has no parent `Rxx`, stop and ask for the requirement.
- `Sxx` derives from accepted `Rxx`, `Dxx`, and architecture; `Txx` derives from `Sxx`.
- Verify: requirements define canonical vertical slices with no design choices, all blocking questions are answered, no open decisions exist, and architecture is current.
