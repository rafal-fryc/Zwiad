# AI Law Reports Directory

This directory contains verified regulatory intelligence reports on artificial intelligence regulation, algorithmic accountability, AI safety frameworks, and related legal developments across US state and federal jurisdictions.

This file lists directory structure only. The authoritative report index is reports/index.json; do not maintain report tables here.

## Directory Structure

Subcategories in `pipeline/config/categories.json`:
- `federal-regulation/` — Federal AI legislation and rulemaking
- `state-legislation/` — State AI bills (chatbot disclosure, algorithmic accountability, etc.)
- `executive-orders/` — Presidential executive orders on AI policy
- `enforcement-actions/` — FTC, state AG, and other AI enforcement actions
- `frameworks-guidance/` — NIST AI RMF, agency guidance, voluntary frameworks
- `health/` — AI in healthcare regulation
- `chatbots/` — Chatbot-specific laws and regulations
- `liability/` — AI liability frameworks and litigation
- `frontier-models/` — Regulation and policy around advanced/frontier AI models

Additional directories on disk (not yet in categories.json):
- `california/` — California-specific AI law matters spanning multiple subcategories
- `employment-ai/` — AI in employment: AEDT laws, WARN Act disclosure, employer AI obligations (pending subcategory approval)
- `state/` — State-level AI laws not yet assigned to a specific subcategory

Reports at the root of this directory cover topics that span subcategories or do not fit neatly into a single subdirectory.

## Cross-References

- SCAN-20260412-003 (Claude Mythos cyberattack) is filed under `reports/cybersecurity/` as the primary topic but has direct relevance to AI governance and frontier model policy.
- SCAN-20260412-028 (TAKE IT DOWN Act first conviction) is filed under `reports/privacy/` and covers AI deepfake enforcement — relevant to AI law practitioners tracking AI-specific criminal statutes.
- SCAN-20260601-019 (Trump AI cybersecurity EO pulled) has direct secondary relevance to cybersecurity — see `reports/cybersecurity/standards-guidance/federal-ai-cybersecurity-eo-frontier-model-postponed-2026-05-20.md` for the companion cybersecurity-primary report.
- SCAN-20260601-036 (Trump AI cabinet divisions) provides political context for SCAN-20260601-019 (pulled EO).
- SCAN-20260601-042 (Colorado SB 189) has secondary relevance to employment AI — see `employment-ai/` for related Connecticut and New York employment AI reports.
