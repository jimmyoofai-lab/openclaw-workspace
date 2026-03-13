# Prompt Templates — Instagram Card Generator

## Base Structure
Every prompt follows this structure:
```
Square 1:1 Instagram card. [LAYOUT]. [TYPOGRAPHY]. [COLORS]. [TEXT CONTENT]. [STYLE DETAILS]. No gradients unless specified. Sharp edges. Clean composition. No watermarks.
```

---

## Template: Cover Card (Обложка)

```
Square 1:1 Instagram card. Bold typographic cover design.

Typography: Extra-bold condensed uppercase headline "[ЗАГОЛОВОК]" fills 60% of card height, very tight line-height. Small pill badge "[МЕТКА]" top-left corner with rounded rectangle background.

Colors: [PALETTE]. Background solid [BG_COLOR]. All text [TEXT_COLOR].

Bottom-right: tiny brand mark or handle "[БРЕНД]" in small caps.

Optional background layer: repeating word "[СЛОВО]" in very subtle lighter shade, stacked diagonally at 30 degrees, behind main text.

Style: editorial, confident, modern SMM. Sharp, no blur on main elements. No stock photo faces.
```

---

## Template: List / Steps Card (Список / Шаги)

```
Square 1:1 Instagram card. Numbered list layout.

Top: small bold label "[ТЕМА]" in pill badge, blue background white text.
Below: numbered items 1–[N]:
  [НОМЕР] bold large number left, "[ПУНКТ]" medium weight text right.

Colors: Background [BG_COLOR], numbers in [ACCENT_COLOR], text [TEXT_COLOR].

Typography: Numbers Extra Bold condensed, list text Regular weight readable size.

Style: clean structured layout, generous spacing between items, no illustrations needed.
```

---

## Template: Stats Card (Цифры / Факты)

```
Square 1:1 Instagram card. Bold statistics layout.

Center: [N] huge numbers arranged in [1 column / 2 columns]:
  "[ЦИФРА_1]" in Extra Bold condensed, label "[ПОДПИСЬ_1]" small below.
  "[ЦИФРА_2]" in Extra Bold condensed, label "[ПОДПИСЬ_2]" small below.

Top: small heading "[ЗАГОЛОВОК]".

Colors: Background [BG_COLOR], numbers [ACCENT_COLOR], labels muted.

Style: numbers dominate, whitespace around each stat, editorial.
```

---

## Template: Quote / Definition Card (Цитата / Определение)

```
Square 1:1 Instagram card. Minimal typographic quote design.

Center: large opening quotation mark, below it "[ТЕКСТ ЦИТАТЫ]" in bold, below it em dash and "[ИСТОЧНИК]" in regular italic.

Or for definition: "[ТЕРМИН]" Extra Bold condensed top, horizontal rule, "[ОПРЕДЕЛЕНИЕ]" body text below.

Colors: Background [BG_COLOR] (light or white preferred), text [TEXT_COLOR].

Style: lots of whitespace, elegant, no decoration except the quote mark.
```

---

## Template: CTA Card (Призыв к действию)

```
Square 1:1 Instagram card. Bold call-to-action design.

Giant uppercase action phrase "[ДЕЙСТВИЕ]" fills most of card, Extra Bold condensed.
Below: one supporting line "[ПОДТЕКСТ]" in medium weight.
Bottom: "[БРЕНД / ССЫЛКА]" in small pill badge or plain small text.

Colors: Background vivid blue #3C3FE8, all text white.

Optional: repeating background text "[СЛОВО]" very subtly in #4A50F5.

Style: high energy, urgent, no distractions. The verb IS the design.
```

---

## Template: Split Comparison Card (Сравнение)

```
Square 1:1 Instagram card. Hard split layout.

Left half: background [COLOR_LEFT], "[ВАРИАНТ А]" bold white text centered.
Right half: background [COLOR_RIGHT], "[ВАРИАНТ Б]" bold [TEXT_RIGHT] text centered.
Center: "VS" or "/" in large bold at the split line.

Top: small label "[ТЕМА СРАВНЕНИЯ]".

Colors: typically blue vs white, or dark vs light.

Style: sharp hard edge split (no gradient), bold contrast, clean.
```

---

## Template: Educational / Step Card (Обучающий контент)

```
Square 1:1 Instagram card. Educational step card.

Top-left: pill badge "Шаг [N]" blue background white text.
Main: bold short title "[НАЗВАНИЕ ШАГА]" large.
Below: "[2–3 строки тела]" in regular weight readable size.
Bottom-right: series label "[СЕРИЯ]" tiny muted.

Colors: Background white or #F5F5F5, title [NAVY], body dark gray, badge blue.

Style: clean, structured, trustworthy. Like a lesson slide but for Instagram.
```

---

## Nano Banana Pro Command

```bash
uv run ~/.openclaw/workspace/skills/nano-banana-pro/scripts/generate_image.py \
  --prompt "[ASSEMBLED PROMPT]" \
  --filename "~/Desktop/YYYY-MM-DD-card-name.png" \
  --resolution 2K \
  --api-key AIzaSyANRnoLmRWhNDm-f5jdbRz_9hKUqzzV7Y8
```

- Use `--input-image` when iterating on existing card
- Default resolution: 2K for Instagram (1K for quick drafts, 4K for final)
- Save to `~/Desktop/` or `~/.openclaw/workspace/cards/[SERIES]/`
