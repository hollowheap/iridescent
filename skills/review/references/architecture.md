# Architecture Lens

## Territory

Module boundaries, vertical slices, dependency direction, ports/adapters, and composition roots.

## Triggers

- The diff adds a module, package, or directory, or moves logic across layers.
- The diff introduces an interface/port, adapter, or global/config dependency wiring.

## Checks

- Group code by cohesive vertical slices rather than scattered horizontal technical layers.
- Core domain logic imports zero HTTP transport, DB clients, ORMs, or framework glue.
- Dependencies flow inward: domain defines ports; infrastructure adapters implement them.
- Wire configuration and dependencies explicitly at the composition root; no hidden globals or inline env reads in domain code.
- Design deep modules: hide internal state and mechanics behind stable boundaries instead of leaking storage or transport details.

## Evidence

- Cite `file:line` for cross-layer imports, leaked internals, or scattered global reads.

## Verify

Domain logic tests run in memory without database drivers or HTTP servers, and slice boundaries hold.
