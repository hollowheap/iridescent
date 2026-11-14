---
name: init
description: Bootstrap AGENTS, context, and architecture.
disable-model-invocation: true
---

## Workflow

1. Inspect workspace for `AGENTS.md` and `.artifacts/CONTEXT.md`. If `AGENTS.md` exists, stop immediately.
2. Inspect workspace manifests, source entrypoints, directory seams, and test runners directly; delegate repo recon to Scout and external research to Researcher only when the calling agent permits delegation.
3. Run build, check, full-suite, and targeted single-test commands in the shell to confirm they pass.
4. Ensure `.gitignore` includes `.artifacts/`.
5. Write `AGENTS.md`, `.artifacts/CONTEXT.md`, and `.artifacts/ARCHITECTURE.md` using `references/template.md`.

## Rules

- Follow the section structure and `<= 60` line budgets for `AGENTS.md` and `.artifacts/CONTEXT.md` in `references/template.md`.
- Keep `AGENTS.md` focused on high-signal agent guidance: verified build/test/single-test commands, non-obvious repo invariants, and safety rules.
- Put multi-step task runbooks into a project skill and keep one pointer line in `AGENTS.md`.
- Run every command in the shell before recording it in `AGENTS.md`.
- Verify: `AGENTS.md` and `.artifacts/CONTEXT.md` are under 60 lines and match `references/template.md`; `.gitignore` includes `.artifacts/`; `.artifacts/ARCHITECTURE.md` defines all required sections.
