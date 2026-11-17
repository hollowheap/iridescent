# Always On Checks

Never skipped; not a lens.

## Checks

- Shallow 1:1 helper: function, wrapper, or module delegates 1:1 with one caller
  and no independent invariant, policy, or translation.
- Single-adapter abstraction: port or interface has one implementation and no
  second consumer or test seam.
- Speculative option or config: flag, env var, or option has no reader or only a
  default path.
- Duplicate validation or seam: same check enforced in two layers without
  distinct responsibility, or a second seam mirrors an existing one.
- Unnecessary dependency or framework: platform, stdlib, or existing dependency
  already covers it.
- Restating comments: comments narrate obvious control flow, restate code, or
  keep history that belongs in git.
- Deletion test: code can be deleted or inlined without changing external
  behavior.

Keep depth only for multiple real adapters, an external boundary, a measured
bottleneck, or a concurrency/compliance invariant.

## Remediation

When cleaning up on explicit request:

1. Run baseline `git status`, tests, and task verify.
2. Prove each candidate with call sites, adapter count, and behavior invariance;
   skip unproven items.
3. Delete or inline one seam at a time without adding new helpers, ports, or
   config.
4. Re-run verify after each removal; revert any change that alters behavior.
5. Name the structural remedy: delete or inline the seam, collapse duplicate
   branches, replace condition chains with a model or dispatcher, move feature
   logic to its owner, or reuse the canonical helper.

## Enforcement Ladder

When a mistake repeats, fix it at the highest effective level:

1. Architecture: remove the wrong path or give each piece of state one owner.
2. Types: make the bad state unrepresentable.
3. Lint or CI: fail with an error that names the correct replacement.
4. Tests: prove the behavior and fail when the behavior breaks.
5. Docs or agent rules: use only for judgment calls, and name the enforcement.

Prove each new guard fails on a real past mistake.

## Evidence

- Cite `file:line`, call-site/adapter count, or the deletion-test result.
- For high-impact claims, invert one condition, rerun the task verify, restore
  the file, and report any test that stayed green.

## Verify

Prefer the smallest removal that eliminates duplication or speculative surface;
re-run task verification.
