---
name: doctor-iridescent
description: Repair malformed workspace structure against bundled templates.
disable-model-invocation: true
---

## Scope

- Covers: repair of malformed existing `.artifacts/` files, links, and headings.
- Excludes: initialization, semantic content, design forks, implementation, review, and target-state guessing.

## Workflow

1. Read generated templates in `references/`: root records, test records, task details, and archive records.
2. Inspect existing workspace files, test links, and detail files for format drift.
3. Repair malformed headings, path pointers, and ownership fields from the templates only.
4. Run the structural checks in `references/checks.md`.
5. Route semantic gaps to `design`, `specify`, `draw`, `plan`, `update`, or `review`.

## Rules

- Enforce retirement fields only in `DECISIONS.md`.
- Treat generated templates as the authority for format repair.
- Let the CLI initialize missing structure; never create initialization files here.
- Never infer the target state from current workspace contents.
- Never write semantic content.
- Never name older versions or prior paths.
- Preserve IDs and existing evidence during repair.
- Route every content gap to its owning skill.

## Verify

- Verify: `check` and `verify-links` output `OK` and remaining gaps name owning skills.
