---
name: wellthlab-content-orchestrator
description: >-
  End-to-end Wellthlab DTC social content pipeline: trend research, weekly scripts,
  Blotato/Canva/Remotion/Higgsfield production, approval gate, and Blotato scheduling.
  Use for "Run Wellthlab content pipeline", weekly social batching, trend research,
  producing approved week content, or scheduling the post queue.
---

# Wellthlab Content Orchestrator

Head of social content for **Wellthlab** (wellthlab.shop). Runs the 4-phase pipeline in `workflows/content-pipeline.md`.

## Trigger phrases
- "Run Wellthlab content pipeline"
- "Research trends and write this week's social content"
- "Run full trend research"
- "Run competitor research" / "Research competitor {slug or name}"
- "Add competitor {name}" → update brand/competitors.yaml, then research
- "Run weekly social workflow"
- "Approve week XX" / "Produce approved week XX"
- "Schedule week XX queue"

## Decision tree

```
Request?
├── User feeds brands → brand/competitors.yaml
├── Competitor playbooks missing/stale → workflows/competitor-research.md
├── No trend brief → workflows/trend-research.md
├── No week scripts → workflows/weekly-social.md (reads trend brief)
├── approval.md status != approved → STOP; point user to content/week-XX/approval.md
├── Approved + blotato briefs → produce-and-queue (Blotato visuals)
├── Approved + canva briefs → Canva MCP (create, autofill, export)
├── Approved + remotion props → python scripts/render_week.py --week XX
├── Approved + UGC → write higgsfield-prompts.md; wait for posts/media/ files
└── Assets ready → schedule_queue.py --dry-run then schedule
```

## Production tools

| Tool | When | Workflow |
|------|------|----------|
| Blotato | Fast AI carousels | produce-and-queue.md |
| Canva | Branded carousels via **Canva MCP** | canva-production.md |
| Remotion | Hook Reels, montages, education clips | remotion-render.md |
| Higgsfield + phone | UGC scenes (never AI products) | higgsfield-prompts.md |

## Non-negotiables
1. Brand: **Wellthlab** — never "Wealth Lab"
2. **Exact product images only** — official Shopify CDN URLs from catalog/briefs; never AI-generate, illustrate, or hallucinate product packaging or labels (`brand/assets.md`)
3. **On-brand always** — colors from `brand/canva.md`; tone from `brand/voice.md`
4. FDA structure/function claims only; disclaimer on supplement captions
5. No fabricated reviews or social proof
6. **Nothing posts or schedules until approval.md is approved**

## Key paths
- Competitor feed: `brand/competitors.yaml`
- Competitor playbooks: `content/research/competitors/{slug}.md`
- Trend brief: `content/research/week-XX/trend-brief.md`
- Week bundle: `content/week-XX/` (social, carousels, canva-briefs, remotion-props, approval)
- Queue: `posts/queue.yaml`
- Media: `posts/media/`
- Brand kit: `brand/voice.md`, `brand/canva.md`
- Catalog: `products/catalog.yaml`

## Commands
```bat
python scripts/sync_catalog.py
python scripts/canva_connect.py connect --client-id ID --client-secret SECRET
python scripts/canva_connect.py test
python scripts/canva_produce.py --week XX --brief {id} --dry-run
python scripts/canva_produce.py --week XX --brief {id}
python scripts/render_week.py --week XX
python scripts/schedule_queue.py --dry-run
python scripts/schedule_queue.py
```
