<div align="center">

 <h1>Telegram Auto-Forwarder</h1>

  <p><b>High-Speed Asynchronous Channel & Group Forwarding Bot</b></p>

  <p>
    An automated Python service built on the MTProto Pyrogram framework and TgCrypto that streams and relays incoming messages, media, and documents between Telegram channels or groups in real time.
  </p>

  <p>
    <a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.11" /></a>
    <a href="https://docs.pyrogram.org"><img src="https://img.shields.io/badge/Pyrogram-2.0-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Pyrogram" /></a>
    <a href="https://www.docker.com"><img src="https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker" /></a>
    <a href="https://flask.palletsprojects.com"><img src="https://img.shields.io/badge/Flask-Healthcheck-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" /></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License" /></a>
  </p>

</div>

---

## Overview

**Telegram Auto-Forwarder** is a resilient background daemon that monitors source Telegram channels, supergroups, or chats and instantly clones/forwards messages to a target channel. 

Equipped with a built-in lightweight Flask health-check endpoint, it is turnkey ready for 24/7 cloud container deployments on platforms like **Railway**, **Render**, **Koyeb**, or **Fly.io** without getting stopped for lack of open HTTP ports.

---

## Key Features

- **Instant Event-Driven Relay** — Built on Pyrogram's asynchronous event loop with C-accelerated cryptographic processing (`tgcrypto`).
- **Media & Formatting Retention** — Forwards all message types including text, photos, video files, voice notes, stickers, and documents with markup intact.
- **Dockerized Deployment** — Containerized with a minimal `python:3.11-slim` footprint for rapid 1-click cloud deployments.
- **Cloud Health-Check Server** — Integrated non-blocking Flask web server responding to HTTP health pings to keep cloud dynos alive.
- **String Session Support** — Authenticates using Pyrogram String Sessions, eliminating the need to commit sensitive SQLite `.session` files to version control.

---

## Tech Stack

| Layer | Technology | Purpose |
| :--- | :--- | :--- |
| **Framework** | [Pyrogram 2.0](https://docs.pyrogram.org) | Asynchronous Telegram MTProto API framework |
| **Crypto Acceleration** | [TgCrypto](https://github.com/pyrogram/tgcrypto) | Fast C-extensions for MTProto payload encryption/decryption |
| **Web Server** | [Flask 3.0](https://flask.palletsprojects.com) | HTTP health-check endpoint for cloud hosting |
| **Containerization** | [Docker](https://www.docker.com) | Multi-arch container image based on `python:3.11-slim` |

---

## Getting Started

### Prerequisites
- **Python**: `>= 3.10`
- **Telegram API Credentials**: `API_ID` & `API_HASH` from [my.telegram.org](https://my.telegram.org)
- **Pyrogram String Session**: Generated using `Client.export_session_string()`

### Local Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/CodeByPartho/telegram-forwarder.git
   cd telegram-forwarder
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set environment variables**:
   Create a `.env` file or export in your shell:
   ```bash
   export API_ID="1234567"
   export API_HASH="your_telegram_api_hash"
   export SESSION_STRING="your_pyrogram_string_session"
   export SOURCE_GROUP="-1001234567890"
   export TARGET_GROUP="-1009876543210"
   export PORT="8080"
   ```

4. **Run the bot**:
   ```bash
   python main.py
   ```

---

## Docker Deployment

Build and run using Docker:
```bash
docker build -t telegram-forwarder .
docker run -d --env-file .env -p 8080:8080 telegram-forwarder
```

---

## License

This project is licensed under the **[MIT License](LICENSE)**.

---

<p align="center">Built by Partho</p>
