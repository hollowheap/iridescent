---
name: doctor-iridescent
description: Publish canonical workspace end state and route drift to lifecycle skills.
disable-model-invocation: true
---

## Scope

- Covers: canonical workspace target state, layout drift naming, and routing gaps to lifecycle skills.
- Excludes: deriving truth from current files, RDST content reconciliation, design changes, and implementation.

## Workflow

1. Load the canonical target state from `references/slicing.md` and `references/artifacts.md`; treat current files as evidence only.
2. Inspect the workspace only to identify drift from that target.
3. Run structural checks in `references/checks.md`, including `check` and `verify-links` when available.
4. Emit a target-state request listing required records, detail files, links, owning skills, and observed drift.
5. Stop; lifecycle skills perform repairs and doctor re-checks only after requested work completes.

## Rules

- Never infer the canonical end state from current workspace contents.
- Canonical target: root records under `.artifacts/`, per-spec ledgers, per-task details, superseded entries marked in place, and the coupling in `references/slicing.md`.
- Required coupling: every in-scope `Rxx` has `Dxx`; every `Dxx` has `Sxx` or an accepted no-spec outcome; every `Sxx` has a ledger; every `Cxx` has `Txx`; every `Txx` has detail and case links; every `Supersedes` and `Covers` target resolves.
- Route each gap: `Rxx` or `Dxx` to `design`, `Sxx` to `specify`, ledgers or cases to `draw`, `Txx` or detail links to `plan`, stale code-to-spec content to `update`.
- Preserve immutable `Rxx`, `Dxx`, `Sxx`, `Txx`, and `Vxx` IDs during migration.
- Use `git mv` for tracked files and `mv` for untracked files when migrating `artifacts/` into `.artifacts/`.
- Keep both `AGENTS.md` and `.artifacts/CONTEXT.md` under 60 lines.
- Never invent `scripts/iridescent-artifacts` if the host harness or project omits it; report its absence explicitly.
- Route supersession and stale-code gaps to `update`; never repair content directly.
- Verify: the target-state request names required records and owning skills, `check` and `verify-links` output `OK` when available, no active parent references a superseded ID, and no drift is treated as authority.
