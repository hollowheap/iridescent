# iridescent

Harness-agnostic Markdown skill suite, RDST trace CLI (`scripts/artifacts.sh`), and workspace artifact rules for the RDST delivery loop (`brainstorm`, `design`, `specify`, `plan`, `implement`, `review`, `update`).

## Essential Commands

- Check whitespace and conflict markers: `git diff --check`
- Check wrapper script syntax: `bash -n skills/*/scripts/artifacts.sh`
- Check RDST trace CLI syntax and status: `python3 -m py_compile scripts/artifacts.sh && ./scripts/artifacts.sh status`
- Verify every skill defines frontmatter, Workflow, Rules, and Verify sections: `for f in skills/*/SKILL.md; do grep -q '^name:' "$f" && grep -q '^description:' "$f" && grep -q '^## Workflow' "$f" && grep -q '^## Rules' "$f" && grep -q '^- Verify:' "$f" || { echo "FAIL: $f"; exit 1; }; done`

## Conventions

- Keep skills self-contained and harness-agnostic: never hardcode host-specific directories or cross-skill `../` relative paths inside `skills/`; reference sibling skills with `{{skill:<name>}}`.
- Keep skill bodies concise (`## Workflow`, `## Rules`, `- Verify:`); place tables, examples, formats, and checklists in `references/*.md`.
- Keep `implement` focused on implementation principles and TDD (`skills/implement/references/principles.md`, `tdd.md`) and `review` focused on audit checklists (`skills/review/references/*.md`).
- Keep all non-source workspace paths under `.artifacts/` per `rules/artifacts.md`.
- Never fabricate test pass counts or unverified commands in `AGENTS.md`.
- Never bypass hooks or commit signing (`--no-verify`, `--no-gpg-sign`, `gpgSign=false`).

## Context

- [.artifacts/context.md](.artifacts/context.md) — stack summary, entrypoints, and module seams.
- [.artifacts/architecture.md](.artifacts/architecture.md) — system shape, contracts, debt, and evidence.
