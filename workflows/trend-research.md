# Trend Research

## Trigger
- Every Sunday before content drafting, or on demand: **"Run full trend research"**
- Partial (catalog-only): runs inside Sunday Cursor Automation

## Phase 0 — Competitor brands (when configured)

If `brand/competitors.yaml` has entries, run `workflows/competitor-research.md` first:

1. Research fed brands → `content/research/competitors/{slug}.md` playbooks
2. Pull **adapted hook templates** (not verbatim copy) into this week's trend brief

Skip if user only wants catalog fallback (Sunday automation cron).

## Instructions

1. Read `brand/competitors.yaml` → brands user wants to mimic (formats only)
2. Read existing `content/research/competitors/*.md` playbooks (refresh stale ones per workflow)
3. Read `campaigns/active.yaml` → `current_focus` products
4. Read `brand/voice.md` → content pillars
5. Read prior week `content/week-XX/social.md` — note what angles were used (avoid repeats)

### External research (Agents Window + Blotato MCP)

6. Call Blotato `list_top_posts` + `get_post_analytics` on recent Wellthlab posts
7. Call Blotato `create_source`:
   - `perplexity-query`: "Top TikTok hook formats for supplement DTC brands in 2026"
   - `tiktok` or `youtube` URLs from `brand/competitors.yaml` and competitor playbooks
   - `customInstructions`: "Extract hook patterns, visual formats, and CTA styles — not verbatim copy"
8. Optional: browser scrape competitor product pages for angle differentiation

### Catalog fallback (when Blotato unavailable)

9. Read `products/catalog.yaml` + `products/catalog-summary.yaml`
10. Infer hooks from product benefits, competitor playbooks, and `campaigns/active.yaml` angles

## Output

Save to `content/research/week-XX/trend-brief.md`:

```markdown
# Week XX Trend Brief

## Winning patterns
- Hook formats (with examples)
- Visual/audio trends to borrow (not copy)
- Competitor angles to differentiate from

## Adapted from competitor research
- {Brand}: their mechanic → Wellthlab hook template (original copy)
- (from content/research/competitors/*.md)

## Recommended for Wellthlab
- 3 hook templates adapted to our products
- 2 carousel topics (tag tool: blotato | canva | remotion)
- 1 UGC format to film

## Products to push
(from campaigns/active.yaml current_focus)

## Sources
- [list URLs / Blotato source IDs]
- Competitor playbooks: content/research/competitors/
```

## Rules
- Brand name is **Wellthlab** — never "Wealth Lab"
- No fabricated competitor claims or fake social proof
- Structure/function claims only for supplement angles
