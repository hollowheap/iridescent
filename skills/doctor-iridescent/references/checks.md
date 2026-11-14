# Doctor Checks & Repairs

1. **Legacy `artifacts/` directory**: If `artifacts/` exists alongside or instead of `.artifacts/`, migrate files into `.artifacts/` (using `git mv` when tracked) and remove the empty `artifacts/` directory.
2. **Stray root artifacts**: Move misplaced root files (`context.md`, `architecture.md`, `brainstorm.md`, `requirements.md`, `decisions.md`, `specs.md`, `tasks.md`, `reviews.md`, `repomap.md`) into `.artifacts/`.
3. **Stale path pointers**: Update `artifacts/` references in `AGENTS.md` and `.artifacts/*.md` to `.artifacts/`.
4. **Gitignore coverage**: Ensure `.gitignore` includes `.artifacts/` (replacing any legacy `artifacts/` ignore pattern when migrating).
5. **Context hygiene**: Ensure `.artifacts/context.md` is under 60 lines and has no `## Commands` section; relocate commands to `AGENTS.md` `## Essential Commands` and keep `.artifacts/context.md` limited to `## Stack & Entrypoints` and `## Module Seams`.
6. **AGENTS.md hygiene**: Ensure `AGENTS.md` keeps `## Essential Commands` and points to `.artifacts/context.md` and `.artifacts/architecture.md` without test pass counts.
7. **Graph & link integrity**: Run `scripts/artifacts.sh check` and `scripts/artifacts.sh verify-links`; fix broken links or malformed references without altering RDST IDs, and route stale code-to-spec content to `{{skill:update}}`.
