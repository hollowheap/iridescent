# Decision Record

Group accepted decisions under the exact architecture H2 heading: `### System Shape`, `### Module Seams`, `### Framework & Library Choices`, `### Data & Contracts`, or `### Operations & Security`.

### <Architecture H2>

- [x] Dxx [Rxx]: <accepted decision>
  - Context: <problem, constraints, and forces>
  - Alternatives: <rejected options and why>
  - Consequences: <what changes, what gets harder>
  - Supersedes: <Dyy>      # only when replacing a decision

## Rules

- Record accepted decisions only; resolve ambiguities via the question tool before writing a decision. An accepted decision may remain `[ ]` only until its child specs complete.
- The H3 heading is the sole architecture reference; it must match an H2 in `ARCHITECTURE.md` exactly. Include strictly `Context`, `Alternatives`, `Consequences`, and optional `Supersedes`; never add a per-decision `Arch:` or `Verify:` field (verification belongs strictly to child specs).
- Include `Supersedes` only when replacing an earlier decision; omit it when it does not apply.
