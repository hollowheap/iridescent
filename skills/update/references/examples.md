# Update Examples

## Bad
- Refreshing `CONTEXT.md` while leaving completed tasks unmarked in `TASKS.md`.
- Keeping an unaccepted open decision in `DECISIONS.md` instead of resolving it in `design`.
- Overwriting the entire `TASKS.md` file and destroying notes instead of using surgical `sed`.
- Marking a spec `[x]` without executing its Verify check.

## Good
- Run `sed -i 's/^- \[ \] T01:/- [x] T01:/' .artifacts/TASKS.md`, verify the build passes, and run `scripts/artifacts.sh verify-links`.
- Update `ARCHITECTURE.md` from accepted decisions and ensure every `Dxx` traces to specs or code.
