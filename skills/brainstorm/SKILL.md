---
name: brainstorm
description: Record destination, facts, and options from given context.
disable-model-invocation: true
---

## Scope

- Covers: destination, audience, constraints, verified facts, and options from the supplied request.
- Excludes: user questions, accepted decisions, specs, tasks, implementation, and open-ended exploration.

## Workflow

1. Read the request, repository facts, and existing `.artifacts/BRAINSTORM.md`.
2. Choose a depth budget before recording anything: `brief`, `bounded`, or `exploratory`.
3. Record destination, facts, and options within the supplied scope, source cap, and direction cap, respectively.
4. Write `.artifacts/BRAINSTORM.md` with `references/template.md`, then stop.

## Rules

- Depth budget `brief`: 0 sources, 0 directions, no probes.
- Depth budget `bounded`: 2 sources, 2 directions, no probes.
- Depth budget `exploratory`: 3 sources, 3 directions, probes allowed.
- Keep all brainstorm artifacts under `.artifacts/`; the CLI maintains the ignore file.
- Never add facts outside the approved request or repository.
- Never exceed the chosen budget to reduce uncertainty.
- Never ask the user or use a question call.
- Mark ambiguity as `UNRESOLVED` and route it to `design`, `specify`, or `draw`.
- Find facts in the repository, tools, and primary sources before recording them.
- Store primary-source notes in `.artifacts/research/<topic>.md`.
- Write disposable probes only to `.artifacts/scripts/` when the budget allows them.
- Keep production source and git state read-only.
- Brainstorm emits options; `design` writes accepted `Dxx` records.

## Verify

- Verify: caps were respected, no questions were asked, and unresolved items are named.
