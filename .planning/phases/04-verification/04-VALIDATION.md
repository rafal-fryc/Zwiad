---
phase: 4
slug: verification
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-04-07
---

# Phase 4 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | bash + jq (test scripts) |
| **Config file** | `tests/run-all.sh` |
| **Quick run command** | `bash tests/test-reviewer-validation.sh` |
| **Full suite command** | `bash tests/run-all.sh` |
| **Estimated runtime** | ~5 seconds |

---

## Sampling Rate

- **After every task commit:** Run `bash tests/test-reviewer-validation.sh`
- **After every plan wave:** Run `bash tests/run-all.sh`
- **Before `/gsd-verify-work`:** Full suite must be green
- **Max feedback latency:** 5 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 04-01-01 | 01 | 0 | VERF-01 | — | N/A | unit | `bash tests/test-reviewer-validation.sh` | ❌ W0 | ⬜ pending |
| 04-01-02 | 01 | 0 | VERF-02 | — | N/A | unit | `bash tests/test-reviewer-validation.sh` | ❌ W0 | ⬜ pending |
| 04-01-03 | 01 | 0 | VERF-03 | — | N/A | unit | `bash tests/test-reviewer-iteration.sh` | ❌ W0 | ⬜ pending |
| 04-01-04 | 01 | 0 | VERF-04 | — | N/A | unit | `bash tests/test-reviewer-annotation.sh` | ❌ W0 | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] `tests/test-reviewer-validation.sh` — stubs for VERF-01, VERF-02 (schema and feedback structure)
- [ ] `tests/test-reviewer-iteration.sh` — stubs for VERF-03 (iteration logic, escalation trigger)
- [ ] `tests/test-reviewer-annotation.sh` — stubs for VERF-04 (per-claim annotation presence)
- [ ] `tests/fixtures/sample-reviewer-feedback.json` — valid feedback fixture
- [ ] `tests/fixtures/sample-reviewer-output.json` — complete reviewer envelope fixture

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| Reviewer identifies unsupported claims in real reports | VERF-01 | Requires live LLM agent invocation | Run `run-reviewer.sh` against a sample report with known false claims; verify feedback JSON identifies them |
| Researcher revises report after reviewer feedback | VERF-03 | Requires multi-agent iteration | Run full iteration loop manually; verify researcher addresses critical/major issues |
| Human escalation flow works end-to-end | VERF-03 | Requires human interaction | Simulate 3 failed rounds; verify escalation markdown is generated; add APPROVED marker; verify pipeline resumes |

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 5s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
