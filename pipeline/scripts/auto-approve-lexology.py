#!/usr/bin/env python3
"""Auto-approve scanner findings for US privacy/cyber/AI-law only.

Replaces the human Discord approval gate for bulk Lexology backfill.

Usage: python3 pipeline/scripts/auto-approve-lexology.py <run-id>

Reads:  pipeline/runs/<run-id>/scanner-deduped.json
Writes: pipeline/runs/<run-id>/scanner-approved.json
        pipeline/runs/<run-id>/scanner-auto-rejected.json
"""

import json
import re
import sys
from pathlib import Path

ALLOWED_TOPICS = {"privacy", "cybersecurity", "ai-law"}

US_STATES = {
    "alabama", "alaska", "arizona", "arkansas", "california", "colorado",
    "connecticut", "delaware", "florida", "georgia", "hawaii", "idaho",
    "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana", "maine",
    "maryland", "massachusetts", "michigan", "minnesota", "mississippi",
    "missouri", "montana", "nebraska", "nevada", "new hampshire", "new jersey",
    "new mexico", "new york", "north carolina", "north dakota", "ohio",
    "oklahoma", "oregon", "pennsylvania", "rhode island", "south carolina",
    "south dakota", "tennessee", "texas", "utah", "vermont", "virginia",
    "washington", "west virginia", "wisconsin", "wyoming",
    "district of columbia", "dc", "d.c.", "puerto rico",
}
US_FEDERAL = {"federal", "us", "u.s.", "usa", "united states", "us federal"}
STATE_ABBREV = {
    "al","ak","az","ar","ca","co","ct","de","fl","ga","hi","id","il","in","ia",
    "ks","ky","la","me","md","ma","mi","mn","ms","mo","mt","ne","nv","nh","nj",
    "nm","ny","nc","nd","oh","ok","or","pa","ri","sc","sd","tn","tx","ut","vt",
    "va","wa","wv","wi","wy",
}

CRYPTO_PATTERN = re.compile(
    r"\b(crypto|cryptocurrency|cryptocurrencies|bitcoin|stablecoin|stablecoins|"
    r"web3|digital\s+asset|digital\s+assets)\b",
    re.IGNORECASE,
)


def is_us_jurisdiction(jurisdiction: str) -> bool:
    if not jurisdiction:
        return False
    j = jurisdiction.strip().lower()
    if j in US_FEDERAL or j in US_STATES:
        return True
    # Short abbreviations like "CA", "NY"
    if len(j) == 2 and j in STATE_ABBREV:
        return True
    # Composite strings like "US - California" or "California (US)"
    for needle in US_FEDERAL | US_STATES:
        if re.search(rf"\b{re.escape(needle)}\b", j):
            return True
    return False


def is_crypto(finding: dict) -> bool:
    blob = " ".join(
        str(finding.get(k, "")) for k in ("title", "summary", "description", "headline")
    )
    return bool(CRYPTO_PATTERN.search(blob))


def classify(finding: dict) -> tuple[bool, str]:
    topic = (finding.get("topic") or finding.get("category") or "").strip().lower()
    if topic not in ALLOWED_TOPICS:
        return False, "off_topic"
    if is_crypto(finding):
        return False, "crypto"
    jurisdiction = finding.get("jurisdiction") or finding.get("jurisdictions") or ""
    if isinstance(jurisdiction, list):
        jurisdiction = ", ".join(str(j) for j in jurisdiction)
    if not is_us_jurisdiction(jurisdiction):
        return False, "non_us"
    return True, ""


def _extract_findings(payload) -> list:
    if isinstance(payload, dict):
        data = payload.get("data", payload)
        if isinstance(data, dict):
            return data.get("findings", []) or []
    if isinstance(payload, list):
        return payload
    return []


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: auto-approve-lexology.py <run-id>", file=sys.stderr)
        sys.exit(2)

    run_id = sys.argv[1]
    project_root = Path(__file__).resolve().parents[2]
    run_dir = project_root / "pipeline" / "runs" / run_id

    deduped_path = run_dir / "scanner-deduped.json"
    if not deduped_path.exists():
        # Fall back to raw scanner output if dedup step was skipped
        deduped_path = run_dir / "scanner-output.json"
        if not deduped_path.exists():
            print(f"ERROR: no scanner-deduped.json or scanner-output.json in {run_dir}",
                  file=sys.stderr)
            sys.exit(1)

    payload = json.loads(deduped_path.read_text())
    findings = _extract_findings(payload)

    approved: list = []
    rejected: list = []
    for f in findings:
        ok, reason = classify(f)
        if ok:
            approved.append(f)
        else:
            fr = dict(f)
            fr["rejected_reason"] = reason
            rejected.append(fr)

    approved_out = {"data": {"findings": approved}}
    rejected_out = {"data": {"findings": rejected}}

    (run_dir / "scanner-approved.json").write_text(
        json.dumps(approved_out, indent=2)
    )
    (run_dir / "scanner-auto-rejected.json").write_text(
        json.dumps(rejected_out, indent=2)
    )

    reasons: dict[str, int] = {}
    for r in rejected:
        reasons[r["rejected_reason"]] = reasons.get(r["rejected_reason"], 0) + 1

    print(f"[auto-approve] run={run_id} total={len(findings)} "
          f"approved={len(approved)} rejected={len(rejected)} reasons={reasons}")


if __name__ == "__main__":
    main()
