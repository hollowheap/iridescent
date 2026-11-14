# iridescent

Skill suite, RDST trace CLI (`scripts/iridescent-artifacts`), and workspace artifact rules for the RDST delivery loop: `brainstorm` → `design` → `specify` → `plan` → `implement` → `review` → `update`.

## Skills

- `init` — bootstrap `AGENTS.md`, `.gitignore`, `.artifacts/CONTEXT.md`, and `.artifacts/ARCHITECTURE.md`.
- `brainstorm` — explore 2–3 contrasting archetypes; bound questions to destination, scope, and hard constraints.
- `design` — define slice requirements (`Rxx`), accepted decisions (`Dxx`), and `.artifacts/ARCHITECTURE.md`; bound questions to architectural and design forks.
- `specify` — derive public boundary invariants (`Sxx`) from accepted `Rxx`/`Dxx`; probe only ambiguous seam edge cases.
- `plan` — split `Sxx` into atomic verified tasks (`Txx`); ask questions only when task granularity, ordering, or verify commands are ambiguous.
- `implement` — execute the next ready task test-first with `references/tdd.md` and `references/principles.md`; never interrogate with questions during coding (escalate missing contracts or forks strictly to the `specify` or `design` skill).
- `review` — audit diffs, slices, seams, and robustness using `references/simplicity.md` and triggered review lenses (`architecture`, `api`, `data`, `security`, `performance`, `tests`, `ui`).
- `update` — reconcile `AGENTS.md` and `.artifacts/` with workspace reality and settle completed parent checkboxes.
- `how-to-iridescent` — inspect workspace state, explain the lifecycle loop, and recommend the next skill.
- `doctor-iridescent` — diagnose and repair workspace layout, migrate legacy `artifacts/` paths to `.artifacts/`, and verify trace links.

UI rendered checks in `review` delegate to the sibling `opal` skill when installed and degrade to `ui: skipped` otherwise.

## Artifacts CLI (`scripts/iridescent-artifacts`)

Python 3 standard-library CLI bundled into every scripted skill (`scripts/iridescent-artifacts`) and exposed as the `iridescent-artifacts` Nix package:

```sh
scripts/iridescent-artifacts status
scripts/iridescent-artifacts unconverted-reqs | unconverted-decs | unconverted-specs
scripts/iridescent-artifacts next-id <r|d|s|t>
scripts/iridescent-artifacts next-task | frontier
scripts/iridescent-artifacts check | verify-links | sync | tree [ID] | trace <ID>
```

## Rules

- `rules/artifacts.md` — always-on `.artifacts/` placement, `.gitignore` hygiene, RDST locality, and noisy-output redirection rule.

## Install

### `npx skills` (`vercel-labs/skills`)

```sh
npx skills add hollowheap/iridescent
```

Each `skills/<name>/` directory is self-contained (no cross-skill `../` paths) and bundles `scripts/iridescent-artifacts` where needed. Because `npx skills add` installs `skills/` only, copy or append `rules/artifacts.md` into your harness rule/instruction file (for example `.claude/rules/artifacts.md`, `.kiro/steering/artifacts.md`, or `AGENTS.md`).

### Nix Flake & Home Manager (`flake.nix`)

- `homeManagerModules.default` (`programs.iridescent.enable = true`): installs `iridescent-artifacts` into `home.packages`, installs `skills/` (with `scripts/iridescent-artifacts` wired to Nix `python3`), and installs `rules/artifacts.md` into enabled harnesses (`claude-code`, `opencode`, `codex`, `crush`, `github-copilot-cli`, `antigravity-cli`, `kiro-cli`, `pi-coding-agent`).
- `packages.<system>.iridescent-artifacts` (and `default`): standalone `iridescent-artifacts` CLI derivation (with `artifacts` and `artifacts.sh` aliases).
- `overlays.default`: overlays `pkgs.iridescent-artifacts`.
