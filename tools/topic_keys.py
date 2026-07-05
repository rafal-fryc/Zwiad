#!/usr/bin/env python3
"""Generate stable topic keys for regulatory findings.

A topic key is a deterministic identifier for a regulatory story (bill,
enforcement action, rulemaking, guidance). The key is stable across runs so
the dedup layer can detect repeats and the update layer (Phase 2) can route
new developments to existing reports.

Usage as a library:
    from topic_keys import topic_key
    key, confidence, topic_type = topic_key(finding, rules)

Usage as a CLI (for non-Python callers):
    python3 tools/topic_keys.py --finding-json '{"title":"...","jurisdiction":"..."}'
        Prints {"topic_key":..., "topic_type":..., "confidence":...} to stdout.
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Tuple

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_RULES_PATH = PROJECT_ROOT / "pipeline" / "config" / "topic-key-rules.json"

US_STATE_ABBREV = {
    "alabama": "AL", "alaska": "AK", "arizona": "AZ", "arkansas": "AR",
    "california": "CA", "colorado": "CO", "connecticut": "CT", "delaware": "DE",
    "florida": "FL", "georgia": "GA", "hawaii": "HI", "idaho": "ID",
    "illinois": "IL", "indiana": "IN", "iowa": "IA", "kansas": "KS",
    "kentucky": "KY", "louisiana": "LA", "maine": "ME", "maryland": "MD",
    "massachusetts": "MA", "michigan": "MI", "minnesota": "MN", "mississippi": "MS",
    "missouri": "MO", "montana": "MT", "nebraska": "NE", "nevada": "NV",
    "new hampshire": "NH", "new jersey": "NJ", "new mexico": "NM", "new york": "NY",
    "north carolina": "NC", "north dakota": "ND", "ohio": "OH", "oklahoma": "OK",
    "oregon": "OR", "pennsylvania": "PA", "rhode island": "RI", "south carolina": "SC",
    "south dakota": "SD", "tennessee": "TN", "texas": "TX", "utah": "UT",
    "vermont": "VT", "virginia": "VA", "washington": "WA", "west virginia": "WV",
    "wisconsin": "WI", "wyoming": "WY",
}

BILL_TYPE_RE = re.compile(
    r"\b(HB|SB|AB|HR|SR|HJR|SJR|H\.?B\.?|S\.?B\.?|A\.?B\.?|HF|SF|HP|SP|LB|LD)\s*\.?\s*(\d{1,5}[A-Z]?)\b",
    re.IGNORECASE,
)

# Full-word bill type forms → short canonical abbreviations
BILL_TYPE_LONG_FORMS = [
    (re.compile(r"\bHouse\s+Bill\s+(?:No\.?\s+)?(\d{1,5}[A-Z]?)\b", re.IGNORECASE), "HB"),
    (re.compile(r"\bSenate\s+Bill\s+(?:No\.?\s+)?(\d{1,5}[A-Z]?)\b", re.IGNORECASE), "SB"),
    (re.compile(r"\bAssembly\s+Bill\s+(?:No\.?\s+)?(\d{1,5}[A-Z]?)\b", re.IGNORECASE), "AB"),
    (re.compile(r"\bHouse\s+Joint\s+Resolution\s+(?:No\.?\s+)?(\d{1,5}[A-Z]?)\b", re.IGNORECASE), "HJR"),
    (re.compile(r"\bSenate\s+Joint\s+Resolution\s+(?:No\.?\s+)?(\d{1,5}[A-Z]?)\b", re.IGNORECASE), "SJR"),
    (re.compile(r"\bHouse\s+Resolution\s+(?:No\.?\s+)?(\d{1,5}[A-Z]?)\b", re.IGNORECASE), "HR"),
    (re.compile(r"\bSenate\s+Resolution\s+(?:No\.?\s+)?(\d{1,5}[A-Z]?)\b", re.IGNORECASE), "SR"),
    (re.compile(r"\bLegislative\s+Document\s+(?:No\.?\s+)?(\d{1,5}[A-Z]?)\b", re.IGNORECASE), "LD"),
    (re.compile(r"\bLegislative\s+Bill\s+(?:No\.?\s+)?(\d{1,5}[A-Z]?)\b", re.IGNORECASE), "LB"),
]


FEDERAL_JURISDICTIONS = {"federal", "us federal", "united states", "us", "u.s.", "usa"}


def make_bill_key(state_abbrev: str, bill_type: str, bill_number: str, session_year: str) -> str:
    """Single source of truth for bill topic keys, shared with bill_processor.

    The cross-index dedup design (bill_processor <-> scanner findings) hinges
    on both producing byte-identical keys.

    bill_type and bill_number case is PRESERVED (only dots/spaces stripped):
    the scanner path (_find_bill_reference) already uppercases both before they
    reach here, while bill tracker entries with name-slug identifiers (e.g.
    "US-Lofgren-Comprehensive-2026", "US-AI-Guardrails-2026") rely on their
    persisted mixed-case form staying stable.
    """
    bill_type = re.sub(r"[.\s]", "", (bill_type or ""))
    bill_number = re.sub(r"[.\s]", "", (bill_number or ""))
    return f"{state_abbrev.upper()}-{bill_type}-{bill_number}-{session_year}"


def session_to_year(session: str) -> str:
    """Extract the closing 4-digit year from a session string ('2025-2026' -> '2026')."""
    years = re.findall(r"\d{4}", session or "")
    return years[-1] if years else ""


def _find_bill_reference(text: str) -> tuple[str, str] | None:
    """Search text for a bill identifier in either short or long form.
    Returns (bill_type, bill_number) or None."""
    m = BILL_TYPE_RE.search(text)
    if m:
        bill_type = re.sub(r"[.\s]", "", m.group(1)).upper()
        bill_number = m.group(2).upper()
        return bill_type, bill_number
    for pat, short in BILL_TYPE_LONG_FORMS:
        m = pat.search(text)
        if m:
            return short, m.group(1).upper()
    return None


def load_rules(path: Path = DEFAULT_RULES_PATH) -> dict:
    if not path.exists():
        return {"regulator_aliases": {}, "agency_aliases": {}}
    with open(path) as f:
        return json.load(f)


def _slug(text: str, max_len: int = 40) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text).strip("-")
    return text[:max_len].strip("-")


def _hash8(text: str) -> str:
    return hashlib.sha1(text.encode("utf-8")).hexdigest()[:8]


def _canon_regulator(raw: str, rules: dict) -> Tuple[str, bool]:
    """Return (canonical_code, is_known)."""
    if not raw:
        return "UNKNOWN", False
    normalized = raw.strip().lower()
    aliases = rules.get("regulator_aliases", {})
    for canonical, variants in aliases.items():
        if normalized == canonical.lower():
            return canonical, True
        for v in variants:
            if v.lower() in normalized or normalized in v.lower():
                return canonical, True
    return re.sub(r"[^A-Z0-9]", "", raw.upper())[:8] or "UNKNOWN", False


def _extract_year(finding: dict, default_to_current: bool = True) -> str:
    """Extract a 4-digit year from a finding's date-like fields.

    Falls back to the current year when nothing is found (unless
    default_to_current=False). Using the scan year as a session year is a
    deliberate compromise: most regulatory findings in fresh scanner output
    are from the current session, and a deterministic key is more useful than
    a hash fallback. Older stories can still be dated via the explicit fields.
    """
    for field in ("date", "first_reported", "scan_date", "timestamp"):
        val = finding.get(field) or ""
        m = re.match(r"(\d{4})", str(val))
        if m:
            return m.group(1)
    if default_to_current:
        from datetime import datetime, timezone
        return str(datetime.now(timezone.utc).year)
    return ""


def _state_bill_key(finding: dict) -> Tuple[str, str] | None:
    """Try to build a state bill key from finding fields. Returns (key, confidence)."""
    jurisdiction = (finding.get("jurisdiction") or "").strip()
    title = finding.get("title") or ""
    summary = finding.get("summary") or ""

    state_abbrev = None
    low = jurisdiction.lower()
    if low in FEDERAL_JURISDICTIONS:
        state_abbrev = "US"
    elif len(jurisdiction) == 2 and jurisdiction.isupper():
        state_abbrev = jurisdiction
    elif low in US_STATE_ABBREV:
        state_abbrev = US_STATE_ABBREV[low]

    if not state_abbrev:
        return None

    ref = _find_bill_reference(title) or _find_bill_reference(summary)
    if not ref:
        return None

    bill_type, bill_number = ref
    session = _extract_year(finding)

    key = make_bill_key(state_abbrev, bill_type, bill_number, session)
    return key, "high"


def _enforcement_key(finding: dict, rules: dict) -> Tuple[str, str] | None:
    """Build enforcement topic key from regulator + target + year."""
    title = finding.get("title") or ""
    summary = finding.get("summary") or ""
    source = finding.get("source") or ""

    regulator_raw = None
    for candidate in [source, title, summary]:
        for canonical, variants in rules.get("regulator_aliases", {}).items():
            for v in [canonical] + variants:
                if re.search(rf"\b{re.escape(v)}\b", candidate, re.IGNORECASE):
                    regulator_raw = v
                    break
            if regulator_raw:
                break
        if regulator_raw:
            break

    if not regulator_raw:
        return None

    regulator_code, is_known = _canon_regulator(regulator_raw, rules)
    if not is_known:
        return None

    target = None
    patterns = [
        r"(?:settle(?:ment|s|d)?|against|with|penalt(?:y|ies)|fines?|action against|enforcement)\s+(?:with\s+)?([A-Z][A-Za-z0-9&.\- ]{2,40}?)(?:\s+(?:for|over|after|under|on|regarding|in\s+connection)|[,.]|$)",
        r"([A-Z][A-Za-z0-9&.\- ]{2,40}?)\s+(?:to pay|agreed to|consent order|consent decree)",
    ]
    for pat in patterns:
        m = re.search(pat, title, re.IGNORECASE) or re.search(pat, summary, re.IGNORECASE)
        if m:
            candidate = m.group(1).strip()
            if candidate and candidate.lower() not in {regulator_raw.lower(), regulator_code.lower()}:
                target = candidate
                break

    year = _extract_year(finding)
    if not target or not year:
        return None

    target_slug = _slug(target, max_len=30).upper()
    target_slug = re.sub(r"-+", "-", target_slug).strip("-")
    if not target_slug:
        return None

    confidence = "high"
    return f"{regulator_code}-{target_slug}-{year}", confidence


def _rulemaking_key(finding: dict, rules: dict) -> Tuple[str, str] | None:
    """Build rulemaking key from agency + docket id."""
    title = finding.get("title") or ""
    summary = finding.get("summary") or ""

    docket_match = re.search(
        r"\b(?:docket(?:\s+no\.?|\s+number)?|CFR(?:\s+part)?|rin)\s*[:#]?\s*([A-Z0-9][A-Z0-9\-./]{2,30})",
        title + " " + summary,
        re.IGNORECASE,
    )
    if not docket_match:
        return None

    docket_id = docket_match.group(1).upper().rstrip(".,")

    agency_raw = None
    for candidate in [title, summary, finding.get("source") or ""]:
        for canonical, variants in rules.get("agency_aliases", {}).items():
            for v in [canonical] + variants:
                if re.search(rf"\b{re.escape(v)}\b", candidate, re.IGNORECASE):
                    agency_raw = canonical
                    break
            if agency_raw:
                break
        if agency_raw:
            break

    if not agency_raw:
        return None

    confidence = "high"
    return f"{agency_raw}-{docket_id}", confidence


def _guidance_key(finding: dict, rules: dict) -> Tuple[str, str] | None:
    """Build guidance key from org + short slug + year."""
    title = finding.get("title") or ""
    source = finding.get("source") or ""

    org_code = None
    for candidate in [source, title]:
        for canonical, variants in rules.get("agency_aliases", {}).items():
            for v in [canonical] + variants:
                if re.search(rf"\b{re.escape(v)}\b", candidate, re.IGNORECASE):
                    org_code = canonical
                    break
            if org_code:
                break
        if org_code:
            break

    if not org_code:
        return None

    year = _extract_year(finding)
    if not year:
        return None

    title_cleaned = re.sub(rf"\b{re.escape(org_code)}\b", "", title, flags=re.IGNORECASE)
    for variant in rules.get("agency_aliases", {}).get(org_code, []):
        title_cleaned = re.sub(rf"\b{re.escape(variant)}\b", "", title_cleaned, flags=re.IGNORECASE)
    title_cleaned = re.sub(r"^\s*(Releases|Publishes|Issues|Announces|Unveils)\s+", "", title_cleaned, flags=re.IGNORECASE)

    slug = _slug(title_cleaned, max_len=30).upper()
    slug = re.sub(r"-+", "-", slug).strip("-")
    if not slug:
        return None

    return f"{org_code}-{slug}-{year}", "medium"


def _fallback_key(finding: dict) -> Tuple[str, str]:
    """Deterministic hash fallback. Always succeeds."""
    jurisdiction = (finding.get("jurisdiction") or "unknown").lower()
    jur_slug = _slug(jurisdiction, max_len=20) or "unknown"
    year = _extract_year(finding) or "0000"
    title = (finding.get("title") or "") + (finding.get("source_url") or "")
    digest = _hash8(title.strip().lower())
    return f"{jur_slug}-{digest}-{year}", "low"


def _infer_topic_type(finding: dict) -> str:
    """Infer topic_type from development_type + content."""
    dev_type = (finding.get("development_type") or "").lower()
    jurisdiction = (finding.get("jurisdiction") or "").lower()

    if dev_type == "legislation":
        if jurisdiction in {"federal", "us federal", "united states"}:
            return "federal_bill"
        if jurisdiction in US_STATE_ABBREV or (len(jurisdiction) == 2 and jurisdiction.isupper()):
            return "state_bill"
        return "other"
    if dev_type == "enforcement":
        return "enforcement"
    if dev_type == "regulation":
        return "rulemaking"
    if dev_type == "court-decision":
        return "enforcement"
    return "guidance"


def topic_key(finding: dict, rules: dict | None = None) -> Tuple[str, str, str]:
    """Generate a (topic_key, confidence, topic_type) tuple for a finding.

    Confidence: high, medium, low. Low triggers human review via backfill report.
    """
    if rules is None:
        rules = load_rules()

    topic_type = _infer_topic_type(finding)

    handlers = {
        "state_bill": _state_bill_key,
        "federal_bill": _state_bill_key,
        "enforcement": lambda f: _enforcement_key(f, rules),
        "rulemaking": lambda f: _rulemaking_key(f, rules),
        "guidance": lambda f: _guidance_key(f, rules),
    }

    handler = handlers.get(topic_type)
    if handler:
        result = handler(finding)
        if result:
            key, confidence = result
            return key, confidence, topic_type

    key, confidence = _fallback_key(finding)
    return key, confidence, topic_type


def annotate_envelope(envelope: dict, rules: dict) -> dict:
    """Walk a scanner-output envelope and annotate each finding with topic_key
    fields. Modifies and returns the envelope in-place."""
    findings = envelope.get("data", {}).get("findings", [])
    if not isinstance(findings, list):
        return envelope

    scan_date = None
    ts = envelope.get("timestamp")
    if ts:
        m = re.match(r"(\d{4}-\d{2}-\d{2})", ts)
        if m:
            scan_date = m.group(1)

    for finding in findings:
        if finding.get("topic_key"):
            continue
        enriched = dict(finding)
        if scan_date and not enriched.get("date"):
            enriched["date"] = scan_date
        key, confidence, topic_type = topic_key(enriched, rules)
        finding["topic_key"] = key
        finding["topic_type"] = topic_type
        finding["topic_key_confidence"] = confidence
    return envelope


def cmd_one_off(args) -> int:
    try:
        finding = json.loads(args.finding_json)
    except json.JSONDecodeError as e:
        print(json.dumps({"error": f"invalid JSON: {e}"}), file=sys.stderr)
        return 2

    rules = load_rules(Path(args.rules))
    key, confidence, topic_type = topic_key(finding, rules)
    print(json.dumps({
        "topic_key": key,
        "topic_type": topic_type,
        "confidence": confidence,
    }))
    return 0


def cmd_annotate(args) -> int:
    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else input_path
    if not input_path.exists():
        print(f"ERROR: input not found: {input_path}", file=sys.stderr)
        return 2
    with open(input_path) as f:
        envelope = json.load(f)
    rules = load_rules(Path(args.rules))
    annotate_envelope(envelope, rules)

    import os
    import tempfile
    fd, tmp = tempfile.mkstemp(prefix=".topic-keys-", suffix=".json.tmp", dir=str(output_path.parent))
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(envelope, f, indent=2)
        os.replace(tmp, output_path)
    except Exception:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise

    findings = envelope.get("data", {}).get("findings", [])
    from collections import Counter
    conf = Counter(f.get("topic_key_confidence", "unknown") for f in findings)
    typ = Counter(f.get("topic_type", "unknown") for f in findings)
    print(json.dumps({
        "annotated": len(findings),
        "by_confidence": dict(conf),
        "by_topic_type": dict(typ),
    }, indent=2))
    return 0


def main() -> int:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd")

    # Legacy one-off positional mode: `topic_keys.py --finding-json ...`
    # kept for backward compatibility with scanner agent instructions.
    p.add_argument("--finding-json", help="JSON string for a single finding (legacy mode)")
    p.add_argument("--rules", default=str(DEFAULT_RULES_PATH))

    ann = sub.add_parser("annotate", help="Annotate a scanner-output.json with topic_keys in-place")
    ann.add_argument("--input", required=True, help="Path to scanner-output.json")
    ann.add_argument("--output", help="Output path (default: overwrite input)")
    ann.add_argument("--rules", default=str(DEFAULT_RULES_PATH))
    ann.set_defaults(func=cmd_annotate)

    args = p.parse_args()
    if args.cmd == "annotate":
        return args.func(args)
    if args.finding_json:
        return cmd_one_off(args)
    p.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
