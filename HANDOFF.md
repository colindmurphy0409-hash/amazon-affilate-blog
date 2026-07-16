# Wellth Lab Affiliate — ONE setup only

Paste into a new chat: **"Read HANDOFF.md and continue from here."**

---

## ⚠️ WRONG GITHUB LOGIN — STOP IMMEDIATELY

**Correct account ONLY:** `colindmurphy0409-hash` / `colindmurphy0409@gmail.com`  
**NEVER use:** `mindbodywallet`, `mindbodywallet1-dotcom`, or any other GitHub account.

### If an OAuth popup appears (Cursor, Vercel CLI, GitHub, Vercel dashboard)

1. **Check the username shown** before clicking Authorize.
2. If it is **NOT** `colindmurphy0409-hash` → click **Cancel** / **Deny**. Do not proceed.
3. **Never authorize** `mindbodywallet` or `mindbodywallet1-dotcom` — it breaks deploy webhooks and pushes code to the wrong account.

### Vercel ↔ GitHub must both be `colindmurphy0409-hash`

- **GitHub → Settings → Applications → Vercel → Configure** must be authorized as **`colindmurphy0409-hash`**. Wrong account = no webhook, no auto-deploy.
- **Vercel → Account → Authentication → GitHub** must show **`colindmurphy0409-hash`** connected (Step 3 below). Reconnect if it shows any other account.
- **Git remote (verified):** `git@github.com:colindmurphy0409-hash/amazon-affilate-blog.git` — do not change this.

### Log out of wrong GitHub NOW (if wrong account is active)

Open https://github.com/logout, sign out of any `mindbodywallet*` session, then sign in only as **`colindmurphy0409-hash`**. In Cursor: **Settings → Accounts → GitHub → Sign Out**, then sign in again and confirm the popup shows **`colindmurphy0409-hash`**. For Vercel: https://vercel.com/logout → sign in via GitHub as **`colindmurphy0409-hash`** → team **`murph1`**. Clear stale sessions at https://github.com/settings/sessions if needed.

### Agent rules (non-negotiable)

1. **Never use, suggest, or authorize any account other than `colindmurphy0409-hash`.**
2. **Never run `vercel login`** on Colin's PC (OAuth popups → wrong account risk).
3. **Never push to or connect any repo under `mindbodywallet*`.**

---

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

## Name mismatch (cosmetic only — NOT the deploy bug)

| Layer | Spelling | Notes |
|-------|----------|-------|
| GitHub repo | `amazon-affilate-blog` | missing **i** (affil**a**te) |
| Vercel project | `amazon-affiliate-blog` | full word (affil**i**ate) |

Different spellings are fine. Vercel links to a **repo**, not a matching project name. **Auto-deploy is broken because the GitHub ↔ Vercel webhook/link is disconnected**, not because of the spelling.

## DELETE / IGNORE (past mess)

| Kill it | Why |
|---------|-----|
| Any **wrong-account** GitHub or Vercel login | Not Colin's account — use `colindmurphy0409-hash` only |
| Repo **`wellthlab-marketing`** (if exists) | Old Shopify mess |
| Instructions to find a second Vercel project | Only one project exists |

---

## Vercel UI (verified Jul 16, 2026)

**Do not ask Colin for Vercel screenshots again. Do not send him through Settings menus.**

### Accounts

- Log in as **colindmurphy0409-hash** / **murph1** team only.

### Inside project `amazon-affiliate-blog`

**Left sidebar (verified — screenshot Jul 16, 2026):**

