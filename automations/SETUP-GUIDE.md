# Shopify Content Automation — Setup Guide

The agent cannot reliably pre-fill the Automations editor from chat. **You create it once in the UI; it runs forever.**

Automation name: **Shopify Content Automation**

---

## Part A — Create Shopify Content Automation

### Step 1: Open Automations

1. In Cursor, click **Automations** in the left sidebar (clock/robot icon).
2. Click **+ New automation** (top right).

### Step 2: Name it

| Field | Paste this |
|-------|------------|
| **Name** | `Shopify Content Automation` |
| **Description** | `Weekly Wellthlab Shopify social drafts — scripts, carousels, Canva/Remotion briefs. Does not post.` |

### Step 3: Choose trigger

1. Click **Add trigger**
2. Select **On a schedule**
3. Choose **Every week** → **Sunday** → **9:00 AM**  
   (Or **Custom cron**: `0 9 * * 0`)

### Step 4: Connect your repo

1. Find **Repository** or **Git** settings on the automation form
2. Select repo: **`colindmurphy0409-hash/amazon-affilate-blog`**
3. Branch: **`main`**
4. Enable **read and write files** in the repo (if shown)

> **Important:** Push your pipeline files to GitHub first (`workflows/`, `brand/`, `campaigns/`, etc.). The automation only sees what's on `main`, not your local-only files.

### Step 5: Paste the agent prompt

In the big **Instructions** / **Prompt** box, paste everything below:

```
Run Wellthlab weekly content drafting (Phases 1-2 only).

0. Read brand/competitors.yaml — if brands listed, note slugs for user to run "Run competitor research" in Agents Window (Blotato unavailable in cron).
1. Read workflows/trend-research.md — use catalog + campaigns/active.yaml + prior week content + any existing competitor playbooks in content/research/competitors/.
2. Read workflows/weekly-social.md — write content/week-XX/ for current ISO week:
   - social.md (7 scripts with tool tags: blotato | canva | remotion | film)
   - carousels.md
   - canva-briefs.yaml
   - remotion-props.json
   - approval.md (status: draft)
3. Follow brand/assets.md: exact Wellthlab product images only; brand/voice.md for tone.
4. Do NOT post, schedule, or mark approved.
5. Tell the user to review approval.md, then run "Run full trend research" and "Run competitor research" in Agents Window before approving.
```

### Step 6: Save

Click **Save** or **Create**. Toggle **Enabled** on if it's off.

---

## Part B — Optional: Monday growth brief

Repeat Part A with these differences:

| Field | Value |
|-------|--------|
| **Name** | `Monday Wellthlab Growth Brief` |
| **Schedule** | Every **Monday** 9:00 AM (`0 9 * * 1`) |
| **Prompt** | See bottom of this file |

---

## What automations do vs what you still do in chat

```
SUNDAY (automation)     →  Writes draft files to content/week-XX/
MONDAY (automation)     →  Writes growth-brief.md (optional)

YOU in Agents Window:
  "Run competitor research"   →  Blotato studies brands you fed in
  "Run full trend research"   →  Trend brief + hooks
  Review approval.md
  "Approve week XX"
  "Produce week XX"           →  Canva MCP, Remotion, Blotato
  "Schedule week XX queue"    →  Blotato posting
```

**Why the split?** Canva and Blotato MCP only work in the interactive Agents chat (where you OAuth'd Canva). Scheduled automations can't call those tools from project config.

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Automation runs but writes nothing | Commit + push `workflows/`, `brand/`, `campaigns/` to `main` |
| Blank form when agent "opens" automation | Ignore — build manually using this guide |
| Agent doesn't know Wellthlab rules | Ensure `AGENTS.md` and `.cursor/skills/` are pushed |
| Want competitor research on schedule | Run it yourself Monday after Sunday draft, or add brands to `brand/competitors.yaml` and say "Run competitor research" |

---

## Monday prompt (copy/paste)

```
Run workflows/growth-brief.md.

Read kpi/weekly-template.csv, campaigns/active.yaml, products/catalog.yaml.
Write content/week-XX/growth-brief.md for current ISO week.
Under 400 words. Note if KPI data is empty.
```
