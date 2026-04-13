#!/usr/bin/env python3
"""Zwiad Discord bot — interact with the regulatory monitoring pipeline via Discord."""

import asyncio
import email as email_lib
import hashlib
import imaplib
import json
import logging
import os
import re
import socket
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import discord
from discord import app_commands
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------

load_dotenv()

TOKEN = os.environ["DISCORD_TOKEN"]
GUILD_ID = int(os.environ["DISCORD_GUILD_ID"])
CHANNEL_ID = int(os.environ["DISCORD_CHANNEL_ID"])
IMAP_EMAIL = os.environ.get("IMAP_EMAIL", "")
IMAP_PASSWORD = os.environ.get("IMAP_PASSWORD", "")

PROJECT_ROOT = Path(__file__).resolve().parent
RUNS_DIR = PROJECT_ROOT / "pipeline" / "runs"

# Use the shared Zwiad logging setup (tools/logging_setup.py). Writes to stderr
# by default; per-run audit logs can be attached via attach_run_file_handler.
sys.path.insert(0, str(PROJECT_ROOT))
from tools.logging_setup import get_logger, attach_run_file_handler, detach_handler  # noqa: E402
logger = get_logger("zwiad.bot")

MY_GUILD = discord.Object(id=GUILD_ID)

# In-memory approval state: {run_id: {finding_id: bool}}
approval_state: dict[str, dict[str, bool]] = {}

# Track the latest run_id for convenience
latest_run_id: str | None = None

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


class IMAPFetchError(Exception):
    """Raised when fetching new emails from IMAP fails for any reason."""


# Persistent state: track which emails we've already processed by Message-ID so
# we don't re-scan emails that were manually re-marked unread or surfaced after
# a partial failure. See docs/REVIEW-2026-04-10.md and Phase 2 plan.
STATE_DIR = PROJECT_ROOT / "pipeline" / "state"
PROCESSED_EMAILS_PATH = STATE_DIR / "processed-emails.json"


def _load_processed_emails() -> dict:
    """Load the processed-emails state file. Returns empty structure on first run
    or if the file is corrupt (with a warning log)."""
    if not PROCESSED_EMAILS_PATH.exists():
        return {"schema_version": "1.0", "processed": {}}
    try:
        data = json.loads(PROCESSED_EMAILS_PATH.read_text())
        if "processed" not in data:
            data["processed"] = {}
        return data
    except json.JSONDecodeError as e:
        logger.warning("Corrupt %s; starting empty: %s", PROCESSED_EMAILS_PATH, e)
        return {"schema_version": "1.0", "processed": {}}


def _save_processed_emails(data: dict) -> None:
    """Atomic write of the processed-emails state file."""
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(STATE_DIR), prefix=".pe-", suffix=".json.tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        os.replace(tmp, PROCESSED_EMAILS_PATH)
    except Exception:
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except OSError:
                pass
        raise


def _extract_message_id(msg: email_lib.message.Message) -> str:
    """Return a stable per-email ID. Prefer the RFC Message-ID header;
    fall back to a hash of (From, Date, Subject) if missing or malformed."""
    mid = (msg.get("Message-ID") or "").strip()
    if mid:
        return mid
    raw = f"{msg.get('From','')}|{msg.get('Date','')}|{msg.get('Subject','')}"
    return "synth-" + hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def fetch_new_emails(run_id: str) -> list[Path]:
    """Fetch unread emails via IMAP, save as HTML, mark as read. Returns saved file paths.

    Raises IMAPFetchError on network/auth/protocol failures so the caller can
    surface a user-facing message instead of crashing the slash command.

    Emails whose Message-ID is already in pipeline/state/processed-emails.json
    are skipped (and marked \\Seen so they don't keep coming back). This makes
    the bot robust against manual re-marking in Gmail and partial-failure
    recovery.
    """
    if not IMAP_EMAIL or not IMAP_PASSWORD:
        return []

    input_dir = RUNS_DIR / run_id / "emails"
    input_dir.mkdir(parents=True, exist_ok=True)

    processed_data = _load_processed_emails()
    processed_dirty = False

    saved: list[Path] = []
    mail = None
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", timeout=30)
        mail.login(IMAP_EMAIL, IMAP_PASSWORD)
        mail.select("INBOX")
        status, messages = mail.search(None, "UNSEEN")
        if status != "OK" or not messages[0]:
            return []

        msg_ids = messages[0].split()
        for i, msg_id in enumerate(msg_ids):
            try:
                status, data = mail.fetch(msg_id, "(RFC822)")
                if status != "OK" or not data or not data[0]:
                    logger.warning("IMAP fetch returned non-OK for msg_id=%s", msg_id)
                    continue

                msg = email_lib.message_from_bytes(data[0][1])

                # Phase 2: skip emails we've already processed, even if Gmail
                # shows them UNSEEN (manual re-mark, partial-failure recovery).
                mid = _extract_message_id(msg)
                if mid in processed_data["processed"]:
                    logger.info("Skipping already-processed email: %s", mid)
                    mail.store(msg_id, "+FLAGS", "\\Seen")
                    continue

                html_body = None
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/html":
                            html_body = part.get_payload(decode=True)
                            break
                elif msg.get_content_type() == "text/html":
                    html_body = msg.get_payload(decode=True)

                if not html_body:
                    for part in msg.walk() if msg.is_multipart() else [msg]:
                        if part.get_content_type() == "text/plain":
                            text = part.get_payload(decode=True).decode("utf-8", errors="replace")
                            html_body = f"<html><body><pre>{text}</pre></body></html>".encode()
                            break

                if html_body:
                    subject = msg.get("Subject", f"email-{i}")
                    safe_name = re.sub(r"[^\w\s-]", "", subject)[:50].strip().replace(" ", "-")
                    filepath = input_dir / f"{safe_name}-{i}.html"
                    filepath.write_bytes(html_body)
                    saved.append(filepath)

                    meta = {
                        "subject": subject,
                        "from": msg.get("From", ""),
                        "date": msg.get("Date", ""),
                    }
                    meta_path = input_dir / f"{safe_name}-{i}.meta.json"
                    with open(meta_path, "w") as mf:
                        json.dump(meta, mf, indent=2)

                    # Record as processed only after successful save
                    processed_data["processed"][mid] = {
                        "first_seen_run": run_id,
                        "subject": subject,
                        "from": msg.get("From", ""),
                        "processed_at": datetime.now(timezone.utc).isoformat(),
                    }
                    processed_dirty = True

                mail.store(msg_id, "+FLAGS", "\\Seen")
            except (imaplib.IMAP4.error, OSError) as e:
                logger.warning("Failed to process IMAP msg_id=%s: %s", msg_id, e)
                continue
    except imaplib.IMAP4.error as e:
        raise IMAPFetchError(f"IMAP protocol error: {e}") from e
    except (OSError, socket.error, socket.timeout) as e:
        raise IMAPFetchError(f"IMAP network error: {e}") from e
    except Exception as e:
        raise IMAPFetchError(f"Unexpected IMAP failure: {e}") from e
    finally:
        if mail is not None:
            try:
                mail.logout()
            except Exception:
                pass
        # Save processed-emails state even if the loop raised partway. Next
        # /scan will skip emails we successfully stored this run.
        if processed_dirty:
            try:
                _save_processed_emails(processed_data)
            except Exception as e:
                logger.warning("Could not save %s: %s", PROCESSED_EMAILS_PATH, e)

    return saved


