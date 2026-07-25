# Wellth Lab — content stack (DTC + Affiliate)

## Tools

| Tool | Role |
|------|------|
| **Cursor** | Scripts, captions, UTMs, weekly planning, orchestration |
| **Blotato** | AI carousels, schedule + publish TikTok/Instagram |
| **Canva** | Branded carousels — **Canva MCP** (OAuth) |
| **Remotion** | Programmatic hook Reels, product montages (`video/`) |
| **Higgsfield AI** | Lifestyle backdrops only (never AI-generate products) |
| **Astro** | Amazon affiliate landing pages (`site/`) |
| **Vercel** | Host + auto-deploy affiliate site from GitHub |
| **Amazon Associates** | Affiliate tracking + commission reporting |

## Live properties

- **Shopify DTC:** https://wellthlab.shop
- **Affiliate blog:** https://amazon-affilate-blog.vercel.app

---

## DTC weekly pipeline (Shopify Content Automation)

```
Research (trend brief + competitor playbooks)
        ↓
Scripts + briefs (Cursor → content/week-XX/)
        ↓
   ┌────┴────┬──────────┬───────────┐
Blotato   Canva    Remotion   Higgsfield + phone
   └────┬────┴──────────┴───────────┘
        ↓
posts/media/ → posts/queue.yaml → Blotato schedule
```

| Post type | Tool |
|-----------|------|
| Fast AI carousel | Blotato |
| On-brand carousel | Canva MCP |
| Hook Reel (no face) | Remotion HookReel |
| Talking-head / POV | Film + Higgsfield |

```bat
python scripts/sync_catalog.py
python scripts/render_week.py --week XX --dry-run
python scripts/schedule_queue.py --queue posts/queue-week-XX.yaml --dry-run
```

**Cursor each week:** `Run Wellthlab content pipeline` → review → `Approve week XX` → produce & schedule

Setup: `automations/SETUP-GUIDE.md` (**Shopify Content Automation** — Sundays 9am)

---

## Affiliate weekly pipeline

```
Cursor → research + draft content
        ↓
Update ASINs + images in site/data/ and site/public/images/products/
        ↓
run affiliate-validate → run affiliate-build
        ↓
Push to GitHub → Vercel auto-deploy
```

**Cursor each week:** `Run affiliate weekly content` · `Build affiliate landing page for {topic}`

Priorities: set Associates tag · one niche cluster · validate every page · track in `kpi/affiliate-weekly-template.csv`
