---
name: update
description: Reconcile RDST artifacts with code and architecture.
disable-model-invocation: true
---

## Scope

- Covers: reconciling `AGENTS.md` and `.artifacts/` records with workspace reality, code, and verification.
- Excludes: design forks, new requirements, implementation, and review.

## Workflow

1. Inspect workspace reality: `git status`, recent commits, manifests, build runners, and entrypoints.
2. Run essential build, check, and targeted test commands in the shell to confirm they pass.
3. Reconcile `AGENTS.md`, `.artifacts/CONTEXT.md`, and `.artifacts/ARCHITECTURE.md` with workspace reality using `references/template.md`.
4. Verify every `Dxx` is accepted and backed by specs or code; resolve any orphaned open decision via the `design` skill.
5. Reconcile requirements, specs, and tasks in place after executing their verification commands; keep task records minimal.
6. Run `scripts/iridescent-artifacts verify-links` and refresh persistent review records for changed slices.

## Rules

- Follow the section structure and `<= 60` line budgets strictly for `AGENTS.md` and `.artifacts/CONTEXT.md` in `references/template.md`.
- Keep in `AGENTS.md` strictly high-signal guidance: verified build/test/single-test commands, non-obvious repo invariants, and all global "Never ..." safety rules (never move safety rules into skills, never include `.artifacts/` pointers, and never write test pass counts in `AGENTS.md`).
- Keep `.artifacts/CONTEXT.md` limited strictly to `## Stack & Entrypoints` and `## Module Seams` (document strictly high-level seams and entrypoints, never internal functions or `## Commands`).
- Put multi-step task runbooks into a project skill and keep one pointer line in `AGENTS.md`.
- Every `Dxx` in `.artifacts/DECISIONS.md` is accepted only (staying `[ ]` strictly until child specs complete); never leave orphaned open decisions.
- Flip `- [ ]` to `- [x]` strictly via surgical `sed -i` and only after executing the item's verification check in the shell.
- Keep requirement, decision, spec, and task IDs strictly immutable and append-only (never renumber existing IDs).
- Verify: `scripts/iridescent-artifacts verify-links` outputs OK, `AGENTS.md` and `.artifacts/CONTEXT.md` match `references/template.md` (`<= 60` lines each), no orphaned open decisions remain, and persistent review records reflect changed slices.
