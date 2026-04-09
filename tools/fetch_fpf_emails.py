#!/usr/bin/env python3
"""Fetch FPF email .eml files from GitHub repo and extract HTML bodies.

Usage: python3 tools/fetch_fpf_emails.py [--output-dir DIR]
"""

import email
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.parse import quote


def fetch_repo_files(repo: str = "rafal-fryc/FileTransfer") -> list[dict]:
    """List files in the GitHub repo via the API."""
    url = f"https://api.github.com/repos/{repo}/contents"
    req = Request(url, headers={"Accept": "application/vnd.github.v3+json"})
    with urlopen(req) as resp:
        return json.loads(resp.read())


def download_file(download_url: str) -> bytes:
    """Download a file from a URL."""
    req = Request(download_url)
    with urlopen(req) as resp:
        return resp.read()


def extract_html_from_eml(eml_bytes: bytes) -> bytes | None:
    """Extract HTML body from .eml content."""
    msg = email.message_from_bytes(eml_bytes)
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/html":
                return part.get_payload(decode=True)
    elif msg.get_content_type() == "text/html":
        return msg.get_payload(decode=True)
    return None


def extract_metadata_from_eml(eml_bytes: bytes) -> dict:
    """Extract metadata from .eml content."""
    msg = email.message_from_bytes(eml_bytes)
    return {
        "subject": msg.get("Subject", ""),
        "from": msg.get("From", ""),
        "date": msg.get("Date", ""),
    }


def main():
    output_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("tests/fixtures/fpf-emails")
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Fetching file list from GitHub...")
    files = fetch_repo_files()
    eml_files = [f for f in files if f["name"].endswith(".eml")]
    print(f"Found {len(eml_files)} .eml files")

    for f in sorted(eml_files, key=lambda x: x["name"]):
        name = f["name"]
        safe_name = re.sub(r"[^\w\s.-]", "", name).replace(" ", "-")
        base = safe_name.rsplit(".", 1)[0]

        html_path = output_dir / f"{base}.html"
        meta_path = output_dir / f"{base}.meta.json"

        if html_path.exists():
            print(f"  [skip] {name} (already extracted)")
            continue

        print(f"  [download] {name}...")
        eml_bytes = download_file(f["download_url"])

        html_body = extract_html_from_eml(eml_bytes)
        if html_body:
            html_path.write_bytes(html_body)
            meta = extract_metadata_from_eml(eml_bytes)
            with open(meta_path, "w") as mf:
                json.dump(meta, mf, indent=2)
            print(f"    -> {html_path.name} + {meta_path.name}")
        else:
            print(f"    [warn] No HTML body found in {name}")

    print(f"\nDone. Files saved to {output_dir}/")


if __name__ == "__main__":
    main()
