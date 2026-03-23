---
name: cards-generator
description: "Generate Instagram/Telegram visual cards (карточки) via Nano Banana Pro (Gemini image generation). Bold typographic SMM-style design in blue/navy palette. Use when user asks to create карточки, посты, визуал, серию карточек for Instagram/social media, or generate any styled image cards for content. Supports cover cards, lists, stats, quotes, CTAs, comparisons, step-by-step educational cards."
---

# Cards Generator

Generate Instagram-format (1:1) visual cards via Nano Banana Pro.

## Design System
Read `references/design-system.md` for full style guide: color palettes (A–D), typography rules, layout patterns.

## Prompt Templates
Read `references/prompt-templates.md` for ready-made prompt templates by card type:
- Cover / Обложка
- List / Шаги
- Stats / Цифры
- Quote / Определение
- CTA / Призыв
- Split Comparison / Сравнение
- Educational Step / Обучающий шаг

## Reference Images
Stored in `assets/`:
- `ref-digital-agency.jpg` — bright blue marquee style
- `ref-smm-agency.jpg` — cutout photos, bold type
- `ref-isar-dark.jpg` — dark navy informational cards
- `ref-isar-light.jpg` — clean light educational cards

Pass as `--input-image` when user wants to match a specific reference style.

## Workflow

1. **Identify series** — how many cards, what topic, which palette
2. **Pick templates** from `references/prompt-templates.md` for each card type
3. **Fill in content** — replace placeholders with user's text
4. **Draft at 1K** — iterate until composition is right
5. **Final at 2K** — for Instagram use; 4K if user needs print/large

## Nano Banana Pro Command

```bash
uv run ~/.openclaw/workspace/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "[PROMPT]" \
  --filename "~/.openclaw/workspace/cards/[SERIES]/card-N-name.png" \
  --resolution 2K \
  --api-key AIzaSyANRnoLmRWhNDm-f5jdbRz_9hKUqzzV7Y8
```

## Output
- Save to `~/.openclaw/workspace/cards/[series-name]/`
- Name pattern: `card-1-cover.png`, `card-2-list.png`, etc.
- After all cards done — send all via Telegram as photo album

## Key Rules
- Always Russian text unless user says otherwise
- No gradients on text elements — solid fills only
- Pill badges for labels/series markers
- No stock photo faces unless user provides image
- Bold condensed CAPS for main headlines
