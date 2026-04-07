---
phase: 5
slug: pipeline-integration
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-04-07
---

# Phase 5 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | bash test scripts (existing pattern) + Python unittest |
| **Config file** | none — uses existing pipeline/scripts/ pattern |
| **Quick run command** | `python -m pytest tests/test_pipeline.py -x` |
| **Full suite command** | `bash tests/run-phase05-tests.sh` |
| **Estimated runtime** | ~30 seconds |

---

## Sampling Rate

- **After every task commit:** Run `python -m pytest tests/test_pipeline.py -x`
- **After every plan wave:** Run `bash tests/run-phase05-tests.sh`
- **Before `/gsd-verify-work`:** Full suite must be green
- **Max feedback latency:** 30 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 05-01-01 | 01 | 1 | PIPE-01 | — | N/A | integration | `bash tests/test-categorizer-filing.sh` | ❌ W0 | ⬜ pending |
| 05-01-02 | 01 | 1 | PIPE-01 | — | N/A | integration | `bash tests/test-subcategory-pending.sh` | ❌ W0 | ⬜ pending |
| 05-01-03 | 01 | 1 | PIPE-01 | — | N/A | integration | `bash tests/test-symlink-creation.sh` | ❌ W0 | ⬜ pending |
| 05-02-01 | 02 | 1 | PIPE-02 | — | N/A | integration | `bash tests/test-audit-log.sh` | ❌ W0 | ⬜ pending |
| 05-03-01 | 03 | 2 | PIPE-04 | — | N/A | integration | `python -m pytest tests/test_run_pipeline.py` | ❌ W0 | ⬜ pending |
| 05-03-02 | 03 | 2 | PIPE-04 | — | N/A | integration | `bash tests/test-cron-trigger.sh` | ❌ W0 | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] `tests/test-categorizer-filing.sh` — test report filing into topic/subcategory folders
- [ ] `tests/test-subcategory-pending.sh` — test new subcategory flagged for review
- [ ] `tests/test-symlink-creation.sh` — test symlink creation for multi-topic reports
- [ ] `tests/test-audit-log.sh` — test audit log generation per pipeline run
- [ ] `tests/test_run_pipeline.py` — test Python pipeline entry point
- [ ] `tests/test-cron-trigger.sh` — test cron-triggered execution

*These stubs will be refined once PLAN.md tasks are finalized.*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Desktop notification on approval-pending | PIPE-04 | Requires DBUS session and visual confirmation | Run pipeline, verify notify-send popup appears |
| Desktop notification on failure | PIPE-04 | Requires DBUS session and visual confirmation | Kill agent mid-run, verify error notification appears |
| Cron daily execution | PIPE-04 | Requires cron daemon and time passage | Install crontab, wait for trigger, check run directory |

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 30s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
