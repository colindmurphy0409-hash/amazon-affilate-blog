# Canva via MCP (Primary — same as Claude Desktop Connector)

Agents build all Canva assets. **You never open Canva manually.**

## Connect (2 minutes — like Claude Desktop)

1. Canva MCP is in [`.cursor/mcp.json`](../.cursor/mcp.json):
   ```json
   "canva": {
     "url": "https://mcp.canva.com/mcp"
   }
   ```
2. **Restart Cursor** (or reload MCP servers in Settings → MCP)
3. First time an agent uses Canva, **OAuth opens in your browser** — approve with your Canva account (Pro/Teams/Business required)
4. Done. Agents can create, autofill, search, and export designs.

Official docs: [Canva AI Connector help](https://www.canva.com/help/mcp-agent-setup/)

## What agents can do (via MCP)

- Create designs from prompts (carousels, Reels, social posts)
- Autofill brand templates
- Search your Canva library
- Export PDF/PNG/MP4 to use in `posts/media/` or Blotato queue

See [Canva MCP usage](https://www.canva.com/help/mcp-canva-usage/) for full action list.

## Pipeline integration

After `approve week XX`, agent reads `content/week-XX/canva-briefs.yaml` and calls **Canva MCP tools** directly — no manual steps.

Fallback order if MCP unavailable:
1. Canva MCP (this)
2. Remotion render
3. Blotato create_visual

## Not the same as `canva-dev` MCP

| Server | Purpose |
|--------|---------|
| **`canva`** @ `https://mcp.canva.com/mcp` | Create/export designs (what you want) |
| `canva-dev` @ `npx @canva/cli mcp` | Developer docs for building Canva *apps* |

## Legacy: Connect API script

[`scripts/canva_connect.py`](../scripts/canva_connect.py) is only needed for headless CI without MCP. **Ignore it** if MCP is connected.

## Troubleshooting

- **No Canva tools in agent?** Use Agent mode, restart Cursor, re-authorize OAuth
- **Access denied?** Need Canva Pro/Teams/Business; check admin third-party integrations
- **Node.js error?** Canva requires Node.js 22.16+ for some clients
