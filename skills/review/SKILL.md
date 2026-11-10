## Workflow

1. Choose one profile from `references/profiles.md`: `diff` by default, `slice` for a vertical slice, or `robust` for failure-mode or workspace audit.
2. Read the minimum inputs: parent task/spec/decision, architecture section, changed hunks, and one verification.
3. Run the always-on checks: `references/simplicity.md`.
4. Build the lens ledger and run the loaded lenses, then continue. Backend triggers on endpoints, services, transport, persistence, schemas, error mapping, timeouts, retries, and pool lifecycle; the other lens triggers live in their files.
5. Report findings with `file:line`. The diff profile reports high/medium findings inline, caps five, and stops when none remain; low notes are one line or omitted.
6. Persistent reviews write `Vxx` through `artifacts/reviews.md`, include the ledger, and record findings only.
7. Apply minimal patches, re-run the task verification, and record the verdict.

## Rules

- Review runs after implementation. It does not gate requirements, design, specification, or planning.
- Review works by profile: diff, slice, and robustness. Backend, security, performance, and UI are lenses.
- Every review records the lens ledger. Never silently skip a lens.
- Diff review is ephemeral: no review document and no `Vxx`, unless a durable `Qxx` promotes it to a persistent review.
- Review documents live in `artifacts/review/<slice>.md` and contain findings, not phase checklists.
- Review may write `Q` only for real design unknowns; never create `Dxx`, `Sxx`, or `Txx`; resolution remains `Qxx -> Dxx`.
- `deslop` runs only on explicit request after review evidence.
- Rendered checks require `opal`; otherwise mark them unverified and record `ui: skipped`.
- Correctness and security findings block task completion.
- Treat Code Reviewer as read-only; implement fixes in the worker.
- Verify: profile inputs, ledger, `Vxx`/`Qxx` rules, and verification commands are complete.
