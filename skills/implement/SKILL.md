---
name: implement
description: Worker implements the next task test-first.
disable-model-invocation: true
---

## Workflow

1. Run `scripts/iridescent-artifacts next-task`; if NONE, stop immediately.
2. Read only the task, parent spec, decision, and cited architecture section. If a missing contract or unresolved design fork blocks the task, stop and route back to the `specify` or `design` skill.
3. For non-trivial changes, load `references/principles.md` and write the smallest failing seam check via `references/tdd.md`, confirming red; skip `references/tdd.md` for trivial one-liners.
4. Implement the minimum production code required to satisfy the invariant using targeted hunk edits.
5. Rerun the same check until green, then run the task verify and broader suite; hand the final review to the `review` skill.
6. Apply minimal review fixes; mark the task complete only after the test/verify and final review are accepted.
7. Stop; parent specs and decisions are derived from references.

## Quick change

Use only when the change is one file or a small reversible edit with a clear verify.

1. State the change and the failing check, if one is meaningful.
2. Make the minimal edit; no new public option, API, dependency, or artifact.
3. Run the verify. If it fails twice, stop.
4. No R/D/S/T artifacts; commit only when the user asks.

## Rules

- Follow TDD (`references/tdd.md`) for non-trivial behavior, bugs, and changes with a real seam; trivial one-liners and Quick changes may use the task verify.
- Load strictly `references/principles.md` and `references/tdd.md` while coding; never read `references/examples.md`.
- Never interrogate the user with questions during implementation; escalate missing contracts or design forks strictly to the `specify` or `design` skill.
- Reproduce first; prove with the same command after the fix.
- Test strictly the public seam and observable behavior; never add tests that merely mirror internal code.
- Read strictly the task, spec, decision, cited architecture section, and target slice files from `next-task`, never unrelated files.
- The worker alone changes state; the engineer plans and reviews, and Code Reviewer stays strictly read-only.
- Respect accepted seam invariants and apply strictly surgical hunk edits; never refactor unrelated code or append design, spec, plan, or review breakdowns to a task.
- Start only unblocked tasks returned by `next-task`, and mark only the active `Txx` complete after verification and final review are accepted; never mark parent specs or decisions complete.
- Verify: failing check went green, task verify passes, final review is accepted, and `.artifacts/TASKS.md` reflects `- [x] Txx`.
