# Diff Review Profile

Use for every patch review unless a broader profile applies.

## Workflow

1. Read the parent `Sxx` and `Rxx` before opening the diff.
2. Run `git status` and `git diff`; identify behavior changes, not just file churn.
3. Run `references/simplicity.md` and load only lenses whose triggers match the diff.
4. Check correctness, regressions, error paths, type safety, and boundary contracts.
5. Reproduce every high-impact claim with a command; cite `file:line` for each finding.
6. Apply minimal patches for high or medium findings, then re-run task verification and the broader suite.

## Rules

- Apply strictly surgical patches at the smallest failing seam; never rewrite the patch wholesale.
- Treat Code Reviewer as read-only; implement fixes strictly in the worker.
- If the diff touches async work, external I/O, or shared state, load only `## Failure checks` from `references/slice.md`, then resume this profile.
- Verify: zero high or medium findings, compact lens ledger recorded, and verification passes.
