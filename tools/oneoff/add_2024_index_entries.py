#!/usr/bin/env python3
"""One-time script: add 8 August 2024 report entries to reports/index.json.
Run from the project root: python3 tools/add_2024_index_entries.py
"""
import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
INDEX_PATH = PROJECT_ROOT / "reports" / "index.json"

ENTRIES = [
    {
        "topic_key": "texas-3eae2b28-2024",
        "topic_type": "enforcement_action",
        "topic_key_confidence": "medium",
        "report_path": "reports/privacy/enforcement-actions/texas-ag-gm-onstar-driver-data-2024-08-15.md",
        "title": "Texas AG Sues General Motors and OnStar for Unlawful Collection and Sale of Driver Data to Insurers",
        "jurisdiction": "Texas",
        "category": "privacy",
        "subcategory": "enforcement-actions",
        "source_urls": [
            "https://statutes.capitol.texas.gov/Docs/BC/htm/BC.541.htm",
            "https://www.cbsnews.com/news/gm-selling-driver-data-car-insurers-texas-lawsuit/",
            "https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-finalizes-order-settling-allegations-gm-onstar-collected-sold-geolocation-data-without-consumers",
            "https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-sues-general-motors-unlawfully-collecting-drivers-private-data-and",
        ],
        "first_reported": "2024-08-15",
        "last_updated": "2026-04-21",
        "finding_ids": ["SCAN-20240815-001"],
    },
    {
        "topic_key": "massachusetts-9c39c17d-2024",
        "topic_type": "state_bill",
        "topic_key_confidence": "medium",
        "report_path": "reports/privacy/litigation/massachusetts-cpicta-email-checkout-lawsuits-2024-08-15.md",
        "title": "Inbox Overload: Massachusetts Lawsuits Target Online Retailers' Email Collection at Checkout",
        "jurisdiction": "Massachusetts",
        "category": "privacy",
        "subcategory": "litigation",
        "source_urls": [
            "https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXV/Chapter93/Section105",
            "https://www.jdsupra.com/legalnews/inbox-overload-massachusetts-lawsuits-2392145/",
        ],
        "first_reported": "2024-08-15",
        "last_updated": "2024-08-15",
        "finding_ids": ["SCAN-20240815-003"],
    },
    {
        "topic_key": "california-b3fd1bb9-2024",
        "topic_type": "state_bill",
        "topic_key_confidence": "low",
        "report_path": "reports/ai-law/california/california-sb1047-frontier-ai-safety-veto-2024.md",
        "title": "California SB 1047: Safe and Secure Innovation for Frontier Artificial Intelligence Models Act — Full Legislative Arc, Veto, and Follow-On Regulation",
        "jurisdiction": "California",
        "category": "ai-law",
        "subcategory": "california",
        "source_urls": [
            "https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202320240SB1047",
            "https://www.gov.ca.gov/wp-content/uploads/2024/09/SB-1047-Veto-Message.pdf",
        ],
        "first_reported": "2024-08-15",
        "last_updated": "2026-04-21",
        "finding_ids": ["SCAN-20240815-011"],
    },
    {
        "topic_key": "washington-a61532fd-2024",
        "topic_type": "state_bill",
        "topic_key_confidence": "medium",
        "report_path": "reports/privacy/health-data/washington-mhmda-fully-effective-2024-08-15.md",
        "title": "Washington My Health My Data Act Now Fully Effective: Requirements, Scope, and Litigation Outlook",
        "jurisdiction": "Washington",
        "category": "privacy",
        "subcategory": "health-data",
        "source_urls": [
            "https://app.leg.wa.gov/RCW/default.aspx?cite=19.373&full=true",
            "https://www.atg.wa.gov/protecting-washingtonians-personal-health-data-and-privacy",
        ],
        "first_reported": "2024-08-15",
        "last_updated": "2024-08-15",
        "finding_ids": ["SCAN-20240815-013"],
    },
    {
        "topic_key": "IL-HB-3773-2024",
        "topic_type": "state_bill",
        "topic_key_confidence": "medium",
        "report_path": "reports/ai-law/employment-ai/illinois-hb3773-ai-employment-ihra-2024-08-15.md",
        "title": "Illinois HB 3773: AI in Employment Discrimination Prohibited Under Amended Human Rights Act",
        "jurisdiction": "Illinois",
        "category": "ai-law",
        "subcategory": "employment-ai",
        "source_urls": [
            "https://www.ilga.gov/legislation/publicacts/fulltext.asp?Name=103-0804",
            "https://www.ilga.gov/legislation/ilcs/ilcs5.asp?ActID=2266",
        ],
        "first_reported": "2024-08-15",
        "last_updated": "2026-04-21",
        "finding_ids": [
            "SCAN-20240815-018",
            "SCAN-20240815-020",
            "SCAN-20240815-025",
            "SCAN-20240815-026",
        ],
    },
    {
        "topic_key": "illinois-9643bbf8-2024",
        "topic_type": "litigation",
        "topic_key_confidence": "medium",
        "report_path": "reports/privacy/litigation/illinois-bipa-prisma-labs-lensa-magic-avatar-2024-08-06.md",
        "title": "Brantley v. Prisma Labs: Court Dismisses BIPA Class Action Against Lensa AI Magic Avatar App for Lack of Standing",
        "jurisdiction": "Illinois",
        "category": "privacy",
        "subcategory": "litigation",
        "source_urls": [
            "https://www.ilga.gov/Legislation/ILCS/Articles?ActID=3004&ChapterID=57&Print=True",
            "https://www.gtlaw.com/en/insights/2024/8/bipa-update-illinois-limits-liability-and-clarifies-electronic-consent-for-biometric-data-collection",
        ],
        "first_reported": "2024-08-15",
        "last_updated": "2024-08-15",
        "finding_ids": ["SCAN-20240815-019"],
    },
    {
        "topic_key": "rhode-island-70d197db-2024",
        "topic_type": "state_bill",
        "topic_key_confidence": "medium",
        "report_path": "reports/privacy/state-comprehensive-laws/rhode-island-ridtppa-h7787-2024-08-15.md",
        "title": "Rhode Island Data Transparency and Privacy Protection Act (RIDTPPA): Comprehensive Analysis",
        "jurisdiction": "Rhode Island",
        "category": "privacy",
        "subcategory": "state-comprehensive-laws",
        "source_urls": [
            "https://webserver.rilegislature.gov/BillText/BillText24/HouseText24/H7787.pdf",
            "https://webserver.rilegislature.gov/Statutes/TITLE6/6-48.1/INDEX.htm",
        ],
        "first_reported": "2024-08-15",
        "last_updated": "2024-08-15",
        "finding_ids": ["SCAN-20240815-023"],
    },
    {
        "topic_key": "new-york-ef29840c-2024",
        "topic_type": "guidance",
        "topic_key_confidence": "medium",
        "report_path": "reports/privacy/enforcement-actions/new-york-ag-website-privacy-tracking-guide-2024-07-30.md",
        "title": "New York AG Publishes Business Guide to Website Privacy Controls, Identifies Key Mistakes in Online Tracking (July 2024)",
        "jurisdiction": "New York",
        "category": "privacy",
        "subcategory": "enforcement-actions",
        "source_urls": [
            "https://ag.ny.gov/press-release/2024/attorney-general-james-launches-website-privacy-guides-new-york-consumers-and",
            "https://ag.ny.gov/resources/organizations/business-guidance/website-privacy-controls",
        ],
        "first_reported": "2024-08-15",
        "last_updated": "2024-08-15",
        "finding_ids": ["SCAN-20240815-024"],
    },
]