def run_subprocess_checked(cmd: list[str], cwd: Path | None = None, capture: bool = True) -> tuple[bool, str]:
    """Run a subprocess and check its return code.

    Returns (ok, stderr_tail). On success, stderr_tail is empty. On failure,
    contains the last ~500 chars of stderr (or stdout if stderr is empty) for
    user-facing error messages.
    """
    try:
        result = subprocess.run(
            cmd,
            capture_output=capture,
            text=True,
            cwd=str(cwd) if cwd else None,
        )
    except (FileNotFoundError, OSError) as e:
        return False, f"Failed to launch {cmd[0]}: {e}"

    if result.returncode != 0:
        tail = (result.stderr or result.stdout or "").strip()
        if len(tail) > 500:
            tail = "..." + tail[-500:]
        return False, f"exit code {result.returncode}: {tail or '(no output)'}"
    return True, ""


def run_claude_and_log_cost(
    cmd: list[str],
    run_id: str,
    stage: str,
    cwd: Path | None = None,
) -> tuple[bool, str, float]:
    """Run a `claude -p --output-format json ...` invocation, parse the
    structured result for `total_cost_usd`, and append the entry to
    pipeline/runs/<run_id>/cost.json.

    Returns (ok, error_tail, cost_usd). cost_usd is 0.0 if parsing fails.
    """
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(cwd) if cwd else None,
        )
    except (FileNotFoundError, OSError) as e:
        return False, f"Failed to launch {cmd[0]}: {e}", 0.0

    cost_usd = 0.0
    parsed = None
    if result.stdout:
        try:
            parsed = json.loads(result.stdout)
            cost_usd = float(parsed.get("total_cost_usd") or 0.0)
        except (json.JSONDecodeError, ValueError, TypeError) as e:
            logger.debug("Could not parse claude JSON output for cost (%s)", e)

    # Append cost entry regardless of success/failure so partial costs are logged
    _append_cost_entry(run_id, stage, cost_usd, parsed)

    if result.returncode != 0:
        tail = (result.stderr or result.stdout or "").strip()
        if len(tail) > 500:
            tail = "..." + tail[-500:]
        return False, f"exit code {result.returncode}: {tail or '(no output)'}", cost_usd
    return True, "", cost_usd


def _append_cost_entry(run_id: str, stage: str, cost_usd: float, parsed: dict | None) -> None:
    """Append a cost entry to pipeline/runs/<run_id>/cost.json. Best effort —
    never raises."""
    try:
        run_dir = RUNS_DIR / run_id
        if not run_dir.exists():
            return
        cost_path = run_dir / "cost.json"
        if cost_path.exists():
            try:
                data = json.loads(cost_path.read_text())
            except json.JSONDecodeError:
                data = {"run_id": run_id, "total_usd": 0.0, "stages": []}
        else:
            data = {"run_id": run_id, "total_usd": 0.0, "stages": []}

        entry = {
            "stage": stage,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "cost_usd": round(cost_usd, 6),
        }
        if parsed:
            entry["duration_ms"] = parsed.get("duration_ms")
            entry["num_turns"] = parsed.get("num_turns")
            usage = parsed.get("usage") or {}
            entry["input_tokens"] = usage.get("input_tokens")
            entry["output_tokens"] = usage.get("output_tokens")
            entry["cache_read_tokens"] = usage.get("cache_read_input_tokens")
            entry["cache_creation_tokens"] = usage.get("cache_creation_input_tokens")

        data.setdefault("stages", []).append(entry)
        data["total_usd"] = round(data.get("total_usd", 0.0) + cost_usd, 6)
        cost_path.write_text(json.dumps(data, indent=2))
    except Exception as e:
        logger.debug("Cost log write failed for %s: %s", run_id, e)


# Rough per-finding cost estimate for research phase (researcher + reviewer iteration + categorizer)
# Calibrated from run 2026-04-12T21-18-15: 13 findings = $21.13 => ~$1.63/finding
# Reviewer iteration loop (up to 3 rounds per report) doubles/triples the per-finding cost
# over a naive researcher-only estimate.
RESEARCH_COST_PER_FINDING_USD = 1.65


EMAIL_SOURCES_PATH = PROJECT_ROOT / "pipeline" / "config" / "email-sources.json"


def _load_email_source_rules() -> list[dict]:
    """Load the ordered list of email classification rules from config.

    Returns a list of rule dicts. If the config file is missing or malformed,
    falls back to the hardcoded v1 rules so the bot still functions.
    """
    try:
        with open(EMAIL_SOURCES_PATH) as f:
            config = json.load(f)
        return config.get("sources", [])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.warning("Failed to load %s, using hardcoded fallback: %s", EMAIL_SOURCES_PATH, e)
        return [
            {"bucket": "fpf", "sender_contains": ["fpf.org", "informz.net"],
             "subject_contains": ["fpf u.s.", "fpf youth privacy"],
             "match_mode": "sender_and_subject"},
            {"bucket": "iapp", "sender_contains": ["iapp.org"],
             "subject_contains": [], "match_mode": "sender_only"},
            {"bucket": "lexology", "sender_contains": ["lexology"],
             "subject_contains": [], "match_mode": "sender_only"},
        ]


def _match_rule(rule: dict, sender: str, subject: str) -> bool:
    """Return True if the given rule matches the message metadata."""
    sender_hits = any(s.lower() in sender for s in rule.get("sender_contains", []))
    subject_hits = any(s.lower() in subject for s in rule.get("subject_contains", []))
    mode = rule.get("match_mode", "sender_only")
    if mode == "sender_and_subject":
        return sender_hits and subject_hits
    if mode == "sender_or_subject":
        return sender_hits or subject_hits
    if mode == "subject_only":
        return subject_hits
    # Default: sender_only
    return sender_hits


def classify_emails(email_dir: Path) -> dict[str, list[Path]]:
    """Classify emails in a directory by type using metadata sidecars.

    Reads rules from pipeline/config/email-sources.json — first matching rule wins.
    Messages that don't match any rule land in the 'unknown' bucket.
    """
    rules = _load_email_source_rules()
    buckets = {rule["bucket"] for rule in rules} | {"unknown"}
    result: dict[str, list[Path]] = {bucket: [] for bucket in buckets}

    for html_file in sorted(email_dir.glob("*.html")):
        meta_path = html_file.with_suffix(".meta.json")
        if not meta_path.exists():
            result["unknown"].append(html_file)
            continue

        try:
            with open(meta_path) as f:
                meta = json.load(f)
        except json.JSONDecodeError as e:
            logger.warning("Failed to parse %s: %s", meta_path, e)
            result["unknown"].append(html_file)
            continue

        sender = (meta.get("from") or "").lower()
        subject = (meta.get("subject") or "").lower()

        matched = False
        for rule in rules:
            if _match_rule(rule, sender, subject):
                result[rule["bucket"]].append(html_file)
                matched = True
                break
        if not matched:
            result["unknown"].append(html_file)

    return result


def get_latest_run_id() -> str | None:
    """Return the most recent run_id by directory modification time."""
    if not RUNS_DIR.exists():
        return None
    runs = sorted(RUNS_DIR.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True)
    return runs[0].name if runs else None


