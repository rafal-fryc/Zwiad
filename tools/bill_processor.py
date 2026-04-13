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
# Page scraping for PDF links
# ---------------------------------------------------------------------------


def scrape_page_for_pdf(page_url: str, hint: str = "") -> str | None:
    """Fetch a bill page and find a bill text PDF link using BeautifulSoup.

    Filters out non-bill-text PDFs (transcripts, journals, committee statements, etc.)
    and prefers the most recent version of the bill text.
    """
    # URLs/text patterns that indicate NOT a bill text PDF
    EXCLUDE_PATTERNS = (
        "transcript", "journal", "rules", "rulebook", "constitution",
        "committee statement", "committee_statement", "fiscal",
        "testimony", "witness", "agenda", "minutes", "calendar",
        "statement of intent", "/cs/", "/si/", "/am/", "/fa/",
    )
    # Text patterns that indicate a bill text PDF (higher priority)
    BILL_TEXT_MARKERS = (
        "enrolled", "engrossed", "chaptered", "substitute",
        "introduced", "current", "latest", "official",
        "bill text", "full text", "pdf format",
    )

    try:
        from bs4 import BeautifulSoup
        from urllib.parse import urljoin

        req = urllib.request.Request(page_url)
        req.add_header("User-Agent", "Mozilla/5.0 (compatible; Zwiad/1.0)")
        with urllib.request.urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", errors="replace")

        soup = BeautifulSoup(html, "html.parser")

        # Collect all PDF-related links
        pdf_links = []
        seen_urls = set()
        for a in soup.find_all("a", href=True):
            href = a["href"]
            full_url = urljoin(page_url, href)
            if full_url in seen_urls:
                continue

            text = a.get_text(strip=True).lower()
            href_lower = href.lower()

            is_pdf = href_lower.endswith(".pdf") or "pdf" in text or "/pdf" in href_lower
            if not is_pdf:
                continue

            seen_urls.add(full_url)

            # Check if this is likely NOT bill text
            combined = (text + " " + href_lower).lower()
            if any(excl in combined for excl in EXCLUDE_PATTERNS):
                continue

            # Score the link based on how likely it is to be bill text
            score = 0
            if href_lower.endswith(".pdf"):
                score += 10
            if any(marker in text for marker in BILL_TEXT_MARKERS):
                score += 20
            if any(marker in href_lower for marker in ("intro", "enrolled", "engrossed")):
                score += 15
            # Prefer links with the bill type/number in the URL
            if "/hb" in href_lower or "/sb" in href_lower or "/lb" in href_lower:
                score += 5

            pdf_links.append((full_url, text, score, len(pdf_links)))

        if not pdf_links:
            print(f"    [scrape] No bill text PDF links found on page")
            return None

        # Sort by score descending, then prefer later links (more recent versions)
        pdf_links.sort(key=lambda x: (x[2], x[3]), reverse=True)

        best_url, best_text, best_score, _ = pdf_links[0]
        if len(pdf_links) > 1:
            print(f"    [scrape] Found {len(pdf_links)} PDF candidates, best: '{best_text}' (score={best_score})")
        return best_url

    except Exception as e:
        print(f"    [scrape-error] {e}")
        return None


