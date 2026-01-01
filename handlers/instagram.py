from pyrogram import filters
from utils.insta import download_instagram
import os

def insta_handler(app):
    @app.on_message(filters.text & filters.regex("instagram.com"))
    async def insta(_, msg):
        m = await msg.reply("⏳ Downloading Instagram media...")
        file = download_instagram(msg.text)

        if file and os.path.exists(file):
            await msg.reply_video(file)
            os.remove(file)
        else:
            await m.edit("❌ Failed to download Instagram media.")
