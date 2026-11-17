# Doctor Checks & Repairs

1. **Legacy `artifacts/` directory**: If `artifacts/` exists alongside or instead of `.artifacts/`, migrate files into `.artifacts/` (using `git mv` when tracked) and remove the empty `artifacts/` directory.
2. **RDST record locations**: Ensure RDST records are saved at `.artifacts/CONTEXT.md`, `.artifacts/ARCHITECTURE.md`, `.artifacts/BRAINSTORM.md`, `.artifacts/REQUIREMENTS.md`, `.artifacts/DECISIONS.md`, `.artifacts/SPECS.md`, `.artifacts/TASKS.md`, and `.artifacts/REVIEWS.md`, with ledgers in `.artifacts/tests/` and details in `.artifacts/tasks/`.
3. **Path pointers**: Update stale `artifacts/` references in `.artifacts/*.md` to `.artifacts/<RECORD>.md`, and remove any `.artifacts/` pointers from `AGENTS.md`.
4. **Gitignore coverage**: Ensure `.gitignore` includes `.artifacts/` (replacing any legacy `artifacts/` ignore pattern when migrating).
5. **Context & AGENTS budgets**: Ensure `.artifacts/CONTEXT.md` (`## Stack & Entrypoints`, `## Module Seams`) and `AGENTS.md` (`## Essential Commands`, `## Conventions`) are each under 60 lines; relocate any `## Commands` section from `.artifacts/CONTEXT.md` into `AGENTS.md` `## Essential Commands`.
6. **Graph & link integrity**: Run `scripts/iridescent-artifacts check` and `scripts/iridescent-artifacts verify-links`; fix broken links or malformed references while preserving RDST IDs, and route stale code-to-spec content to the `update` skill.
