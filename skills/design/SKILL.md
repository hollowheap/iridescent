---
name: design
description: Turn brainstorm options into accepted decisions and architecture.
disable-model-invocation: true
---

## Scope

- Covers: observable requirements, accepted decisions, and architecture from approved options.
- Excludes: unresolved forks, specs, task breakdown, implementation, and archived history.

## Workflow

1. Run `<skill-dir>/scripts/iridescent-artifacts status` and `active-decisions`; read `.artifacts/REQUIREMENTS.md`, `.artifacts/ARCHITECTURE.md`, and `.artifacts/BRAINSTORM.md`.
2. Convert Options and Destination into architecture slice H2 groups using `references/REQUIREMENTS.md` and `references/slicing.md`.
3. Resolve repository and tool facts directly, then grill unresolved design forks with the host's structured question tool:
   - Never ask unresolved questions as plain chat text.
   - Ask only independent forks in one call with 2-4 concrete options, one recommended answer, and a one-line consequence per answer.
   - Always block before writing `Dxx` if any fork stays unanswered.
4. Write decisions and architecture with templates from `references/DECISIONS.md` and `references/ARCHITECTURE.md`, respectively.
5. Stop at accepted design and architecture; never record unresolved open decisions.

## Rules

- Write mode: append-only for `Dxx`; history lives in `DECISIONS.md`.
- Record rationale for semantic calls in `DECISIONS.md`.
- Reject implementation names in requirements.
- Requirement H2 headings use architecture slice names.
- Resolve facts from the repository before asking; ask the user only for unresolved design choices.
- Use the host's structured question tool for every blocking design fork.
- Give 2-4 concrete options, one recommended answer, and a one-line consequence per answer.
- block before writing `Dxx` when any design fork stays unanswered.
- Defer seam edge cases to `specify` and task breakdown to `plan`.
- Convert each behavior-changing chat choice into an accepted `Dxx` and attach it to a live `Rxx`.
- Write each `Dxx` and its source in the same invocation.
- Keep retirement state in `DECISIONS.md` only.
- Route retired records to `update`; never place retirement fields in live snapshots.

## Verify

- Verify: requirements define canonical slices, blocking questions are answered, decisions are accepted, and architecture is current.
