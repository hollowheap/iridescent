# iridescent

Skill suite for the full delivery loop: brainstorm, design, plan, specify, implement, review, and retro.

## Skills

- `brainstorm` — explore archetypes and candidate questions.
- `design` — outcomes, decisions, architecture.
- `plan` — vertical task breakdown.
- `specify` — contracts and acceptance.
- `implement` — test-first delivery.
- `review` — diff, slice, and robustness review.
- `retro` — loop and process audit.
- `modular-design` — module boundaries and seams.
- `init` — bootstrap AGENTS, context, and architecture.
- `update` — reconcile artifacts with code.
- `author-pr` — draft pull request descriptions.
- `deslop` — remove accidental complexity.
- `git-commit` — commit verified changes.
- `merge-worktree` — integrate a worker worktree.

UI work is delegated to the sibling `opal` skill when installed. Lifecycle skills run without it.

## Install

Each skill lives under `skills/<name>/SKILL.md` and can be copied into a harness skills directory. `opal` is a separate repo because it ships a binary and design tokens.
