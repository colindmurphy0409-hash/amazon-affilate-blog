---
name: amazon-affiliate-orchestrator
description: >-
  Coordinates the full Amazon Associates pipeline from research through
  publish. Use when launching affiliate pages, running the Amazon affiliate
  team workflow, or coordinating multiple affiliate specialists end-to-end.
---

# Amazon Affiliate Orchestrator

Team lead for the Amazon affiliate operation in this repo. Delegate to
specialist skills; do not skip the compliance gate before publish.

## Pipeline

```
Task Progress:
- [ ] 1. Research niche + ASINs
- [ ] 2. Plan keyword cluster
- [ ] 3. Draft content
- [ ] 4. Build affiliate links
- [ ] 5. Scaffold Astro landing page
- [ ] 6. On-page SEO pass
- [ ] 7. CRO pass
- [ ] 8. Compliance gate
- [ ] 9. Validate + deploy
```

## Step 1 — Research

Read `amazon-product-research` skill. Output:
- `affiliate/niches/{niche}.yaml`
- `affiliate/asins/{ASIN}.yaml` per product

## Step 2 — SEO strategy

Read `amazon-seo-master` skill. Output:
- Cluster entry in `seo/affiliate-keywords.yaml`
- Target slug and primary keyword locked

## Step 3 — Content

Read `amazon-content-writer` skill. Output:
- Markdown draft in `content/affiliate/{type}/{slug}.md`
- Frontmatter: title, description, type, asins, primary_keyword

## Step 4 — Links

Read `amazon-link-builder` skill. Run:
```bash
python scripts/build_affiliate_link.py --all
```

## Step 5 — Landing page

Read `amazon-landing-pages` skill. Ensure Astro content collection picks up
the new markdown file in `site/src/content/affiliate/`.

## Step 6 — SEO

Read `amazon-seo` skill. Verify title, meta, H1, schema, internal links.

## Step 7 — CRO

Read `amazon-cro` skill. Verify above-fold hook, CTAs, trust signals.

## Step 8 — Compliance

Read `amazon-compliance` skill. Must pass before publish. No exceptions.

## Step 9 — Validate + deploy

Read `vercel-deploy` skill before any Vercel guidance.

```bash
python scripts/validate_affiliate_page.py
cd site && npm run build
```

Deploy via Vercel:
1. Import screen → Root Directory = `site` **before** first Deploy
2. See `vercel-deploy` skill for domain + DNS steps

## Specialist map

| Task | Skill |
|------|-------|
| ASIN / niche research | `amazon-product-research` |
| Keyword clusters | `amazon-seo-master` |
| Reviews, roundups | `amazon-content-writer` |
| Affiliate URLs | `amazon-link-builder` |
| Astro pages | `amazon-landing-pages` |
| On-page SEO | `amazon-seo` |
| Conversions | `amazon-cro` |
| FTC + Amazon rules | `amazon-compliance` |

## File conventions

| Asset | Location |
|-------|----------|
| Config | `affiliate/config.yaml` (gitignored) |
| ASIN data | `affiliate/asins/{ASIN}.yaml` |
| Links | `affiliate/links/{ASIN}.txt` |
| Content drafts | `content/affiliate/{type}/{slug}.md` |
| Published pages | `site/src/content/affiliate/` (symlinked or copied) |
| Keywords | `seo/affiliate-keywords.yaml` |

## Trigger phrases

- "Launch affiliate page for {topic}"
- "Run full affiliate workflow"
- "Amazon affiliate team"