def main():
    with open(INDEX_PATH) as f:
        index = json.load(f)

    added = 0
    skipped = 0
    for entry in ENTRIES:
        key = entry["topic_key"]
        if key in index["reports"]:
            print(f"SKIP (already exists): {key}")
            skipped += 1
            continue

        record = {
            "topic_key": key,
            "topic_type": entry["topic_type"],
            "topic_key_confidence": entry["topic_key_confidence"],
            "report_path": entry["report_path"],
            "title": entry["title"],
            "jurisdiction": entry.get("jurisdiction"),
            "category": entry["category"],
            "subcategory": entry.get("subcategory"),
            "source_urls": entry.get("source_urls", []),
            "first_reported": entry.get("first_reported"),
            "last_updated": entry.get("last_updated"),
            "current_status": None,
            "status_history": [],
            "finding_ids": entry.get("finding_ids", []),
            "update_count": 0,
        }
        index["reports"][key] = record
        for url in record["source_urls"]:
            if url and url not in index.get("url_index", {}):
                index.setdefault("url_index", {})[url] = key
        print(f"ADDED: {key}")
        added += 1

    index["last_updated"] = datetime.now(timezone.utc).isoformat()

    fd, tmp = tempfile.mkstemp(prefix=".index-", suffix=".json.tmp",
                               dir=str(INDEX_PATH.parent))
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(index, f, indent=2)
        os.replace(tmp, INDEX_PATH)
    except Exception:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise

    print(f"\nDone. Added {added}, skipped {skipped}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
