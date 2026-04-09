#!/usr/bin/env python3
"""Process bills from FPF scanner output: download PDFs, convert to markdown, update tracker.

Usage:
    python3 tools/bill_processor.py --fpf-output <path> --run-id <id>
    python3 tools/bill_processor.py --download-bill --state OR --bill "SB 1546" --url <url>
"""

import argparse
import json
import os
import subprocess
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
BILLS_DIR = PROJECT_ROOT / "bills"
TRACKER_PATH = BILLS_DIR / "tracker.json"
STATES_CONFIG_PATH = PROJECT_ROOT / "pipeline" / "config" / "states.json"


# ---------------------------------------------------------------------------
# Tracker operations
# ---------------------------------------------------------------------------


def load_tracker() -> dict:
    """Load the bill tracker JSON."""
    if TRACKER_PATH.exists():
        with open(TRACKER_PATH) as f:
            return json.load(f)
    return {"schema_version": "1.0", "last_updated": None, "bills": {}}


def save_tracker(tracker: dict) -> None:
    """Save the bill tracker JSON."""
    tracker["last_updated"] = datetime.now(timezone.utc).isoformat()
    with open(TRACKER_PATH, "w") as f:
        json.dump(tracker, f, indent=2)


def load_states_config() -> dict:
    """Load state legislature URL config."""
    if STATES_CONFIG_PATH.exists():
        with open(STATES_CONFIG_PATH) as f:
            return json.load(f)
    return {"schema_version": "1.0", "states": {}}


def bill_key(state_abbrev: str, bill_identifier: str, session: str) -> str:
    """Generate a tracker key like OR-SB-1546-2026."""
    parts = bill_identifier.strip().split()
    if len(parts) >= 2:
        bill_type = parts[0].replace(".", "")
        bill_number = parts[1].replace(".", "")
    else:
        bill_type = bill_identifier.replace(" ", "-").replace(".", "")
        bill_number = ""
    return f"{state_abbrev}-{bill_type}-{bill_number}-{session}"


def bill_dir_name(state: str, bill_identifier: str) -> Path:
    """Get the bill directory path like bills/florida/SB-482."""
    state_dir = state.lower().replace(" ", "-")
    parts = bill_identifier.strip().split()
    if len(parts) >= 2:
        bill_folder = f"{parts[0].replace('.', '')}-{parts[1].replace('.', '')}"
    else:
        bill_folder = bill_identifier.replace(" ", "-").replace(".", "")
    return BILLS_DIR / state_dir / bill_folder


# ---------------------------------------------------------------------------
# URL resolution
# ---------------------------------------------------------------------------


def resolve_redirect(url: str, max_redirects: int = 10) -> str:
    """Follow HTTP redirects to get the final URL."""
    for _ in range(max_redirects):
        try:
            req = urllib.request.Request(url, method="HEAD")
            req.add_header("User-Agent", "Mozilla/5.0 (compatible; Zwiad/1.0)")
            resp = urllib.request.urlopen(req, timeout=15)
            return resp.url
        except urllib.error.HTTPError as e:
            if e.code in (301, 302, 303, 307, 308) and e.headers.get("Location"):
                url = e.headers["Location"]
            else:
                return url
        except Exception:
            return url
    return url


# ---------------------------------------------------------------------------
# Bill download
# ---------------------------------------------------------------------------


def download_pdf(url: str, dest_path: Path) -> bool:
    """Download a PDF from a URL. Returns True on success."""
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "Mozilla/5.0 (compatible; Zwiad/1.0)")
        with urllib.request.urlopen(req, timeout=30) as resp:
            content_type = resp.headers.get("Content-Type", "")
            data = resp.read()

            # Check if it's actually a PDF
            if data[:5] == b"%PDF-" or "pdf" in content_type.lower():
                dest_path.write_bytes(data)
                return True
            else:
                # Save as HTML if it's a web page
                html_path = dest_path.with_suffix(".html")
                html_path.write_bytes(data)
                print(f"    [info] Got HTML instead of PDF, saved to {html_path.name}")
                return False
    except Exception as e:
        print(f"    [error] Download failed: {e}")
        return False


