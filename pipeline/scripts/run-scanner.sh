#!/bin/bash
set -euo pipefail

# Scanner pipeline orchestration script
# Usage: run-scanner.sh [--eml <file.eml>] [--html <file.html>] [--sources-only]
# At least one of --eml, --html, or --sources-only must be provided.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Generate run ID
RUN_ID=$(date -u +"%Y-%m-%dT%H-%M-%S")
RUN_DIR="$PROJECT_ROOT/pipeline/runs/$RUN_ID"

# Parse arguments
EML_FILE=""
HTML_FILE=""
SOURCES_ONLY=false

while [[ $# -gt 0 ]]; do
  case $1 in
    --eml)
      EML_FILE="$2"
      shift 2
      ;;
    --html)
      HTML_FILE="$2"
      shift 2
      ;;
    --sources-only)
      SOURCES_ONLY=true
      shift
      ;;
    -h|--help)
      echo "Usage: $(basename "$0") [--eml <file.eml>] [--html <file.html>] [--sources-only]"
      echo ""
      echo "Options:"
      echo "  --eml <file>      Path to .eml email digest file (will be converted to HTML)"
      echo "  --html <file>     Path to pre-converted HTML digest file"
      echo "  --sources-only    Skip digest parsing, only scan web sources"
      echo ""
      echo "At least one of --eml, --html, or --sources-only must be provided."
      exit 0
      ;;
    *)
      echo "ERROR: Unknown option: $1" >&2
      exit 1
      ;;
  esac
done

# Validate arguments
if [ -z "$EML_FILE" ] && [ -z "$HTML_FILE" ] && [ "$SOURCES_ONLY" = false ]; then
  echo "ERROR: Must provide --eml, --html, or --sources-only" >&2
  exit 1
fi

# Create run directory
mkdir -p "$RUN_DIR"
echo "Pipeline run: $RUN_ID"
echo "Run directory: $RUN_DIR"

# Step 1: Convert EML to HTML if needed
if [ -n "$EML_FILE" ]; then
  echo "Converting EML to HTML..."
  HTML_FILE=$("$SCRIPT_DIR/convert-eml.sh" "$EML_FILE")
  echo "HTML file: $HTML_FILE"
fi

# Step 2: Build scanner prompt
SCANNER_PROMPT="Scan for new regulatory developments."
SCANNER_PROMPT="$SCANNER_PROMPT Pipeline run ID: $RUN_ID."
SCANNER_PROMPT="$SCANNER_PROMPT Read pipeline/config/sources.json for source definitions."

if [ -n "$HTML_FILE" ]; then
  SCANNER_PROMPT="$SCANNER_PROMPT Parse the email digest HTML file at: $HTML_FILE"
  SCANNER_PROMPT="$SCANNER_PROMPT Extract items from privacy, cybersecurity, and AI law sections only."
  SCANNER_PROMPT="$SCANNER_PROMPT Follow each Lexology link to fetch full article text."
fi

if [ "$SOURCES_ONLY" = true ]; then
  SCANNER_PROMPT="$SCANNER_PROMPT Skip digest parsing -- only scan web sources from the config file."
fi

SCANNER_PROMPT="$SCANNER_PROMPT Write your output JSON to: $RUN_DIR/scanner-output.json"
SCANNER_PROMPT="$SCANNER_PROMPT The output must be a valid envelope (schema_version 1.0, stage scanner, status complete or error) with a data object containing a findings array and optional source_failures array."

# Step 3: Invoke scanner agent
echo "Invoking scanner agent..."
claude -p --agent scanner --output-format json \
  --max-turns 25 \
  "$SCANNER_PROMPT"

# Step 4: Validate output
OUTPUT_FILE="$RUN_DIR/scanner-output.json"
if [ ! -f "$OUTPUT_FILE" ]; then
  echo "ERROR: Scanner did not produce output at $OUTPUT_FILE" >&2
  exit 1
fi

echo "Validating scanner output..."
"$PROJECT_ROOT/pipeline/scripts/validate-handoff.sh" scanner "$OUTPUT_FILE"

# Step 4.5: Annotate topic keys (deterministic post-process)
echo "Annotating topic keys..."
python3 "$PROJECT_ROOT/tools/topic_keys.py" annotate --input "$OUTPUT_FILE"

# Step 5: Report results
FINDING_COUNT=$(jq '.data.findings | length' "$OUTPUT_FILE")
FAILURE_COUNT=$(jq '.data.source_failures // [] | length' "$OUTPUT_FILE")
echo ""
echo "Scan complete."
echo "  Findings: $FINDING_COUNT"
echo "  Source failures: $FAILURE_COUNT"
echo "  Output: $OUTPUT_FILE"

# Signal that dedup and review generation should follow
echo ""
echo "Next: Run dedup and generate review file."
echo "  pipeline/scripts/dedup-findings.sh $RUN_ID"
