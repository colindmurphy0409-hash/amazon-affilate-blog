# Competitor & Inspiration Brand Research

## Trigger
- **"Run competitor research"** — research all brands in `brand/competitors.yaml` (up to `max_brands_per_run`)
- **"Research competitor {slug or name}"** — one brand only
- **"Add competitor {name}"** — append to `brand/competitors.yaml`, then run research
- Runs automatically as **Phase 0** inside **"Run full trend research"** when `brand/competitors.yaml` has entries

## Goal

Study top brands the user feeds in. **Mimic their marketing mechanics** (hooks, pacing, carousel arcs, video beats, CTA placement) and **transform** them into Wellthlab voice, products, and exact Shopify imagery.

This is format adaptation — not copying scripts, claims, or visuals.

## Prerequisites

1. Read `brand/competitors.yaml` — user-maintained list of brands to watch
2. Read `brand/voice.md`, `brand/assets.md`, `brand/canva.md`
3. Read `campaigns/active.yaml` → map adaptations to `current_focus` products
4. Read `products/catalog.yaml` — only promote real Wellthlab SKUs

## Instructions

### 1. Select brands

- If user named a brand → match by `slug` or `name`
- Else → pick up to `research_settings.max_brands_per_run` by `priority` (high first)
- Skip brands with a playbook updated within `refresh_after_days` unless user says **force refresh**

### 2. Research each brand (Agents Window + Blotato MCP)

For each brand, gather:

| Source | Tool | What to extract |
|--------|------|-----------------|
| TikTok / Reels URLs in `urls` | Blotato `create_source` (`tiktok`) | Hook (first 3 sec), structure, text-on-screen, audio, CTA |
| YouTube ads / explainers | Blotato `create_source` (`youtube`) | Narrative arc, proof style, pacing |
| Handles without URLs | Blotato `create_source` (`perplexity-query`) | Recent post formats, hook patterns, content mix |
| Brand site / landing page | Blotato `create_source` (`article`) or web fetch | Offer framing, trust signals, hero angles |

**customInstructions** (use on every source):

```
Extract MARKETING MECHANICS only: hook templates, video/carousel structure, visual format,
pacing, CTA style, content pillars, posting patterns. Do NOT return verbatim ad copy to reuse.
Flag anything that would be non-compliant for supplement structure/function claims.
Output bullet lists agents can adapt to a different brand (Wellthlab oral strips).
```

Optional: Blotato `list_top_posts` if researching a connected account (usually competitors won't be connected — use URLs + perplexity).

### 3. Write brand playbook

Save `content/research/competitors/{slug}.md`:

```markdown
# {Brand Name} — Marketing Playbook (adaptation source)

**Researched:** {date}
**Category:** ...
**Why we watch:** (from competitors.yaml)

## What they do well (mechanics)
- Hook patterns (template form, not their exact words)
- Video / Reel formats (beats, duration, text placement)
- Carousel / static formats
- CTA and offer framing
- Visual style (lighting, UGC vs polished — no copying their product shots)

## Patterns to adapt for Wellthlab
| Their pattern | Wellthlab translation | Product | Tool |
|---------------|----------------------|---------|------|
| e.g. "POV problem hook" | "POV: 3pm slump unless..." | Energy Strips | remotion |
| ... | ... | ... | blotato/canva/film |

## Do NOT copy
- Their product imagery, packaging, or claims
- Verbatim hooks or trademarked phrases
- Their social proof / reviews

## Sample adapted hooks (original copy for Wellthlab)
1. ...
2. ...
3. ...

## Sources
- [URLs, Blotato source IDs, handles]
```

### 4. Synthesize for the week

Append or merge into `content/research/week-XX/trend-brief.md`:

```markdown
## Adapted from competitor research
- {Brand}: {1-line mechanic} → Wellthlab hook template
- ...

## Competitor playbooks used
- content/research/competitors/{slug}.md
```

## Rules

- **Wellthlab brand only** in adapted copy — see `brand/voice.md`
- **Exact Wellthlab product images only** in any production brief — see `brand/assets.md`
- Borrow **structure**, not **script** — rewrite every hook and caption
- No fabricated stats, reviews, or "as seen on" from competitor brands
- FDA structure/function framing for supplement content; include disclaimer where needed
- If a competitor makes disease claims, note as **do not emulate**

## User workflow (feeding brands)

1. Edit `brand/competitors.yaml` — add name, handles, TikTok/IG URLs, `why_watch`
2. Say **"Run competitor research"** (or name one brand)
3. Review playbooks in `content/research/competitors/`
4. Say **"Run weekly social workflow"** — scripts must cite adapted patterns from playbooks + trend brief

## Example chat

```
Add competitor Ryse Energy — TikTok @ryse — study their hook Reels and CTA style.

Run competitor research for ag1.

Run full trend research
```
