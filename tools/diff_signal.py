#!/usr/bin/env python3
"""Classify how a new regulatory finding relates to an existing indexed report.

Used by the Phase 2 update-existing-report pipeline: when dedup-findings.sh
hits a topic_key match, it calls this classifier to decide whether the finding
is (a) pure noise to drop silently, or (b) a candidate update that should
append an "## Update {date}" section to the existing report.

The classifier is pure string matching — no LLM — so it's deterministic and
unit-testable.

Library:
    from tools.diff_signal import classify
    result = classify(finding, existing_entry)
    # result = {"diff_signal": "...", "status_before": "...", "status_after": "..."}

CLI (for the bash dedup script):
    python3 tools/diff_signal.py --finding-json '{...}' --existing-json '{...}'
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from typing import Any


# Order matters — first match wins. Each entry: (regex, diff_signal, derived_status_after).
# The derived status_after is a best-effort mapping; downstream can override.
PATTERNS: list[tuple[re.Pattern, str, str]] = [
    (re.compile(r"\bvetoed\b", re.IGNORECASE), "vetoed", "vetoed"),
    (re.compile(r"\bsigned\s+into\s+law\b", re.IGNORECASE), "signed", "signed"),
    (re.compile(r"\benacted\b", re.IGNORECASE), "signed", "signed"),
    (re.compile(r"\bbecame\s+law\b", re.IGNORECASE), "signed", "signed"),
    (re.compile(r"\bsigned\s+by\b", re.IGNORECASE), "signed", "signed"),
    (re.compile(r"\bapproved\s+by\s+governor\b", re.IGNORECASE), "signed", "signed"),
    # Catch-all: bare "signed" verb. Must come AFTER the more specific signed
    # patterns so they win when present.
    (re.compile(r"\bsigned\b", re.IGNORECASE), "signed", "signed"),
    (re.compile(r"\bsubstitute\s+(adopted|passed)\b", re.IGNORECASE), "amendment", "amended"),
    (re.compile(r"\bamended\b", re.IGNORECASE), "amendment", "amended"),
    (re.compile(r"\bamendment\s+adopted\b", re.IGNORECASE), "amendment", "amended"),
    (re.compile(r"\b(?:civil\s+)?penalt(?:y|ies)\b", re.IGNORECASE), "new_penalty", "penalty-imposed"),
    (re.compile(r"\bconsent\s+order\b", re.IGNORECASE), "new_penalty", "consent-order"),
    (re.compile(r"\bsettlement\b", re.IGNORECASE), "new_penalty", "settled"),
    (re.compile(r"\benforcement\s+action\b", re.IGNORECASE), "new_penalty", "enforcement"),
    (re.compile(r"\bfine(?:d|s)?\b", re.IGNORECASE), "new_penalty", "penalty-imposed"),
    (re.compile(r"\bpassed\s+(?:the\s+)?(?:house|senate|committee|chamber)\b", re.IGNORECASE), "status_change", "passed-first-chamber"),
    (re.compile(r"\bpassed\s+both\s+chambers\b", re.IGNORECASE), "status_change", "passed-second-chamber"),
    (re.compile(r"\bcleared\s+committee\b", re.IGNORECASE), "status_change", "passed-committee"),
    (re.compile(r"\breported\s+favorably\b", re.IGNORECASE), "status_change", "passed-committee"),
    (re.compile(r"\badvanced\s+from\s+committee\b", re.IGNORECASE), "status_change", "passed-committee"),
    (re.compile(r"\bdied\b|\bfailed\b|\bstalled\b", re.IGNORECASE), "status_change", "dead"),
    (re.compile(r"\btabled\b", re.IGNORECASE), "status_change", "tabled"),
]

# Intro verbs: only treated as status_change if existing has no current_status yet.
# Otherwise re-stating "introduced" when already tracked = noise.
INTRO_RE = re.compile(r"\b(introduced|filed|prefiled)\b", re.IGNORECASE)


def classify(finding: dict[str, Any], existing: dict[str, Any]) -> dict[str, str]:
    """Classify how `finding` relates to an already-indexed `existing` report entry.

    Returns a dict with keys: diff_signal, status_before, status_after.

    diff_signal is one of: noise | status_change | signed | vetoed | amendment |
    new_penalty | narrative_only.
    """
    title = (finding.get("title") or "").strip()
    summary = (finding.get("summary") or "").strip()
    haystack = f"{title}\n{summary}"

    status_before = (existing.get("current_status") or "").strip()

    for pattern, signal, derived_status in PATTERNS:
        if pattern.search(haystack):
            # If the derived status matches the existing current_status, this is noise
            # (e.g., existing is already "signed" and the finding restates it).
            if derived_status and status_before and derived_status == status_before:
                return {
                    "diff_signal": "noise",
                    "status_before": status_before,
                    "status_after": status_before,
                }
            return {
                "diff_signal": signal,
                "status_before": status_before,
                "status_after": derived_status or status_before,
            }

    # Intro verbs: only a status change if we don't already have a status
    if INTRO_RE.search(haystack):
        if not status_before:
            return {
                "diff_signal": "status_change",
                "status_before": "",
                "status_after": "introduced",
            }
        # Already tracked; restating "introduced" is noise
        if status_before == "introduced":
            return {
                "diff_signal": "noise",
                "status_before": status_before,
                "status_after": status_before,
            }
        # Existing has a later status; re-stating "introduced" is a regression marker — narrative only
        return {
            "diff_signal": "narrative_only",
            "status_before": status_before,
            "status_after": status_before,
        }

    # No verb matched. If the finding seems to restate the same topic with no new signal,
    # treat it as narrative_only — not quite noise because the title/summary may carry fresh
    # context even without a status verb. The reviewer will decide whether to escalate.
    return {
        "diff_signal": "narrative_only",
        "status_before": status_before,
        "status_after": status_before,
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--finding-json", required=True, help="Finding object as JSON string")
    p.add_argument("--existing-json", required=True, help="Existing index entry as JSON string")
    args = p.parse_args()

    try:
        finding = json.loads(args.finding_json)
    except json.JSONDecodeError as e:
        print(json.dumps({"error": f"invalid finding JSON: {e}"}), file=sys.stderr)
        return 2
    try:
        existing = json.loads(args.existing_json) or {}
    except json.JSONDecodeError as e:
        print(json.dumps({"error": f"invalid existing JSON: {e}"}), file=sys.stderr)
        return 2

    print(json.dumps(classify(finding, existing)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
