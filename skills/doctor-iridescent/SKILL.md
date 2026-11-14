---
name: doctor-iridescent
description: Diagnose and repair iridescent workspace layout, legacy `artifacts/` paths, and artifact graph drift.
disable-model-invocation: true
---

## Workflow

1. Inspect the workspace for `AGENTS.md`, `.artifacts/`, legacy `artifacts/`, stray root artifacts, and `scripts/artifacts.sh`.
2. If `AGENTS.md` is missing, stop and instruct the user to run `{{skill:init}}`.
3. Run the structural and version-migration checks in `references/checks.md`, including `scripts/artifacts.sh check` and `scripts/artifacts.sh verify-links` when available.
4. Repair layout drift, migrate legacy `artifacts/` or stray root artifacts into `.artifacts/`, ensure `.gitignore` ignores `.artifacts/`, and update stale path references in `AGENTS.md` and `.artifacts/*.md`.
5. Re-run `scripts/artifacts.sh check` and `scripts/artifacts.sh verify-links` when present, then report repaired items and any gaps requiring `{{skill:update}}`.

## Rules

- Repair structure, paths, pointers, and rule violations only; leave RDST content reconciliation to `{{skill:update}}`.
- Preserve immutable `Rxx`, `Dxx`, `Sxx`, `Txx`, and `Vxx` IDs during any migration.
- Use `git mv` for tracked files and `mv` for untracked files when migrating `artifacts/` into `.artifacts/`.
- Keep `.artifacts/context.md` under 60 lines and move any `## Commands` section into `AGENTS.md` `## Essential Commands`.
- Never invent `scripts/artifacts.sh` if the host harness or project does not provide it; report its absence explicitly.
- Verify: No legacy `artifacts/` directory or stray root artifact remains, `.gitignore` ignores `.artifacts/`, `AGENTS.md` points to `.artifacts/`, and `scripts/artifacts.sh check` and `verify-links` output `OK` when available.
