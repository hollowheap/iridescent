# Doctor Checks & Repairs

1. **Legacy `artifacts/` directory**: If `artifacts/` exists alongside or instead of `.artifacts/`, migrate files into `.artifacts/` (using `git mv` when tracked) and remove the empty `artifacts/` directory.
2. **Stray root or lowercase artifacts**: Move misplaced root artifact files into `.artifacts/` and rename lowercase root artifact files (`context.md`, `architecture.md`, `brainstorm.md`, `requirements.md`, `decisions.md`, `specs.md`, `tasks.md`, `reviews.md`, `repomap.md`) to uppercase (`CONTEXT.md`, `ARCHITECTURE.md`, `BRAINSTORM.md`, `REQUIREMENTS.md`, `DECISIONS.md`, `SPECS.md`, `TASKS.md`, `REVIEWS.md`, `REPOMAP.md`).
3. **Stale path pointers**: Update legacy `artifacts/` or lowercase filename references in `.artifacts/*.md` to `.artifacts/<UPPERCASE>.md`, and remove any `.artifacts/` pointers from `AGENTS.md`.
4. **Gitignore coverage**: Ensure `.gitignore` includes `.artifacts/` (replacing any legacy `artifacts/` ignore pattern when migrating).
5. **Context & AGENTS budgets**: Ensure `.artifacts/CONTEXT.md` (`## Stack & Entrypoints`, `## Module Seams`) and `AGENTS.md` (`## Essential Commands`, `## Conventions`) are each under 60 lines; relocate any `## Commands` section from `.artifacts/CONTEXT.md` into `AGENTS.md` `## Essential Commands`.
6. **Graph & link integrity**: Run `scripts/artifacts.sh check` and `scripts/artifacts.sh verify-links`; fix broken links or malformed references without altering RDST IDs, and route stale code-to-spec content to `{{skill:update}}`.
