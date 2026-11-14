---
name: doctor-iridescent
description: Diagnose and repair iridescent workspace layout, legacy `artifacts/` paths, and artifact graph drift.
disable-model-invocation: true
---

## Workflow

1. Inspect the workspace for `AGENTS.md`, `.artifacts/`, legacy `artifacts/`, stray root or lowercase artifact files, and `scripts/artifacts.sh`.
2. If `AGENTS.md` is missing, stop and instruct the user to run `{{skill:init}}`.
3. Run the structural and version-migration checks in `references/checks.md`, including `scripts/artifacts.sh check` and `scripts/artifacts.sh verify-links` when available.
4. Repair layout drift, migrate legacy `artifacts/` or stray/lowercase artifact files into uppercase `.artifacts/*.md`, ensure `.gitignore` ignores `.artifacts/`, and update stale path references in `.artifacts/*.md`.
5. Re-run `scripts/artifacts.sh check` and `scripts/artifacts.sh verify-links` when present, then report repaired items and any gaps requiring `{{skill:update}}`.

## Rules

- Repair structure, filenames, paths, and line budgets only; leave RDST content reconciliation to `{{skill:update}}`.
- Preserve immutable `Rxx`, `Dxx`, `Sxx`, `Txx`, and `Vxx` IDs during any migration.
- Use `git mv` for tracked files and `mv` for untracked files when migrating `artifacts/` into `.artifacts/`.
- Keep both `AGENTS.md` and `.artifacts/CONTEXT.md` under 60 lines.
- Verify: No legacy `artifacts/` directory, lowercase root artifact filename, or stray root artifact remains, `.gitignore` ignores `.artifacts/`, `AGENTS.md` and `.artifacts/CONTEXT.md` are under 60 lines, and `scripts/artifacts.sh check` and `verify-links` output `OK` when available.
