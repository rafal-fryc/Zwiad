#!/bin/bash
set -euo pipefail

# Install Zwiad pipeline cron job
# Usage: bash pipeline/cron/install-cron.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
CRONTAB_FILE="$SCRIPT_DIR/crontab.example"

if [ ! -f "$CRONTAB_FILE" ]; then
  echo "ERROR: crontab.example not found at $CRONTAB_FILE" >&2
  exit 1
fi

# Create logs directory for cron output
mkdir -p "$PROJECT_ROOT/pipeline/logs"

# Discover environment for notify-send
CURRENT_DISPLAY="${DISPLAY:-:0}"
CURRENT_DBUS="${DBUS_SESSION_BUS_ADDRESS:-unix:path=/run/user/$(id -u)/bus}"
CURRENT_PATH="$PATH"
CLAUDE_PATH="$(which claude 2>/dev/null || echo '/home/rafal/.local/bin/claude')"
PYTHON_PATH="$(which python3 2>/dev/null || echo '/usr/bin/python3')"

echo "Detected environment:"
echo "  DISPLAY=$CURRENT_DISPLAY"
echo "  DBUS=$CURRENT_DBUS"
echo "  claude=$CLAUDE_PATH"
echo "  python3=$PYTHON_PATH"
echo ""

# Test notify-send works
if notify-send --urgency=low "Zwiad" "Cron setup test" 2>/dev/null; then
  echo "notify-send: OK"
else
  echo "WARNING: notify-send failed -- notifications may not work from cron"
fi

# Build crontab entry with detected environment
CRON_ENTRY="# Zwiad Pipeline - installed $(date -u +%Y-%m-%dT%H:%M:%SZ)
DISPLAY=$CURRENT_DISPLAY
DBUS_SESSION_BUS_ADDRESS=$CURRENT_DBUS
PATH=$CURRENT_PATH
0 6 * * * cd $PROJECT_ROOT && $PYTHON_PATH run_pipeline.py run --web-only >> $PROJECT_ROOT/pipeline/logs/cron.log 2>&1"

# Merge with existing crontab (preserve other entries)
EXISTING=$(crontab -l 2>/dev/null || true)

# Check if Zwiad entry already exists
if echo "$EXISTING" | grep -q "run_pipeline.py"; then
  echo ""
  echo "WARNING: Zwiad cron entry already exists. Current crontab:"
  echo "$EXISTING" | grep -A1 "Zwiad"
  echo ""
  read -p "Replace existing entry? [y/N] " REPLY
  if [[ ! "$REPLY" =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 0
  fi
  # Remove old Zwiad entries
  EXISTING=$(echo "$EXISTING" | grep -v "Zwiad\|run_pipeline.py\|DBUS_SESSION_BUS_ADDRESS" | sed '/^$/d')
fi

# Install
echo "$EXISTING
$CRON_ENTRY" | crontab -

echo ""
echo "Cron job installed. Verify with: crontab -l"
echo "Pipeline will run daily at 06:00 UTC."
echo "Cron output logged to: $PROJECT_ROOT/pipeline/logs/cron.log"