def load_findings(run_id: str) -> list[dict]:
    """Load new-topic findings from scanner-deduped.json (or scanner-output.json)."""
    for name in ("scanner-deduped.json", "scanner-output.json"):
        path = RUNS_DIR / run_id / name
        if path.exists():
            with open(path) as f:
                data = json.load(f)
            return data.get("data", {}).get("findings", [])
    return []


def load_candidate_updates(run_id: str) -> list[dict]:
    """Load Phase 2 candidate_updates from scanner-deduped.json.

    Returns an empty list if dedup hasn't run yet (falls through to
    scanner-output.json which may not carry the field).
    """
    path = RUNS_DIR / run_id / "scanner-deduped.json"
    if not path.exists():
        return []
    with open(path) as f:
        data = json.load(f)
    return data.get("data", {}).get("candidate_updates", []) or []


def relevance_color(relevance: str) -> discord.Color:
    return {
        "high": discord.Color.green(),
        "medium": discord.Color.gold(),
        "low": discord.Color.greyple(),
    }.get(relevance, discord.Color.default())


def build_finding_embed(
    finding: dict, index: int, total: int, run_id: str
) -> discord.Embed:
    """Build a Discord embed for a single finding."""
    title = f"[{finding['id']}] {finding['title']}"
    if len(title) > 256:
        title = title[:253] + "..."

    summary = finding.get("summary", "")
    if len(summary) > 400:
        summary = summary[:397] + "..."

    embed = discord.Embed(
        title=title,
        description=summary,
        color=relevance_color(finding.get("relevance", "")),
        url=finding.get("source_url"),
    )
    embed.add_field(name="Category", value=finding.get("category", "—"), inline=True)
    embed.add_field(
        name="Jurisdiction", value=finding.get("jurisdiction", "—"), inline=True
    )
    embed.add_field(
        name="Type", value=finding.get("development_type", "—"), inline=True
    )
    embed.add_field(
        name="Source", value=finding.get("source", "—"), inline=False
    )
    embed.add_field(
        name="Relevance", value=finding.get("relevance", "—"), inline=True
    )
    embed.set_footer(text=f"Run {run_id} | Finding {index} of {total}")
    return embed


def topic_color(topic: str) -> discord.Color:
    return {
        "privacy": discord.Color.green(),
        "cybersecurity": discord.Color.blue(),
        "ai-law": discord.Color.orange(),
    }.get(topic, discord.Color.default())


def extract_report_summary(filepath: Path) -> dict | None:
    """Extract title, executive summary, and frontmatter from a report markdown file."""
    if not filepath.exists():
        return None

    text = filepath.read_text()

    # Parse YAML frontmatter
    meta = {}
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    key, val = line.split(":", 1)
                    meta[key.strip()] = val.strip().strip('"')
            text = parts[2]

    # Extract first H1 as title
    title_match = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = title_match.group(1) if title_match else filepath.stem

    # Extract executive summary section
    summary = ""
    summary_match = re.search(
        r"##\s+(?:Executive )?Summary.*?\n\n(.+?)(?=\n##|\Z)",
        text,
        re.DOTALL,
    )
    if summary_match:
        summary = summary_match.group(1).strip()
        summary = re.sub(r"<!--.*?-->", "", summary).strip()

    return {
        "title": title,
        "summary": summary,
        "meta": meta,
        "path": str(filepath.relative_to(PROJECT_ROOT)),
    }


def find_run_reports(run_id: str) -> list[dict]:
    """Load filed report paths from categorizer-output.json, falling back to researcher outputs.

    Lenient reader: the canonical schema key is `filed_reports` but some
    categorizer outputs have hallucinated `reports_filed` (reverse order) with
    `report_path` instead of `destination_path`. Normalize both shapes so the
    bot doesn't break when the agent drifts from the spec.
    """
    cat_path = RUNS_DIR / run_id / "categorizer-output.json"
    if cat_path.exists():
        with open(cat_path) as f:
            data = json.load(f)
        raw = (
            data.get("data", {}).get("filed_reports")
            or data.get("data", {}).get("reports_filed")
            or []
        )
        # Normalize each entry to the canonical shape
        normalized = []
        for e in raw:
            normalized.append({
                "finding_id": e.get("finding_id", ""),
                "destination_path": e.get("destination_path") or e.get("report_path", ""),
                "source_path": e.get("source_path", ""),
                "topic": e.get("topic") or e.get("category", ""),
                "subcategory": e.get("subcategory") or "",
                "is_pending": e.get("is_pending", False),
                "symlinks": e.get("symlinks", []),
                # Preserve any extra fields so downstream UIs can show them
                "action": e.get("action"),
                "notes": e.get("notes"),
            })
        return normalized

    # Fallback: read researcher-*.json files for report_path
    run_dir = RUNS_DIR / run_id
    if not run_dir.exists():
        return []
    reports = []
    for rfile in sorted(run_dir.glob("researcher-*.json")):
        with open(rfile) as f:
            rdata = json.load(f)
        rd = rdata.get("data", rdata)
        if rd.get("report_path"):
            reports.append({
                "finding_id": rd.get("finding_id", ""),
                "destination_path": rd["report_path"],
                "topic": "",
                "subcategory": "",
            })
    return reports


def write_approved_json(run_id: str, approved_ids: set[str]) -> Path:
    """Write scanner-approved.json from approved finding IDs.

    Approved IDs may span both new findings and Phase 2 candidate_updates.
    Auto-approved updates (from the reviewer policy matrix) are added to the
    approved set automatically by cmd_scan — they don't require explicit user
    action. Each entry preserves its original fields so the orchestrator's
    Mode 2 branch can tell updates apart from new findings via `is_update`
    and `operation`.
    """
    source_path = RUNS_DIR / run_id / "scanner-deduped.json"
    if not source_path.exists():
        source_path = RUNS_DIR / run_id / "scanner-output.json"

    with open(source_path) as f:
        source = json.load(f)

    source_findings = source.get("data", {}).get("findings", []) or []
    source_updates = source.get("data", {}).get("candidate_updates", []) or []

    approved_findings = [f for f in source_findings if f["id"] in approved_ids]

    # Ensure candidate_updates that the user approved AND auto-approved
    # updates (pre-marked with operation=append_update) get captured. We mark
    # updates with operation=append_update so downstream stages route them.
    approved_updates = []
    for u in source_updates:
        if u["id"] in approved_ids:
            entry = dict(u)
            entry["operation"] = "append_update"
            approved_updates.append(entry)

    envelope = {
        "schema_version": source.get("schema_version", "1.0"),
        "pipeline_run_id": source.get("pipeline_run_id", run_id),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "stage": "human-review",
        "status": "complete",
        "data": {
            "findings": approved_findings + approved_updates,
        },
    }

    output_path = RUNS_DIR / run_id / "scanner-approved.json"
    with open(output_path, "w") as f:
        json.dump(envelope, f, indent=2)

    return output_path


# ---------------------------------------------------------------------------
# Views (buttons)
# ---------------------------------------------------------------------------


