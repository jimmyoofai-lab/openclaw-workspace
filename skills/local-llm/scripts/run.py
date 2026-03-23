#!/usr/bin/env python3
"""
Run a prompt through local Ollama LLM (no API tokens used).
Default model: qwen2.5:3b
"""
import argparse, json, sys, urllib.request, urllib.error

OLLAMA_URL = "http://localhost:11434"

def list_models():
    with urllib.request.urlopen(f"{OLLAMA_URL}/api/tags") as r:
        data = json.loads(r.read())
    for m in data.get("models", []):
        print(m["name"])

def run(model, prompt, system=None, stream=True, temperature=0.7, max_tokens=2048):
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})

    payload = json.dumps({
        "model": model,
        "messages": messages,
        "stream": stream,
        "options": {
            "temperature": temperature,
            "num_predict": max_tokens,
        }
    }).encode()

    req = urllib.request.Request(
        f"{OLLAMA_URL}/api/chat",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            if stream:
                for line in r:
                    line = line.strip()
                    if not line:
                        continue
                    obj = json.loads(line)
                    token = obj.get("message", {}).get("content", "")
                    if token:
                        print(token, end="", flush=True)
                    if obj.get("done"):
                        print()  # newline at end
                        break
            else:
                data = json.loads(r.read())
                print(data["message"]["content"])
    except urllib.error.URLError as e:
        print(f"ERROR: Cannot connect to Ollama at {OLLAMA_URL}: {e}", file=sys.stderr)
        print("Start with: systemctl start ollama", file=sys.stderr)
        return 1
    return 0

def main(argv):
    p = argparse.ArgumentParser(prog="local-llm")
    sub = p.add_subparsers(dest="cmd")

    # list command
    sub.add_parser("list", help="List installed models")

    # run command
    r = sub.add_parser("run", help="Run a prompt")
    r.add_argument("prompt", nargs="?", help="Prompt text (or pipe via stdin)")
    r.add_argument("--model", "-m", default="qwen2.5:3b")
    r.add_argument("--system", "-s", default=None, help="System prompt")
    r.add_argument("--no-stream", action="store_true")
    r.add_argument("--temperature", "-t", type=float, default=0.7)
    r.add_argument("--max-tokens", type=int, default=2048)

    args = p.parse_args(argv)

    if args.cmd == "list":
        list_models()
        return 0

    if args.cmd == "run" or args.cmd is None:
        prompt = args.prompt if hasattr(args, "prompt") and args.prompt else None
        if prompt is None:
            if not sys.stdin.isatty():
                prompt = sys.stdin.read().strip()
            else:
                print("ERROR: provide a prompt or pipe text via stdin", file=sys.stderr)
                return 2
        model = args.model if hasattr(args, "model") else "qwen2.5:3b"
        system = args.system if hasattr(args, "system") else None
        stream = not args.no_stream if hasattr(args, "no_stream") else True
        temp = args.temperature if hasattr(args, "temperature") else 0.7
        mtok = args.max_tokens if hasattr(args, "max_tokens") else 2048
        return run(model, prompt, system, stream, temp, mtok)

    p.print_help()
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
