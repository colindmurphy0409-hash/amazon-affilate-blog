# Wellth Lab Affiliate — ONE setup only

Paste into a new chat: **"Read HANDOFF.md and continue from here."**

## THE ONLY THINGS THAT EXIST

| What | Exact name |
|------|------------|
| **GitHub account** | `colindmurphy0409-hash` / `colindmurphy0409@gmail.com` |
| **GitHub repo** | `amazon-affilate-blog` (one **f** in affilate — typo is intentional) |
| **Vercel team** | `murph1` (Hobby plan; team label may show **murph**) |
| **Vercel project** | `amazon-affiliate-blog` (two **f**'s in affiliate — this is the ONLY project) |
| **Live URL** | https://wellthlab.blog |
| **Vercel fallback URL** | https://amazon-affiliate-blog.vercel.app |
| **Domain (Hostinger)** | `wellthlab.blog` |
| **Amazon tag** | `wellthlab-20` |
| **Code on PC** | `C:\Users\mindb\.cursor\amazon-affiliate-blog` |

## Name mismatch (important)

| Layer | Spelling | Notes |
|-------|----------|-------|
| GitHub repo | `amazon-affilate-blog` | one **f** |
| Vercel project | `amazon-affiliate-blog` | two **f**'s |

Same English Wellth Lab site. Different spellings on GitHub vs Vercel. **Vercel auto-deploy from GitHub push does not work reliably** because of this wiring. Use **GitHub Actions** (see Deploy section below).

## DELETE / IGNORE (past mess)

| Kill it | Why |
|---------|-----|
| Any **mindbodywallet** GitHub or Vercel login | Not Colin's account |
| Repo **`wellthlab-marketing`** (if exists) | Old Shopify mess |
| Instructions to find a second Vercel project | Only one project exists |

---

## Vercel UI (verified Jul 16, 2026)

**Do not ask Colin for Vercel screenshots again. Do not send him through Settings menus.**

### Accounts

- Log in as **colindmurphy0409-hash** / **murph1** team — not mindbodywallet.

### Inside project `amazon-affiliate-blog`

**Left sidebar (verified):**

- Overview
- Deployments
- Logs
- Analytics
- Speed Insights
- Observability
- Firewall
- Cron
- Environment Variables
- **Domains** ← add custom domains here
- Connect (Beta)
- Integrations
- Storage
- **Settings**
- Usage
- Billing

**There is NO "Projects" in this sidebar.** "Projects" only appears on the team home screen (click **murph1** top-left → back to team view).

### Domains page (verified)

- **Direct URL:** https://vercel.com/murph1/amazon-affiliate-blog/domains
- Button: **Add Existing** (not "Save" on add modal)
- Edit modal uses **Save** / **Update**
- **wellthlab.blog** — Valid Configuration, Production
- **amazon-affiliate-blog.vercel.app** — Valid Configuration, Production

### Deployments page (verified)

- **Direct URL:** https://vercel.com/murph1/amazon-affiliate-blog/deployments
- Top row filters: All Branches, All Authors, All Environments, Select Date Range, Status
- **NO "Create Deployment" button** anywhere on this page
- Each row has **⋯** menu on the far right
- Reload page: **Ctrl + R** (F5 may change screen brightness on Colin's keyboard)

### Settings — what exists vs what does NOT

**Project Settings** (click Settings in left sidebar inside project):

- Colin reports **NO Git** item visible there.

**Team Settings** (wrong place — opens if you use broken Git URL):

- Shows **murph** / Hobby, General, Billing, Build and Deployment, Domains, Members, etc.
- Bottom sections: Transfer, Leave Team, Delete Team
- **NO Git** here either — this is team-level, not project-level

**Broken URL (do not use):**

- https://vercel.com/murph1/amazon-affiliate-blog/settings/git → lands on **Team Settings**, not Git

### NEVER tell Colin to look for

- Settings → Domains
- Settings → Git
- Create Deployment button
- Projects (when already inside a project)
- Vercel CLI login (wrong-account OAuth popups)

---

## Hostinger DNS (verified for wellthlab.blog)

| Type | Name | Content/Value | TTL |
|------|------|---------------|-----|
| A | `@` | `216.198.79.1` | 14400 |
| TXT | `_vercel` | `vc-domain-verify=wellthlab.blog,705572af491f99483000` | 14400 |

Legacy IP `76.76.21.21` still worked during propagation; Vercel recommends `216.198.79.1`.

Hostinger field names: **Type, Name, Value, TTL** (table shows **Content**).

---

## Deploy (GitHub Actions — no Vercel menus)

**Problem:** Pushes to GitHub (`ddfb6e1`, `75bbf69`, etc.) did not trigger new Vercel deployments. Latest Vercel build stuck at `f5a1e2d` ("Affiliate-only cleanup") while site still showed old air fryer placeholders.

**Solution:** `.github/workflows/deploy-vercel.yml` deploys on every push to `main` using Vercel CLI + project name + team slug. **Only one secret required:** `VERCEL_TOKEN`.

### One-time setup (direct URLs only)

1. **Create Vercel token:** https://vercel.com/account/tokens  
   - Name it `github-deploy`, copy the token.

2. **Add GitHub secret:** https://github.com/colindmurphy0409-hash/amazon-affilate-blog/settings/secrets/actions  
   - New secret → Name: `VERCEL_TOKEN` → paste token → Add secret.

3. **Re-run deploy:** https://github.com/colindmurphy0409-hash/amazon-affilate-blog/actions/workflows/deploy-vercel.yml  
   - Click **Run workflow** → branch `main` → Run workflow.

After success, hard-refresh https://wellthlab.blog with **Ctrl + Shift + R**.

### Optional secrets (NOT required with current workflow)

`VERCEL_ORG_ID` and `VERCEL_PROJECT_ID` were used in an older workflow version. Current workflow uses `vercel link --project=amazon-affiliate-blog --scope=murph1` instead. IDs can be fetched later with token via API if needed.

---

## Site content (Jul 16, 2026)

Four published guides (tag `wellthlab-20` on all links):

| Guide | Type | Category |
|-------|------|----------|
| `/tymo-curlpro-review` | Review | Beauty |
| `/meridian-trimmer-review` | Review | Beauty |
| `/whoop-peak-vs-galaxy-watch-8` | Comparison | Fitness |
| `/renpho-morphoscan-vs-withings-body-smart` | Comparison | Home |

Old air fryer guides unpublished (`published: false`).

---

## SSH

`git@github.com:colindmurphy0409-hash/amazon-affilate-blog.git`

## DO NOT

- Run Vercel CLI login on Colin's PC (wrong account popups)
- Use mindbodywallet anything
- Guess Vercel menu paths — use direct URLs in this file only
- Ask Colin for Vercel UI screenshots we already documented above
