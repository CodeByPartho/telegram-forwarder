import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from flask import Flask
from threading import Thread

# Get from Railway environment variables
API_ID = int(os.environ['API_ID'])
API_HASH = os.environ['API_HASH']
SESSION = os.environ['SESSION_STRING']
SOURCE = os.environ['SOURCE_GROUP']
TARGET = os.environ['TARGET_GROUP']

# Telegram client
client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)

async def main():
    # Connect
    await client.connect()
    print("✅ Connected to Telegram!")
    
    # Get groups
    source_chat = await client.get_entity(SOURCE)
    target_chat = await client.get_entity(TARGET)
    
    print(f"👁️ Watching: {source_chat.title}")
    print(f"📤 Forwarding to: {target_chat.title}")
    
    # Forward messages
    @client.on(events.NewMessage(chats=source_chat))
    async def handler(event):
        await client.send_message(target_chat, event.message)
        print(f"✓ Forwarded message")
    
    # Keep running
    await client.run_until_disconnected()

# Web server to keep alive
app = Flask(__name__)
@app.route('/')
def home():
    return "Telegram Forwarder is Running!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# Start everything
if __name__ == "__main__":
    # Start web server
    Thread(target=run_flask, daemon=True).start()
    
    # Start Telegram
    asyncio.run(main())
