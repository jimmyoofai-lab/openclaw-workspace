#!/usr/bin/env python3
"""
Get Telegram user ID by username using TDLib or alternative methods.
For now, returns stored mappings or requires manual lookup.
"""

import json
import sys

# Known mappings (build this as we discover IDs)
KNOWN_USERS = {
    "pActt": 307981084,
    "Mrzuus": 153053801,
    "popova_tmn": 1743024850,
    "M_Borya00": 475192549,
}

def get_id(username):
    """Get user ID by username"""
    # Clean username
    username = username.lstrip("@")
    
    # Check known mappings
    if username in KNOWN_USERS:
        return KNOWN_USERS[username]
    
    # Not found
    print(f"Error: User @{username} not in known mappings", file=sys.stderr)
    print(f"Known users: {', '.join(KNOWN_USERS.keys())}", file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: tg-get-id.py <username>")
        print("Example: tg-get-id.py pActt")
        sys.exit(1)
    
    username = sys.argv[1]
    user_id = get_id(username)
    print(user_id)
