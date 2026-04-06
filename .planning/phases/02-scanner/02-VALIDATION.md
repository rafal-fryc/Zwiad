---
phase: 2
slug: scanner
status: draft
nyquist_compliant: false
wave_0_complete: false
created: 2026-04-06
---

# Phase 2 — Validation Strategy

> Per-phase validation contract for feedback sampling during execution.

---

## Test Infrastructure

| Property | Value |
|----------|-------|
| **Framework** | bash + jq (matches Phase 1 pattern) |
| **Config file** | none — uses pipeline/scripts/ |
| **Quick run command** | `bash tests/test-scanner.sh` |
| **Full suite command** | `bash tests/test-scanner-full.sh` |
| **Estimated runtime** | ~30 seconds |

---

## Sampling Rate

- **After every task commit:** Run `bash tests/test-scanner.sh`
- **After every plan wave:** Run `bash tests/test-scanner-full.sh`
- **Before `/gsd-verify-work`:** Full suite must be green
- **Max feedback latency:** 30 seconds

---

## Per-Task Verification Map

| Task ID | Plan | Wave | Requirement | Threat Ref | Secure Behavior | Test Type | Automated Command | File Exists | Status |
|---------|------|------|-------------|------------|-----------------|-----------|-------------------|-------------|--------|
| 02-01-01 | 01 | 1 | SCAN-01 | — | N/A | integration | `bash tests/test-scanner.sh digest` | ❌ W0 | ⬜ pending |
| 02-01-02 | 01 | 1 | SCAN-02 | — | N/A | integration | `bash tests/test-scanner.sh gov` | ❌ W0 | ⬜ pending |
| 02-01-03 | 01 | 1 | SCAN-03 | — | N/A | integration | `bash tests/test-scanner.sh lawfirm` | ❌ W0 | ⬜ pending |
| 02-02-01 | 02 | 2 | SCAN-04 | — | N/A | integration | `bash tests/test-scanner.sh dedup` | ❌ W0 | ⬜ pending |
| 02-03-01 | 03 | 2 | SCAN-05 | — | N/A | integration | `bash tests/test-scanner.sh approval` | ❌ W0 | ⬜ pending |
| 02-03-02 | 03 | 2 | PIPE-03 | — | N/A | integration | `bash tests/test-scanner.sh gate` | ❌ W0 | ⬜ pending |

*Status: ⬜ pending · ✅ green · ❌ red · ⚠️ flaky*

---

## Wave 0 Requirements

- [ ] `tests/test-scanner.sh` — test runner for scanner integration tests
- [ ] `tests/fixtures/sample-digest.html` — sample Lexology digest HTML for parsing tests
- [ ] `tests/fixtures/sample-findings.json` — expected scanner output for validation

*If none: "Existing infrastructure covers all phase requirements."*

---

## Manual-Only Verifications

| Behavior | Requirement | Why Manual | Test Instructions |
|----------|-------------|------------|-------------------|
| WebSearch returns relevant government results | SCAN-02 | Requires live web access | Run scanner against real sources, verify results |
| WebFetch retrieves full Lexology articles | SCAN-01 | Requires live web access | Fetch a known Lexology URL, verify content extraction |

---

## Validation Sign-Off

- [ ] All tasks have `<automated>` verify or Wave 0 dependencies
- [ ] Sampling continuity: no 3 consecutive tasks without automated verify
- [ ] Wave 0 covers all MISSING references
- [ ] No watch-mode flags
- [ ] Feedback latency < 30s
- [ ] `nyquist_compliant: true` set in frontmatter

**Approval:** pending
