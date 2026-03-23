#!/usr/bin/env python3
"""
Generate images via Cloudflare Workers AI.
Free tier: 10,000 neurons/day. Response can take 2-3 min — normal for free tier.
"""
import argparse, base64, http.client, json, os, re, ssl, sys
from datetime import datetime
from pathlib import Path

MODELS = {
    "flux-schnell": "@cf/black-forest-labs/flux-1-schnell",
    "sdxl":        "@cf/stabilityai/stable-diffusion-xl-base-1.0",
    "sd15":        "@cf/runwayml/stable-diffusion-v1-5",
    "dreamshaper": "@cf/lykon/dreamshaper-8-lcm",
}

def _stamp(): return datetime.now().strftime("%Y-%m-%d-%H%M%S")
def _slug(t, n=50): return (re.sub(r"[^a-z0-9]+","-",t.lower()).strip("-")[:n] or "img")

def generate(prompt, account_id, api_token, model_key="flux-schnell", width=1024, height=1024, steps=4):
    # Remove proxy env vars — CF API should be accessed directly
    for k in ("HTTP_PROXY","HTTPS_PROXY","ALL_PROXY","http_proxy","https_proxy","all_proxy"):
        os.environ.pop(k, None)

    model = MODELS.get(model_key, model_key)
    path = f"/client/v4/accounts/{account_id}/ai/run/{model}"
    payload = json.dumps({"prompt": prompt, "width": width, "height": height, "steps": steps})

    print(f"Connecting to Cloudflare Workers AI ({model_key})...", file=sys.stderr)
    ctx = ssl.create_default_context()
    conn = http.client.HTTPSConnection("api.cloudflare.com", 443, context=ctx, timeout=60)
    conn.request("POST", path, payload, {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    })
    r = conn.getresponse()
    # Increase socket timeout for slow body download (free tier can be very slow)
    if conn.sock:
        conn.sock.settimeout(300)
    content_len = r.getheader("Content-Length", "?")
    print(f"Response: {r.status}, size: {content_len} bytes", file=sys.stderr)

    if r.status != 200:
        err = r.read().decode(errors="replace")
        print(f"ERROR {r.status}: {err[:400]}", file=sys.stderr)
        return None

    # Read full body with progress (can be slow on free tier)
    print("Downloading response body (may take 2-3 min on free tier)...", file=sys.stderr)
    chunks, total = [], 0
    while True:
        chunk = r.read(32768)
        if not chunk: break
        chunks.append(chunk)
        total += len(chunk)
        if total % 65536 < 32768:
            print(f"  {total}/{content_len} bytes", file=sys.stderr, flush=True)

    body = b"".join(chunks)
    data = json.loads(body)
    return base64.b64decode(data["result"]["image"])

def main(argv):
    p = argparse.ArgumentParser(prog="cf-image-gen")
    p.add_argument("--prompt", required=True)
    p.add_argument("--model", default="flux-schnell", choices=list(MODELS.keys()))
    p.add_argument("--width", type=int, default=1024)
    p.add_argument("--height", type=int, default=1024)
    p.add_argument("--steps", type=int, default=4)
    p.add_argument("--count", type=int, default=1)
    p.add_argument("--out-dir", default=None)
    p.add_argument("--account-id", default=None)
    p.add_argument("--api-token", default=None)
    args = p.parse_args(argv)

    account_id = args.account_id or os.environ.get("CF_ACCOUNT_ID")
    api_token  = args.api_token  or os.environ.get("CF_API_TOKEN")
    if not account_id or not api_token:
        print("ERROR: set CF_ACCOUNT_ID and CF_API_TOKEN", file=sys.stderr); return 2

    out_dir = args.out_dir or os.path.join(os.getcwd(), "tmp", f"cf-image-{_stamp()}")
    os.makedirs(out_dir, exist_ok=True)

    import time
    for i in range(args.count):
        print(f"\n[{i+1}/{args.count}]", file=sys.stderr)
        img = generate(args.prompt, account_id, api_token, args.model, args.width, args.height, args.steps)
        if img is None: return 1
        fname = f"{_stamp()}-{i+1:02d}-{_slug(args.prompt)}.jpg"
        path = os.path.join(out_dir, fname)
        Path(path).write_bytes(img)
        print(f"saved {fname} ({len(img)} bytes)")
        if args.count > 1 and i < args.count - 1: time.sleep(0.5)

    print(f"out_dir={out_dir}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
