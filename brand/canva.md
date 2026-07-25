# Wellthlab Canva Brand Kit (Agent Production)

Agents use this file when running Canva MCP or `scripts/canva_produce.py`.
**The user never builds in Canva manually.**

**Product imagery:** exact official Shopify images only — see `brand/assets.md`. Never AI-generate products.
**Voice:** see `brand/voice.md` for tone on all slide copy.

## Colors

| Token | Hex | Use |
|-------|-----|-----|
| Ink | `#0f172a` | Headlines, body text |
| Ink soft | `#475569` | Secondary text |
| Cream | `#fafaf8` | Backgrounds |
| Surface | `#f1f5f9` | Cards, slide backgrounds |
| Primary (teal) | `#0d9488` | Accents, CTAs, highlights |
| Primary dark | `#0f766e` | CTA buttons |
| Border | `#e2e8f0` | Dividers |

## Typography
- **Headlines:** Montserrat Bold (or Canva equivalent)
- **Body:** Montserrat Regular / Inter

## Brand templates (Canva Connect autofill)

Store template IDs in `tools/canva.yaml` under `brand_templates`:

| Key | Dimensions | Use |
|-----|------------|-----|
| `carousel_1080x1350` | 1080×1350 | Education carousel |
| `reel_1080x1920` | 1080×1920 | Vertical Reel export |

Autofill field names must match `field_map` in `tools/canva.yaml`.

## Browser fallback template URLs

If Connect API is not configured, agent opens these in browser and fills slides from `canva-briefs.yaml`:

- Carousel template: _add Canva share link after first agent-created template_
- Reel template: _add link here_

## Agent commands

```bat
python scripts/canva_produce.py --week XX --brief {id} --dry-run
python scripts/canva_produce.py --week XX --brief {id}
```

## Setup (one-time, then agents run forever)

Full guide: [`workflows/canva-connect-setup.md`](workflows/canva-connect-setup.md)

```bat
python scripts/canva_connect.py connect --client-id YOUR_ID --client-secret YOUR_SECRET
python scripts/canva_connect.py test
python scripts/canva_connect.py list-templates
```

## Remotion parity
Same hex values used in `video/src/brand.ts` when Canva API unavailable (automatic fallback).
