---
name: vercel-deploy
description: >-
  Deploys the Astro affiliate site to Vercel without failed builds. Use when
  deploying to Vercel, importing GitHub repos, fixing Vercel build errors, or
  guiding users through first-time Vercel setup for this project.
---

# Vercel Deploy (Amazon Affiliate Blog)

## Hard rules — never violate

1. **Never tell the user to Deploy with blank Root Directory** if the import/configure screen shows an editable Root Directory field. Set `site` first.
2. **Never redeploy a failed build** without fixing Root Directory or `vercel.json` first.
3. **Never assume** Settings → General has Root Directory. It is under **Settings → Build and Deployment** on some accounts, or only on the **import screen**.
4. **GitHub account on Vercel must match** the account that owns the repo. If Vercel only shows `colindmurphy0409-hash` projects, code must be on that GitHub account — not a different account.
5. **`vercel.json` at repo root is a fallback**, not a substitute for telling users to set Root Directory to `site` when they can.

## Why builds fail on this repo

| Symptom | Cause | Fix |
|---------|-------|-----|
| Python entrypoint error | `requirements.txt` at repo root; Vercel detects Python | Root Directory = `site` OR `vercel.json` buildCommand |
| Missing affiliate config | Vercel root `site` cannot read `../affiliate/` | Config lives in `site/data/affiliate-config.yaml` |
| Empty Deployments at account level | User on team Deployments, not inside project | Projects → click project → Deployments |
| Repo not in import list | Wrong GitHub account connected to Vercel | Push to connected account or grant Vercel access |

## First deploy checklist (give user IN THIS ORDER)

```
- [ ] 1. Code pushed to GitHub account that Vercel can see
- [ ] 2. vercel.com/new → Import amazon-affilate-blog
- [ ] 3. Root Directory → Edit → type: site
- [ ] 4. Framework: Astro (auto)
- [ ] 5. Deploy (only after step 3)
- [ ] 6. Green Ready → Visit
- [ ] 7. Top nav → **Domains** → Add Existing → `wellthlab.blog` (NOT Settings → Domains)
- [ ] 8. Hostinger DNS records from Vercel
```

## User instructions template (copy this)

**On the import screen, before Deploy:**
1. Click **Edit** next to Root Directory
2. Type: `site`
3. Click **Deploy**

Do not skip step 2.

## If Root Directory field does not exist

Repo root `vercel.json` with `cd site` **conflicts** when Root Directory is already `site`. Use one or the other, not both.

```json
{
  "buildCommand": "cd site && npm install && npm run build",
  "outputDirectory": "site/dist",
  "installCommand": "cd site && npm install",
  "framework": null
}
```

Tell user: leave blank only in this case, then Deploy.

## Custom domain (wellthlab.blog)

**Never say Settings → Domains** for this user. Their Project Settings sidebar has General, Build and Deployment, Git, etc. — **no Domains item**.

### Where Domains actually is

1. Open the project → click **Domains** in the **top nav bar** (Overview | Deployments | … | **Domains** | Settings)
2. Or direct URL: `https://vercel.com/murph/amazon-affilate-blog/domains`
3. Click **Add Existing** → type `wellthlab.blog`

### After adding domain

- **Connect to environment → Production** (NOT redirect to www)
- Hostinger DNS: A `@` → `76.76.21.21`, CNAME `www` → `cname.vercel-dns.com`
- "Invalid Configuration" until DNS propagates — normal

## After deploy

1. Add domain via **Domains tab** (not Settings)
2. Copy DNS to Hostinger
3. Submit `https://wellthlab.blog` to Amazon Associates

## Anti-patterns (learned from failures)

- ❌ "Deploy with blank root directory" when field is visible on import screen
- ❌ "Redeploy" before fixing root directory
- ❌ Sending user to Settings → General for Root Directory
- ❌ Pushing code to `mindbodywallet1-dotcom` when Vercel uses `colindmurphy0409-hash`
- ❌ Contradicting prior advice in the same session

## Agent self-check before any deploy advice

Ask yourself:
1. Can the user edit Root Directory on their current screen? → If yes, insist on `site` before Deploy.
2. Did the last deploy fail with Python error? → Root Directory or vercel.json not applied.
3. Is the user on account Deployments (empty) vs project Deployments? → Redirect to Projects → click project.
