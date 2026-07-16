# Wellth Lab — Amazon Affiliate Blog

**Live site:** [amazon-affilate-blog.vercel.app](https://amazon-affilate-blog.vercel.app)

Research-backed Amazon product reviews, roundups, and comparisons. Astro static site deployed on Vercel.

## Run this (Windows)

```bat
run install              REM once — Python deps
run affiliate-install    REM once — npm deps in site/
run affiliate-link --all REM build affiliate URLs from ASINs
run affiliate-validate   REM compliance + SEO checks
run affiliate-dev        REM preview at localhost:4321
run affiliate-build      REM build to site/dist/
```

Full guide: [OPERATE.md](OPERATE.md) · Team roster: [AGENTS.md](AGENTS.md) · Session handoff: [HANDOFF.md](HANDOFF.md)

## Weekly loop

1. **Cursor** — "Run affiliate weekly content" or "Build affiliate landing page for {topic}"
2. **Validate** — `run affiliate-validate`
3. **Build** — `run affiliate-build`
4. **Deploy** — push to GitHub → Vercel auto-deploys

Copy `affiliate/config.example.yaml` → `affiliate/config.yaml` and set your Amazon Associates tracking ID.

## Project layout

```
site/                    Astro affiliate site (Vercel root = site/)
affiliate/               Associates config + ASIN research
content/affiliate/       Content drafts (reviews, roundups)
seo/affiliate-keywords.yaml   Keyword clusters
scripts/                 Validation + link builder
AGENTS.md                Specialist team + skills
OPERATE.md               How to run everything
HANDOFF.md               Accounts, URLs, session context
```

## In Cursor chat

| Say | I run |
|-----|-------|
| "Run affiliate weekly content" | Full content pipeline |
| "Build affiliate landing page for {topic}" | New page workflow |
| "Publish affiliate page" | Pre-deploy checklist |
| `run affiliate-validate` | Compliance + SEO checks |
| `run affiliate-build` | Production build |