class FindingView(discord.ui.View):
    """Approve/Reject buttons for a single finding."""

    def __init__(self, run_id: str, finding_id: str):
        super().__init__(timeout=None)
        self.run_id = run_id
        self.finding_id = finding_id

    @discord.ui.button(label="Approve", style=discord.ButtonStyle.green)
    async def approve(self, interaction: discord.Interaction, button: discord.ui.Button):
        approval_state.setdefault(self.run_id, {})[self.finding_id] = True
        button.label = "Approved"
        button.disabled = True
        self.children[1].disabled = True  # disable Reject too
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label="Reject", style=discord.ButtonStyle.red)
    async def reject(self, interaction: discord.Interaction, button: discord.ui.Button):
        approval_state.setdefault(self.run_id, {})[self.finding_id] = False
        button.label = "Rejected"
        button.disabled = True
        self.children[0].disabled = True  # disable Approve too
        await interaction.response.edit_message(view=self)


# ---------------------------------------------------------------------------
# Bot
# ---------------------------------------------------------------------------


class ZwiadBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


bot = ZwiadBot()


@bot.event
async def on_ready():
    print(f"Zwiad bot online as {bot.user}")
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("**Zwiad bot online.** Use `/scan` to start a pipeline run.")


# ---------------------------------------------------------------------------
# /scan
# ---------------------------------------------------------------------------


@bot.tree.command(name="scan", description="Start a pipeline scan")
async def cmd_scan(interaction: discord.Interaction):
    global latest_run_id

    await interaction.response.send_message(
        "Checking for new emails and starting scan..."
    )

    channel = bot.get_channel(CHANNEL_ID)
    run_id = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H-%M-%S")
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    # Attach per-run audit log — writes everything logged during this scan to
    # pipeline/runs/<run_id>/audit.log alongside the other stage artifacts
    audit_handler = attach_run_file_handler(logger, run_id)
    logger.info("scan starting run_id=%s", run_id)

    # Fetch new emails
    try:
        email_files = await asyncio.to_thread(fetch_new_emails, run_id)
    except IMAPFetchError as e:
        logger.exception("IMAP fetch failed for run %s", run_id)
        await channel.send(
            f"**IMAP fetch failed for `{run_id}`** — {e}\n"
            f"Continuing with web sources only."
        )
        email_files = []

    if email_files:
        await channel.send(
            f"**Found {len(email_files)} new email(s).** Classifying..."
        )
    else:
        await channel.send("No new emails. Scanning web sources only...")

    # Classify emails
    email_dir = run_dir / "emails"
    classified = (
        classify_emails(email_dir)
        if email_files
        else {"fpf": [], "lexology": [], "iapp": [], "unknown": []}
    )

    fpf_emails = classified.get("fpf", [])
    lexology_emails = classified.get("lexology", [])
    iapp_emails = classified.get("iapp", [])
    digest_emails = lexology_emails + iapp_emails

    if fpf_emails:
        await channel.send(f"**{len(fpf_emails)} FPF legislative email(s)** detected. Processing bills...")
    if lexology_emails:
        await channel.send(f"**{len(lexology_emails)} Lexology digest(s)** detected.")
    if iapp_emails:
        await channel.send(f"**{len(iapp_emails)} IAPP newsletter(s)** detected.")

    # Run FPF scan if FPF emails found
    if fpf_emails:
        def _run_fpf_scan():
            prompt = (
                f"FPF scan for run {run_id}. "
                f"Process FPF emails in pipeline/runs/{run_id}/emails/. "
                f"Write output to pipeline/runs/{run_id}/."
            )
            cmd = [
                "claude", "-p",
                "--agent", "orchestrator",
                "--output-format", "json",
                "--permission-mode", "acceptEdits",
                "--max-turns", "20",
                prompt,
            ]
            return run_claude_and_log_cost(cmd, run_id, "fpf-scan", cwd=PROJECT_ROOT)

        ok, err, cost = await asyncio.to_thread(_run_fpf_scan)
        if not ok:
            await channel.send(f"FPF scan FAILED for `{run_id}` — {err}")
        elif cost > 0:
            logger.info("fpf-scan cost run_id=%s usd=%.4f", run_id, cost)

        # Post FPF results
        fpf_results_path = run_dir / "fpf-bills-processed.json"
        if fpf_results_path.exists():
            with open(fpf_results_path) as f:
                fpf_results = json.load(f)
            new_bills = fpf_results.get("new_bills", 0)
            status_updates = fpf_results.get("status_updates", 0)
            dl_success = fpf_results.get("downloads_success", 0)
            dl_failed = fpf_results.get("downloads_failed", 0)

            embed = discord.Embed(
                title="FPF Legislative Scan Results",
                color=discord.Color.teal(),
            )
            embed.add_field(name="New Bills", value=str(new_bills), inline=True)
            embed.add_field(name="Status Updates", value=str(status_updates), inline=True)
            embed.add_field(name="PDFs Downloaded", value=f"{dl_success} success, {dl_failed} pending", inline=False)
            embed.set_footer(text=f"Run {run_id}")
            await channel.send(embed=embed)

    # Run Lexology/IAPP/web scan
    def _run_scan():
        if digest_emails:
            input_paths = "\n".join(f"  - {p}" for p in digest_emails)
            prompt = (
                f"Scan phase for run {run_id}. "
                f"Input digest files (each file has a .meta.json sidecar indicating source type — "
                f"Lexology if sender contains 'lexology', IAPP if sender contains 'iapp.org'):\n"
                f"{input_paths}\n"
                f"Parse each digest according to its source type (see scanner agent instructions) and "
                f"combine all findings into a single scanner-output.json. "
                f"Write all output to pipeline/runs/{run_id}/."
            )
        else:
            prompt = (
                f"Scan phase for run {run_id}. Web sources only (--sources-only). "
                f"No email digest. Write all output to pipeline/runs/{run_id}/."
            )

        cmd = [
            "claude", "-p",
            "--agent", "orchestrator",
            "--output-format", "json",
            "--permission-mode", "acceptEdits",
            "--max-turns", "60",
            prompt,
        ]

        ok, err, cost = run_claude_and_log_cost(cmd, run_id, "scan", cwd=PROJECT_ROOT)
        return run_id, ok, err, cost

    run_id, scan_ok, scan_err, scan_cost = await asyncio.to_thread(_run_scan)

    # Recovery path: if the orchestrator failed (e.g. hit max-turns doing
    # exploratory work) but the scanner still produced scanner-output.json,
    # finish the deterministic steps (annotate + dedup + generate-review)
    # ourselves so the run isn't stuck with un-deduped findings.
    if not scan_ok:
        scanner_output = run_dir / "scanner-output.json"
        scanner_deduped = run_dir / "scanner-deduped.json"
        if scanner_output.exists() and not scanner_deduped.exists():
            logger.warning("scan orchestrator failed but scanner-output.json exists; running recovery")
            await channel.send(
                f"Orchestrator failed (`{scan_err[:100]}`). "
                f"Scanner output exists — running recovery (annotate + dedup + review)..."
            )
            recovery_ok = True
            for cmd_list, label in [
                (["python3", "tools/topic_keys.py", "annotate", "--input", str(scanner_output)], "annotate"),
                (["bash", "pipeline/scripts/dedup-findings.sh", run_id], "dedup"),
                (["bash", "pipeline/scripts/generate-review.sh", run_id], "generate-review"),
            ]:
                rec_ok, rec_err = await asyncio.to_thread(
                    run_subprocess_checked, cmd_list, PROJECT_ROOT
                )
                if not rec_ok:
                    await channel.send(f"Recovery step `{label}` failed: {rec_err[:200]}")
                    recovery_ok = False
                    break
            if recovery_ok:
                (run_dir / "scan-complete.marker").write_text("SCAN_PHASE_COMPLETE\n")
                await channel.send(f"Recovery complete. Scan can proceed.")
                scan_ok = True  # Treat as recovered — continue to post findings
        if not scan_ok:
            await channel.send(f"Scan FAILED for `{run_id}` — {scan_err}")
    elif scan_cost > 0:
        logger.info("scan cost run_id=%s usd=%.4f", run_id, scan_cost)
        await channel.send(f"Scan cost: **${scan_cost:.4f}**")
    latest_run_id = run_id

    findings = load_findings(run_id)
    candidate_updates = load_candidate_updates(run_id)
    channel = bot.get_channel(CHANNEL_ID)

    # Phase 2: classify each update via the reviewer policy so the UI can
    # show "N auto-apply, M need review". Auto-approved updates are added to
    # the approval set automatically so /research processes them without a
    # button click.
    auto_approved_updates, escalated_updates = _classify_updates(candidate_updates)

    if not findings and not candidate_updates:
        await channel.send(f"Scan `{run_id}` complete but no findings or updates were produced. Check `pipeline/runs/{run_id}/` for errors.")
        logger.warning("scan produced no findings run_id=%s", run_id)
        detach_handler(audit_handler)
        return

    logger.info(
        "scan complete run_id=%s findings=%d updates=%d auto=%d escalated=%d",
        run_id, len(findings), len(candidate_updates),
        len(auto_approved_updates), len(escalated_updates),
    )
    summary = (
        f"**Scan complete: `{run_id}`** — "
        f"**{len(findings)} new findings**, "
        f"**{len(candidate_updates)} updates** "
        f"({len(auto_approved_updates)} auto-apply, {len(escalated_updates)} need review)."
    )
    await channel.send(summary)

    # Initialize approval state with auto-approved update IDs pre-checked
    approval_state[run_id] = {u["id"]: True for u in auto_approved_updates}

    for i, finding in enumerate(findings, 1):
        embed = build_finding_embed(finding, i, len(findings), run_id)
        view = FindingView(run_id, finding["id"])
        await channel.send(embed=embed, view=view)
        await asyncio.sleep(0.5)

    # Post escalated updates with a distinct prefix so users see they're updates
    if escalated_updates:
        await channel.send(f"**— {len(escalated_updates)} updates need review —**")
        for i, upd in enumerate(escalated_updates, 1):
            embed = build_update_embed(upd, i, len(escalated_updates), run_id)
            view = FindingView(run_id, upd["id"])
            await channel.send(embed=embed, view=view)
            await asyncio.sleep(0.5)

    if auto_approved_updates:
        await channel.send(
            f"**{len(auto_approved_updates)} status-change updates** auto-approved "
            f"(high-confidence bill status changes). They will apply automatically on `/research`."
        )

    await channel.send(
        f"**Review complete.** Click Approve/Reject on each item above, "
        f"then run `/approve` to finalize."
    )
    detach_handler(audit_handler)


