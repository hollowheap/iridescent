---
name: review
description: Audit changed code and slices with severity-ordered findings.
disable-model-invocation: true
---

## Scope

- Covers: read-only audits of changed hunks, slices, seams, and durable findings.
- Excludes: requirements, design, specification, planning, and feature implementation.

## Workflow

1. Read the minimum inputs: parent task, spec, decision, architecture section, changed hunks, and one verification.
2. Run `references/simplicity.md`; load only lenses triggered by the change.
3. Report findings ordered by severity (`High`, `Medium`, `Low`), leading with correctness and security:
   - Cite `file:line` and a named structural remedy; drop unrun behavioral speculation.
   - Keep five `High`/`Medium` findings maximum; keep `Low` notes one line or omit them.
4. Write durable findings with templates from `references/review-record.md` and `references/REVIEWS.md`, respectively.
5. Route unresolved design forks to `design`; return findings to implementation and confirm the final verdict.

## Rules

- Run review strictly after implementation.
- Treat implementation self-audit as context, not proof.
- Load `references/simplicity.md` and matching lenses only.
- Write only durable review records and their index.
- Do not claim rendered checks unless a reproducible rendered command is recorded.
- Block completion on correctness, security, or unresolved design findings.
- Keep review strictly read-only; apply fixes only during implementation.

## Verify

- Verify: severity order, named remedies, durable-record rules, and verification pass.
