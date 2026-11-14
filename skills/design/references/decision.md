# Decision Record

Group accepted decisions under the exact architecture H2 heading: `### System Shape`, `### Module Seams`, `### Framework & Library Choices`, `### Data & Contracts`, or `### Operations & Security`.

### <Architecture H2>

- [x] Dxx [Rxx]: <accepted decision>
  - Context: <problem, constraints, and forces>
  - Alternatives: <rejected options and why>
  - Consequences: <what changes, what gets harder>
  - Supersedes: <Dyy>      # only when replacing a decision

## Rules

- Record accepted decisions only; resolve ambiguities via the question tool before writing a decision. An accepted decision may remain `[ ]` until its child specs complete.
- The H3 heading is the architecture reference; it must exactly match an H2 in `architecture.md`. Do not add a per-decision `Arch:` field.
- Verification belongs to child specs. Do not add a decision-level `Verify:` field.
- Include `Supersedes` only when replacing an earlier decision; omit it when it does not apply.
