#!/bin/bash
set -euo pipefail
# Round-trip every documented example envelope through validate-handoff.sh.
# Filename convention: <stage>-<variant>.json -> stage is the part before the first '-'
# except 'fpf-scanner' which contains a dash; handle it explicitly.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXAMPLES_DIR="$SCRIPT_DIR/../schemas/examples"
FAIL=0
for f in "$EXAMPLES_DIR"/*.json; do
  base=$(basename "$f" .json)
  case "$base" in
    fpf-scanner*) stage="fpf-scanner" ;;
    *) stage="${base%%-*}" ;;
  esac
  if "$SCRIPT_DIR/validate-handoff.sh" "$stage" "$f" >/dev/null 2>&1; then
    echo "OK   $base ($stage)"
  else
    echo "FAIL $base ($stage)"
    FAIL=1
  fi
done
exit $FAIL
