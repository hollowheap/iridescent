# Always On Checks

Never skipped; not a lens.

## Checks

- Single-adapter abstraction: is there a port or interface with one implementation and no second consumer?
- One-use helper: does a function, module, or option have exactly one caller and no independent reason to exist?
- Speculative option or config: does an option exist without a current caller or a current requirement?
- Duplicate validation or seam: is the same check enforced in two places, or does a second seam mirror an existing one?
- Unnecessary framework or dependency: can the platform, standard library, or an existing dependency do the job?
- Test restating implementation: does the test assert internals instead of a public seam or user-visible behavior?
- Deletion test: can the code be deleted without changing behavior, and does anything outside the diff still require it?

## Evidence

- Cite `file:line` for each finding.
- Name the deletion test result or the concrete duplicate.

## Verify

Prefer the smallest change that removes the duplication or speculative surface; re-run the task verification.
