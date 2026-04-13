"""Shared logging setup for Zwiad Python tools.

Usage:
    from tools.logging_setup import get_logger, attach_run_file_handler

    logger = get_logger(__name__)
    logger.info("starting scan for %s", run_id)

    # Optional: also write to pipeline/runs/<run_id>/audit.log
    attach_run_file_handler(logger, run_id)

Goals:
- Single consistent format across all Zwiad Python tools
- stdout logging always on (so scripts look normal when invoked directly)
- Optional per-run file handler writes to pipeline/runs/<run_id>/audit.log
  so a run's audit trail ends up in one place alongside its other artifacts
- Idempotent: calling get_logger() twice for the same name is safe
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RUNS_DIR = PROJECT_ROOT / "pipeline" / "runs"

_DEFAULT_FORMAT = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
_CONFIGURED = False


def get_logger(name: str = "zwiad") -> logging.Logger:
    """Return a configured logger. Safe to call multiple times."""
    global _CONFIGURED
    logger = logging.getLogger(name)
    if not _CONFIGURED:
        root = logging.getLogger("zwiad")
        if not root.handlers:
            handler = logging.StreamHandler(sys.stderr)
            handler.setFormatter(logging.Formatter(_DEFAULT_FORMAT))
            root.addHandler(handler)
            root.setLevel(logging.INFO)
            root.propagate = False
        _CONFIGURED = True
    return logger


def attach_run_file_handler(logger: logging.Logger, run_id: str) -> logging.FileHandler | None:
    """Attach a FileHandler writing to pipeline/runs/<run_id>/audit.log.

    Returns the handler so the caller can remove it at end-of-run if desired.
    If the run directory doesn't exist, returns None without attaching.
    """
    run_dir = RUNS_DIR / run_id
    if not run_dir.exists():
        logger.warning("Cannot attach audit log handler — run dir missing: %s", run_dir)
        return None
    audit_path = run_dir / "audit.log"
    handler = logging.FileHandler(audit_path, mode="a", encoding="utf-8")
    handler.setFormatter(logging.Formatter(_DEFAULT_FORMAT))
    handler.setLevel(logging.INFO)
    # Attach to the root zwiad logger so all child loggers inherit it
    logging.getLogger("zwiad").addHandler(handler)
    return handler


def detach_handler(handler: logging.FileHandler | None) -> None:
    """Remove a previously-attached file handler (e.g. at end-of-run)."""
    if handler is None:
        return
    logging.getLogger("zwiad").removeHandler(handler)
    try:
        handler.close()
    except Exception:
        pass
