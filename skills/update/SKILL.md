---
name: update
description: Reconcile live indices, evidence, and archive migration.
disable-model-invocation: true
---

## Scope

- Covers: reconciling live indices, task details, completion receipts, and retired records in `.artifacts/archive/`.
- Excludes: design forks, new requirements, implementation, and review.

## Workflow

1. Read newly completed task details and `.artifacts/tasks/quick.md`.
2. Run only the verify commands recorded in those receipts.
3. Apply completions, reconcile live indices and named records from receipts, and move retired records to `.artifacts/archive/` with historical IDs.
4. Keep `Supersedes` only in `DECISIONS.md`; remove retired IDs from live records.
5. Run `verify-links` and refresh existing persistent review records.

## Rules

- Write mode: snapshot; rewrite in place with no retired IDs or markers.
- Reconcile only receipts and named records.
- Keep `AGENTS.md` under 500 tokens.
- Keep live indices live and archived records archived.
- Archive records only after replacement evidence is verified.
- Preserve superseded history in archive entries.
- Route unresolved design forks to `design` and unresolved seams to `specify` or `draw`.

## Verify

- Verify: `verify-links` outputs OK, live files carry no retirement fields except `DECISIONS.md`, and archive links resolve.
