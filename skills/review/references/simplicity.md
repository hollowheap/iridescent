# Always On Checks

Never skipped; not a lens.

## Checks

- Shallow 1:1 helper: function, wrapper, or module delegates 1:1 with one caller and no independent invariant, policy, or translation.
- Single-adapter abstraction: port or interface has one implementation and no second consumer or test seam.
- Speculative option or config: flag, env var, or option has no reader or only a default path.
- Duplicate validation or seam: same check enforced in two layers without distinct responsibility, or a second seam mirrors an existing one.
- Unnecessary dependency or framework: platform, stdlib, or existing dependency already covers it.
- Restating comments: comments narrate obvious control flow, restate code, or keep history that belongs in git.
- Deletion test: code can be deleted or inlined without changing external behavior.

Keep depth only for multiple real adapters, an external boundary, a measured bottleneck, or a concurrency/compliance invariant.

## Remediation

When cleaning up on explicit request:

1. Run baseline `git status`, tests, and task verify.
2. Prove each candidate with call sites, adapter count, and behavior invariance; skip unproven items.
3. Delete or inline one seam at a time without adding new helpers, ports, or config.
4. Re-run verify after each removal; revert any change that alters behavior.

## Evidence

- Cite `file:line`, call-site/adapter count, or the deletion-test result.

## Verify

Prefer the smallest removal that eliminates duplication or speculative surface; re-run task verification.
