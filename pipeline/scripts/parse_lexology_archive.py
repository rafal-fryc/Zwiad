#!/usr/bin/env python3
"""Deterministic parser for Lexology archive digest HTML.

Replaces the scanner agent for bulk Lexology backfill: parses the digest
straight to a scanner-output.json envelope without any LLM calls or
WebFetches. Lexology's email layout is stable enough that regex extraction
is reliable; anything ambiguous is skipped rather than hallucinated.

Usage:
    python3 pipeline/scripts/parse_lexology_archive.py \\
        --digest path/to/digest.html \\
        --meta   path/to/digest.meta.json \\
        --run-id 2026-04-15T12-00-00 \\
        --output pipeline/runs/<run-id>/scanner-output.json
"""

import argparse
import html as html_module
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# --- taxonomies --------------------------------------------------------------

# Topic section (h3) -> Zwiad category
SECTION_TO_CATEGORY = {
    "it & data protection": "privacy",
    "data protection": "privacy",
    "privacy": "privacy",
    "privacy & data protection": "privacy",
    "data protection & privacy": "privacy",
    "cybersecurity": "cybersecurity",
    "information security": "cybersecurity",
    "cyber security": "cybersecurity",
    "cyber": "cybersecurity",
    "artificial intelligence": "ai-law",
    "ai": "ai-law",
}

# Keyword fallback on title+snippet when section is generic ("Litigation",
# "Tech, Data, Telecoms & Media", etc.). Applied AFTER section match fails.
KEYWORD_CATEGORY = [
    (re.compile(r"\b(artificial intelligence|generative ai|llm|large language model|"
                r"machine learning|algorithmic|automated decision|gen[- ]?ai|ai[- ]?act|"
                r"deepfake|chatbot|ai model|ai system)\b", re.I), "ai-law"),
    (re.compile(r"\b(ransomware|data breach|cyberattack|cyber attack|cyber incident|"
                r"breach notification|infosec|ciso|vulnerability disclosure|zero[- ]day|"
                r"threat actor|security incident|malware)\b", re.I), "cybersecurity"),
    (re.compile(r"\b(privacy|data protection|gdpr|ccpa|personal data|personal "
                r"information|biometric|consumer data|sensitive data|"
                r"data broker|children.?s privacy|coppa)\b", re.I), "privacy"),
]

# Geographic region anchor -> default jurisdiction
REGION_DEFAULT_JURISDICTION = {
    "usa": "Federal",
    "us": "Federal",
    "unitedstates": "Federal",
    "united states": "Federal",
    "northamerica": "North America",
    "north america": "North America",
    "europe": "EU",
    "europeanunion": "EU",
    "asiapacific": "Asia Pacific",
    "asia pacific": "Asia Pacific",
    "asia": "Asia",
    "latinamerica": "Latin America",
    "latin america": "Latin America",
    "middleeast": "Middle East",
    "middle east": "Middle East",
    "africa": "Africa",
    "canada": "Canada",
    "unitedkingdom": "UK",
    "uk": "UK",
    "germany": "Germany",
    "france": "France",
    "ireland": "Ireland",
    "italy": "Italy",
    "spain": "Spain",
    "netherlands": "Netherlands",
    "switzerland": "Switzerland",
    "australia": "Australia",
    "newzealand": "New Zealand",
    "japan": "Japan",
    "china": "China",
    "southkorea": "South Korea",
    "india": "India",
    "singapore": "Singapore",
    "brazil": "Brazil",
    "mexico": "Mexico",
    "global": "Global",
    "international": "Global",
    "internationaldevelopments": "Global",
    "international developments": "Global",
}

US_STATES = [
    "Alabama","Alaska","Arizona","Arkansas","California","Colorado",
    "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho",
    "Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine",
    "Maryland","Massachusetts","Michigan","Minnesota","Mississippi",
    "Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey",
    "New Mexico","New York","North Carolina","North Dakota","Ohio",
    "Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina",
    "South Dakota","Tennessee","Texas","Utah","Vermont","Virginia",
    "Washington","West Virginia","Wisconsin","Wyoming","District of Columbia",
]
US_STATE_RE = re.compile(
    r"\b(" + "|".join(re.escape(s) for s in US_STATES) + r")\b"
)

