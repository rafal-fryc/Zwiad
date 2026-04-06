#!/bin/bash
set -euo pipefail

# Resolve paths relative to pipeline/ directory, not cwd
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

EXPECTED_VERSION="1.0"

usage() {
  echo "Usage: $(basename "$0") <schema-name> <json-file>"
  echo ""
  echo "Validates a JSON handoff file against the envelope schema and a stage-specific schema."
  echo ""
  echo "Arguments:"
  echo "  schema-name   One of: scanner, researcher, reviewer, categorizer"
  echo "  json-file     Path to the JSON file to validate"
  echo ""
  echo "Examples:"
  echo "  $(basename "$0") scanner pipeline/state/2026-04-06T14-30-00/scanner-output.json"
}

# 1. Usage check
if [ $# -lt 2 ]; then
  usage
  exit 1
fi

SCHEMA="$1"
FILE="$2"

# 2. File existence check
if [ ! -f "$FILE" ]; then
  echo "ERROR: File not found: $FILE" >&2
  exit 1
fi

# 3. JSON syntax validation
if ! jq empty "$FILE" 2>/dev/null; then
  echo "ERROR: Invalid JSON in $FILE" >&2
  exit 1
fi

# 4. Envelope validation
if ! jq -e -f "${SCRIPT_DIR}/schemas/envelope.jq" "$FILE" >/dev/null 2>&1; then
  echo "ERROR: Envelope validation failed for $FILE" >&2
  echo "Required envelope fields: schema_version, pipeline_run_id, timestamp, stage, status, data" >&2
  exit 1
fi

# 5. Schema version check (D-08)
ACTUAL_VERSION=$(jq -r '.schema_version' "$FILE")
if [ "$ACTUAL_VERSION" != "$EXPECTED_VERSION" ]; then
  echo "ERROR: Schema version mismatch in $FILE: expected $EXPECTED_VERSION, got $ACTUAL_VERSION" >&2
  exit 1
fi

# 6. Stage-specific validation
STAGE_JQ="${SCRIPT_DIR}/schemas/${SCHEMA}.jq"
if [ -f "$STAGE_JQ" ]; then
  if ! jq -e -f "$STAGE_JQ" "$FILE" >/dev/null 2>&1; then
    echo "ERROR: Stage-specific validation failed for $FILE against $SCHEMA" >&2
    exit 1
  fi
fi

# 7. Success
echo "OK: $FILE validates against $SCHEMA"
exit 0
