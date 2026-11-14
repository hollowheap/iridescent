---
name: specify
description: Turn accepted design into verified specs.
disable-model-invocation: true
---

## Workflow

1. Run `scripts/artifacts.sh unconverted-decs`; if output is NONE, stop immediately.
2. Derive `Sxx` from accepted `Rxx`, `Dxx`, and the architecture view. If a parent or architecture section is missing, stop.
3. Probe ambiguous seams with the question tool and block until answered; if an answer changes design or architecture, return to `{{skill:design}}` to record `Dxx` before writing `Sxx`.
4. Run `scripts/artifacts.sh next-id s` to obtain sequential `Sxx` IDs.
5. Append public boundary invariants to `.artifacts/SPECS.md` under the vertical-slice H3 heading and the `#### <Arch>` H4 group (see `references/examples.md` only if the format is unfamiliar); cite the accepted decision and architecture section.
6. Run `scripts/artifacts.sh check` to verify trace links and graph shape.

## Rules

- Every spec references a parent `Rxx` and accepted `Dxx`.
- Specify public seams and external behavioral invariants (including edge-case failure behavior).
- Every spec declares an explicit verification command and sits under an H4 heading named after the architecture H2.
- Block via the question tool on design forks and route design changes through `{{skill:design}}`.
- Parent decision completion is derived from child references.
- Verify: `scripts/artifacts.sh check` outputs OK and `unconverted-specs` lists the new items.
