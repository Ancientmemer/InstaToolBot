import threading
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

# ================== UPTIME SERVER ==================
class PingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()


def run_http_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), PingHandler)
    server.serve_forever()
# ==================================================

app = Client(
    "instatoolbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

from handlers.start import start_handler
from handlers.instagram import insta_handler
from handlers.caption import caption_handler
from handlers.chat import chat_handler

start_handler(app)
insta_handler(app)
caption_handler(app)
chat_handler(app)

print("🔥 InstaToolBot Started")
app.run()
