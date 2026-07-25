# Cursor Automations — Wellthlab DTC

Prefill specs for the Automations editor. Repo: `colindmurphy0409-hash/amazon-affilate-blog` (branch: `main`).

## 1. Shopify Content Automation

**Schedule:** Every Sunday at 9:00 AM (`0 9 * * 0`)
**Prompt:**
```
Run Wellthlab weekly content drafting (Phases 1–2 only).

0. Read brand/competitors.yaml — if brands listed, note slugs for user to run "Run competitor research" in Agents Window (Blotato unavailable in cron).
1. Read workflows/trend-research.md — use catalog + campaigns/active.yaml + prior week content + any existing competitor playbooks in content/research/competitors/.
2. Read workflows/weekly-social.md — write content/week-XX/ for current ISO week:
   - social.md (7 scripts with tool tags: blotato | canva | remotion | film)
   - carousels.md
   - canva-briefs.yaml
   - remotion-props.json
   - approval.md (status: draft)
3. Do NOT post, schedule, or mark approved.
4. Tell the user to review approval.md and run "Run full trend research" in Agents Window for Blotato competitor research.
```

## 2. Monday Growth Brief

**Schedule:** Every Monday at 9:00 AM (`0 9 * * 1`)

**Prompt:**
```
Run workflows/growth-brief.md.

Read kpi/weekly-template.csv, campaigns/active.yaml, products/catalog.yaml.
Write content/week-XX/growth-brief.md for current ISO week.
Under 400 words. Note if KPI data is empty.
```

## Finish in editor
- Confirm git repo + branch scope
- Enable file read/write in repo
- Cloud compute if needed for longer runs
