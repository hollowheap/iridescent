# Performance Lens

## Territory

Hot paths, large data, startup latency, repeated work, unbounded growth, and measured regressions.

## Triggers

- The diff adds a loop, query, render, cache, or allocation on a hot path.
- The diff changes startup, rebuild, scheduling, or background work.
- The diff handles large or unbounded data.
- A measurement shows a regression, or the change claims a speedup.

## Checks

- Measure before optimizing; cite the command, trace, or benchmark.
- State the expected load and whether the code is correct at that load.
- Look for repeated work, N+1 queries, unbounded lists or caches, blocking I/O, and per-item process or network calls.
- For rendered interfaces, check layout thrashing, expensive animation, unoptimized images, render churn, and `will-change` left on at rest.
- Check startup and rebuild cost, not only steady-state runtime.
- Prefer simpler algorithms and existing platform behavior before adding caches or frameworks.
- Do not trade correctness, security, or clarity for an unmeasured micro-optimization.

## Evidence

- Report the measurement command, workload, and before/after numbers.
- Cite `file:line` for each suspected hotspot.

## Verify

Run the same measurement before and after; report the numbers and the workload.
