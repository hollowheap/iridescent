---
name: init
description: Bootstrap AGENTS, context, and architecture.
disable-model-invocation: true
---

## Scope

- Covers: first-time workspace bootstrap of `AGENTS.md`, `.artifacts/CONTEXT.md`, and `.artifacts/ARCHITECTURE.md`.
- Excludes: workspaces that already have `AGENTS.md`, design decisions, and feature implementation.

## Workflow

1. Inspect workspace for `AGENTS.md` and `.artifacts/CONTEXT.md`; stop immediately if `AGENTS.md` exists.
2. Inspect manifests, entrypoints, seams, and test runners directly.
3. Run build, check, full-suite, and targeted single-test commands in the shell to confirm they pass.
4. Ensure the CLI initialized `.artifacts/.gitignore`.
5. Write `AGENTS.md`, `.artifacts/CONTEXT.md`, and `.artifacts/ARCHITECTURE.md` with templates from `references/AGENTS.md`, `references/CONTEXT.md`, and `references/ARCHITECTURE.md`, respectively.

## Rules

- Use the generated templates as the authority for every file created here.
- Keep `AGENTS.md` under 500 tokens.
- Record only commands and facts observed in the shell.
- Put multi-step task runbooks into a project skill.

## Verify

- Verify: all three files match their templates and `.artifacts/.gitignore` exists.
