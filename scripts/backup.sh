#!/bin/bash
# Backup OpenClaw workspace
BACKUP_DIR="/root/.openclaw/backups"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M")
ARCHIVE="$BACKUP_DIR/workspace_$TIMESTAMP.tar.gz"

mkdir -p "$BACKUP_DIR"

tar -czf "$ARCHIVE" \
  -C /root/.openclaw \
  workspace \
  2>/dev/null

# Keep only last 7 backups
ls -t "$BACKUP_DIR"/workspace_*.tar.gz 2>/dev/null | tail -n +8 | xargs rm -f

echo "Backup done: $ARCHIVE"
