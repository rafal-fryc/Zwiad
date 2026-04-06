#!/bin/bash
set -euo pipefail

# Convert .eml file to HTML using eml-to-html Python CLI (D-01)
# Usage: convert-eml.sh <input.eml>
# Output: prints path to generated .html file

INPUT_FILE="$1"
if [ -z "${INPUT_FILE:-}" ] || [ ! -f "$INPUT_FILE" ]; then
  echo "ERROR: File not found: ${INPUT_FILE:-<none>}" >&2
  echo "Usage: $(basename "$0") <input.eml>" >&2
  exit 1
fi

# eml-to-html outputs HTML file alongside the .eml
eml-to-html "$INPUT_FILE"

HTML_FILE="${INPUT_FILE%.eml}.html"
if [ -f "$HTML_FILE" ]; then
  echo "$HTML_FILE"
else
  echo "ERROR: Conversion failed -- no HTML output at $HTML_FILE" >&2
  exit 1
fi