- Overview
- Deployments
- Logs
- Environment Variables
- **Domains** ← add custom domains here
- Connect
- Integrations
- CDN
- Firewall
- Observability
- Speed Insights
- Analytics
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
- Each row has **⋯** menu on the far right (typical options: Visit, View Build Logs, Redeploy, Promote to Production on previews — **Redeploy only rebuilds the same old commit; it does not pull new code from GitHub**)
- Reload page: **Ctrl + R** (F5 may change screen brightness on Colin's keyboard)

### Integrations and Connect — NEVER for auto-deploy (verified Jul 16, 2026)

**NEVER send Colin to Integrations or Connect to fix deploy or reconnect Git.** Both are useless for GitHub auto-deploy.

**Deploy fix is GitHub-only:** https://github.com/settings/installations (Step 1 below).

- **Integrations** (left sidebar — **not** "Connections"): third-party **marketplace only**. Direct URL: https://vercel.com/murph1/amazon-affiliate-blog/integrations — screenshot shows **"No Integrations Installed"** and Browse Marketplace. **NOT** GitHub repo connection. **NOT** where Vercel links push → deploy.
- **Connect** (left sidebar, below Domains): Vercel Connect beta for **AI agents / runtime credentials**. Direct URL: https://vercel.com/murph1/amazon-affiliate-blog/connect — installs a **separate** GitHub App for agents, **NOT** the standard push → deploy webhook. **Will not** restore auto-deploy.

**Where git deploy actually lives:** GitHub-side Vercel GitHub App (Step 1) + Vercel account GitHub auth (Step 3). No working **Settings → Git** in Colin's project UI.

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

- **Integrations** or **Connect** to fix deploy (both useless — GitHub-only fix: https://github.com/settings/installations)
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

## Deploy (normal path — no tokens)

**What should happen:** You push to GitHub → Vercel builds automatically. No tokens, no manual deploy.

**What's actually wrong:** GitHub pushes (`ddfb6e1` through `0266649`) never triggered a new Vercel build. Production is stuck at `f5a1e2d` ("Affiliate-only cleanup"). `wellthlab.blog` still shows old air fryer guides. Empty-commit push was tried — still no new deployment row.

**Root cause:** The Vercel GitHub App webhook/link to this repo is broken or missing. Not a repo-name typo.

**Evidence project was connected once:** Deployments page shows past builds from GitHub commits. The link dropped — fix from **GitHub** (Vercel app permissions / webhook), not from Vercel Integrations or Connect.

**Deployments ⋯ menu:** Redeploy only rebuilds the **same old commit** — does not pull new code from GitHub. Not a fix.

### Fix auto-deploy — one step at a time (do only the current step)

**Step 1 — Grant Vercel access to your repo (GitHub side only — no tokens)**

#### What "Configure" actually shows (verified Jul 16, 2026 — screenshot)

Clicking **Configure** on Vercel at https://github.com/settings/installations **does** open the correct GitHub App page. Colin's screenshot is **not** Pinterest, Vercel docs, or a broken/wrong page.

**What Colin sees (bottom of page):**

- `vercel bot commented Apr 14, 2022`
- A deployment table with old projects like `front/next-site/svelte-app` — status **Ready** / **Building**

That is **historical Vercel bot activity** from an old 2022 project. It sits at the **bottom** of the Configure page. **Repository access is above this — scroll up.**

**Common mistake:** clicking the **Vercel** name/link instead of the **Configure** button on the right. Use **Configure** only.

#### Path A — scroll up on the same page (try first)

1. Open: https://github.com/settings/installations  
2. Find **Vercel** → click **Configure** (the button, not the app name)  
3. **Scroll to the top** of the page (Page Up or drag scrollbar up)  
4. Find **Repository access** → choose **Only select repositories**  
5. Check **`colindmurphy0409-hash/amazon-affilate-blog`**  
6. Click **Save**

#### Path B — repo-level installations (if Path A has no Repository access at top)

1. Open: https://github.com/colindmurphy0409-hash/amazon-affilate-blog/settings/installations  
2. Find **Vercel** → **Configure**  
3. Grant access to this repo → **Save**

#### Path C — confirm webhook after access is saved

1. Open: https://github.com/colindmurphy0409-hash/amazon-affilate-blog/settings/hooks  
2. You should see a **Vercel** webhook (URL contains `vercel.com`)  
3. If **no webhook**: repeat Path A or B, or reinstall from https://github.com/apps/vercel

If **Vercel** is not listed on the account installations page: install from https://github.com/apps/vercel for `colindmurphy0409-hash` and grant `amazon-affilate-blog`.

Tell the next chat: *"Step 1 done"* — you'll get Step 2 only (webhooks check if not already done via Path C).

**Step 2 — Confirm Vercel webhook exists** (may already be done in Step 1 Path C)

1. Open: https://github.com/colindmurphy0409-hash/amazon-affilate-blog/settings/hooks  
2. You should see a **Vercel** webhook (URL contains `vercel.com`)  
3. If **no webhook**: repeat Step 1 Path A or B, or reinstall from https://github.com/apps/vercel

Tell the next chat: *"Step 2 done — webhook yes/no"*.

**Step 3 — Reconnect GitHub account on Vercel (account level, NOT project Git)**

**Prerequisite:** Logged into Vercel as **`colindmurphy0409-hash` / team `murph1`**. If OAuth shows **wrong account**, cancel — do not authorize. User confirmed correct GitHub Jul 16, 2026; do not instruct logout unless Colin asks.

1. Open: https://vercel.com/account/settings/authentication  
2. Under **GitHub**, click **Disconnect** (if shown)  
3. Click **Connect** / **Reconnect** → authorize as **`colindmurphy0409-hash`** only  
4. Confirm no **"Errors logging in with GitHub"** banner

Tell the next chat: *"Step 3 done"*.

**Step 4 — Watch for a new deployment**

1. Open: https://vercel.com/murph1/amazon-affiliate-blog/deployments  
2. Press **Ctrl + R** after 60 seconds  
3. Look for a **new top row** (commit message like "Add six-product affiliate guides…" or newer)  
4. When it shows **Ready**, hard-refresh https://wellthlab.blog with **Ctrl + Shift + R**

If Step 4 shows a new deployment → auto-deploy is fixed. Future pushes work with no tokens.

### Trigger deploy without Vercel UI (after Step 1 saves repo access)

No Vercel dashboard navigation needed once GitHub has granted repo access and the webhook exists.

**Option 1 — empty commit (preferred, no tokens):**

```bat
cd C:\Users\mindb\.cursor\amazon-affiliate-blog
git commit --allow-empty -m "Trigger Vercel deploy"
git push origin main
```

Then wait 60s and reload https://vercel.com/murph1/amazon-affiliate-blog/deployments (Ctrl+R). A **new top row** should appear. Empty commit was tried **before** Step 1 was fixed — it failed because the webhook was missing. Retry only **after** Step 1 Save succeeds.

**Option 2 — GitHub Actions (token fallback only):**

Manual **Run workflow** on `.github/workflows/deploy-vercel.yml` — requires `VERCEL_TOKEN` secret (see below). Use only if Option 1 still fails after Steps 1–3.

### If Steps 1–4 fail (token fallback only)

Auto-deploy is still broken on Vercel's side — not normal. Fallback: `.github/workflows/deploy-vercel.yml` (manual **Run workflow** only) needs one secret `VERCEL_TOKEN` from https://vercel.com/account/tokens added at https://github.com/colindmurphy0409-hash/amazon-affilate-blog/settings/secrets/actions — use only if the no-token steps above fail.

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
- Use or mention any GitHub account other than **`colindmurphy0409-hash`** (never name wrong accounts to Colin — say "wrong account" only)
- Instruct logout/re-login unless Colin explicitly asks
- Guess Vercel menu paths — use direct URLs in this file only
- Ask Colin for Vercel UI screenshots we already documented above
