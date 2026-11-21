# Robustness Review Profile

Use for whole-system failure-mode, recovery, and cross-slice workspace audits. Complements `references/slice.md` and `references/seam.md` across the pre-defined slice roster.

## Gate

Agent-heavy. Propose the canonical slice and shared-seam roster, concurrency, and output; wait for approval and spawn only read-only subagents.

## Workflow

1. Preflight: `<skill-dir>/scripts/iridescent-artifacts status`; read canonical slices from `.artifacts/REQUIREMENTS.md` and `.artifacts/ARCHITECTURE.md`, prioritizing slices touched by recent git history; start from a clean baseline, never mid-rewrite.
2. Dispatch one read-only subagent per approved slice (applying `references/slice.md` + triggered lenses) and per cross-cutting boundary (`references/seam.md`). Self-contained prompt: repo, slice/seam, option sweep, primary docs, failure paths, report shape, no edits. Persist `.artifacts/review/<slice>.md`.
3. Reproduce high-impact claims locally. Separate dead config, missing recovery, and missing preference.
4. Synthesize cross-slice findings by severity: data loss, lockout, exposure, dead config, seam drift. Name concrete contracts; never turn every finding into a knob.
5. Flag unresolved design forks as blocking findings routed strictly to the `design` skill; never write `Rxx`, `Dxx`, `Sxx`, or `Txx` during review.
6. Compare recorded architecture with observed structure; report drift as a blocking finding routed to `update`.

## Evidence

- Every finding names the failure and reproduction command.
- "Could be configured" is not a finding.
- Local files first, official docs second; reject options covered by modern upstream defaults under `Rejected defaults`.
- Every claim needs `file:line`, a URL, or a reproduction run; drop unrun behavioral speculation, and use `UNVERIFIED` only when an environment dependency is absent.
- Treat child sessions as untrusted; verify tools, scope, and claims.

## Report

Each finding: `Current` (`file:line`), `Gap`, `Failure/impact`, `Config` (minimal shape), `Source`, `Default check`, `Confidence`.
Add `## Lens ledger`, `## Failure modes`, `## Seams`, `## Rejected defaults`, and `## Blocking Design Forks`.

## Verify

- `.artifacts/review/<slice>.md` exists for approved slices (`Vxx` indexed in `.artifacts/REVIEWS.md`).
- Every slice names one user-visible outcome and one end-to-end verification.
- High-impact claims were reproduced locally, not trusted from a child report.
