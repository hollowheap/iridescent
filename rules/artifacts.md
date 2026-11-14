# Artifact Placement

- Keep non-source workspace artifacts under `.artifacts/`, never in the repo root or source tree.
- Ensure `.artifacts/` is listed in `.gitignore` before writing workspace artifacts.
- Keep iridescent and RDST terms, IDs, and `.artifacts/` paths local; never mention them in commits, PRs, code comments, or public docs.
- Reusable probes and validation scripts live in `.artifacts/scripts/`; throwaway scratch files live in `.artifacts/scratch/`.
- Pipe noisy command output through `head`, `tail`, or `rg`; redirect large output, logs, or search dumps to `.artifacts/logs/` or `.artifacts/errors/` and return the path with a targeted `rg` or `tail` command, never the full dump.
- Working notes live in `.artifacts/notes/`, primary-source research in `.artifacts/research/<topic>.md`, and persistent reviews in `.artifacts/review/<slice>.md` (indexed by `.artifacts/reviews.md`).
- Workspace and RDST records live at `.artifacts/` root: `context.md`, `architecture.md`, `brainstorm.md`, `requirements.md`, `decisions.md`, `specs.md`, `tasks.md`, `reviews.md`, and `repomap.md`.
