---
phase: 3
slug: report-generation
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-04-06
---

# Phase 3 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | bash + jq (matches Phase 1/2 pattern) |
| **Config file** | none — uses pipeline/scripts/ |
| **Quick run command** | `bash tests/test-researcher.sh` |
| **Full suite command** | `bash tests/test-researcher-full.sh` |
| **Estimated runtime** | ~30 seconds |

---

## Sampling Rate

- **After every task commit:** Run `bash tests/test-researcher.sh`
- **After every plan wave:** Run `bash tests/test-researcher-full.sh`
- **Before `/gsd-verify-work`:** Full suite must be green
- **Max feedback latency:** 30 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 03-01-01 | 01 | 1 | REPT-01 | — | N/A | integration | `bash tests/test-researcher.sh report` | ❌ W0 | ⬜ pending |
| 03-01-02 | 01 | 1 | REPT-02 | — | N/A | integration | `bash tests/test-researcher.sh format` | ❌ W0 | ⬜ pending |
| 03-02-01 | 02 | 2 | REPT-03 | — | N/A | integration | `bash tests/test-researcher.sh confidence` | ❌ W0 | ⬜ pending |
| 03-02-02 | 02 | 2 | REPT-04 | — | N/A | integration | `bash tests/test-researcher.sh related` | ❌ W0 | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] `tests/test-researcher.sh` — test runner for researcher integration tests
- [ ] `tests/fixtures/sample-approved-findings.json` — approved findings fixture for testing
- [ ] `tests/fixtures/sample-researcher-output.json` — expected researcher output for validation

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| WebSearch returns relevant legal texts | REPT-01 | Requires live web access | Run researcher on a real finding, verify citations link to actual sources |
| Format selection matches relevance | REPT-02 | Requires Claude judgment evaluation | Check HIGH relevance → client-alert, MEDIUM/LOW → research-memo |

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 30s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