def try_state_config(state_abbrev: str, bill_identifier: str, session: str,
                     states_config: dict) -> str | None:
    """Try to construct a bill PDF URL from state config patterns.

    Only returns a URL for 'direct_pdf' strategy states. For 'page_with_pdf_link'
    states, returns None (those need agent-based scraping).
    """
    state_cfg = states_config.get("states", {}).get(state_abbrev)
    if not state_cfg:
        return None

    strategy = state_cfg.get("strategy", "")
    if strategy != "direct_pdf":
        return None

    parts = bill_identifier.strip().split()
    if len(parts) < 2:
        return None

    bill_type = parts[0].replace(".", "")
    bill_number = parts[1].replace(".", "")

    pattern = state_cfg.get("pdf_pattern")
    if not pattern:
        return None

    # Build template variables for state-specific URL patterns
    template_vars = {
        "session": session,
        "bill_type": bill_type,
        "bill_number": bill_number,
        "bill_type_lower": bill_type.lower(),
        # Utah needs zero-padded bill numbers (e.g., 286 -> 0286)
        "bill_number_padded": bill_number.zfill(4),
        # Federal: chamber slug for congress.gov
        "chamber_slug": "senate-bill" if bill_type.upper() in ("S", "SB") else "house-bill",
    }

    try:
        url = pattern.format(**template_vars)
        return url
    except (KeyError, IndexError):
        return None


def download_bill(state_abbrev: str, state_name: str, bill_identifier: str,
                  session: str, fpf_url: str | None, states_config: dict,
                  bill_directory: Path) -> dict:
    """Three-tier bill download. Returns result dict."""
    versions_dir = bill_directory / "versions"
    versions_dir.mkdir(parents=True, exist_ok=True)

    # Determine version label
    existing_versions = list(versions_dir.glob("v*-*.pdf")) + list(versions_dir.glob("v*-*.html"))
    version_num = len(existing_versions) // 2 + 1  # rough count
    if version_num == 1:
        version_label = "introduced"
    else:
        version_label = f"version-{version_num}"

    pdf_name = f"v{version_num}-{version_label}.pdf"
    pdf_path = versions_dir / pdf_name

    result = {
        "download_status": "failed",
        "version_id": f"v{version_num}-{version_label}",
        "pdf_path": None,
        "md_path": None,
        "resolved_url": None,
        "method": None,
    }

    # Tier 1: Follow FPF redirect link
    if fpf_url:
        print(f"  [tier1] Resolving FPF link: {fpf_url[:80]}...")
        resolved = resolve_redirect(fpf_url)
        result["resolved_url"] = resolved
        print(f"    -> {resolved[:100]}")

        if resolved != fpf_url:
            if download_pdf(resolved, pdf_path):
                result["download_status"] = "success"
                result["pdf_path"] = str(pdf_path.relative_to(PROJECT_ROOT))
                result["method"] = "fpf-redirect"
                return result

    # Tier 2: State config pattern
    config_url = try_state_config(state_abbrev, bill_identifier, session, states_config)
    if config_url:
        print(f"  [tier2] Trying state config URL: {config_url[:100]}...")
        if download_pdf(config_url, pdf_path):
            result["download_status"] = "success"
            result["pdf_path"] = str(pdf_path.relative_to(PROJECT_ROOT))
            result["resolved_url"] = config_url
            result["method"] = "state-config"
            return result

    # Tier 3: Log for manual/agent resolution
    print(f"  [tier3] Automated download failed. Logging for manual resolution.")
    result["download_status"] = "pending-manual"
    result["method"] = "needs-manual"

    return result


# ---------------------------------------------------------------------------
# Docling conversion
# ---------------------------------------------------------------------------


def convert_pdf_to_markdown(pdf_path: Path) -> Path | None:
    """Convert a PDF to markdown using docling. Returns md path or None."""
    md_path = pdf_path.with_suffix(".md")
    # Force CPU mode — Tegra GPU (Orin CC 8.7) causes CUDA memory errors with docling
    old_cuda = os.environ.get("CUDA_VISIBLE_DEVICES")
    os.environ["CUDA_VISIBLE_DEVICES"] = ""
    try:
        from docling.document_converter import DocumentConverter
        converter = DocumentConverter()
        doc_result = converter.convert(str(pdf_path))
        markdown = doc_result.document.export_to_markdown()
        md_path.write_text(markdown)
        print(f"    [docling] Converted to {md_path.name}")
        return md_path
    except Exception as e:
        print(f"    [docling-error] {e}")
        return None
    finally:
        if old_cuda is not None:
            os.environ["CUDA_VISIBLE_DEVICES"] = old_cuda
        elif "CUDA_VISIBLE_DEVICES" in os.environ:
            del os.environ["CUDA_VISIBLE_DEVICES"]


