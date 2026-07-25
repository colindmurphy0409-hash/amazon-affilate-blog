# Produce and Queue

## Trigger
After user says **"approve week XX"** — verify `content/week-XX/approval.md` has `status: approved`

## Prerequisites
- `approval.md` marked approved (hard stop if not)
- Blotato MCP authenticated (for Track A)
- Product PNGs available for Remotion (Shopify CDN URLs or `video/public/assets/products/`)

---

## Track A — Blotato AI carousels

For each brief in `carousels.md` tagged `tool: blotato`:

1. `blotato_list_visual_templates` → pick slideshow/carousel template
2. `blotato_create_visual` with prompt from brief
3. Poll `blotato_get_visual_status` every 15s until `done`
4. Add to `posts/queue.yaml`:
   - `status: pending`
   - `mediaUrls` from `imageUrls` or `mediaUrl`
   - `platforms: [tiktok, instagram]`
   - caption from brief

---

## Track B — Canva (agent via MCP)

For each brief tagged `tool: canva`:

1. Agent uses **Canva MCP** tools (connected in `.cursor/mcp.json`)
2. Reads `content/week-XX/canva-briefs.yaml` + `brand/canva.md`
3. Creates/autofills design, exports to `posts/media/`
4. **Never** ask the user to open Canva

See `workflows/canva-production.md` and `workflows/canva-connect-setup.md`.

---

## Track C — Remotion programmatic Reels

For each entry in `content/week-XX/remotion-props.json`:

1. Validate props against approved scripts in `social.md`
2. Ensure product images exist in `video/public/assets/products/`
3. Run:

```bat
python scripts/render_week.py --week XX
```

4. Rendered files land in `posts/media/` — update `posts/queue.yaml`

See `workflows/remotion-render.md` for composition details.

---

## Track D — UGC + Higgsfield

For scripts tagged `tool: film` in `carousels.md`:

1. Write `content/week-XX/higgsfield-prompts.md` (lifestyle scenes only — **never AI-generate products**)
2. User films product close-ups on phone
3. Optional: Higgsfield backdrop scenes per `wl-higgsfield-prompt-pack.md`
4. Export to `posts/media/day-XX-{product}.mp4`
5. Update queue `video:` paths

---

## Schedule (requires explicit go-ahead)

```bat
python scripts/schedule_queue.py --dry-run
python scripts/schedule_queue.py
```

Or Blotato MCP `create_post` with `useNextFreeSlot: true`.

**Never schedule without user confirming assets are ready.**
