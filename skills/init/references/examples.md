# Init Examples

## Bad
- Running init when `AGENTS.md` already exists, resetting or overwriting repo conventions.
- Dumping 300 lines of file trees and internal types into `CONTEXT.md`.
- Writing unverified commands that fail during subsequent implementation.
- Creating `CONTEXT.md` without an architecture view.

## Good
- Confirm `AGENTS.md` does not exist, scout manifests, verify `nix flake check`, and emit initial `AGENTS.md`, `.artifacts/CONTEXT.md`, and `.artifacts/ARCHITECTURE.md`.
