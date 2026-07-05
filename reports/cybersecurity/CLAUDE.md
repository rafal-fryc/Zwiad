# Cybersecurity Reports Directory

This directory contains verified regulatory intelligence reports on cybersecurity law, policy, and enforcement developments across US state and federal jurisdictions.

This file lists directory structure only. The authoritative report index is reports/index.json; do not maintain report tables here.

## Directory Structure

Subcategories in `pipeline/config/categories.json`:
- `federal-frameworks/` — Federal cybersecurity frameworks, strategies, and policy
- `incident-reporting/` — Federal and state cyber incident reporting requirements
- `enforcement-actions/` — FTC, CISA, and sector-specific cybersecurity enforcement
- `critical-infrastructure/` — Critical infrastructure protection and sector-specific rules
- `standards-guidance/` — NIST frameworks, CISA guidance, security standards

Additional directories on disk (not yet in categories.json):
- `ai-threat-response/` — AI-specific threat response and security matters
- `state/` — State-level cybersecurity laws and enforcement

Reports at the root of this directory cover topics that span subcategories or do not fit neatly into a single subdirectory.

## Cross-References

- SCAN-20260412-003 (Claude Mythos) has secondary relevance to AI law and governance. See `reports/ai-law/` for related AI regulation reports including SCAN-20260412-026 (Trump AI EO).
- SCAN-20260601-010 (AI Cybersecurity EO draft/postponement) has direct secondary relevance to AI law frontier model policy — see `reports/ai-law/frontier-models/`.
- SCAN-20260601-014 (CYBERCOM/NSA AI task force) has secondary relevance to AI governance and frontier model security.
- SCAN-20260601-018 (HHS OCR cybersecurity reorganization) has secondary relevance to health data privacy — see `reports/privacy/health-data/`.
