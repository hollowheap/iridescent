# iridescent

Declarative Markdown skill suite (`skills/`), Python 3 RDST trace CLI (`scripts/iridescent-artifacts`), and Nix flake (`flake.nix`).

## Essential Commands

- Check whitespace and conflict markers: `git diff --check`
- Check generated skill assets and wrappers: `python3 -B scripts/sync-skill-assets --check && python3 -B -m unittest tests.test_generated_assets tests.test_portable_skills`
- Check trace CLI syntax, tests, and workspace status: `python3 -B -m py_compile scripts/iridescent-artifacts && python3 -B -m unittest discover -s tests && ./scripts/iridescent-artifacts status`
- Verify every skill defines frontmatter, Scope, Workflow, Rules, and Verify sections: `for f in skills/*/SKILL.md; do grep -q '^name:' "$f" && grep -q '^description:' "$f" && grep -q '^## Scope' "$f" && grep -q '^## Workflow' "$f" && grep -q '^## Rules' "$f" && grep -q '^- Verify:' "$f" || { echo "FAIL: $f"; exit 1; }; done`
- Check Nix flake outputs and package evaluation: `nix flake check path:. --no-write-lock-file`

## Conventions

- Keep each `skills/<name>/` directory strictly self-contained for `npx skills add`: never use cross-skill `../` paths or hardcode host-specific directories inside `skills/`; reference sibling skills plainly with `skill` (e.g., `` `design` skill ``).
- Keep skill bodies concise (leading `## Scope`, `## Workflow` <= 7 steps, `## Rules`, `- Verify:`); put templates, formats, lenses, and examples in `references/*.md`.
- Keep `implement` focused on implementation principles and TDD (`skills/implement/references/principles.md`, `tdd.md`) and `review` focused on audit checklists (`skills/review/references/*.md`).
- Keep every scripted skill's `scripts/` tree unchanged in Nix installs so each wrapper resolves its sibling `iridescent-artifacts-cli`.
- Never bypass hooks or commit signing (`--no-verify`, `--no-gpg-sign`, `gpgSign=false`).
