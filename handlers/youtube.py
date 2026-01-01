from pyrogram import filters
from utils.yt import download_youtube
import os
from pyrogram.errors import MessageNotModified

def yt_handler(app):
    @app.on_message(filters.text & filters.regex("youtube.com|youtu.be"))
    async def yt(_, msg):
        m = await msg.reply("⏳ Downloading YouTube content...")

        file = download_youtube(msg.text)

        if file and os.path.exists(file):
            await msg.reply_video(file)
            os.remove(file)
        else:
            try:
                await m.edit("❌ YouTube video blocked on this server.\n🎧 Try audio-only or try again later.")
            except MessageNotModified:
                pass
