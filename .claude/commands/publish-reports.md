---
description: Sync all Zwiad memos to the zwiad-reports publish repo and push to GitHub (triggers Vercel rebuild)
allowed-tools: Bash(pipeline/scripts/sync-memos-to-publish.sh)
---

Run the bulk-publish script to sync every memo in `~/projecty/Zwiad/reports/` into the `zwiad-reports` publish repo, translating frontmatter and filenames to the site's expected format, then committing and pushing. A GitHub Action in `zwiad-reports` fires Vercel's Deploy Hook, which rebuilds `sitehome` — so memos appear at `sitehome.com/reports` within ~2 minutes.

Execute: `pipeline/scripts/sync-memos-to-publish.sh`

Report back the number of memos changed/new and whether the push succeeded. If the output says "No changes to publish," tell the user nothing needed updating.
