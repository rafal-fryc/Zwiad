---
phase: 1
slug: agent-framework
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-04-06
---

# Phase 1 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | bash test scripts (no external framework — pure CLI project) |
| **Config file** | none — Wave 0 creates test scripts |
| **Quick run command** | `bash tests/test-agent-launch.sh` |
| **Full suite command** | `bash tests/run-all.sh` |
| **Estimated runtime** | ~30 seconds |

---

## Sampling Rate

- **After every task commit:** Run `bash tests/test-agent-launch.sh`
- **After every plan wave:** Run `bash tests/run-all.sh`
- **Before `/gsd-verify-work`:** Full suite must be green
- **Max feedback latency:** 30 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 1-01-01 | 01 | 1 | PIPE-05 | — | N/A | integration | `bash tests/test-agent-launch.sh` | ❌ W0 | ⬜ pending |
| 1-01-02 | 01 | 1 | PIPE-06 | — | N/A | integration | `bash tests/test-schema-validation.sh` | ❌ W0 | ⬜ pending |
| 1-01-03 | 01 | 1 | PIPE-06 | — | Malformed JSON caught | integration | `bash tests/test-validation-failure.sh` | ❌ W0 | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] `tests/test-agent-launch.sh` — verify agent subprocess launches and exits cleanly
- [ ] `tests/test-schema-validation.sh` — verify valid JSON passes schema validation
- [ ] `tests/test-validation-failure.sh` — verify malformed JSON is caught and reported
- [ ] `tests/run-all.sh` — runner that executes all test scripts

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Orchestrator spawns subagents via Agent tool | PIPE-05 | Requires live Claude session | Run orchestrator agent, verify it spawns scanner stub and receives output |

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 30s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
