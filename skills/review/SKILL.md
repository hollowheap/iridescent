---
name: review
description: Audit diffs, simplify code, and review slices, seams, and robustness.
disable-model-invocation: true
---

## Scope

- Covers: diff, slice, seam, and robustness reviews with a lens ledger, findings, and verification.
- Excludes: requirements, design, specification, planning, and feature implementation.

## Workflow

1. Use `references/diff.md` by default; load `references/profiles.md` only when choosing `slice`, `seam`, or `robust`, or recording a persistent `Vxx`.
2. Read minimum inputs: parent task/spec/decision, architecture section, changed hunks, and one verification.
3. Run `references/simplicity.md` as an always-on preservation and deslop gate, then load only matching lenses by trigger: `architecture` (new modules/ports/layer moves/global wiring), `api` (handlers/RPC/schemas/error envelopes/timeouts), `data` (DB schemas/migrations/queries/pools), `security` (auth/secrets/input/network/permissions), `performance` (hot loops/large data/startup), `tests` (new or edited tests/contract checks), `ui` (markup/CSS/layout/focus/tokens).
4. Record the lens ledger (`Lenses: loaded=[...]; skipped=[...]; considered=[...]` for `diff`; table in `profiles.md` for persistent reviews).
5. Report findings with `file:line` and a named remedy for structural findings. The `diff` profile reports high/medium findings inline, caps five, and stops when none remain; low notes are one line or omitted.
6. Persistent reviews write `Vxx` through `.artifacts/REVIEWS.md` and record findings only.
7. Apply minimal patches, re-run task verification, and record the verdict.

## Rules

- Run review strictly after implementation; it does not gate requirements, design, specification, or planning.
- Load `references/simplicity.md` as an always-on preservation and deslop gate, plus the active profile reference and lenses whose trigger matches the diff (never untriggered lenses, unused profiles, or `references/examples.md`); account strictly for every lens in the ledger without silent skips.
- Keep diff review strictly ephemeral (no review document and no `Vxx`) unless durable debt promotes it to a persistent review.
- Persistent review documents live in `.artifacts/review/<slice>.md` and contain strictly findings, not phase checklists.
- Report unresolved design forks as blocking findings routed strictly to the `design` skill; write only `Vxx` and `.artifacts/review/<slice>.md` (only `robust` updates `.artifacts/ARCHITECTURE.md`, and never write `Rxx`, `Dxx`, `Sxx`, or `Txx` during review).
- Rendered checks require `opal`; otherwise mark them unverified and record `ui: skipped`.
- Correctness, security, and unresolved design findings block completion.
- Treat Code Reviewer as read-only; implement fixes strictly in the worker.
- Verify: profile inputs, lens ledger, named remedies, `Vxx` rules, and verification commands are complete.
