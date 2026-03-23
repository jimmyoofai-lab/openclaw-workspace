#!/bin/bash
# Hugging Face Spaces Image Generation via curl

set -e

PROMPT=""
MODEL="lightning"
FILENAME=""
WIDTH=512
HEIGHT=512

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --prompt) PROMPT="$2"; shift 2 ;;
        --model) MODEL="$2"; shift 2 ;;
        --filename) FILENAME="$2"; shift 2 ;;
        --width) WIDTH="$2"; shift 2 ;;
        --height) HEIGHT="$2"; shift 2 ;;
        *) shift ;;
    esac
done

if [ -z "$PROMPT" ]; then
    echo "Error: --prompt required" >&2
    exit 1
fi

# Generate filename if not provided
if [ -z "$FILENAME" ]; then
    TIMESTAMP=$(date +%Y-%m-%d-%H-%M-%S)
    CLEAN_PROMPT=$(echo "$PROMPT" | sed 's/[^a-zA-Z0-9 -]//g' | cut -c1-30 | tr ' ' '-')
    FILENAME="${TIMESTAMP}-${CLEAN_PROMPT}.png"
fi

echo "📸 Generating with $MODEL..." >&2
echo "Prompt: $PROMPT" >&2

# Call HF API and get image URL
# Note: This is simplified - actual HF Spaces endpoints vary
# For now, return error with helpful message
echo "⚠️  Direct HF Space API calls require special setup." >&2
echo "Recommend using fal.ai or replicate.com for free image generation" >&2
echo "Or use nano-banana-pro with your own Google API key" >&2
exit 1
