#!/usr/bin/env python3
"""Zwiad Discord bot — interact with the regulatory monitoring pipeline via Discord."""

import asyncio
import email as email_lib
import imaplib
import json
import os
import re
import subprocess
import sys
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

MY_GUILD = discord.Object(id=GUILD_ID)

# In-memory approval state: {run_id: {finding_id: bool}}
approval_state: dict[str, dict[str, bool]] = {}

# Track the latest run_id for convenience
latest_run_id: str | None = None

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def fetch_new_emails(run_id: str) -> list[Path]:
    """Fetch unread emails via IMAP, save as HTML, mark as read. Returns saved file paths."""
    if not IMAP_EMAIL or not IMAP_PASSWORD:
        return []

    input_dir = RUNS_DIR / run_id / "emails"
    input_dir.mkdir(parents=True, exist_ok=True)

    saved = []
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    try:
        mail.login(IMAP_EMAIL, IMAP_PASSWORD)
        mail.select("INBOX")
        status, messages = mail.search(None, "UNSEEN")
        if status != "OK" or not messages[0]:
            return []

        msg_ids = messages[0].split()
        for i, msg_id in enumerate(msg_ids):
            status, data = mail.fetch(msg_id, "(RFC822)")
            if status != "OK":
                continue

            msg = email_lib.message_from_bytes(data[0][1])

            # Extract HTML body
            html_body = None
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/html":
                        html_body = part.get_payload(decode=True)
                        break
            elif msg.get_content_type() == "text/html":
                html_body = msg.get_payload(decode=True)

            if not html_body:
                # Fall back to plain text wrapped in HTML
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

                # Save metadata sidecar for email classification
                meta = {
                    "subject": subject,
                    "from": msg.get("From", ""),
                    "date": msg.get("Date", ""),
                }
                meta_path = input_dir / f"{safe_name}-{i}.meta.json"
                with open(meta_path, "w") as mf:
                    json.dump(meta, mf, indent=2)

            # Mark as read
            mail.store(msg_id, "+FLAGS", "\\Seen")
    finally:
        try:
            mail.logout()
        except Exception:
            pass

    return saved


def classify_emails(email_dir: Path) -> dict[str, list[Path]]:
    """Classify emails in a directory by type using metadata sidecars.

    Returns dict mapping type ('fpf', 'lexology', 'unknown') to list of HTML file paths.
    """
    result: dict[str, list[Path]] = {"fpf": [], "lexology": [], "unknown": []}

    for html_file in sorted(email_dir.glob("*.html")):
        meta_path = html_file.with_suffix(".meta.json")
        if not meta_path.exists():
            result["unknown"].append(html_file)
            continue

        with open(meta_path) as f:
            meta = json.load(f)

        sender = (meta.get("from") or "").lower()
        subject = (meta.get("subject") or "").lower()

        if ("fpf.org" in sender or "informz.net" in sender) and "fpf u.s." in subject:
            result["fpf"].append(html_file)
        elif "lexology" in sender:
            result["lexology"].append(html_file)
        else:
            result["unknown"].append(html_file)

    return result


def get_latest_run_id() -> str | None:
    """Return the most recent run_id by directory modification time."""
    if not RUNS_DIR.exists():
        return None
    runs = sorted(RUNS_DIR.iterdir(), key=lambda p: p.stat().st_mtime, reverse=True)
    return runs[0].name if runs else None


