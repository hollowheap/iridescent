# Workspace Templates

## `AGENTS.md` (`<= 60` lines)

```markdown
# <Repository Name>

<One-sentence summary of the stack, domain, and primary deliverable.>

## Essential Commands

- Build / check: `<verified command>`
- Test suite: `<verified command>`
- Single test / module: `<verified command for targeted feedback>`

## Conventions

- <Non-obvious architectural, boundary, or toolchain invariant.>
- <Safety rule ("Never ...") that holds on every turn.>
- <Optional one-line pointer to a project skill when a multi-step workflow runbook exists.>
```

## `.artifacts/CONTEXT.md` (`<= 60` lines)

```markdown
# Context

## Stack & Entrypoints

- <Runtime, language, and build/package manifests.>
- <Primary service, CLI, or library entrypoints with exact paths.>

## Module Seams

- **<Slice or Module> (`<path>`)**: <Owned responsibility, public boundary, and inward dependency direction.>
```

## `.artifacts/ARCHITECTURE.md`

```markdown
# Architecture

Last verified: <YYYY-MM-DD>.
Scope: <system or feature slice>.

## System Shape

Hosts, services, deployment units, data flow, and trust boundaries.

## Module Seams

Vertical slices, ownership, public boundaries, composition roots, and inward dependency direction.

## Framework & Library Choices

Selected frameworks, packages, versions, extension points, and exit costs.

## Data & Contracts

Schemas, protocols, error model, compatibility, and storage.

## Operations & Security

Observability, backups, rollback, secrets, exposure, and recovery.

## Known Debt

Accepted gaps with owner and impact.

## Evidence

Accepted decisions, specs, and checks that support the current view.
```
