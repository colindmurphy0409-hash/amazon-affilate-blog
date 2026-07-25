# Weekly Social Content Batch

## Trigger
Run every Sunday, or on demand: **"Run weekly social workflow"**

## Prerequisites
- Read `content/research/week-XX/trend-brief.md` if it exists (hooks must come from trend brief)
- Read `content/research/competitors/*.md` playbooks — adapt formats, rewrite all copy for Wellthlab
- Read `brand/voice.md`, `brand/assets.md`, `products/catalog.yaml`, and `campaigns/active.yaml`

## Instructions

1. Determine ISO week number XX for output paths
2. Generate 7 days of TikTok/Reels content (one post per day)
3. Prioritize products in `campaigns/active.yaml` → `current_focus`
4. Save outputs:
   - `content/week-XX/social.md` — UGC scripts
   - `content/week-XX/carousels.md` — production briefs with tool tags
   - `content/week-XX/canva-briefs.yaml` — machine-readable autofill payloads for agent Canva production
   - `content/week-XX/canva-briefs.md` — human-readable slide copy (optional mirror)
   - `content/week-XX/remotion-props.json` — render props for Remotion-track Reels
   - `content/week-XX/approval.md` — review checklist (`status: draft`)

## Post structure (social.md)
```
### Day N — [Product] — [Angle]
**Tool:** film | remotion | canva | blotato
**Hook (first 3 sec):** ...
**Script:** ...
**Caption:** ...
**CTA:** [link with utm]
**Shot list:** 1. ... 2. ... 3. ...
**Audio:** trending / original / voiceover
**Pillar:** routine-hacks | clean-science | real-life | social-proof
```

## Carousel brief structure (carousels.md)
```
### Carousel N — [Topic]
**Tool:** blotato | canva | remotion | film
**Template:** (Blotato template name OR Canva template OR Remotion composition)
**Prompt/slides:** ...
**Caption:** ...
**CTA:** wellthlab.shop/...?utm_...
**Status:** draft
```

## Content mix (7 days)
- 2x UGC / filmed Reels (`tool: film`)
- 1x Remotion hook reel (`tool: remotion`, composition: HookReel)
- 1x Canva branded carousel (`tool: canva`)
- 1x Blotato AI carousel (`tool: blotato`)
- 1x education (strips vs pills, stack your day, clean label)
- 1x bundle push or social proof

## remotion-props.json shape
```json
{
  "compositions": [
    {
      "id": "HookReel",
      "output": "posts/media/day-02-energy-hook.mp4",
      "props": {
        "hook": "...",
        "productImage": "energy-strips.png",
        "captionLines": ["...", "..."],
        "cta": "wellthlab.shop"
      }
    }
  ]
}
```

## approval.md template
```markdown
# Week XX — Ready for Review
**Status:** draft

- [ ] 7 scripts (social.md)
- [ ] Production briefs (carousels.md)
- [ ] Canva autofill payloads (canva-briefs.yaml)
- [ ] Remotion props (remotion-props.json)
- [ ] Trend brief cited (research/week-XX/trend-brief.md)

Say **"approve week XX"** to proceed to production.
```

## Rules
- No medical claims beyond catalog benefits
- Include FDA disclaimer in caption when making supplement claims
- Keep hooks under 8 words when possible
- Always mention wellthlab.shop
- Brand name: **Wellthlab** — never "Wealth Lab"
- **Exact product images only** — official Shopify CDN URLs; never AI-generate or hallucinate products (`brand/assets.md`)
- **On-brand colors and tone** — `brand/canva.md`, `brand/voice.md`
