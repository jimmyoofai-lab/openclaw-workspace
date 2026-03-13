# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Whisper (Speech-to-Text)

**Локально:**
- Установлен: `/opt/homebrew/bin/whisper`
- Модель: turbo (по умолчанию, быстро)
- Кэш: ~/.cache/whisper

**На VPS (157.22.175.174):**
- Установка: `apt-get install ffmpeg && pip install openai-whisper`
- Использование: `whisper /path/audio.mp3 --model turbo --output_format txt`

**Автоматическая обработка:**
- Telegram шлёт голосовые → я получаю транскрипцию автоматически
- Сохраняю в памяти (MEMORY.md)
- Можно улучшить качество (модель medium)

---

Add whatever helps you do your job. This is your cheat sheet.