def update_current_symlink(bill_directory: Path, md_path: Path) -> None:
    """Update the current.md symlink to point to the latest version."""
    current = bill_directory / "current.md"
    if current.exists() or current.is_symlink():
        current.unlink()
    try:
        current.symlink_to(md_path.relative_to(bill_directory))
    except Exception:
        # Fallback: just copy the file
        import shutil
        shutil.copy2(md_path, current)


# ---------------------------------------------------------------------------
# Main processing
# ---------------------------------------------------------------------------


def process_bills(fpf_output_path: str, run_id: str, skip_convert: bool = False) -> dict:
    """Process all bills from FPF scanner output."""
    with open(fpf_output_path) as f:
        fpf_output = json.load(f)

    bills = fpf_output.get("data", {}).get("bills", [])
    tracker = load_tracker()
    states_config = load_states_config()

    results = {
        "run_id": run_id,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "bills_processed": [],
        "new_bills": 0,
        "status_updates": 0,
        "downloads_success": 0,
        "downloads_failed": 0,
        "conversions_success": 0,
    }

    for i, bill in enumerate(bills):
        state_abbrev = bill["state_abbrev"]
        bill_id = bill["bill_identifier"]
        state = bill["state"]
        session = bill.get("session", "2026")

        key = bill_key(state_abbrev, bill_id, session)
        bill_dir = bill_dir_name(state, bill_id)

        print(f"\n[{i+1}/{len(bills)}] {state_abbrev} {bill_id} (key: {key})")

        is_new = key not in tracker["bills"]

        if is_new:
            results["new_bills"] += 1
            # Create new tracker entry
            tracker["bills"][key] = {
                "bill_identifier": bill_id,
                "state": state,
                "state_abbrev": state_abbrev,
                "session": session,
                "title": bill.get("title", ""),
                "category": bill.get("category", []),
                "topics": bill.get("topics", []),
                "sponsors": bill.get("sponsors", []),
                "current_status": bill.get("status", "introduced"),
                "bill_dir": str(bill_dir.relative_to(PROJECT_ROOT)),
                "current_version": None,
                "download_status": "pending",
                "bill_text_url": bill.get("bill_text_url"),
                "status_history": [],
                "versions": [],
                "first_seen_run": run_id,
                "last_updated_run": run_id,
            }
        else:
            results["status_updates"] += 1
            existing = tracker["bills"][key]
            # Update status if changed
            if bill.get("status") and bill["status"] != existing["current_status"]:
                existing["current_status"] = bill["status"]
            existing["last_updated_run"] = run_id
            # Update fields that may have been enriched
            if bill.get("title") and not existing.get("title"):
                existing["title"] = bill["title"]
            if bill.get("sponsors") and not existing.get("sponsors"):
                existing["sponsors"] = bill["sponsors"]

        # Add status history entry
        tracker["bills"][key]["status_history"].append({
            "date": bill.get("last_action_date") or datetime.now(timezone.utc).strftime("%Y-%m-%d"),
            "status": bill.get("status", "introduced"),
            "detail": bill.get("status_detail", ""),
            "source_email_date": fpf_output.get("data", {}).get("email_dates", [""])[0] if fpf_output.get("data", {}).get("email_dates") else "",
            "source_run_id": run_id,
        })

        # Download bill text (only for new bills or if we don't have it yet)
        entry = tracker["bills"][key]
        if entry["download_status"] in ("pending", "failed"):
            dl_result = download_bill(
                state_abbrev, state, bill_id, session,
                bill.get("bill_text_url"),
                states_config, bill_dir,
            )

            entry["download_status"] = dl_result["download_status"]
            if dl_result.get("resolved_url"):
                entry["bill_text_url"] = dl_result["resolved_url"]

            if dl_result["download_status"] == "success":
                results["downloads_success"] += 1
                entry["current_version"] = dl_result["version_id"]
                version_entry = {
                    "version_id": dl_result["version_id"],
                    "date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                    "pdf_path": dl_result["pdf_path"],
                    "md_path": None,
                }

                # Convert PDF to markdown (skip if --skip-convert)
                if not skip_convert:
                    pdf_path = PROJECT_ROOT / dl_result["pdf_path"]
                    md_path = convert_pdf_to_markdown(pdf_path)
                    if md_path:
                        results["conversions_success"] += 1
                        version_entry["md_path"] = str(md_path.relative_to(PROJECT_ROOT))
                        update_current_symlink(bill_dir, md_path)

                entry["versions"].append(version_entry)

                # Write per-bill metadata.json
                bill_dir.mkdir(parents=True, exist_ok=True)
                with open(bill_dir / "metadata.json", "w") as f:
                    json.dump(entry, f, indent=2)
            else:
                results["downloads_failed"] += 1
        else:
            print(f"  [skip] Already downloaded (status: {entry['download_status']})")

        bill_result = {
            "bill_key": key,
            "bill_identifier": bill_id,
            "state": state,
            "is_new": is_new,
            "status": bill.get("status", "introduced"),
            "download_status": entry["download_status"],
        }
        results["bills_processed"].append(bill_result)

    # Save tracker
    save_tracker(tracker)

    # Write processing results
    results_path = PROJECT_ROOT / "pipeline" / "runs" / run_id / "fpf-bills-processed.json"
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n--- Summary ---")
    print(f"Bills processed: {len(results['bills_processed'])}")
    print(f"New bills: {results['new_bills']}")
    print(f"Status updates: {results['status_updates']}")
    print(f"Downloads success: {results['downloads_success']}")
    print(f"Downloads failed: {results['downloads_failed']}")
    print(f"Conversions success: {results['conversions_success']}")

    return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="Zwiad bill processor")
    subparsers = parser.add_subparsers(dest="command")

    # Process FPF output
    proc = subparsers.add_parser("process", help="Process bills from FPF scanner output")
    proc.add_argument("--fpf-output", required=True, help="Path to fpf-scanner-output.json")
    proc.add_argument("--run-id", required=True, help="Pipeline run ID")
    proc.add_argument("--skip-convert", action="store_true",
                      help="Skip docling PDF-to-markdown conversion (do downloads only)")

    # Convert PDFs for all bills in tracker that have PDFs but no markdown
    conv = subparsers.add_parser("convert", help="Run docling conversion on downloaded PDFs")
    conv.add_argument("--limit", type=int, default=0, help="Max bills to convert (0=all)")

    # Download single bill
    dl = subparsers.add_parser("download", help="Download a single bill")
    dl.add_argument("--state", required=True, help="State abbreviation (e.g., OR)")
    dl.add_argument("--state-name", default="", help="Full state name")
    dl.add_argument("--bill", required=True, help="Bill identifier (e.g., 'SB 1546')")
    dl.add_argument("--session", default="2026", help="Legislative session")
    dl.add_argument("--url", default="", help="URL to bill text")

    args = parser.parse_args()

    if args.command == "process":
        process_bills(args.fpf_output, args.run_id, skip_convert=args.skip_convert)
    elif args.command == "convert":
        tracker = load_tracker()
        converted = 0
        for key, entry in tracker["bills"].items():
            if args.limit and converted >= args.limit:
                break
            for ver in entry.get("versions", []):
                if ver.get("pdf_path") and not ver.get("md_path"):
                    pdf_path = PROJECT_ROOT / ver["pdf_path"]
                    if pdf_path.exists():
                        print(f"Converting {key}: {pdf_path.name}...")
                        md_path = convert_pdf_to_markdown(pdf_path)
                        if md_path:
                            ver["md_path"] = str(md_path.relative_to(PROJECT_ROOT))
                            bill_dir = pdf_path.parent.parent
                            update_current_symlink(bill_dir, md_path)
                            converted += 1
        save_tracker(tracker)
        print(f"\nConverted {converted} PDFs to markdown.")
    elif args.command == "download":
        states_config = load_states_config()
        bill_dir = bill_dir_name(args.state_name or args.state, args.bill)
        result = download_bill(
            args.state, args.state_name or args.state,
            args.bill, args.session, args.url or None,
            states_config, bill_dir,
        )
        print(json.dumps(result, indent=2))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
