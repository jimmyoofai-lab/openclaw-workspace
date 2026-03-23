#!/usr/bin/env python3
"""Transcribe audio file using faster-whisper."""
import sys
import os

os.environ.pop("ALL_PROXY", None)
os.environ.pop("HTTP_PROXY", None)
os.environ.pop("HTTPS_PROXY", None)

if len(sys.argv) < 2:
    print("Usage: transcribe.py <audio_file> [language]")
    sys.exit(1)

audio_file = sys.argv[1]
language = sys.argv[2] if len(sys.argv) > 2 else "ru"

from faster_whisper import WhisperModel
model = WhisperModel("small", device="cpu", compute_type="int8")
segments, info = model.transcribe(audio_file, language=language)
text = " ".join(seg.text.strip() for seg in segments)
print(text)
