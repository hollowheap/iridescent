# Artifact Placement

- Store all non-source workspace artifacts strictly under `.artifacts/`, never in the repo root or source tree.
- The CLI maintains `.artifacts/.gitignore`; this placement list is a reminder.
- Keep iridescent and RDST terms, IDs, and `.artifacts/` paths strictly inside `.artifacts/` and interactive chat; never emit them in commits, PRs, code comments, or public docs.
- Reusable probes and validation scripts live in `.artifacts/scripts/`; throwaway scratch files live in `.artifacts/scratch/`.
- Pipe noisy command output through `head`, `tail`, or `rg`; redirect large output, logs, or search dumps to `.artifacts/logs/` or `.artifacts/errors/` and return strictly the path with a targeted `rg` or `tail` command (never the full dump).
- Working notes live in `.artifacts/notes/`, primary-source research in `.artifacts/research/<topic>.md`, and persistent reviews in `.artifacts/review/<slice>.md` (indexed by `.artifacts/REVIEWS.md`).
- Workspace and RDST records live at `.artifacts/` root: `CONTEXT.md`, `ARCHITECTURE.md`, `BRAINSTORM.md`, `REQUIREMENTS.md`, `DECISIONS.md`, `SPECS.md`, `TASKS.md`, and `REVIEWS.md`.
- Real test files live in the repository test suite; per-task details live in `.artifacts/tasks/<Txx>.md`.
- Live root records are authoritative for graph commands; detail files are linked evidence.
- Detail fields are contract and must keep exact names and order.
- Run `verify-links` before continuing workspace changes.
- Follow `references/slicing.md` for slice boundaries, cardinality, coupling, and target-state requests.

- Retired records live in `.artifacts/archive/`: `REQUIREMENTS.md`, `SPECS.md`, `TASKS.md`, and `tasks/<Txx>.md`.
- Retired records keep historical IDs; active roots keep live records only.
- `DECISIONS.md` is the only live file with supersession fields.
- Active records never reference archived IDs as parents.
