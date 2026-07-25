# Remotion Render

## Trigger
After approval, when `content/week-XX/remotion-props.json` exists

## Setup (one-time)

```bat
cd video
npm install
```

## Compositions

| ID | Duration | Props | Use |
|----|----------|-------|-----|
| `HookReel` | 15–20s, 9:16 | hook, productImage, captionLines[], cta | Animated hook + product photo |
| `ProductMontage` | 20–30s, 9:16 | productImage, bullets[], cta | Product showcase, no face |
| `EducationStrip` | 25–40s, 9:16 | title, tips[], productImage, cta | "Did you know" format |

## Render one composition

```bat
cd video
npx remotion render HookReel ../posts/media/day-02-energy-hook.mp4 --props="{\"hook\":\"3pm and I'm done\",\"productImage\":\"energy-strips.png\",\"captionLines\":[\"Clean lift\",\"No water\"],\"cta\":\"wellthlab.shop\"}"
```

## Batch render from week props

```bat
python scripts/render_week.py --week 30
```

Reads `content/week-XX/remotion-props.json` and renders each entry to `posts/media/`.

## Asset rules
- Product images: real PNGs from Shopify in `video/public/assets/products/`
- Never AI-generate product packaging
- Hook text must match approved script in `social.md`
- Brand colors from `brand/canva.md`

## Preview in Studio

```bat
cd video
npx remotion studio
```
