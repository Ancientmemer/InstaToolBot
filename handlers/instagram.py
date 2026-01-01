from pyrogram import filters
from utils.insta import download_instagram

def insta_handler(app):
    @app.on_message(filters.text & filters.regex("instagram.com"))
    async def insta(_, msg):
        await msg.reply("⏳ Downloading Instagram media...")
        file = download_instagram(msg.text)
        if file:
            await msg.reply_video(file)
        else:
            await msg.reply("❌ Failed to download.")
