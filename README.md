# iridescent

Skill suite and RDST trace CLI for the delivery loop: `brainstorm` → `design` → `specify` → `draw` → `plan` → `implement` → `review` → `update`.

## Skills

- `init` — bootstrap `AGENTS.md`, `CONTEXT.md`, and `ARCHITECTURE.md`; the CLI maintains `.artifacts/.gitignore`.
- `brainstorm` — record destination, verified facts, and options from supplied context.
- `design` — turn options into accepted `Dxx` decisions, `Rxx` requirements, and architecture.
- `specify` — derive public-boundary invariants (`Sxx`) from accepted `Rxx`.
- `draw` — write red test cases for one `Sxx` in the repository test suite.
- `plan` — split `Sxx` cases into atomic verified tasks (`Txx`).
- `implement` — run drawn tests, write production code, self-audit the diff, and record a completion receipt.
- `review` — audit changed hunks with severity-ordered, read-only findings.
- `update` — reconcile live snapshots from decisions, receipts, and verified code.
- `how-to-iridescent` — explain the lifecycle and current workspace state.
- `doctor-iridescent` — repair malformed workspace structure against generated templates.

## Artifacts CLI (`scripts/iridescent-artifacts`)

Python 3 standard-library CLI with a skill-local wrapper and CLI copy under `<skill-dir>/scripts/`:

```sh
scripts/iridescent-artifacts status
scripts/iridescent-artifacts active-decisions
scripts/iridescent-artifacts archive [--dry-run]
scripts/iridescent-artifacts unconverted-reqs
scripts/iridescent-artifacts unconverted-decs
scripts/iridescent-artifacts unconverted-specs
scripts/iridescent-artifacts undrawn-specs
scripts/iridescent-artifacts next-task
scripts/iridescent-artifacts complete <Txx>
scripts/iridescent-artifacts frontier
scripts/iridescent-artifacts next-id <r|d|s|t>
scripts/iridescent-artifacts tree [ID]
scripts/iridescent-artifacts trace <ID>
scripts/iridescent-artifacts check
scripts/iridescent-artifacts verify-links
```

## Install

### `npx skills` (`vercel-labs/skills`)

```sh
npx skills add hollowheap/iridescent
```

Each `skills/<name>/` directory is self-contained. Generated templates, contracts, and CLI copies are committed for portable installs. Run `scripts/sync-skill-assets --check` to verify generated files against `assets/`.

### Nix Flake & Home Manager (`flake.nix`)

- `homeManagerModules.default` installs the CLI and skills into enabled harnesses.
- `packages.<system>.iridescent-artifacts` provides the standalone CLI.
- `overlays.default` overlays `pkgs.iridescent-artifacts`.
