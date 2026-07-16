# How to run this

Amazon affiliate landing pages only. No store sync, no social scheduling — just content → validate → build → deploy.

**Live site:** https://amazon-affilate-blog.vercel.app

## Setup once

```bat
run install
run affiliate-install
```

Copy `affiliate/config.example.yaml` to `affiliate/config.yaml` and set your Amazon Associates tracking ID (`wellthlab-20`).

## Weekly loop

1. **Cursor** — "Run affiliate weekly content" or "Build affiliate landing page for {topic}"
2. **Validate** — `run affiliate-validate`
3. **Build** — `run affiliate-build`
4. **Deploy** — push to GitHub → Vercel auto-deploys from `colindmurphy0409-hash/amazon-affilate-blog`

## Commands

| Command | What it does |
|---------|--------------|
| `run install` | Install Python deps (once) |
| `run affiliate-install` | Install Astro/npm deps in `site/` (once) |
| `run affiliate-link B0XXXXXX` | Build one affiliate URL |
| `run affiliate-link --all` | Build URLs for all ASINs |
| `run affiliate-validate` | Compliance + SEO validation |
| `run affiliate-dev` | Local preview at localhost:4321 |
| `run affiliate-build` | Production build to `site/dist/` |

See [AGENTS.md](AGENTS.md) for the full specialist team and skills.

## Publish checklist

1. Content draft in `content/affiliate/` → published to `site/src/content/affiliate/`
2. ASIN data in `site/data/asins/*.yaml` and `affiliate/asins/*.yaml`
3. Product images in `site/public/images/products/`
4. `run affiliate-validate` exits 0
5. `published: true` in frontmatter only after validation passes
6. Push to GitHub

## In Cursor chat

- "Run affiliate weekly content" → full pipeline
- "Build affiliate landing page for {topic}" → new page
- "Publish affiliate page" → pre-deploy checklist
- `run affiliate-validate` → compliance + SEO
- `run affiliate-build` → production build
