# Requirement Record

Group requirements by vertical slice under meaningful H3 headings. Use `### Cross-cutting` only for a requirement that genuinely spans slices.

### <Slice>

- [ ] Rxx: <observable outcome>
  - Verify: <acceptance command>
  - Acceptance: <observable result>
  - Constraints: <non-negotiable constraint or none>
  - Non-goals: <excluded outcome or none>
  - Rationale: <why this outcome matters>

## Rules

- Describe strictly what changes for the user (observable outcomes), never how it is built.
- Never name a file, module, framework, library, option, or API; move every solution choice to a decision.
- Keep one outcome per requirement.
