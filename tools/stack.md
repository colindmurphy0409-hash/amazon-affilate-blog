# Wellth Lab Amazon Affiliate — content stack

## Tools

| Tool | Role |
|------|------|
| **Cursor (this project)** | Content, ASIN research, SEO, validation, deploy |
| **Astro** | Static affiliate landing pages (`site/`) |
| **Vercel** | Host + auto-deploy from GitHub |
| **Amazon Associates** | Affiliate tracking + commission reporting |

## Live site

**https://amazon-affilate-blog.vercel.app**

Future custom domain: `wellthlab.blog` (not connected yet)

## Weekly pipeline

```
Cursor → research + draft content
        ↓
Update ASINs + images in site/data/ and site/public/images/products/
        ↓
run affiliate-validate → run affiliate-build
        ↓
Push to GitHub → Vercel auto-deploy
        ↓
Track in kpi/affiliate-weekly-template.csv
```

## Priorities

1. **Set Associates tag** — `affiliate/config.yaml` (`wellthlab-20`)
2. **One niche cluster** — 3+ interlinked pages before expanding
3. **Validate every page** — `run affiliate-validate` before go-live
4. **Track weekly** — `kpi/affiliate-weekly-template.csv`

## What to tell Cursor each week

- `Run affiliate weekly content` → research → draft → page
- `Build affiliate landing page for {topic}` → single page pipeline
- `Publish affiliate page` → pre-deploy checklist
