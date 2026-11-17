---
name: design
description: Resolve design forks into accepted decisions and architecture.
disable-model-invocation: true
---

## Scope

- Covers: observable requirements, accepted decisions, and architecture for accepted design changes.
- Excludes: unresolved design forks, specs, task breakdown, and implementation.

## Workflow

1. Run `scripts/iridescent-artifacts status`; read `.artifacts/REQUIREMENTS.md`, `.artifacts/ARCHITECTURE.md`, and `.artifacts/BRAINSTORM.md` when present.
2. Convert observable outcomes into requirements using `references/requirements.md`, grouped by canonical vertical-slice H3 headings; reject any requirement that names a framework, module, file, or API.
3. Grill architectural and design forks (system shape, vertical slices, module seams, stack choices, data contracts, and operations/security) with the host's structured question tool; ask only independent forks in one call with 2-4 options, a recommendation, and answer consequences, block before writing `Dxx` if any choice remains unanswered.
4. Record strictly accepted decisions with `references/decision.md` under the exact architecture H2 heading; omit `Arch:` and `Verify:` fields because the H3 and child specs carry them.
5. Update `.artifacts/ARCHITECTURE.md` with `references/architecture.md` for accepted design changes; record vertical slice ownership, inward seams, and composition roots.
6. Stop at accepted design and architecture; never record unresolved open decisions.

## Rules

- Requirements describe strictly observable outcomes, acceptance, constraints, and non-goals, never implementation choices.
- Vertical-slice H3 headings in `.artifacts/REQUIREMENTS.md` define the canonical slice roster for downstream specs, tasks, and reviews.
- Decisions are accepted only; resolve every architectural or design fork via the host's structured question tool before writing `Dxx`, and defer seam-level edge cases to the `specify` skill and task breakdown to the `plan` skill. An accepted decision may stay `[ ]` only until its child specs complete.
- Design covers system shape, vertical slices, module seams, framework and library choices, data contracts, and operations.
- Any behavior-changing decision made in chat becomes an accepted `Dxx` before the next action. If it has no parent `Rxx`, stop and ask for the requirement.
- `Sxx` derives from accepted `Rxx`, `Dxx`, and architecture; `Txx` derives from `Sxx`.
- Verify: requirements define canonical vertical slices with strictly observable outcomes (no design choices), all blocking questions are answered, only accepted decisions exist, and `.artifacts/ARCHITECTURE.md` is current.
