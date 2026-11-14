---
name: review
description: Review diffs, slices, seams, and robustness.
disable-model-invocation: true
---

## Workflow

1. Use `references/diff.md` by default; load `references/profiles.md` only when choosing `slice`, `seam`, or `robust`, or recording a persistent `Vxx`.
2. Read minimum inputs: parent task/spec/decision, architecture section, changed hunks, and one verification.
3. Run `references/simplicity.md`, then load only matching lenses by trigger: `architecture` (new modules/ports/layer moves/global wiring), `api` (handlers/RPC/schemas/error envelopes/timeouts), `data` (DB schemas/migrations/queries/pools), `security` (auth/secrets/input/network/permissions), `performance` (hot loops/large data/startup), `tests` (new or edited tests/contract checks), `ui` (markup/CSS/layout/focus/tokens).
4. Record the lens ledger (`Lenses: loaded=[...]; skipped=[...]; considered=[...]` for `diff`; table in `profiles.md` for persistent reviews).
5. Report findings with `file:line`. The `diff` profile reports high/medium findings inline, caps five, and stops when none remain; low notes are one line or omitted.
6. Persistent reviews write `Vxx` through `.artifacts/REVIEWS.md` and record findings only.
7. Apply minimal patches, re-run task verification, and record the verdict.

## Rules

- Review runs after implementation.
- Load `references/simplicity.md`, the active profile reference, and lenses whose trigger matches the diff; account for every lens in the ledger.
- Diff review is ephemeral unless durable debt promotes it to a persistent review.
- Persistent review documents live in `.artifacts/review/<slice>.md` and record findings.
- Report unresolved design forks as blocking findings for `{{skill:design}}`.
- Rendered checks require `opal`; otherwise mark them unverified and record `ui: skipped`.
- Correctness, security, and unresolved design findings block completion.
- Treat Code Reviewer as read-only; implement fixes in the worker.
- Verify: profile inputs, lens ledger, `Vxx` rules, and verification commands are complete.
