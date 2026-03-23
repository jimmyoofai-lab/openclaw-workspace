#!/usr/bin/env python3
"""
Hugging Face Spaces Image Generation
Free image generation without API keys
"""

import argparse
import requests
import sys
from datetime import datetime
from pathlib import Path
import time

# Hugging Face Spaces endpoints (free, no auth)
MODELS = {
    "lightning": "https://nerijs-sd15-lightning.hf.space/",
    "sd15": "https://black-forest-labs-sdxl-lite.hf.space/",
    "sdxl": "https://stabilityai-stable-diffusion-xl.hf.space/"
}

def generate_filename(prompt: str) -> str:
    """Generate filename from prompt and timestamp"""
    now = datetime.now()
    ts = now.strftime("%Y-%m-%d-%H-%M-%S")
    # Clean prompt for filename
    clean_prompt = "".join(c if c.isalnum() or c in " -" else "" for c in prompt[:40])
    clean_prompt = "-".join(clean_prompt.split())[:30]
    if not clean_prompt:
        clean_prompt = "image"
    return f"{ts}-{clean_prompt}.png"

def call_hf_space(space_url: str, prompt: str, width: int = 512, height: int = 512) -> bytes:
    """Call Hugging Face Space API"""
    import os
    try:
        # Disable SOCKS proxy for HF API calls
        proxies = {
            'http': None,
            'https': None
        }
        
        # For Gradio spaces, POST to /run/predict
        payload = {
            "data": [prompt, width, height]  # Most spaces use this format
        }
        
        response = requests.post(
            f"{space_url}run/predict",
            json=payload,
            proxies=proxies,
            timeout=180
        )
        response.raise_for_status()
        
        # Gradio returns dict with "data" key containing image URL or base64
        result = response.json()
        if "data" in result and len(result["data"]) > 0:
            image_url = result["data"][0]
            if isinstance(image_url, str) and image_url.startswith("http"):
                # Download image (no proxy)
                img_response = requests.get(image_url, proxies=proxies, timeout=30)
                return img_response.content
        return None
    except Exception as e:
        print(f"Error calling HF Space: {e}", file=sys.stderr)
        return None

def main():
    parser = argparse.ArgumentParser(description="Generate images via Hugging Face Spaces")
    parser.add_argument("--prompt", required=True, help="Image description")
    parser.add_argument("--model", default="lightning", choices=list(MODELS.keys()), help="Model to use")
    parser.add_argument("--filename", help="Output filename")
    parser.add_argument("--width", type=int, default=512, help="Image width")
    parser.add_argument("--height", type=int, default=512, help="Image height")
    
    args = parser.parse_args()
    
    # Generate filename if not provided
    filename = args.filename or generate_filename(args.prompt)
    
    print(f"📸 Generating with {args.model}...", file=sys.stderr)
    print(f"Prompt: {args.prompt}", file=sys.stderr)
    
    space_url = MODELS[args.model]
    image_data = call_hf_space(space_url, args.prompt, args.width, args.height)
    
    if image_data:
        output_path = Path.cwd() / filename
        output_path.write_bytes(image_data)
        print(str(output_path))  # Print path for tool integration
    else:
        print("Error: Failed to generate image", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
