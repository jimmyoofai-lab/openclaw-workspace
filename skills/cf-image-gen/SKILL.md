---
name: cf-image-gen
version: 1.0.0
description: Generate images via Cloudflare Workers AI. FREE — 10,000 neurons/day. Models: FLUX Schnell, SDXL, DreamShaper. Works from any VPS IP.
---

# Cloudflare Workers AI Image Generation

Генерация изображений через Cloudflare Workers AI — бесплатно, без кредитки.

## Setup

1. Зарегистрируйся на https://dash.cloudflare.com
2. Зайди в **AI → Workers AI** и получи API токен
3. Скопируй Account ID (на главной странице дашборда, справа)

```bash
export CF_ACCOUNT_ID="abc123def456..."
export CF_API_TOKEN="your_api_token_here"
```

## Usage

```bash
python3 ~/.openclaw/workspace/skills/cf-image-gen/scripts/gen.py \
  --prompt "a fox reading a book in a cozy library, warm lighting"
```

Options:
- `--prompt TEXT` — описание изображения (обязательно)
- `--model flux-schnell|sdxl|sd15|dreamshaper` — модель (default: flux-schnell)
- `--width N` — ширина в пикселях (default: 1024)
- `--height N` — высота в пикселях (default: 1024)
- `--steps N` — шаги инференса (4 для FLUX, 20 для SDXL)
- `--count N` — количество изображений
- `--out-dir PATH` — папка для сохранения

## Models

| Ключ | Модель | Стиль |
|------|--------|-------|
| `flux-schnell` | FLUX.1 Schnell | Фотореализм, общее назначение |
| `sdxl` | Stable Diffusion XL | Художественный, детализированный |
| `sd15` | Stable Diffusion 1.5 | Быстрый, базовый |
| `dreamshaper` | DreamShaper 8 LCM | Арт, иллюстрации |

## Free limits

- **10,000 neurons/day** бесплатно (1 изображение ≈ 300-500 neurons)
- Т.е. ~20-30 изображений/день бесплатно на FLUX Schnell

## Examples

```bash
# FLUX Schnell (быстро, бесплатно)
python3 ~/.openclaw/workspace/skills/cf-image-gen/scripts/gen.py \
  --prompt "cyberpunk city at night" --model flux-schnell

# SDXL (выше качество)
python3 ~/.openclaw/workspace/skills/cf-image-gen/scripts/gen.py \
  --prompt "oil painting of a mountain lake" --model sdxl --steps 20

# 3 варианта сразу
python3 ~/.openclaw/workspace/skills/cf-image-gen/scripts/gen.py \
  --prompt "a cozy café interior, soft lighting" --count 3
```

## Output

PNG файлы в `out_dir`, путь печатается в конце.
