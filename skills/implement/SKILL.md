---
name: implement
description: Worker implements the next task test-first.
disable-model-invocation: true
---

## Workflow

1. Run `scripts/artifacts.sh next-task`; if NONE, stop immediately.
2. Read the task, spec, decision, architecture, and plan; do not read unrelated files. If a missing contract or unresolved design fork blocks the task, stop and route back to `{{skill:specify}}` or `{{skill:design}}`.
3. For non-trivial changes, load `references/principles.md` and write the smallest failing seam check via `references/tdd.md`, confirming red; skip `references/tdd.md` for trivial one-liners.
4. Implement the minimum production code required to satisfy the invariant using targeted hunk edits.
5. Rerun the same check until green, then run the task verify and broader suite; hand the final review to `{{skill:review}}`.
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
- Follow `references/principles.md` across touched boundaries while coding; never read `references/examples.md`.
- Do not interrogate the user with questions during implementation; if a spec or design decision is missing or contradicts the codebase, stop and escalate to `{{skill:specify}}` or `{{skill:design}}`.
- Reproduce first; prove with the same command after the fix.
- Test the public seam, not the implementation; do not add tests that merely mirror code.
- `next-task` prints the task, spec, decision, and command context; do not load unrelated files.
- The worker alone changes state. The engineer plans and reviews; Code Reviewer stays read-only.
- Respect accepted seam invariants; change internal implementation without breaking public boundaries.
- Apply minimal hunk edits; avoid unsolicited refactoring or premature abstractions.
- Never add design, spec, plan, or review breakdowns to a task.
- Do not start a task whose plan is blocked; do not mark it complete without final review acceptance.
- Never mark parent specs or decisions complete.
- Verify: failing check went green, task verify passes, final review is accepted, and `.artifacts/tasks.md` reflects `- [x] Txx`.
