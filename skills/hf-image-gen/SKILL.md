---
name: hf-image-gen
version: 1.0.0
license: MIT
description: Free image generation via Hugging Face Spaces (no API key needed). Uses Lightning SD 1.0 or Stable Diffusion v1.5 - completely free, runs on HF infrastructure.
---

# Hugging Face Spaces Image Generation

Generate images for free using Hugging Face Spaces. No API keys, no quotas. Just run and wait.

## Quick Start

```bash
python3 ~/.openclaw/workspace/skills/hf-image-gen/scripts/generate.py --prompt "your image description"
```

## Available Models

- **Lightning** (fastest, ~5-10 seconds)
- **Stable Diffusion 1.5** (higher quality, ~30 seconds)
- **SDXL** (best quality, ~60 seconds)

## Usage

```bash
python3 ~/.openclaw/workspace/skills/hf-image-gen/scripts/generate.py \
  --prompt "A serene Japanese garden" \
  --model lightning \
  --filename "output.png"
```

Options:
- `--prompt TEXT` - Image description (required)
- `--model MODEL` - lightning | sd15 | sdxl (default: lightning)
- `--filename NAME` - Output filename (default: timestamp + random)
- `--height NUM` - Image height (default: 512)
- `--width NUM` - Image width (default: 512)

## Examples

```bash
# Fast draft
python3 ~/.openclaw/workspace/skills/hf-image-gen/scripts/generate.py \
  --prompt "sunset over mountains" \
  --model lightning

# Final render
python3 ~/.openclaw/workspace/skills/hf-image-gen/scripts/generate.py \
  --prompt "sunset over mountains, cinematic lighting" \
  --model sdxl
```

## No Auth Needed

All models run on Hugging Face Spaces without authentication. Just internet connection required.
