# Data Lens

## Territory

Persistence, database schemas, migrations, transactions, queries, and connection/pool lifecycles.

## Triggers

- The diff adds or changes a DB schema, migration, query, transaction, or persistent file/state format.
- The diff changes connection setup, pool sizing, or shutdown/cleanup of storage resources.

## Checks

- Migrations and state-format updates use safe expand-and-contract steps without data loss or breaking live readers.
- Large-table locks, backfills, and destructive drops/truncates are bounded and guarded.
- Multi-step writes execute atomically in a transaction or remain idempotent on partial failure.
- Connections, cursors, and pools close cleanly on completion, error, and shutdown.

## Evidence

- Cite `file:line` for the schema/migration, transaction boundary, or pool lifecycle.

## Verify

Persistence or migration checks cover empty state, existing rows, rollback/partial-failure recovery, and clean shutdown.
