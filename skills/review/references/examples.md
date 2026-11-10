# Review Examples

## Bad
- Reviewing requirements, design, specification, and planning as separate phases.
- Asking the reviewer to rewrite entire files instead of citing exact line numbers.
- Putting gate checklists in tasks instead of keeping tasks minimal.
- Omitting a lens row because the lens looked irrelevant; a skipped lens with no row is an unreported gap.

## Good
- Review the implemented change against its parent `Sxx`, cite `file:line`, patch boundary bugs, and re-verify.
- Run the final review after implementation, not during design or planning.
- The reviewer sees a shallow wrapper and demands a new port; with one adapter, that is speculative.
- Record every lens: `backend: considered`, `security: considered`, `performance: considered`, `ui: skipped (opal not invoked)`, `simplicity: loaded`.
