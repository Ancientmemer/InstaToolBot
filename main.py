from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "instatoolbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

from handlers.start import start_handler
from handlers.instagram import insta_handler
from handlers.youtube import yt_handler
from handlers.caption import caption_handler
from handlers.chat import chat_handler

start_handler(app)
insta_handler(app)
yt_handler(app)
caption_handler(app)
chat_handler(app)

print("🔥 InstaToolBot Started")
app.run()