# Development type detection from title
DEV_TYPE_RULES = [
    (re.compile(r"\b(enforcement|settlement|penalty|fine|sanction|agree(s|d)?\s+"
                r"to\s+pay|ag\s+settles|ftc\s+settles)\b", re.I), "enforcement"),
    (re.compile(r"\b(court|ruling|decision|appeal|opinion|holds?|affirms?|"
                r"reversed?|plaintiff|defendant|lawsuit)\b", re.I), "court-decision"),
    (re.compile(r"\b(final rule|proposed rule|rulemaking|notice of proposed|"
                r"regulation(s)?|regulatory)\b", re.I), "regulation"),
    (re.compile(r"\b(guidance|framework|advisory|faq|best practice|principles?)\b",
                re.I), "guidance"),
    (re.compile(r"\b(bill|act|legislation|hb\s?\d+|sb\s?\d+|signed|vetoed|"
                r"introduced|passed|statute)\b", re.I), "legislation"),
]

# --- regex ------------------------------------------------------------------

# Match a geography anchor like <a name="usa">USA</a> or <a name="europe">Europe</a>
REGION_ANCHOR_RE = re.compile(
    r'<a\b[^>]*?\sname=["\']([a-zA-Z]+)["\'][^>]*>',
    re.I,
)

# Topic section header <h3>IT &amp; Data Protection</h3>
TOPIC_RE = re.compile(r"<h3[^>]*>\s*(.*?)\s*</h3>", re.I | re.DOTALL)

# Article block: <h4>...<a href="URL" target="_blank">TITLE</a> ... </h4>
# followed (after some markup) by <div>FIRM</div><div>SNIPPET</div>
ARTICLE_RE = re.compile(
    r"<h4[^>]*>\s*"
    r"<a\b[^>]*?\shref=[\"\']([^\"\']+)[\"\'][^>]*>"
    r"(.*?)</a>"
    r".*?</h4>"
    r".*?<div[^>]*>(.*?)</div>"          # firm line
    r"\s*<div[^>]*>(.*?)</div>",          # snippet
    re.I | re.DOTALL,
)

UTM_RE = re.compile(r"[?&](utm_[^=&]+|g)=[^&]*", re.I)


# --- helpers ----------------------------------------------------------------


