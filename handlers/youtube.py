from pyrogram import filters
from utils.yt import download_youtube
import os

def yt_handler(app):
    @app.on_message(filters.text & filters.regex("youtube.com|youtu.be"))
    async def yt(_, msg):
        m = await msg.reply("⏳ Downloading YouTube video...")
        file = download_youtube(msg.text)

        if file and os.path.exists(file):
            await msg.reply_video(file)
            os.remove(file)
        else:
            await m.edit("❌ Failed to download YouTube video.")