def scrape_page_for_pdf_js(page_url: str) -> str | None:
    """Fetch a JS-rendered bill page using playwright and find a PDF link.

    Falls back gracefully if playwright is not installed.
    """
    EXCLUDE_PATTERNS = (
        "transcript", "journal", "rules", "rulebook", "constitution",
        "committee statement", "fiscal", "testimony", "witness",
        "agenda", "minutes", "calendar", "statement of intent",
        "/cs/", "/si/", "/am/", "/fa/",
    )
    BILL_TEXT_MARKERS = (
        "enrolled", "engrossed", "chaptered", "substitute",
        "introduced", "current", "latest", "official",
        "bill text", "full text", "pdf format", "bill pdf",
    )

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return None

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(page_url, timeout=30000)
            page.wait_for_load_state("networkidle", timeout=15000)

            links = page.eval_on_selector_all("a[href]", """elements => elements.map(e => ({
                href: e.href,
                text: e.textContent.trim()
            }))""")
            browser.close()

        pdf_links = []
        seen = set()
        for link in links:
            href = link["href"]
            text = link["text"].lower()
            href_lower = href.lower()

            if href in seen:
                continue

            is_pdf = href_lower.endswith(".pdf") or "pdf" in text or "/pdf" in href_lower
            if not is_pdf:
                continue

            seen.add(href)
            combined = (text + " " + href_lower).lower()
            if any(excl in combined for excl in EXCLUDE_PATTERNS):
                continue

            score = 0
            if href_lower.endswith(".pdf"):
                score += 10
            if any(m in text for m in BILL_TEXT_MARKERS):
                score += 20
            if any(m in href_lower for m in ("intro", "enrolled", "engrossed")):
                score += 15
            pdf_links.append((href, text, score, len(pdf_links)))

        if not pdf_links:
            print(f"    [js-scrape] No bill text PDF links found")
            return None

        pdf_links.sort(key=lambda x: (x[2], x[3]), reverse=True)
        best_url, best_text, best_score, _ = pdf_links[0]
        print(f"    [js-scrape] Found {len(pdf_links)} PDF candidates, best: '{best_text}' (score={best_score})")
        return best_url

    except Exception as e:
        print(f"    [js-scrape-error] {e}")
        return None


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

    # Determine chamber from bill type
    is_senate = bill_type.upper() in ("S", "SB", "SF", "SB", "SJR")

    # Build template variables for state-specific URL patterns
    template_vars = {
        "session": session,
        "bill_type": bill_type,
        "bill_number": bill_number,
        "bill_type_lower": bill_type.lower(),
        # Utah/Maryland: zero-padded bill numbers (e.g., 286 -> 0286)
        "bill_number_padded": bill_number.zfill(4),
        # Federal: chamber slug for congress.gov
        "chamber_slug": "senate-bill" if is_senate else "house-bill",
        # Rhode Island: chamber folder and single-letter bill type
        "chamber_folder": "SenateText26" if is_senate else "HouseText26",
        "bill_type_ri": "S" if is_senate else "H",
        # New Mexico: chamber letter
        "chamber": "S" if is_senate else "H",
        # Wisconsin/Kansas: chamber lower
        "chamber_lower": "sen" if is_senate else "asm",
        # Vermont: single-letter bill type with dot
        "bill_type_vt": "S" if is_senate else "H",
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

    # Tier 2b: Scrape bill page for PDF link (page_with_pdf_link states)
    state_cfg = states_config.get("states", {}).get(state_abbrev, {})
    if state_cfg.get("strategy") == "page_with_pdf_link":
        page_url = result.get("resolved_url") or fpf_url
        if page_url:
            print(f"  [tier2b] Scraping page for PDF link: {page_url[:80]}...")
            pdf_url = scrape_page_for_pdf(page_url, state_cfg.get("pdf_selector_hint", ""))
            if pdf_url:
                print(f"    Found PDF: {pdf_url[:100]}")
                if download_pdf(pdf_url, pdf_path):
                    result["download_status"] = "success"
                    result["pdf_path"] = str(pdf_path.relative_to(PROJECT_ROOT))
                    result["resolved_url"] = pdf_url
                    result["method"] = "page-scrape"
                    return result

    # Tier 2c: JS-rendered page scraping via playwright
    page_url = result.get("resolved_url") or fpf_url
    if page_url and not page_url.startswith("https://FPF.informz.net"):
        print(f"  [tier2c] JS scraping via playwright: {page_url[:80]}...")
        pdf_url = scrape_page_for_pdf_js(page_url)
        if pdf_url:
            print(f"    Found PDF: {pdf_url[:100]}")
            if download_pdf(pdf_url, pdf_path):
                result["download_status"] = "success"
                result["pdf_path"] = str(pdf_path.relative_to(PROJECT_ROOT))
                result["resolved_url"] = pdf_url
                result["method"] = "js-scrape"
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


def _load_cross_index_helpers():
    """Lazy-import update_reports_index helpers. Returns (add_entry_fn, load_fn, save_fn) or None."""
    try:
        if __package__ in (None, ""):
            import sys as _sys
            _sys.path.insert(0, str(PROJECT_ROOT))
            from tools.update_reports_index import add_entry, load_index, save_index
        else:
            from .update_reports_index import add_entry, load_index, save_index  # type: ignore
        return add_entry, load_index, save_index
    except Exception:
        return None


def _cross_index_bill_to_reports(index: dict, entry: dict, key: str, bill: dict, run_id: str) -> None:
    """Write a thin bill reference into reports/index.json so the dedup stage
    can detect when a Lexology/IAPP story covers an already-tracked FPF bill.

    The key matches the bill_key format used by topic_keys.py _state_bill_key,
    so when the scanner later produces a finding for this bill, dedup catches
    it via Pass 1a (topic_key match) with no further configuration.

    If a non-FPF entry already exists at the same key (e.g., a Lexology report
    was written first about the same bill), the existing report_path and
    subcategory are preserved — we only merge source_urls and refresh
    last_updated + current_status.
    """
    categories = bill.get("category") or ["privacy"]
    primary_category = categories[0] if categories else "privacy"
    # Schema requires one of privacy/cybersecurity/ai-law
    if primary_category not in ("privacy", "cybersecurity", "ai-law"):
        primary_category = "privacy"

    state_abbrev = bill.get("state_abbrev", "")
    topic_type = "federal_bill" if state_abbrev == "US" else "state_bill"

    from datetime import datetime as _dt, timezone as _tz
    today = _dt.now(_tz.utc).strftime("%Y-%m-%d")

    # URLs: always merge the bill_text_url. The add_entry helper dedupes.
    urls = []
    if bill.get("bill_text_url"):
        urls.append(bill["bill_text_url"])

    existing = index.get("reports", {}).get(key)
    if existing and existing.get("subcategory") != "fpf-tracked-bill":
        # A real report (Lexology/IAPP) already exists at this key. Don't
        # clobber its report_path or subcategory — just merge URLs, refresh
        # status, and append the FPF finding_id for traceability.
        existing.setdefault("source_urls", [])
        for u in urls:
            try:
                if __package__ in (None, ""):
                    from tools.url_norm import normalize_url
                else:
                    from .url_norm import normalize_url  # type: ignore
                n = normalize_url(u)
            except Exception:
                n = u
            if n and n not in existing["source_urls"]:
                existing["source_urls"].append(n)
                index.setdefault("url_index", {})[n] = key
        existing["last_updated"] = today
        new_status = bill.get("status")
        if new_status and new_status != existing.get("current_status"):
            existing["current_status"] = new_status
        existing.setdefault("finding_ids", [])
        fpf_id = f"FPF-{run_id}"
        if fpf_id not in existing["finding_ids"]:
            existing["finding_ids"].append(fpf_id)
        return

    # New FPF-originated entry OR existing FPF entry (safe to refresh)
    bill_dir_rel = entry.get("bill_dir", "")
    report_path = f"{bill_dir_rel}/current.md" if bill_dir_rel else "bills/tracker.json"

    add_entry, _, _ = _load_cross_index_helpers() or (None, None, None)
    if add_entry is None:
        return
    add_entry(index, {
        "topic_key": key,
        "topic_type": topic_type,
        "topic_key_confidence": "high",
        "report_path": report_path,
        "title": bill.get("title", f"{bill.get('bill_identifier', key)}"),
        "jurisdiction": bill.get("state", ""),
        "category": primary_category,
        "subcategory": "fpf-tracked-bill",
        "source_urls": urls,
        "first_reported": bill.get("last_action_date") or today,
        "last_updated": today,
        "current_status": bill.get("status", "introduced"),
        "finding_id": f"FPF-{run_id}",
    })


def process_bills(fpf_output_path: str, run_id: str, skip_convert: bool = False) -> dict:
    """Process all bills from FPF scanner output."""
    # Attach per-run audit log so bill-download progress lands alongside
    # the run's other artifacts (pipeline/runs/<run_id>/audit.log).
    try:
        if __package__ in (None, ""):
            import sys as _sys
            _sys.path.insert(0, str(PROJECT_ROOT))
            from tools.logging_setup import get_logger, attach_run_file_handler
        else:
            from .logging_setup import get_logger, attach_run_file_handler
        _log = get_logger("zwiad.bill_processor")
        attach_run_file_handler(_log, run_id)
        _log.info("bill_processor starting run_id=%s", run_id)
    except Exception:
        pass  # Logging is best-effort; never block bill processing

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

    # Cross-index bills into reports/index.json so the general dedup layer
    # (Lexology/IAPP path) can detect when a Lexology story covers an
    # already-tracked FPF bill. See I1 in docs/REVIEW-2026-04-10.md.
    _helpers = _load_cross_index_helpers()
    if _helpers is not None:
        add_entry, load_index, save_index = _helpers
        try:
            reports_index = load_index()
            cross_indexed = 0
            for bill in bills:
                state_abbrev = bill["state_abbrev"]
                bill_id = bill["bill_identifier"]
                session = bill.get("session", "2026")
                key = bill_key(state_abbrev, bill_id, session)
                entry = tracker["bills"].get(key, {})
                _cross_index_bill_to_reports(reports_index, entry, key, bill, run_id)
                cross_indexed += 1
            save_index(reports_index)
            print(f"Cross-indexed {cross_indexed} bills into reports/index.json")
        except Exception as e:
            print(f"Warning: cross-index write failed: {e}")

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
