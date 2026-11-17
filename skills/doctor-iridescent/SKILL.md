---
name: doctor-iridescent
description: Diagnose and repair iridescent workspace layout, legacy `artifacts/` paths, and artifact graph drift.
disable-model-invocation: true
---

## Scope

- Covers: repairing workspace layout, migrating legacy `artifacts/` paths, and fixing artifact graph or link drift.
- Excludes: RDST content reconciliation, design changes, and implementation.

## Workflow

1. Inspect the workspace for `AGENTS.md`, `.artifacts/`, legacy `artifacts/`, stray root RDST records, and `scripts/iridescent-artifacts`.
2. If `AGENTS.md` is missing, stop and instruct the user to run the `init` skill.
3. Run the structural and version-migration checks in `references/checks.md`, including `scripts/iridescent-artifacts check` and `scripts/iridescent-artifacts verify-links` when available.
4. Repair layout drift, migrate legacy `artifacts/` or misplaced RDST records to `.artifacts/<RECORD>.md`, ensure `.gitignore` ignores `.artifacts/`, validate linked detail files, and update stale path references in `.artifacts/*.md`.
5. Re-run `scripts/iridescent-artifacts check` and `scripts/iridescent-artifacts verify-links` when present, then report repaired items and any gaps requiring the `update` skill.

## Rules

- Repair structure, RDST record paths, and line budgets only; leave RDST content reconciliation to the `update` skill.
- Preserve immutable `Rxx`, `Dxx`, `Sxx`, `Txx`, and `Vxx` IDs during any migration.
- Use `git mv` for tracked files and `mv` for untracked files when migrating `artifacts/` into `.artifacts/`.
- Keep both `AGENTS.md` and `.artifacts/CONTEXT.md` under 60 lines.
- Never invent `scripts/iridescent-artifacts` if the host harness or project omits it; report its absence explicitly.
- Verify: RDST records live at `.artifacts/{CONTEXT,ARCHITECTURE,BRAINSTORM,REQUIREMENTS,DECISIONS,SPECS,TASKS,REVIEWS}.md`, test ledgers live under `.artifacts/tests/`, task details live under `.artifacts/tasks/`, `.gitignore` ignores `.artifacts/`, `AGENTS.md` and `.artifacts/CONTEXT.md` are under 60 lines, and `scripts/iridescent-artifacts check` and `verify-links` output `OK` when available.