def _classify_updates(candidate_updates: list[dict]) -> tuple[list[dict], list[dict]]:
    """Apply the update-review-policy rules in-process so the Discord UI can
    pre-sort updates into auto-approved (quiet) vs escalated (need review).

    Returns (auto_approved, escalated). Each list preserves the original entry
    dicts (shallow). This mirrors the reviewer.md policy logic; the real
    reviewer re-applies it on the research side so the bot's pre-sort is
    purely cosmetic — it doesn't override the reviewer's verdict.
    """
    policy_path = PROJECT_ROOT / "pipeline" / "config" / "update-review-policy.json"
    try:
        policy = json.loads(policy_path.read_text())
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.warning("Cannot read %s; escalating all updates: %s", policy_path, e)
        return [], list(candidate_updates)

    auto = policy.get("auto_approve", {})
    esc = policy.get("always_escalate", {})
    auto_signals = set(auto.get("diff_signal") or [])
    auto_confidence = auto.get("require_confidence", "high")
    esc_signals = set(esc.get("diff_signal") or [])
    esc_topic_types = set(esc.get("topic_types_always_escalate") or [])
    low_conf_escalates = bool(esc.get("low_confidence_always_escalates"))

    auto_approved: list[dict] = []
    escalated: list[dict] = []
    for u in candidate_updates:
        signal = u.get("diff_signal", "")
        topic_type = u.get("topic_type", "")
        confidence = u.get("topic_key_confidence", "")

        if signal in esc_signals \
                or topic_type in esc_topic_types \
                or (low_conf_escalates and confidence == "low"):
            escalated.append(u)
        elif signal in auto_signals and confidence == auto_confidence:
            auto_approved.append(u)
        else:
            escalated.append(u)
    return auto_approved, escalated


def build_update_embed(update: dict, index: int, total: int, run_id: str) -> discord.Embed:
    """Discord embed for a Phase 2 candidate_update entry needing human review."""
    title = f"[UPDATE {update['id']}] {update.get('title','')}"
    if len(title) > 256:
        title = title[:253] + "..."
    signal = update.get("diff_signal", "unknown")
    status_before = update.get("status_before", "")
    status_after = update.get("status_after", "")
    prev_key = update.get("previous_topic_key", "")
    prev_path = update.get("previous_report_path", "")

    color = {
        "signed": discord.Color.green(),
        "vetoed": discord.Color.red(),
        "amendment": discord.Color.gold(),
        "new_penalty": discord.Color.orange(),
    }.get(signal, discord.Color.blurple())

    embed = discord.Embed(title=title, color=color)
    embed.description = (update.get("summary", "") or "")[:1024]
    embed.add_field(name="Signal", value=signal, inline=True)
    embed.add_field(name="Transition", value=f"{status_before or '?'} → {status_after or '?'}", inline=True)
    embed.add_field(name="Existing report", value=f"`{prev_key}`\n`{prev_path}`", inline=False)
    if update.get("source_url"):
        embed.add_field(name="Source", value=update["source_url"][:200], inline=False)
    embed.set_footer(text=f"{index}/{total} | run {run_id}")
    return embed


# ---------------------------------------------------------------------------
# /findings — re-post findings for an existing run
# ---------------------------------------------------------------------------


@bot.tree.command(name="findings", description="Show findings for a run")
@app_commands.describe(run_id="Run ID (defaults to latest)")
async def cmd_findings(interaction: discord.Interaction, run_id: str = None):
    run_id = run_id or latest_run_id or get_latest_run_id()
    if not run_id:
        await interaction.response.send_message("No runs found.")
        return

    findings = load_findings(run_id)
    if not findings:
        await interaction.response.send_message(f"No findings for run `{run_id}`.")
        return

    await interaction.response.send_message(
        f"**Run `{run_id}`** — {len(findings)} findings:"
    )

    approval_state.setdefault(run_id, {})
    channel = interaction.channel

    for i, finding in enumerate(findings, 1):
        embed = build_finding_embed(finding, i, len(findings), run_id)
        view = FindingView(run_id, finding["id"])
        await channel.send(embed=embed, view=view)
        await asyncio.sleep(0.5)

    await channel.send("Click Approve/Reject, then `/approve` to finalize.")


# ---------------------------------------------------------------------------
# /approve — finalize approvals
# ---------------------------------------------------------------------------


