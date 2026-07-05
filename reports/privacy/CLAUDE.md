# Privacy Reports Directory

This directory contains verified regulatory intelligence reports on privacy law developments across US state and federal jurisdictions.

This file lists directory structure only. The authoritative report index is reports/index.json; do not maintain report tables here.

## Directory Structure

Subcategories in `pipeline/config/categories.json`:
- `state-comprehensive-laws/` — State omnibus consumer privacy statutes (Virginia-model, CCPA-model, etc.)
- `federal-legislation/` — Federal privacy bills and DOJ data security programs
- `enforcement-actions/` — FTC, state AG, and private enforcement actions
- `data-breach/` — Data breach notification laws and enforcement
- `childrens-privacy/` — COPPA, state children's online privacy laws, social media restrictions
- `health-data/` — HIPAA, Washington My Health My Data, health sector privacy
- `financial-privacy/` — GLBA, state financial privacy laws, banking sector data rules

Additional directories on disk (not yet in categories.json):
- `california/` — California-specific privacy matters spanning multiple subcategories
- `litigation/` — Court decisions, class actions, and civil litigation (pending subcategory approval)

Reports at the root of this directory cover topics that span subcategories or do not fit neatly into a single subdirectory.

## Cross-References

- SCAN-20260412-003 (Claude Mythos cyberattack) is filed under `reports/cybersecurity/` as the primary topic but has secondary relevance to AI governance — see `reports/ai-law/` for related AI regulation reports.
- SCAN-20260412-026 (Trump AI EO state preemption) is filed under `reports/ai-law/` but has direct implications for state privacy law preemption.
- SCAN-20260412-028 supersedes SCAN-20260412-009. Do not cite 009 in new client materials.
- SCAN-20260601-034 (IL/CT/NY AI-privacy laws) has secondary relevance to AI law — see `reports/ai-law/state-legislation/`.
- SCAN-20260601-047 (FTC TAKE IT DOWN Act platforms) is the parent report updated by SCAN-20260601-003 (FTC enforcement start) and SCAN-20260601-011 (nudify warning letters).
