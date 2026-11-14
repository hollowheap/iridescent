---
name: brainstorm
description: Explore archetypes and candidate questions.
disable-model-invocation: true
---

## Workflow

1. Frame the destination: what changes for the user when this is done? Record it under `## Destination`.
2. Inspect the problem space, module seams, and directory structure.
3. If the domain is unfamiliar or contested, gather 2-3 primary sources via `references/research.md`; record evidence in `.artifacts/research/<topic>.md` and link it under `## References`.
4. Clarify destination, scope boundaries, and hard constraints interactively with the question tool; block if a core constraint is unanswered, and defer concrete design, contract, and task questions to `{{skill:design}}`.
5. If feasibility probing is needed, write disposable scripts into `.artifacts/scripts/`.
6. Formulate and compare 2-3 distinct architectural, code-organization, or UX archetypes against coupling, discoverability, blast radius, YAGNI, and failure modes.
7. Emit the recommendation, trade-off matrix, and any deferred design forks to `.artifacts/BRAINSTORM.md` using `references/template.md`.

## Rules

- Research only when the domain is unfamiliar or contested; primary sources only.
- Design research lives in `.artifacts/research/`; audit evidence lives in `.artifacts/review/`.
- Explore structural trade-offs and compare at least 2 contrasting alternatives with explicit failure modes.
- Write disposable test probes only to `.artifacts/scripts/`.
- Keep questions bounded to problem framing, scope, and constraints; resolve them inline with the question tool.
- Verify: `.artifacts/BRAINSTORM.md` has Destination, References, Archetypes, Trade-offs, Recommendation, and Out of scope.
