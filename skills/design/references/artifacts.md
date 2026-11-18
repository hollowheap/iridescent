# Artifact Placement

- Store all non-source workspace artifacts strictly under `.artifacts/`, never in the repo root or source tree.
- Ensure `.artifacts/` is listed in `.gitignore` before writing workspace artifacts.
- Keep iridescent and RDST terms, IDs, and `.artifacts/` paths strictly inside `.artifacts/` and interactive chat; never emit them in commits, PRs, code comments, or public docs.
- Reusable probes and validation scripts live in `.artifacts/scripts/`; throwaway scratch files live in `.artifacts/scratch/`.
- Pipe noisy command output through `head`, `tail`, or `rg`; redirect large output, logs, or search dumps to `.artifacts/logs/` or `.artifacts/errors/` and return strictly the path with a targeted `rg` or `tail` command (never the full dump).
- Working notes live in `.artifacts/notes/`, primary-source research in `.artifacts/research/<topic>.md`, and persistent reviews in `.artifacts/review/<slice>.md` (indexed by `.artifacts/REVIEWS.md`).
- Workspace and RDST records live at `.artifacts/` root: `CONTEXT.md`, `ARCHITECTURE.md`, `BRAINSTORM.md`, `REQUIREMENTS.md`, `DECISIONS.md`, `SPECS.md`, `TASKS.md`, and `REVIEWS.md`.
- Per-spec test ledgers live in `.artifacts/tests/<Sxx>.md`; per-task details live in `.artifacts/tasks/<Txx>.md`, linked from root records.
- Root records are authoritative; detail files are linked evidence.
- Detail fields are contract and must keep exact names and order.
- Run `verify-links` before continuing workspace changes.
- Follow `references/slicing.md` for slice boundaries, cardinality, coupling, and target-state requests.

- Superseded `Rxx` and `Sxx` stay in live root records; the replacement record points to them with `Supersedes:`.
- Agents skip superseded entries during normal work.
- Active records use `Supersedes: <old-id>`.
- Coverage-restoration cases use `Covers: Sxx/Cxx`.
- Active records never reference superseded IDs as parents.