@bot.tree.command(name="approve", description="Finalize approved findings")
@app_commands.describe(
    run_id="Run ID (defaults to latest)",
    all_findings="Approve all findings without reviewing (default: False)",
)
async def cmd_approve(
    interaction: discord.Interaction,
    run_id: str = None,
    all_findings: bool = False,
):
    run_id = run_id or latest_run_id or get_latest_run_id()
    if not run_id:
        await interaction.response.send_message("No runs found.")
        return

    if all_findings:
        findings = load_findings(run_id)
        approved_ids = {f["id"] for f in findings}
    else:
        state = approval_state.get(run_id, {})
        approved_ids = {fid for fid, approved in state.items() if approved}

    if not approved_ids:
        await interaction.response.send_message(
            f"No findings approved for `{run_id}`. "
            "Use the Approve buttons on findings first, or pass `all_findings: True`."
        )
        return

    output_path = write_approved_json(run_id, approved_ids)
    await interaction.response.send_message(
        f"**{len(approved_ids)} finding(s) approved** for run `{run_id}`.\n"
        f"Written to `{output_path.name}`.\n"
        f"Run `/research run_id:{run_id}` to start the research phase."
    )


# ---------------------------------------------------------------------------
# /research
# ---------------------------------------------------------------------------


@bot.tree.command(name="research", description="Start full research pipeline for approved findings")
@app_commands.describe(run_id="Run ID to research")
async def cmd_research(interaction: discord.Interaction, run_id: str = None):
    run_id = run_id or latest_run_id or get_latest_run_id()
    if not run_id:
        await interaction.response.send_message("No runs found.")
        return

    approved_path = RUNS_DIR / run_id / "scanner-approved.json"
    if not approved_path.exists():
        await interaction.response.send_message(
            f"No approved findings for `{run_id}`. Run `/approve` first."
        )
        return

    with open(approved_path) as f:
        approved = json.load(f)
    findings = approved.get("data", {}).get("findings", [])

    if not findings:
        await interaction.response.send_message("No approved findings to research.")
        return

    estimated_cost = len(findings) * RESEARCH_COST_PER_FINDING_USD
    await interaction.response.send_message(
        f"**Starting research phase for `{run_id}`** — "
        f"{len(findings)} finding(s). Estimated cost: **~${estimated_cost:.2f}** "
        f"(~${RESEARCH_COST_PER_FINDING_USD:.2f}/finding). "
        f"Delegating to orchestrator Mode 2."
    )

    channel = bot.get_channel(CHANNEL_ID)
    run_dir = RUNS_DIR / run_id
    audit_handler = attach_run_file_handler(logger, run_id)
    logger.info("research starting run_id=%s findings=%d estimated_usd=%.2f",
                run_id, len(findings), estimated_cost)

    # Single call into the orchestrator — it handles researcher per finding,
    # reviewer iteration, escalation detection, and categorizer invocation.
    def _run_research_phase():
        prompt = (
            f"Research phase for run {run_id}. Process approved findings from "
            f"pipeline/runs/{run_id}/scanner-approved.json. "
            f"Follow Mode 2 of the orchestrator instructions end-to-end: researcher "
            f"per finding, reviewer iteration, escalation check, then categorizer if "
            f"no escalations pending. Write the pipeline-complete.marker on success "
            f"or has-escalations.marker if escalations block categorization."
        )
        cmd = [
            "claude", "-p",
            "--agent", "orchestrator",
            "--output-format", "json",
            "--permission-mode", "acceptEdits",
            "--max-turns", "120",
            prompt,
        ]
        return run_claude_and_log_cost(cmd, run_id, "research", cwd=PROJECT_ROOT)

    ok, err, actual_cost = await asyncio.to_thread(_run_research_phase)
    if not ok:
        await channel.send(f"Research phase FAILED for `{run_id}` — {err}")
        detach_handler(audit_handler)
        return
    if actual_cost > 0:
        logger.info("research cost run_id=%s usd=%.4f", run_id, actual_cost)
        await channel.send(
            f"Research cost: **${actual_cost:.4f}** "
            f"(estimated ${estimated_cost:.2f})"
        )

    # Interpret result markers
    pipeline_complete = (run_dir / "pipeline-complete.marker").exists()
    has_escalations = (run_dir / "has-escalations.marker").exists() or any(
        run_dir.glob("escalation-*.json")
    )
    reviewer_output = run_dir / "reviewer-output.json"

    # Review stats if available
    if reviewer_output.exists():
        try:
            with open(reviewer_output) as f:
                rev_data = json.load(f)
            reviews = rev_data.get("data", {}).get("reviews", [])
            verified = sum(1 for r in reviews if r.get("status") == "verified")
            escalated = sum(1 for r in reviews if r.get("status") == "needs-human-review")
            await channel.send(
                f"**Review stats:** {verified} verified, {escalated} escalated."
            )
        except json.JSONDecodeError as e:
            logger.warning("Failed to parse reviewer-output.json for %s: %s", run_id, e)

    if has_escalations and not pipeline_complete:
        await channel.send(
            f"**Pipeline paused for `{run_id}`** — escalations need human review. "
            "Resolve escalations, then run `/research` again."
        )
        return

    if pipeline_complete:
        filed = find_run_reports(run_id)
        await channel.send(
            f"**Pipeline complete for `{run_id}`!** "
            f"{len(filed)} report(s) filed. Use `/results` to view them."
        )
    else:
        error_log = run_dir / "error.log"
        tail = ""
        if error_log.exists():
            tail = error_log.read_text()[-500:]
        await channel.send(
            f"Research phase ended without pipeline-complete.marker for `{run_id}`. "
            f"Check pipeline/runs/{run_id}/ for details.\n"
            + (f"```\n{tail}\n```" if tail else "")
        )
    detach_handler(audit_handler)


# ---------------------------------------------------------------------------
# /status
# ---------------------------------------------------------------------------


@bot.tree.command(name="status", description="Check pipeline run status")
@app_commands.describe(run_id="Run ID (defaults to latest)")
async def cmd_status(interaction: discord.Interaction, run_id: str = None):
    run_id = run_id or latest_run_id or get_latest_run_id()
    if not run_id:
        await interaction.response.send_message("No runs found.")
        return

    run_dir = RUNS_DIR / run_id
    if not run_dir.exists():
        await interaction.response.send_message(f"Run `{run_id}` not found.")
        return

    files = [f.name for f in run_dir.iterdir()]

    # Determine status
    if "pipeline-complete.marker" in files:
        status = "Complete"
        color = discord.Color.green()
    elif "has-escalations.marker" in files:
        status = "Escalations Pending"
        color = discord.Color.orange()
    elif "scanner-approved.json" in files:
        status = "Approved — ready for research"
        color = discord.Color.blue()
    elif "scan-complete.marker" in files:
        status = "Scan complete — awaiting review"
        color = discord.Color.gold()
    elif "scanner-output.json" in files:
        status = "Scanning complete — processing"
        color = discord.Color.gold()
    else:
        status = "In progress"
        color = discord.Color.greyple()

    # Count findings
    findings = load_findings(run_id)
    approved_count = 0
    if "scanner-approved.json" in files:
        with open(run_dir / "scanner-approved.json") as f:
            approved_data = json.load(f)
        approved_count = len(approved_data.get("data", {}).get("findings", []))

    embed = discord.Embed(title=f"Run {run_id}", color=color)
    embed.add_field(name="Status", value=status, inline=False)
    embed.add_field(name="Findings", value=str(len(findings)), inline=True)
    embed.add_field(name="Approved", value=str(approved_count), inline=True)
    embed.add_field(name="Artifacts", value="\n".join(sorted(files)) or "none", inline=False)

    await interaction.response.send_message(embed=embed)


