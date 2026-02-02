import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from flask import Flask
from threading import Thread

# Get from Railway environment variables
API_ID = int(os.environ['API_ID'])
API_HASH = os.environ['API_HASH']
SESSION = os.environ['SESSION_STRING']
SOURCE = os.environ['SOURCE_GROUP']
TARGET = os.environ['TARGET_GROUP']

# Create Pyrogram client
app = Client(
    "forwarder",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=SESSION
)

# Forward message function
@app.on_message(filters.chat(SOURCE))
async def forward_message(client, message: Message):
    try:
        await message.forward(TARGET)
        print(f"✓ Forwarded: {message.id}")
    except Exception as e:
        print(f"✗ Error: {e}")

async def main():
    print("Starting Telegram forwarder...")
    await app.start()
    print("✅ Connected to Telegram!")
    
    # Get chat info
    source_chat = await app.get_chat(SOURCE)
    target_chat = await app.get_chat(TARGET)
    
    print(f"👁️ Watching: {source_chat.title}")
    print(f"📤 Forwarding to: {target_chat.title}")
    print("🚀 Forwarder is active!")
    
    # Keep running
    await idle()

# Web server
flask_app = Flask(__name__)
@flask_app.route('/')
def home():
    return "Telegram Forwarder Running!"

def run_web():
    flask_app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    # Start web server
    Thread(target=run_web, daemon=True).start()
    
    # Start Telegram client
    app.run(main())
