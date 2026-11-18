---
name: update
description: Reconcile RDST artifacts with code and architecture.
disable-model-invocation: true
---

## Scope

- Covers: reconciling `.artifacts/` records with workspace reality, superseding stale records, and rewriting live snapshots.
- Excludes: design forks, new requirements, implementation, and review.

## Workflow

1. Inspect workspace reality: `git status`, recent commits, manifests, build runners, and entrypoints.
2. Run essential build, check, and targeted test commands in the shell to confirm they pass.
3. Reconcile `.artifacts/CONTEXT.md` and `.artifacts/ARCHITECTURE.md` with workspace reality using `references/template.md`.
4. Verify every `Dxx` is accepted and backed by specs or code; resolve orphaned open decisions via the `design` skill.
5. Complete supersession: confirm `Rnew` or `Snew`, confirm `Covers:` red proof, migrate active `Txx`, record `Supersedes:` on the replacement, and remove stale parent links.
6. Reconcile requirements, specs, and tasks in place after executing their verification commands; keep task records minimal.
7. Run `scripts/iridescent-artifacts verify-links` and refresh persistent review records for changed slices.

## Rules

- Follow the section structure and `<= 60` line budgets strictly for `AGENTS.md` and `.artifacts/CONTEXT.md` in `references/template.md`.
- Keep requirement, decision, spec, and task IDs strictly immutable; never renumber existing IDs.
- Superseded `Rxx` and `Sxx` remain in live root files and are named by active `Supersedes:` fields.
- Active records declare `Supersedes: <old-id>`.
- Agents skip superseded entries during normal work.
- Active records never reference superseded IDs as parents.
- Retire an old spec only after its replacement ledger covers every old case with `Covers:` and fresh red proof.
- Rewrite root records as live snapshots after all active tasks migrate; never leave stale entries for agents to read.
- Verify: `verify-links` outputs OK, no active parent references a superseded ID, and superseded entries are clearly marked.
