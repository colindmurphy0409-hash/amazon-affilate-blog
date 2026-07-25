# Canva Production (Agent via MCP)

## Trigger
After approval, for any brief in `carousels.md` tagged `tool: canva`

**The user never opens Canva.** Agents use the **Canva MCP** (`https://mcp.canva.com/mcp`).

## Prerequisites
- Canva MCP connected in `.cursor/mcp.json` (see `workflows/canva-connect-setup.md`)
- OAuth completed on first use (browser popup — same as Claude Desktop Connector)
- Canva Pro/Teams/Business plan

## Agent steps

1. Read `content/week-XX/canva-briefs.yaml` for slide copy + dimensions
2. Use **Canva MCP tools** to:
   - Create or autofill a design from the brief
   - Apply Wellthlab brand colors + tone (`brand/canva.md`, `brand/voice.md`)
   - Insert **exact** product images via `upload-asset-from-url` using Shopify CDN URLs from the brief — **never** let generate-design invent product packaging (`brand/assets.md`)
   - Export as MP4 (Reel) or PNG carousel → save/download to `posts/media/`
3. Update `posts/queue.yaml` with the exported file path or public URL

## Example agent prompt (after approval)

```
Using Canva MCP, produce the strips-vs-pills carousel from
content/week-30/canva-briefs.yaml. Export 1080x1350 MP4 to
posts/media/day-05-strips-carousel.mp4. Use real product photo
from the brief. Never ask me to open Canva.
```

## Fallback (only if MCP fails)

1. **Remotion** — `python scripts/render_week.py --week XX`
2. **Blotato** — `blotato_create_visual`

Log fallback in `approval.md` under Production notes.

## Do NOT use

- Manual Canva UI steps for the user
- `scripts/canva_connect.py` unless running headless without MCP
