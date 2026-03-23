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

### VPS (основной сервер)
- **Host:** 157.22.175.174
- **User:** root
- **Key:** /root/.openclaw/workspace/.ssh/vps_key
- **OS:** Ubuntu, Linux 6.8.0-101-generic
- **Disk:** 59G total, 6.4G used, 50G free
- **RAM:** 3.8G total, ~2.1G available

```bash
ssh -i /root/.openclaw/workspace/.ssh/vps_key root@157.22.175.174
```

---

Add whatever helps you do your job. This is your cheat sheet.

## SSH

### VPS (this server - 4adclaw)
- Host: 157.22.175.174
- User: root
- Key: /root/.openclaw/workspace/.ssh/vps_key
- Connect: ssh -i /root/.openclaw/workspace/.ssh/vps_key root@157.22.175.174
- Claude Code: /usr/bin/claude (v2.1.74)
- API Proxy: HTTPS_PROXY=socks5://127.0.0.1:10808

## API Keys

### OpenAI
- OPENAI_API_KEY: Set on VPS (/root/.bashrc)
- Used for: DALL-E 3 image generation
- Skill: openai-dalle3

### Telegram
- Bot Token: 8703598230:AAEuDTOBEk2jEH-QZiycKBv0I8mpphXXRx8
- Use: Get Telegram user ID by username, send messages
- API: https://api.telegram.org/bot{TOKEN}/
