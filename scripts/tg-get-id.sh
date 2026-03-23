#!/bin/bash
# Get Telegram user ID by username

BOT_TOKEN="8703598230:AAEuDTOBEk2jEH-QZiycKBv0I8mpphXXRx8"
USERNAME=$1

if [ -z "$USERNAME" ]; then
    echo "Usage: $0 <username>"
    echo "Example: $0 pActt"
    exit 1
fi

# Ensure username starts with @
if [[ ! "$USERNAME" =~ ^@ ]]; then
    USERNAME="@$USERNAME"
fi

# Call Telegram Bot API
RESPONSE=$(curl -s "https://api.telegram.org/bot${BOT_TOKEN}/getChat?chat_id=${USERNAME}")

# Extract ID from response
ID=$(echo "$RESPONSE" | grep -o '"id":[0-9]*' | head -1 | grep -o '[0-9]*')

if [ -z "$ID" ]; then
    echo "Error: Could not find user $USERNAME"
    echo "Response: $RESPONSE"
    exit 1
fi

echo "$ID"
