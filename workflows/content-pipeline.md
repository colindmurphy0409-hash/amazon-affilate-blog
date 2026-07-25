# Wellthlab Content Pipeline (Master)

## Trigger phrases
- **"Run Wellthlab content pipeline"** — full loop with approval pause
- **"Run full trend research"** — Phase 0–1 (competitors + Blotato sources)
- **"Run competitor research"** — Phase 0 only (`brand/competitors.yaml`)
- **"Run weekly social workflow"** — Phase 2 only
- **"Approve week XX"** — unlock Phase 4
- **"Schedule week XX queue"** — dry-run + Blotato schedule

## Phases

```
Phase 0  competitor-research.md   → content/research/competitors/{slug}.md (from brand/competitors.yaml)
Phase 1  trend-research.md       → content/research/week-XX/trend-brief.md
Phase 2  weekly-social.md        → social.md, carousels.md, canva-briefs.md, remotion-props.json, approval.md
Phase 3  YOU review approval.md → say "approve week XX"
Phase 4  produce-and-queue.md    → Blotato | Canva | Remotion | film → posts/queue.yaml → schedule
```

## Production tool picker

| Post type | Tool |
|-----------|------|
| Fast AI carousel / slideshow | **Blotato** (`tool: blotato`) |
| On-brand carousel / thumbnail | **Canva** (agent via API or browser — user never manual) |
| Hook-text Reel, no face | **Remotion** HookReel (`tool: remotion`) |
| Product montage | **Remotion** ProductMontage |
| Education tips video | **Remotion** EducationStrip |
| Talking-head / POV | **Film** + Higgsfield scenes (`tool: film`) |

## Weekly mix (7 posts)
- 2 UGC Reels (film)
- 1 Remotion hook reel
- 1 Canva carousel
- 1 Blotato carousel
- 1 education post
- 1 bundle / social-proof post

## Non-negotiables
- Brand: **Wellthlab** (wellthlab.shop)
- **Exact product images only** — official Shopify CDN URLs; never AI-generate, illustrate, or hallucinate products (`brand/assets.md`)
- **On-brand colors and tone** — `brand/canva.md`, `brand/voice.md`
- FDA structure/function claims only; include disclaimer on supplement captions
- No fabricated reviews or social proof
- Nothing posts or schedules until `approval.md` is approved

## Related workflows
- `workflows/competitor-research.md`
- `workflows/trend-research.md`
- `workflows/weekly-social.md`
- `workflows/canva-production.md`
- `workflows/remotion-render.md`
- `workflows/produce-and-queue.md`
- `workflows/growth-brief.md` (Monday KPI brief)
- `workflows/sync-catalog.md` (before each content batch)

## Stack reference
See `tools/stack.md` for Blotato, Canva, Remotion, Higgsfield roles.
