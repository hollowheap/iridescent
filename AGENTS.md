# iridescent

Declarative Markdown skill suite (`skills/`), Python 3 RDST trace CLI (`scripts/artifacts.sh`), workspace artifact rule (`rules/artifacts.md`), and Nix flake (`flake.nix`).

## Essential Commands

- Check whitespace and conflict markers: `git diff --check`
- Check shell wrapper syntax: `bash -n skills/*/scripts/artifacts.sh`
- Check trace CLI syntax and workspace status: `python3 -B -m py_compile scripts/artifacts.sh && ./scripts/artifacts.sh status`
- Verify every skill defines frontmatter, Workflow, Rules, and Verify sections: `for f in skills/*/SKILL.md; do grep -q '^name:' "$f" && grep -q '^description:' "$f" && grep -q '^## Workflow' "$f" && grep -q '^## Rules' "$f" && grep -q '^- Verify:' "$f" || { echo "FAIL: $f"; exit 1; }; done`
- Check Nix flake outputs and package evaluation: `nix flake check path:. --no-write-lock-file`

## Conventions

- Keep each `skills/<name>/` directory self-contained for `npx skills add`: never use cross-skill `../` paths or hardcode host-specific directories inside `skills/`; reference sibling skills with `{{skill:<name>}}`.
- Keep skill bodies concise (`## Workflow` <= 7 steps, `## Rules`, `- Verify:`); put templates, formats, lenses, and examples in `references/*.md`.
- Keep `implement` focused on implementation principles and TDD (`skills/implement/references/principles.md`, `tdd.md`) and `review` focused on audit checklists (`skills/review/references/*.md`).
- In `flake.nix` `mkSkillFileAttrs`, prepend `helperEntry` before `renderedFiles` because `builtins.listToAttrs` keeps the first duplicate key.
- Never bypass hooks or commit signing (`--no-verify`, `--no-gpg-sign`, `gpgSign=false`).