def load_findings(run_id: str) -> list[dict]:
    """Load findings from scanner-deduped.json (or scanner-output.json)."""
    for name in ("scanner-deduped.json", "scanner-output.json"):
        path = RUNS_DIR / run_id / name
        if path.exists():
            with open(path) as f:
                data = json.load(f)
            return data.get("data", {}).get("findings", [])
    return []


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
    """Load filed report paths from categorizer-output.json, falling back to researcher outputs."""
    cat_path = RUNS_DIR / run_id / "categorizer-output.json"
    if cat_path.exists():
        with open(cat_path) as f:
            data = json.load(f)
        return data.get("data", {}).get("filed_reports", [])

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
    """Write scanner-approved.json from approved finding IDs."""
    # Read source data
    source_path = RUNS_DIR / run_id / "scanner-deduped.json"
    if not source_path.exists():
        source_path = RUNS_DIR / run_id / "scanner-output.json"

    with open(source_path) as f:
        source = json.load(f)

    approved_findings = [
        f for f in source.get("data", {}).get("findings", []) if f["id"] in approved_ids
    ]

    envelope = {
        "schema_version": source.get("schema_version", "1.0"),
        "pipeline_run_id": source.get("pipeline_run_id", run_id),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "stage": "human-review",
        "status": "complete",
        "data": {"findings": approved_findings},
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

    # Fetch new emails
    email_files = await asyncio.to_thread(fetch_new_emails, run_id)

    if email_files:
        await channel.send(
            f"**Found {len(email_files)} new email(s).** Classifying..."
        )
    else:
        await channel.send("No new emails. Scanning web sources only...")

    # Classify emails
    email_dir = run_dir / "emails"
    classified = classify_emails(email_dir) if email_files else {"fpf": [], "lexology": [], "unknown": []}

    fpf_emails = classified.get("fpf", [])
    lexology_emails = classified.get("lexology", [])

    if fpf_emails:
        await channel.send(f"**{len(fpf_emails)} FPF legislative email(s)** detected. Processing bills...")
    if lexology_emails:
        await channel.send(f"**{len(lexology_emails)} Lexology digest(s)** detected.")

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
            subprocess.run(cmd, capture_output=True, text=True, cwd=str(PROJECT_ROOT))

        await asyncio.to_thread(_run_fpf_scan)

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

    # Run Lexology/web scan
    def _run_scan():
        if lexology_emails:
            input_path = str(lexology_emails[0])
            prompt = (
                f"Scan phase for run {run_id}. "
                f"Input digest file: {input_path}. "
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
            "--max-turns", "30",
            prompt,
        ]

        subprocess.run(cmd, capture_output=True, text=True, cwd=str(PROJECT_ROOT))
        return run_id

    run_id = await asyncio.to_thread(_run_scan)
    latest_run_id = run_id

    findings = load_findings(run_id)
    channel = bot.get_channel(CHANNEL_ID)

    if not findings:
        await channel.send(f"Scan `{run_id}` complete but no findings were produced. Check `pipeline/runs/{run_id}/` for errors.")
        return

    await channel.send(f"**Scan complete: `{run_id}`** — {len(findings)} findings. Posting for review...")

    # Initialize approval state
    approval_state[run_id] = {}

    for i, finding in enumerate(findings, 1):
        embed = build_finding_embed(finding, i, len(findings), run_id)
        view = FindingView(run_id, finding["id"])
        await channel.send(embed=embed, view=view)
        await asyncio.sleep(0.5)  # avoid rate limits

    await channel.send(
        f"**Review complete.** Click Approve/Reject on each finding above, "
        f"then run `/approve` to finalize."
    )


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

    await interaction.response.send_message(
        f"**Starting full pipeline for `{run_id}`** — "
        f"{len(findings)} finding(s) to research, review, and categorize."
    )

    channel = bot.get_channel(CHANNEL_ID)
    run_dir = RUNS_DIR / run_id

    # --- Stage 1: Researcher (one call per finding) ---

    async def _research_finding(index, finding):
        finding_id = finding["id"]
        output_path = f"pipeline/runs/{run_id}/researcher-{finding_id}.json"

        # Skip if already researched
        if (PROJECT_ROOT / output_path).exists():
            return True

        finding_json = json.dumps(finding)
        prompt = (
            f"Research this regulatory development. Finding {index + 1} of {len(findings)}. "
            f"Pipeline run ID: {run_id}. "
            f"Finding data: {finding_json}. "
            f"Write your output to {output_path}."
        )

        cmd = [
            "claude", "-p",
            "--agent", "researcher",
            "--output-format", "json",
            "--permission-mode", "acceptEdits",
            "--max-turns", "20",
            prompt,
        ]

        result = await asyncio.to_thread(
            subprocess.run, cmd, capture_output=True, text=True, cwd=str(PROJECT_ROOT)
        )
        return (PROJECT_ROOT / output_path).exists()

    await channel.send("**Stage 1/3: Researching findings...**")

    for i, finding in enumerate(findings):
        finding_id = finding["id"]
        title = finding.get("title", "")[:60]

        # Skip already-researched findings
        if (run_dir / f"researcher-{finding_id}.json").exists():
            await channel.send(f"`[{i+1}/{len(findings)}]` {title} — already researched, skipping")
            continue

        await channel.send(f"`[{i+1}/{len(findings)}]` Researching: {title}...")
        success = await _research_finding(i, finding)
        if not success:
            await channel.send(f"  Warning: researcher did not produce output for {finding_id}")

    await channel.send(f"**Research complete.** {len(findings)} findings processed.")

    # --- Stage 2: Reviewer (uses existing shell script) ---

    await channel.send("**Stage 2/3: Reviewing and fact-checking reports...**")

    def _run_reviewer():
        cmd = [
            "bash", "pipeline/scripts/run-reviewer.sh", run_id,
        ]
        return subprocess.run(cmd, capture_output=True, text=True, cwd=str(PROJECT_ROOT))

    reviewer_result = await asyncio.to_thread(_run_reviewer)

    reviewer_output = run_dir / "reviewer-output.json"
    if reviewer_output.exists():
        with open(reviewer_output) as f:
            rev_data = json.load(f)
        reviews = rev_data.get("data", {}).get("reviews", [])
        verified = sum(1 for r in reviews if r.get("status") == "verified")
        escalated = sum(1 for r in reviews if r.get("status") == "needs-human-review")
        await channel.send(
            f"**Review complete.** {verified} verified, {escalated} escalated."
        )
    else:
        await channel.send(
            "Warning: reviewer did not produce output. "
            f"stderr: {reviewer_result.stderr[:300] if reviewer_result.stderr else 'none'}"
        )

    # --- Stage 3: Categorizer ---

    # Check for escalations — skip categorizer if escalations pending
    if (run_dir / "has-escalations.marker").exists() or any(
        run_dir.glob("escalation-*.json")
    ):
        (run_dir / "has-escalations.marker").write_text("ESCALATIONS_PENDING\n")
        await channel.send(
            f"**Pipeline paused for `{run_id}`** — escalations need human review. "
            "Resolve escalations, then run `/research` again."
        )
        return

    await channel.send("**Stage 3/3: Categorizing reports...**")

    def _run_categorizer():
        prompt = (
            f"Categorize verified reports. "
            f"Reviewer output: pipeline/runs/{run_id}/reviewer-output.json. "
            f"Pipeline run ID: {run_id}. "
            f"Write output to pipeline/runs/{run_id}/categorizer-output.json"
        )
        cmd = [
            "claude", "-p",
            "--agent", "categorizer",
            "--output-format", "json",
            "--permission-mode", "acceptEdits",
            "--max-turns", "10",
            prompt,
        ]
        return subprocess.run(cmd, capture_output=True, text=True, cwd=str(PROJECT_ROOT))

    await asyncio.to_thread(_run_categorizer)

    if (run_dir / "categorizer-output.json").exists():
        (run_dir / "pipeline-complete.marker").write_text("PIPELINE_COMPLETE\n")
        filed = find_run_reports(run_id)
        await channel.send(
            f"**Pipeline complete for `{run_id}`!** "
            f"{len(filed)} report(s) filed. Use `/results` to view them."
        )
    else:
        await channel.send(
            "Warning: categorizer did not produce output. "
            "Check the run directory for details."
        )


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
