#!/usr/bin/env bash
set -euo pipefail
SELF_DIR="$(cd -P "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -f "$SELF_DIR/../../../scripts/artifacts.sh" ]; then
  exec python3 "$SELF_DIR/../../../scripts/artifacts.sh" "$@"
elif command -v iridescent-artifacts >/dev/null 2>&1; then
  exec iridescent-artifacts "$@"
elif [ -f "$PWD/scripts/artifacts.sh" ]; then
  exec python3 "$PWD/scripts/artifacts.sh" "$@"
elif [ -f "$SELF_DIR/artifacts.py" ]; then
  exec python3 "$SELF_DIR/artifacts.py" "$@"
elif command -v curl >/dev/null 2>&1; then
  curl -fsSL https://raw.githubusercontent.com/hollowheap/iridescent/main/scripts/artifacts.sh -o "$SELF_DIR/artifacts.py"
  exec python3 "$SELF_DIR/artifacts.py" "$@"
else
  echo "Error: scripts/artifacts.sh backend not found. Install iridescent-artifacts or place scripts/artifacts.sh in the workspace." >&2
  exit 1
fi
