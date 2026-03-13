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

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## SSH

### VPS (4adclaw)
- Host: 157.22.175.174
- User: root
- Key: ~/.ssh/vps_key (в папке workspace/.ssh/)
- Connect: `ssh -i ~/.openclaw/workspace/.ssh/vps_key root@157.22.175.174`
- Claude Code: `/usr/bin/claude` (v2.1.74)
- Proxy для API: `HTTPS_PROXY=socks5://127.0.0.1:10808`
- Запуск Claude Code на VPS: `ssh -i ~/.openclaw/workspace/.ssh/vps_key root@157.22.175.174 'HTTPS_PROXY=socks5://127.0.0.1:10808 claude ...'`

---

Add whatever helps you do your job. This is your cheat sheet.
