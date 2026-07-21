# SEO foundation — wellthlab.blog

One-time setup for Google Search Console and analytics. Agents reference this file; Colin only needs the verified steps below.

## Already in the codebase

| Item | Location |
|------|----------|
| Canonical domain | `site/astro.config.mjs` → `site: 'https://wellthlab.blog'` |
| XML sitemap | Auto-generated at `/sitemap-index.xml` via `@astrojs/sitemap` |
| robots.txt | `site/public/robots.txt` |
| Vercel Analytics | `@vercel/analytics` in `SiteAnalytics.astro` (enable in Vercel dashboard) |
| Google verification meta | Set `PUBLIC_GOOGLE_SITE_VERIFICATION` in Vercel env vars |

## Step 1 — Google Search Console (Colin, one action)

1. Open [Google Search Console](https://search.google.com/search-console)
2. **Add property** → **URL prefix** → `https://wellthlab.blog`
3. Choose **HTML tag** verification
4. Copy the `content="..."` value from the meta tag Google gives you
5. In Vercel → **amazon-affiliate-blog** → **Settings** → **Environment Variables**:
   - Name: `PUBLIC_GOOGLE_SITE_VERIFICATION`
   - Value: paste the content value only (not the full tag)
   - Environment: Production
6. Redeploy (push to `main` or redeploy latest in Vercel)
7. Back in Search Console → **Verify**
8. **Sitemaps** → submit: `https://wellthlab.blog/sitemap-index.xml`

## Step 2 — Request indexing for live pages

After verification, use **URL Inspection** for each published guide:

- `https://wellthlab.blog/meridian-trimmer-review`
- `https://wellthlab.blog/tymo-curlpro-review`
- `https://wellthlab.blog/renpho-morphoscan-vs-withings-body-smart`
- `https://wellthlab.blog/whoop-peak-vs-galaxy-watch-8`
- New pages as they publish (e.g. immersion blender roundup)

Click **Request indexing** once per URL.

## Step 3 — Enable Vercel Analytics (optional, recommended)

1. Vercel → **amazon-affiliate-blog** → **Analytics** tab
2. Enable Web Analytics (Hobby plan includes basic analytics)
3. Sessions appear in dashboard within 24h of first visit

## Weekly KPI tracking

Log in `kpi/affiliate-weekly-template.csv`:

```csv
date,sessions,amazon_clicks,ctr_pct,new_pages,top_page,niche,notes
```

- **Sessions**: Vercel Analytics or GA4
- **Amazon clicks**: Amazon Associates → Reports → Link Type Report

## After each new publish

1. Push to `main` (auto-deploy)
2. GSC → URL Inspection → new slug → Request indexing
3. Update `seo/affiliate-keywords.yaml` status to `published`
4. Add KPI row for the week
