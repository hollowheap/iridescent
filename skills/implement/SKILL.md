---
name: implement
description: Implement the next task test-first.
disable-model-invocation: true
---

## Scope

- Covers: implementing the next unblocked task and small reversible quick changes with verified tests.
- Excludes: design decisions, specs, planning, review verdicts, and unrelated refactors.

## Workflow

1. Run `<skill-dir>/scripts/iridescent-artifacts next-task`; stop immediately if `NONE`.
2. Read only the task, parent spec, decision, and cited architecture section; route missing contracts or forks to `specify` or `design`.
3. Load `references/principles.md` for non-trivial edits, plus `references/boundaries.md` when touching APIs, storage, auth, hot paths, or UI.
4. Run assigned drawn tests via `references/tdd.md` and confirm red before editing production code.
5. Implement minimal clean code via surgical hunk edits, keeping refactors separate from feature work.
6. Rerun checks until green, self-audit `git diff`, append a receipt, and run `complete Txx`.
7. Pass minimal task and diff context (not session history) to read-only review and fix findings.

## Rules

- Use the quick path only for single-file reversible edits with a clear verify; keep the same proof standard.
- Append task completions and quick changes to `.artifacts/tasks/quick.md` with `references/QUICK-CHANGE.md`.
- Use CLI handoff; do not reread unrelated snapshots.
- Write completion only after verification and review acceptance.
- Mark completion with CLI `complete Txx`; never edit `TASKS.md` directly.
- Self-audit only the diff using triggered boundary checks, including UI contrast, focus, keyboard, and reduced motion.

- Follow `references/tdd.md` for non-trivial behavior, bugs, and real seams; trivial one-liners and Quick changes may use the task verify.
- Load `references/principles.md`, `references/tdd.md`, and triggered `references/boundaries.md`.
- Never ask the user during implementation; escalate missing contracts or forks strictly to `specify` or `design`.
- Reproduce failures first, then prove fixes with the same command.
- Test strictly observable behavior at the public seam; never mirror private implementation steps.
- Read strictly the task, spec, decision, cited architecture section, and target slice files from `next-task`.
- Keep implementation edits separate from read-only review; pass only clean task and diff context to review.
- Apply surgical hunk edits; never refactor unrelated code or append design, spec, or review breakdowns to `TASKS.md`.
- Start only unblocked tasks from `next-task`; complete each task through the CLI.

## Verify

- Verify: red check went green, diff self-audit and task verify pass, review accepts, receipt is written, and CLI marks `Txx` done.
