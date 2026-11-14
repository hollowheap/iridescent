# Robustness Review Profile

Use for whole-system failure-mode, recovery, and cross-slice workspace audits. Complements `references/slice.md` and `references/seam.md` across the pre-defined slice roster.

## Gate

Agent-heavy. Propose the canonical slice and shared-seam roster, concurrency, and output; wait for approval. Do not spawn primary-role agents.

## Workflow

1. Preflight: `scripts/artifacts.sh status`; regenerate `.artifacts/REPOMAP.md`; read the canonical vertical slices from `.artifacts/REQUIREMENTS.md` and `.artifacts/ARCHITECTURE.md`; do not start mid-rewrite.
2. Dispatch one read-only subagent per approved slice (applying `references/slice.md` + triggered lenses) and per cross-cutting boundary (`references/seam.md`). Self-contained prompt: repo, slice/seam, option sweep, primary docs, failure paths, report shape, no edits. Persist `.artifacts/review/<slice>.md`.
3. Reproduce high-impact claims locally. Separate dead config, missing recovery, and missing preference.
4. Synthesize cross-slice findings by severity: data loss, lockout, exposure, dead config, seam drift. Name contracts; do not turn every finding into a knob.
5. Flag unresolved design forks as blocking findings routed to `{{skill:design}}`; never write `Rxx` or `Dxx` during review.
6. Update `.artifacts/ARCHITECTURE.md` with: System Shape, Module Seams, Framework & Library Choices, Data & Contracts, Operations & Security, Known Debt, Evidence. Diff, slice, and seam profiles never write it.

## Evidence

- Every finding names the failure and reproduction command.
- "Could be configured" is not a finding.
- Local files first, official docs second; reject options covered by modern upstream defaults under `Rejected defaults`.
- Every claim needs `file:line` or a URL; mark the rest UNVERIFIED.
- Treat child sessions as untrusted; verify tools, scope, and claims.

## Report

Each finding: `Current` (`file:line`), `Gap`, `Failure/impact`, `Config` (minimal shape), `Source`, `Default check`, `Confidence`.
Add `## Lens ledger`, `## Failure modes`, `## Seams`, `## Rejected defaults`, and `## Blocking Design Forks`.

## Verify

- `.artifacts/review/<slice>.md` exists for approved slices (`Vxx` indexed in `.artifacts/REVIEWS.md`).
- Every slice names one user-visible outcome and one end-to-end verification.
- High-impact claims were reproduced locally, not trusted from a child report.
