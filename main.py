import os
import asyncio
from pyrogram import Client, filters, idle
from pyrogram.types import Message
from flask import Flask
from threading import Thread

# Environment variables (e.g. Railway, Render, or local .env)
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

# Forward message handler
@app.on_message(filters.chat(SOURCE))
async def forward_message(client, message: Message):
    try:
        await message.forward(TARGET)
        print(f"-> Forwarded message ID: {message.id}")
    except Exception as e:
        print(f"!! Forward error: {e}")

async def main():
    print("Starting Telegram forwarder...")
    await app.start()
    print("✓ Connected to Telegram!")
    
    # Get chat info
    source_chat = await app.get_chat(SOURCE)
    target_chat = await app.get_chat(TARGET)
    
    print(f"👀 Watching source: {source_chat.title}")
    print(f"📢 Forwarding target: {target_chat.title}")
    print("🚀 Forwarder is active!")
    
    # Keep running until interrupted
    await idle()

# Health check web server for cloud platforms (e.g., Railway/Koyeb/Render)
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Telegram Forwarder Active"

def run_web():
    port = int(os.environ.get("PORT", 8080))
    flask_app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    # Start web server for cloud container health checks
    Thread(target=run_web, daemon=True).start()
    
    # Start Telegram client event loop
    app.run(main())
