---
name: local-llm
version: 1.0.0
description: Run prompts through local Ollama LLM on VPS — zero API tokens. Default model qwen2.5:3b (1.9GB, fast for simple tasks).
---

# Local LLM (Ollama)

Запускает локальную языковую модель прямо на VPS. **Не тратит API токены.**

## Когда использовать

- Суммаризация текста
- Форматирование / переформатирование данных
- Простые вопросы и ответы
- Классификация, извлечение данных
- Любые задачи где не нужна сила Claude

## Установленные модели

| Модель | Размер | Описание |
|--------|--------|----------|
| qwen2.5:3b | 1.9GB | Основная — хорошее качество, быстро |

## Скрипт

```
python3 skills/local-llm/scripts/run.py run "<prompt>"
python3 skills/local-llm/scripts/run.py run "<prompt>" --model qwen2.5:3b
python3 skills/local-llm/scripts/run.py list
echo "текст" | python3 skills/local-llm/scripts/run.py run
```

## Параметры

- `--model / -m` — модель (default: qwen2.5:3b)
- `--system / -s` — системный промпт
- `--temperature / -t` — температура (default: 0.7)
- `--max-tokens` — макс. токенов в ответе (default: 2048)
- `--no-stream` — отдать весь ответ сразу, не стримить

## Инфраструктура

- Ollama слушает на `localhost:11434`
- Сервис: `systemctl status ollama`
- Логи: `journalctl -u ollama -f`
- Добавить модель: `ollama pull <model>`

## Добавить больше моделей (опционально)

```bash
ollama pull qwen2.5:7b    # 4.7GB — лучше, медленнее
ollama pull phi3.5         # 2.3GB — альтернатива
ollama pull mistral:7b    # 4.1GB — хорош для текста
```
