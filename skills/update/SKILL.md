---
name: update
description: Reconcile RDST artifacts with code and architecture.
disable-model-invocation: true
---

## Workflow

1. Inspect workspace reality: `git status`, recent commits, manifests, build runners, and entrypoints.
2. Run essential build, check, and targeted test commands in the shell to confirm they pass.
3. Reconcile `AGENTS.md`, `.artifacts/CONTEXT.md`, and `.artifacts/ARCHITECTURE.md` with workspace reality using `references/template.md`.
4. Verify every `Dxx` is accepted and backed by specs or code; resolve any orphaned open decision via `{{skill:design}}`.
5. Reconcile requirements, specs, and tasks in place after executing their verification commands; keep task records minimal.
6. Run `scripts/artifacts.sh verify-links` and refresh persistent review records for changed slices.

## Rules

- Follow the section structure and `<= 60` line budgets for `AGENTS.md` and `.artifacts/CONTEXT.md` in `references/template.md`.
- Keep `AGENTS.md` focused on high-signal agent guidance: verified build/test/single-test commands, non-obvious repo invariants, and safety rules.
- Put multi-step task runbooks into a project skill and keep one pointer line in `AGENTS.md`.
- Use surgical `sed -i` for flipping `- [ ]` to `- [x]` after running the item's verification check in the shell.
- Keep requirement, decision, spec, and task IDs immutable.
- Verify: `scripts/artifacts.sh verify-links` outputs OK, `AGENTS.md` and `.artifacts/CONTEXT.md` match `references/template.md` (`<= 60` lines each), no orphaned open decisions remain, and persistent review records reflect changed slices.
