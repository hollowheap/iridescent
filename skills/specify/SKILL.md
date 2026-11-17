---
name: specify
description: Turn accepted design into verified specs.
disable-model-invocation: true
---

## Scope

- Covers: converting accepted decisions into public-boundary specs in `.artifacts/SPECS.md`.
- Excludes: design decisions, task planning, implementation, and review.

## Workflow

1. Run `scripts/iridescent-artifacts unconverted-decs`; if output is NONE, stop immediately.
2. Derive `Sxx` from accepted `Rxx`, `Dxx`, and the architecture view. If a parent or architecture section is missing, stop.
3. Probe ambiguous seams with the host's structured question tool, giving 2-4 options, a recommendation, and answer consequences; block until answered, and return to the `design` skill to record `Dxx` before writing `Sxx` if an answer changes design or architecture.
4. Run `scripts/iridescent-artifacts next-id s` to obtain sequential `Sxx` IDs.
5. Append public boundary invariants to `.artifacts/SPECS.md` under the vertical-slice H3 heading and the `#### <Arch>` H4 group with `Seam`, `Behavior`, `Failures`, and `Verify` fields (see `references/examples.md` only if the format is unfamiliar); cite the accepted decision and architecture section.
6. Run `scripts/iridescent-artifacts check` to verify trace links and graph shape.

## Rules

- Reference parent `Rxx` and accepted `Dxx` strictly by ID; never restate their text.
- Specify strictly public seams and external behavioral invariants (including edge-case failure behavior), never private implementation details.
- Write zero stubs; if verification is not known from requirements, design, and architecture, stop and resolve the decision.
- Every spec declares `Seam`, `Behavior`, `Failures`, and an explicit `Verify` command and sits strictly under an `#### <Arch>` H4 heading named exactly after the architecture H2; never repeat an `Arch:` field per spec.
- Never resolve a design fork inside a spec; block via the host's structured question tool and route design changes strictly through the `design` skill.
- Edit only `.artifacts/SPECS.md`; never mark parent decisions complete (conversion is derived strictly from child references).
- Verify: `scripts/iridescent-artifacts check` outputs OK and `unconverted-specs` lists the new items.