def clean_text(s: str) -> str:
    """Strip HTML tags, unescape entities, collapse whitespace."""
    if not s:
        return ""
    s = re.sub(r"<[^>]+>", " ", s)
    s = html_module.unescape(s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def normalize_url(u: str) -> str:
    u = html_module.unescape(u.strip())
    u = re.sub(r"\s+", "", u)
    # Strip UTM + Lexology ?g= tracking
    u = UTM_RE.sub("", u)
    u = re.sub(r"[?&]$", "", u)
    if u.startswith("http://"):
        u = "https://" + u[7:]
    u = u.rstrip("/")
    return u


def classify_category(section: str, title: str, snippet: str) -> str | None:
    """Keyword-first classification: AI & cyber beat privacy when both signals
    appear. Section mapping is a fallback only.
    """
    blob = f"{title} {snippet}"
    for pattern, cat in KEYWORD_CATEGORY:
        if pattern.search(blob):
            return cat
    sec = section.lower().strip()
    if sec in SECTION_TO_CATEGORY:
        return SECTION_TO_CATEGORY[sec]
    return None


def classify_development_type(title: str, snippet: str) -> str:
    blob = f"{title} {snippet}"
    for pattern, dt in DEV_TYPE_RULES:
        if pattern.search(blob):
            return dt
    return "other"


def infer_jurisdiction(region_default: str, title: str, snippet: str) -> str:
    """If region is US, look for state mentions; else use region default."""
    blob = f"{title} {snippet}"
    if region_default == "Federal":
        m = US_STATE_RE.search(blob)
        if m:
            return m.group(1)
        return "Federal"
    if region_default in ("North America", "Global"):
        m = US_STATE_RE.search(blob)
        if m:
            return m.group(1)
    return region_default


def find_region_for_offset(regions: list[tuple[int, str]], offset: int) -> str:
    """Given a list of (offset, region_name) pairs sorted by offset, return the
    region whose anchor precedes `offset`. Default to 'Global' if nothing."""
    current = "Global"
    for pos, name in regions:
        if pos <= offset:
            current = name
        else:
            break
    return current


def find_section_for_offset(sections: list[tuple[int, str]], offset: int) -> str:
    current = ""
    for pos, name in sections:
        if pos <= offset:
            current = name
        else:
            break
    return current


# --- main parsing -----------------------------------------------------------


def parse_digest(html: str) -> list[dict]:
    """Return list of raw findings dicts from digest HTML."""
    regions: list[tuple[int, str]] = []
    for m in REGION_ANCHOR_RE.finditer(html):
        anchor = m.group(1).lower()
        if anchor in REGION_DEFAULT_JURISDICTION:
            regions.append((m.start(), REGION_DEFAULT_JURISDICTION[anchor]))

    sections: list[tuple[int, str]] = []
    for m in TOPIC_RE.finditer(html):
        sections.append((m.start(), clean_text(m.group(1))))

    findings: list[dict] = []
    for m in ARTICLE_RE.finditer(html):
        raw_url, raw_title, raw_firm, raw_snippet = m.groups()
        title = clean_text(raw_title)
        if not title or len(title) < 5:
            continue
        url = normalize_url(raw_url)
        if not url.startswith("https://"):
            continue

        firm = clean_text(raw_firm) if raw_firm else ""
        snippet = clean_text(raw_snippet)
        if len(snippet.split()) < 8:
            continue

        offset = m.start()
        section = find_section_for_offset(sections, offset)
        region = find_region_for_offset(regions, offset)

        category = classify_category(section, title, snippet)
        if category is None:
            continue

        jurisdiction = infer_jurisdiction(region, title, snippet)
        dev_type = classify_development_type(title, snippet)

        findings.append({
            "title": title,
            "source_url": url,
            "source": f"Lexology / {firm}" if firm else "Lexology",
            "summary": snippet,
            "jurisdiction": jurisdiction,
            "category": category,
            "development_type": dev_type,
            "relevance": "medium",
            "_section": section,
            "_region": region,
        })

    # De-duplicate by URL within the same digest
    seen = set()
    unique: list[dict] = []
    for f in findings:
        if f["source_url"] in seen:
            continue
        seen.add(f["source_url"])
        unique.append(f)
    return unique


def build_envelope(run_id: str, digest_date: str, findings: list[dict]) -> dict:
    """Wrap findings in the Zwiad scanner envelope format."""
    date_compact = digest_date.replace("-", "")
    out_findings = []
    for i, f in enumerate(findings, 1):
        entry = {
            "id": f"SCAN-{date_compact}-{i:03d}",
            "title": f["title"],
            "source": f["source"],
            "source_url": f["source_url"],
            "summary": f["summary"],
            "date": digest_date,
            "relevance": f["relevance"],
            "jurisdiction": f["jurisdiction"],
            "development_type": f["development_type"],
            "category": f["category"],
        }
        out_findings.append(entry)

    return {
        "schema_version": "1.0",
        "pipeline_run_id": run_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "stage": "scanner",
        "status": "complete",
        "data": {
            "findings": out_findings,
            "source_failures": [],
        },
    }


# --- CLI --------------------------------------------------------------------


def _digest_date_from_meta_or_filename(meta: dict, digest_path: Path) -> str:
    m = re.match(r"(\d{4}-\d{2}-\d{2})", digest_path.name)
    if m:
        return m.group(1)
    date_str = meta.get("date", "")
    # RFC 2822: "Tue, 07 May 2024 13:22:31 +0000"
    dm = re.search(r"(\d{1,2})\s+(\w+)\s+(\d{4})", date_str)
    if dm:
        try:
            parsed = datetime.strptime(dm.group(0), "%d %b %Y")
            return parsed.strftime("%Y-%m-%d")
        except ValueError:
            pass
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--digest", required=True, type=Path)
    ap.add_argument("--meta", required=True, type=Path)
    ap.add_argument("--run-id", required=True)
    ap.add_argument("--output", required=True, type=Path)
    args = ap.parse_args()

    html = args.digest.read_text(encoding="utf-8", errors="replace")
    meta = json.loads(args.meta.read_text()) if args.meta.exists() else {}
    digest_date = _digest_date_from_meta_or_filename(meta, args.digest)

    findings = parse_digest(html)
    envelope = build_envelope(args.run_id, digest_date, findings)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(envelope, indent=2))

    cats: dict[str, int] = {}
    for f in envelope["data"]["findings"]:
        cats[f["category"]] = cats.get(f["category"], 0) + 1
    print(f"[parse-lexology] run={args.run_id} date={digest_date} "
          f"findings={len(findings)} categories={cats}",
          file=sys.stderr)


if __name__ == "__main__":
    main()
