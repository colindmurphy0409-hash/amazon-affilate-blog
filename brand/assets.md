# Wellthlab Product Imagery & Brand Compliance

**Hard rules for all DTC marketing production** (Canva, Remotion, Blotato, Higgsfield, social copy).

## Product images — exact only

When a product appears in any asset, use the **exact official image** from wellthlab.shop. Never substitute.

| Allowed | Forbidden |
|---------|-----------|
| Shopify CDN URL from `products/catalog.yaml` or `canva-briefs.yaml` `product_image_url` | AI-generated product photos, tins, strips, labels, or packaging |
| `upload-asset-from-url` / download from verified Shopify `src` | Canva "generate" inventing a product look |
| PNG in `video/public/assets/products/` copied from Shopify | Stock photos pretending to be Wellthlab products |
| Lifestyle scenes (Higgsfield) **without** product — composite real product in edit | "Similar" or approximate product renders |

**Before production:** run `python scripts/sync_catalog.py` if URLs may be stale. Resolve image URLs via `https://wellthlab.shop/products/{handle}.json` → `images[].src` when missing.

If the exact image cannot be fetched, **stop and fix the URL** — do not proceed with a placeholder or generated product.

## Brand colors

Use tokens from `brand/canva.md` (Remotion: `video/src/brand.ts`). Do not invent palettes.

| Token | Hex |
|-------|-----|
| Primary (teal) | `#0d9488` |
| Primary dark | `#0f766e` |
| Cream background | `#fafaf8` |
| Ink (text) | `#0f172a` |

## Brand tone

Follow `brand/voice.md` on every caption, slide, hook, and CTA:

- **Wellthlab** — never "Wealth Lab"
- Direct, confident, science-aware, human — not clinical or preachy
- Short sentences; speak to how it fits the day
- FDA structure/function claims only; include disclaimer on supplement content

## Tool-specific reminders

- **Canva MCP:** `upload-asset-from-url` with Shopify URL; never rely on generate-design to draw the product
- **Remotion:** only files in `video/public/assets/products/` sourced from Shopify
- **Blotato:** pass real product image URLs in visual payloads when supported
- **Higgsfield:** lifestyle/backdrop only; composite real product in Remotion or phone edit