def _classify_run_state(run_dir: Path) -> str:
    """Classify a run directory into a state bucket for /runs overview."""
    if not run_dir.exists():
        return "missing"
    names = {f.name for f in run_dir.iterdir()}
    if "pipeline-complete.marker" in names:
        return "complete"
    if "has-escalations.marker" in names or any(run_dir.glob("escalation-*.json")):
        return "escalations"
    if "fpf-complete.marker" in names:
        return "fpf-complete"
    if "scanner-approved.json" in names:
        return "ready-to-research"
    if "scan-complete.marker" in names:
        return "awaiting-approval"
    if "scanner-output.json" in names or "fpf-scanner-output.json" in names:
        return "scanning"
    return "in-progress"


# ---------------------------------------------------------------------------
# /runs — overview of all pipeline runs
# ---------------------------------------------------------------------------


@bot.tree.command(name="runs", description="Overview of all pipeline runs by state")
async def cmd_runs(interaction: discord.Interaction):
    if not RUNS_DIR.exists():
        await interaction.response.send_message("No runs directory yet.")
        return

    run_dirs = sorted(
        (p for p in RUNS_DIR.iterdir() if p.is_dir()),
        key=lambda p: p.name,
        reverse=True,
    )
    if not run_dirs:
        await interaction.response.send_message("No pipeline runs yet.")
        return

    from collections import Counter
    counts: Counter[str] = Counter()
    by_state: dict[str, list[str]] = {}
    for d in run_dirs:
        state = _classify_run_state(d)
        counts[state] += 1
        by_state.setdefault(state, []).append(d.name)

    state_order = [
        ("awaiting-approval", discord.Color.gold(), "Awaiting approval"),
        ("escalations", discord.Color.orange(), "Escalations pending"),
        ("ready-to-research", discord.Color.blue(), "Ready to research"),
        ("scanning", discord.Color.greyple(), "Scanning"),
        ("in-progress", discord.Color.greyple(), "In progress"),
        ("complete", discord.Color.green(), "Complete"),
        ("fpf-complete", discord.Color.teal(), "FPF complete"),
    ]

    embed = discord.Embed(
        title=f"Pipeline runs ({len(run_dirs)} total)",
        color=discord.Color.blurple(),
    )
    for state, _color, label in state_order:
        if counts.get(state, 0) == 0:
            continue
        runs = by_state[state][:5]
        more = len(by_state[state]) - len(runs)
        value = "\n".join(f"`{r}`" for r in runs)
        if more > 0:
            value += f"\n… +{more} more"
        embed.add_field(
            name=f"{label} ({counts[state]})",
            value=value or "—",
            inline=False,
        )

    embed.set_footer(text="Tip: /status <run_id> for details on a specific run")
    await interaction.response.send_message(embed=embed)


# ---------------------------------------------------------------------------
# /health — pre-flight check for setup issues
# ---------------------------------------------------------------------------


@bot.tree.command(name="health", description="Verify bot setup: env vars, claude CLI, config files")
async def cmd_health(interaction: discord.Interaction):
    checks: list[tuple[str, bool, str]] = []

    # 1. Required env vars
    for key in ("DISCORD_TOKEN", "DISCORD_GUILD_ID", "DISCORD_CHANNEL_ID"):
        checks.append((f"env {key}", bool(os.environ.get(key)), "set" if os.environ.get(key) else "missing"))
    imap_ok = bool(IMAP_EMAIL and IMAP_PASSWORD)
    checks.append(("env IMAP_EMAIL/IMAP_PASSWORD", imap_ok, "set" if imap_ok else "missing — /scan will skip email fetch"))

    # 2. Claude CLI on PATH
    ok, err = run_subprocess_checked(["claude", "--version"])
    checks.append(("claude CLI", ok, err or "available"))

    # 3. Config files
    for rel in (
        "pipeline/config/categories.json",
        "pipeline/config/sources.json",
        "pipeline/config/topic-key-rules.json",
    ):
        p = PROJECT_ROOT / rel
        if p.exists():
            try:
                json.loads(p.read_text())
                checks.append((rel, True, "valid json"))
            except json.JSONDecodeError as e:
                checks.append((rel, False, f"invalid json: {e}"))
        else:
            checks.append((rel, False, "missing"))

    # 4. State files
    for rel in ("reports/index.json", "bills/tracker.json"):
        p = PROJECT_ROOT / rel
        if p.exists():
            try:
                json.loads(p.read_text())
                checks.append((rel, True, "valid json"))
            except json.JSONDecodeError as e:
                checks.append((rel, False, f"invalid json: {e}"))
        else:
            checks.append((rel, False, "missing (will be created on first run)"))

    # 5. Python tools
    for rel in (
        "tools/topic_keys.py",
        "tools/update_reports_index.py",
        "tools/url_norm.py",
        "tools/bill_processor.py",
    ):
        p = PROJECT_ROOT / rel
        checks.append((rel, p.exists(), "present" if p.exists() else "missing"))

    all_ok = all(ok for _, ok, _ in checks)
    embed = discord.Embed(
        title="Zwiad health check",
        color=discord.Color.green() if all_ok else discord.Color.red(),
    )
    lines = []
    for name, ok, detail in checks:
        icon = "[OK]" if ok else "[FAIL]"
        lines.append(f"`{icon}` {name}  —  {detail}")
    # Discord field value limit is 1024 chars; split if needed
    chunk = ""
    idx = 1
    for line in lines:
        if len(chunk) + len(line) + 1 > 1000:
            embed.add_field(name=f"Checks (part {idx})", value=chunk, inline=False)
            chunk = line
            idx += 1
        else:
            chunk = f"{chunk}\n{line}" if chunk else line
    if chunk:
        embed.add_field(name=f"Checks (part {idx})" if idx > 1 else "Checks", value=chunk, inline=False)
    embed.set_footer(text="All green = ready to /scan")
    await interaction.response.send_message(embed=embed)


# ---------------------------------------------------------------------------
# /results — show completed research reports
# ---------------------------------------------------------------------------


class ResultsSelectView(discord.ui.View):
    """Dropdown to expand individual report details."""

    def __init__(self, reports_data: list[dict], run_id: str):
        super().__init__(timeout=None)
        self.reports_data = reports_data
        self.run_id = run_id

        options = []
        for i, rd in enumerate(reports_data):
            label = rd["title"][:100]
            options.append(discord.SelectOption(
                label=label,
                value=str(i),
                description=f"{rd['topic']} | {rd['jurisdiction']}",
            ))

        # Discord select menus max 25 options
        select = discord.ui.Select(
            placeholder="Select a report to expand...",
            options=options[:25],
        )
        select.callback = self._on_select
        self.add_item(select)

    async def _on_select(self, interaction: discord.Interaction):
        idx = int(interaction.data["values"][0])
        rd = self.reports_data[idx]

        summary = rd["summary"] or "No summary available."
        if len(summary) > 4000:
            summary = summary[:3997] + "..."

        embed = discord.Embed(
            title=rd["title"][:256],
            description=summary,
            color=topic_color(rd["topic"]),
        )
        embed.add_field(name="Category", value=rd["topic"], inline=True)
        embed.add_field(name="Jurisdiction", value=rd["jurisdiction"], inline=True)
        embed.add_field(name="Type", value=rd["dev_type"], inline=True)
        embed.add_field(name="Subcategory", value=rd["subcategory"], inline=True)
        embed.set_footer(text=f"Run {self.run_id} | {rd['path']}")
        await interaction.response.send_message(embed=embed)


