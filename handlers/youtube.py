from pyrogram import filters
from utils.yt import download_youtube

def yt_handler(app):
    @app.on_message(filters.text & filters.regex("youtube.com|youtu.be"))
    async def yt(_, msg):
        await msg.reply("⏳ Downloading YouTube video...")
        file = download_youtube(msg.text)
        if file:
            await msg.reply_video(file)
        else:
            await msg.reply("❌ Failed to download.")
