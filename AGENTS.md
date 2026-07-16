# Amazon Affiliate Marketing Team

This repo is **only** the Amazon affiliate blog at https://amazon-affilate-blog.vercel.app — product reviews, roundups, and comparisons.

## ⛔ NEVER — accounts (every agent, every task)

**ONLY GitHub / Vercel / git:** `colindmurphy0409-hash` / `colindmurphy0409@gmail.com`  
**Git remote:** `git@github.com:colindmurphy0409-hash/amazon-affilate-blog.git`

**User confirmed correct GitHub — Jul 16, 2026.** Do not instruct logout unless asked.

| Never | Instead |
|-------|---------|
| Use or suggest any other GitHub account | Use `colindmurphy0409-hash` only |
| Run `vercel login` on Colin's PC | Push to `main`; Vercel auto-deploys |
| Name wrong/banned GitHub accounts to Colin | Say **"wrong account"** only — never spell other usernames |
| Tell Colin to log out of GitHub/Vercel/Cursor | Only if Colin explicitly asks |

Full rule: `.cursor/rules/wellthlab-accounts-only.mdc`. Deploy context: `HANDOFF.md`.

## Start here

For full pipelines, use the **amazon-affiliate-orchestrator** skill.

Trigger phrases:
- "Launch affiliate page for {topic}"
- "Run full affiliate workflow"
- "Amazon affiliate team"

## Team roster

| Role | Skill | When to use |
|------|-------|-------------|
| Team lead | `amazon-affiliate-orchestrator` | End-to-end page launches |
| Product research | `amazon-product-research` | Niche ideas, ASIN shortlists |
| Content writer | `amazon-content-writer` | Reviews, roundups, comparisons |
| Landing pages | `amazon-landing-pages` | Astro page scaffolding |
| On-page SEO | `amazon-seo` | Titles, meta, schema, links |
| SEO strategy | `amazon-seo-master` | Clusters, calendars, topical maps |
| CRO | `amazon-cro` | CTA layout, conversion audits |
| Compliance | `amazon-compliance` | FTC + Amazon rules (required gate) |
| Link builder | `amazon-link-builder` |
| Vercel deploy | `vercel-deploy` | Deploy + domain setup |

## Orchestrator decision tree

```
New page request?
├── Unknown niche → amazon-product-research
├── Need keyword plan → amazon-seo-master
├── Write content → amazon-content-writer
├── Build URLs → amazon-link-builder
├── Create Astro page → amazon-landing-pages
├── SEO pass → amazon-seo
├── CRO pass → amazon-cro
├── Compliance gate → amazon-compliance (required)
└── Validate → scripts/validate_affiliate_page.py → deploy
```

## File conventions

| Asset | Path |
|-------|------|
| Associates config | `affiliate/config.yaml` (gitignored) |
| Config template | `affiliate/config.example.yaml` |
| Disclosure copy | `affiliate/disclosure.md` |
| ASIN research | `affiliate/asins/{ASIN}.yaml` |
| Affiliate links | `affiliate/links/{ASIN}.txt` |
| Content drafts | `content/affiliate/{type}/{slug}.md` |
| Published content | `site/src/content/affiliate/{slug}.md` |
| Keyword clusters | `seo/affiliate-keywords.yaml` |
| Weekly KPIs | `kpi/affiliate-weekly-template.csv` |

## Workflows

| Say in chat | Workflow file |
|-------------|---------------|
| "Run affiliate product research" | `workflows/affiliate-product-research.md` |
| "Build affiliate landing page for {topic}" | `workflows/affiliate-landing-page.md` |
| "Publish affiliate page" | `workflows/affiliate-publish-checklist.md` |
| "Run affiliate weekly content" | `workflows/affiliate-weekly-content.md` |

## Commands

```bat
run affiliate-link B0XXXXXX   REM build one affiliate URL
run affiliate-link --all      REM build all ASIN links
run affiliate-validate        REM compliance + SEO checks
run affiliate-dev             REM Astro dev server
run affiliate-build           REM production build
```

## Compliance gate

No page ships without:
1. `amazon-compliance` skill checklist passed
2. `python scripts/validate_affiliate_page.py` exits 0
3. `published: true` in frontmatter only after both pass