@bot.tree.command(name="results", description="Show research reports from a completed run")
@app_commands.describe(run_id="Run ID (defaults to latest)")
async def cmd_results(interaction: discord.Interaction, run_id: str = None):
    run_id = run_id or latest_run_id or get_latest_run_id()
    if not run_id:
        await interaction.response.send_message("No runs found.")
        return

    filed = find_run_reports(run_id)
    if not filed:
        await interaction.response.send_message(
            f"No research results for run `{run_id}`. "
            "The research phase may not have completed yet."
        )
        return

    # Build report data for summary and dropdown
    reports_data = []
    for report in filed:
        dest = report.get("destination_path", "")
        filepath = PROJECT_ROOT / dest
        info = extract_report_summary(filepath)
        if not info:
            continue
        topic = report.get("topic", info["meta"].get("category", ""))
        reports_data.append({
            "title": info["title"],
            "summary": info["summary"],
            "topic": topic,
            "subcategory": report.get("subcategory", "—"),
            "jurisdiction": info["meta"].get("jurisdiction", "—"),
            "dev_type": info["meta"].get("development_type", "—"),
            "path": info["path"],
        })

    if not reports_data:
        await interaction.response.send_message("Could not read any reports.")
        return

    # Group by topic
    by_topic: dict[str, list] = {}
    for i, rd in enumerate(reports_data):
        by_topic.setdefault(rd["topic"], []).append((i + 1, rd))

    # Count by topic
    topic_counts = " | ".join(f"{len(v)} {k}" for k, v in by_topic.items())

    # Build summary text
    lines = []
    topic_emoji = {"privacy": "🟢", "cybersecurity": "🔵", "ai-law": "🟠"}
    for topic, items in by_topic.items():
        emoji = topic_emoji.get(topic, "⚪")
        lines.append(f"\n**{emoji} {topic.upper()}**")
        for num, rd in items:
            title_short = rd["title"][:70]
            lines.append(f"`{num}.` {title_short} — *{rd['jurisdiction']}*")

    summary_text = "\n".join(lines)
    if len(summary_text) > 4000:
        summary_text = summary_text[:3997] + "..."

    embed = discord.Embed(
        title=f"Research Results — Run {run_id}",
        description=summary_text,
        color=discord.Color.blurple(),
    )
    embed.set_footer(text=f"{len(reports_data)} reports | {topic_counts}")

    view = ResultsSelectView(reports_data, run_id)
    await interaction.response.send_message(embed=embed, view=view)


# ---------------------------------------------------------------------------
# /bills — list tracked bills
# ---------------------------------------------------------------------------

BILLS_DIR = PROJECT_ROOT / "bills"
TRACKER_PATH = BILLS_DIR / "tracker.json"


def load_tracker() -> dict:
    if TRACKER_PATH.exists():
        with open(TRACKER_PATH) as f:
            return json.load(f)
    return {"schema_version": "1.0", "bills": {}}


@bot.tree.command(name="bills", description="List tracked legislative bills")
@app_commands.describe(state="Filter by state abbreviation (e.g., FL, OR)")
async def cmd_bills(interaction: discord.Interaction, state: str = None):
    tracker = load_tracker()
    bills = tracker.get("bills", {})

    if not bills:
        await interaction.response.send_message("No bills tracked yet. Run `/scan` with FPF emails first.")
        return

    if state:
        state = state.upper()
        bills = {k: v for k, v in bills.items() if v.get("state_abbrev") == state}
        if not bills:
            await interaction.response.send_message(f"No bills tracked for state `{state}`.")
            return

    # Group by state
    by_state: dict[str, list] = {}
    for key, bill in sorted(bills.items()):
        st = bill.get("state", "Unknown")
        by_state.setdefault(st, []).append((key, bill))

    lines = []
    for st in sorted(by_state):
        lines.append(f"**{st}**")
        for key, bill in by_state[st]:
            status = bill.get("current_status", "?")
            title = bill.get("title", "")[:50]
            dl = "📄" if bill.get("download_status") == "success" else "⏳"
            cats = ", ".join(bill.get("category", []))
            lines.append(f"  {dl} `{bill['bill_identifier']}` — {status} | {cats}")
            if title:
                lines.append(f"    _{title}_")
        lines.append("")

    text = "\n".join(lines)
    if len(text) > 4000:
        text = text[:3997] + "..."

    embed = discord.Embed(
        title=f"Tracked Bills ({len(bills)} total)",
        description=text,
        color=discord.Color.teal(),
    )
    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="bill", description="Show details for a specific bill")
@app_commands.describe(identifier="Bill key (e.g., OR-SB-1546-2026) or bill ID (e.g., SB 1546)")
async def cmd_bill(interaction: discord.Interaction, identifier: str):
    tracker = load_tracker()
    bills = tracker.get("bills", {})

    # Try exact key match first
    bill = bills.get(identifier.upper())

    # Fuzzy match: search by bill_identifier
    if not bill:
        search = identifier.upper().replace(".", "").strip()
        for key, b in bills.items():
            if b.get("bill_identifier", "").upper().replace(".", "") == search:
                bill = b
                break
            if search in key.upper():
                bill = b
                break

    if not bill:
        await interaction.response.send_message(f"Bill `{identifier}` not found in tracker.")
        return

    # Build status history timeline
    history_lines = []
    for entry in bill.get("status_history", []):
        date = entry.get("date", "?")
        status = entry.get("status", "?")
        detail = entry.get("detail", "")
        line = f"**{date}** — {status}"
        if detail:
            line += f": {detail[:80]}"
        history_lines.append(line)

    history_text = "\n".join(history_lines[-10:]) or "No history recorded"

    embed = discord.Embed(
        title=f"{bill.get('state', '')} {bill.get('bill_identifier', '')}",
        description=bill.get("title", "No title"),
        color=discord.Color.teal(),
    )
    embed.add_field(name="Status", value=bill.get("current_status", "?"), inline=True)
    embed.add_field(name="Category", value=", ".join(bill.get("category", [])), inline=True)
    embed.add_field(name="Topics", value=", ".join(bill.get("topics", [])) or "—", inline=True)
    embed.add_field(name="Sponsors", value=", ".join(bill.get("sponsors", []))[:200] or "—", inline=False)
    embed.add_field(name="Download", value=bill.get("download_status", "?"), inline=True)
    embed.add_field(name="Session", value=bill.get("session", "?"), inline=True)

    if bill.get("bill_text_url"):
        embed.add_field(name="URL", value=bill["bill_text_url"][:200], inline=False)

    embed.add_field(name="Status History", value=history_text[:1024], inline=False)

    versions = bill.get("versions", [])
    if versions:
        ver_text = "\n".join(
            f"• {v['version_id']}: {'✅ MD' if v.get('md_path') else '📄 PDF only'}"
            for v in versions[-5:]
        )
        embed.add_field(name="Versions", value=ver_text, inline=False)

    await interaction.response.send_message(embed=embed)


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    bot.run(TOKEN)
