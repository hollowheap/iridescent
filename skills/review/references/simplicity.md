# Always On Checks

Never skipped; not a lens.

## Checks

- Shallow 1:1 helper: function, wrapper, or module delegates 1:1 with one caller and no independent invariant, policy, or translation.
- Single-adapter abstraction: port or interface has one implementation and no second consumer or test seam.
- Speculative option or config: flag, env var, or option has no reader or only a default path.
- Duplicate validation or seam: same check enforced in two layers without distinct responsibility, or a second seam mirrors an existing one.
- Unnecessary dependency or framework: platform, stdlib, or existing dependency already covers it.
- Restating comments: comments narrate obvious control flow, restate code, or keep history that belongs in git.
- Dead code: unused imports, branches, flags, or unreachable helpers remain in touched files.
- Mixed refactor and feature: behavior-preserving cleanup and feature changes share one patch.
- Broken Chesterton's Fence: an existing guard, invariant, or ordering was removed without proving why it existed.
- Behavior drift: simplification changed outputs, errors, side effects, ordering, or existing tests.
- Deletion test: code can be deleted or inlined without changing external behavior.

Keep depth only for multiple real adapters, an external boundary, a measured bottleneck, or a concurrency or compliance invariant.

## Remediation

Flag bloat and recommend cleanup unconditionally in every review:

1. Verify baseline `git status`, tests, and task verify pass.
2. Prove each candidate with call sites, adapter count, and behavior preservation; skip unproven items.
3. Recommend deleting or inlining one seam at a time without adding new helpers, ports, or config.
4. Require verification after each removal and revert any change that alters outputs, errors, side effects, or ordering.
5. Name the structural remedy: delete or inline the seam, collapse duplicate branches, replace condition chains with a model or dispatcher, move feature logic to its owner, or reuse the canonical helper.

## Enforcement Ladder

When a mistake repeats, fix it at the highest effective level:

1. Architecture: remove the wrong path or give each piece of state one owner.
2. Types: make the bad state unrepresentable.
3. Lint or CI: fail with an error that names the correct replacement.
4. Tests: prove the behavior and fail when the behavior breaks.
5. Docs or agent rules: use only for judgment calls, and name the enforcement.

Prove each new guard fails on a real past mistake. Require a reason, expiry date, and human approval for every exception.

## Evidence

- Cite `file:line`, call-site count, adapter count, or the deletion-test result.
- Confirm non-mutating reproduction output; never edit files during read-only review.

## Verify

Prefer the smallest removal that eliminates duplication or speculative surface; re-run task verification.
