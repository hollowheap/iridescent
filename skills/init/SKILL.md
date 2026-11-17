---
name: init
description: Bootstrap AGENTS, context, and architecture.
disable-model-invocation: true
---

## Scope

- Covers: first-time workspace bootstrap of `AGENTS.md`, `.artifacts/CONTEXT.md`, and `.artifacts/ARCHITECTURE.md`.
- Excludes: workspaces that already have `AGENTS.md`, design decisions, and feature implementation.

## Workflow

1. Inspect workspace for `AGENTS.md` and `.artifacts/CONTEXT.md`. If `AGENTS.md` exists, stop immediately.
2. Inspect workspace manifests, source entrypoints, directory seams, and test runners directly; delegate repo recon to Scout and external research to Researcher only when the calling agent permits delegation.
3. Run build, check, full-suite, and targeted single-test commands in the shell to confirm they pass.
4. Ensure `.gitignore` includes `.artifacts/`.
5. Write `AGENTS.md`, `.artifacts/CONTEXT.md`, and `.artifacts/ARCHITECTURE.md` using `references/template.md`.

## Rules

- Follow the section structure and `<= 60` line budgets strictly for `AGENTS.md` and `.artifacts/CONTEXT.md` in `references/template.md`.
- Keep in `AGENTS.md` strictly high-signal guidance: verified build/test/single-test commands, non-obvious repo invariants, and all global "Never ..." safety rules (never move safety rules into skills, never include `.artifacts/` pointers, and never write test pass counts in `AGENTS.md`).
- Keep `.artifacts/CONTEXT.md` limited strictly to `## Stack & Entrypoints` and `## Module Seams` (document strictly high-level seams and entrypoints, never internal functions or `## Commands`).
- Put multi-step task runbooks into a project skill and keep one pointer line in `AGENTS.md`.
- Record only commands you executed and observed pass in the shell.
- Verify: `AGENTS.md` and `.artifacts/CONTEXT.md` are under 60 lines and match `references/template.md`; `.gitignore` includes `.artifacts/`; `.artifacts/ARCHITECTURE.md` defines all required sections.
