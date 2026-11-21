# Doctor Checks

1. **Wrong format**: Repair malformed existing `AGENTS.md` and `.artifacts/` root records against templates.
2. **Wrong locations**: Repair misplaced test links, task details, and retired records.
3. **Path pointers**: Repair broken pointers to current workspace paths using the templates.
4. **Gitignore coverage**: Confirm the CLI-created `.artifacts/.gitignore` is present.
5. **Instruction budgets**: Ensure `AGENTS.md` stays under 500 tokens and `.artifacts/CONTEXT.md` matches its template.
6. **Graph integrity**: Run `<skill-dir>/scripts/iridescent-artifacts check` and `verify-links`; repair only structural failures.
7. **Retirement integrity**: Confirm retirement fields appear only in `DECISIONS.md` and retired records keep their historical IDs.
8. **Remaining gaps**: Emit semantic gaps as a target-state request with the owning lifecycle skill.
