from pyrogram import filters
from utils.insta import download_instagram
import os

def insta_handler(app):
    @app.on_message(filters.text & filters.regex("instagram.com"))
    async def insta(_, msg):
        m = await msg.reply("⏳ Downloading Instagram post...\n\nIt may take some time 🫠\nPlease wait....\n\nᴩᴏᴡᴇʀᴇᴅ ʙʏ: @jb_links")

        files = download_instagram(msg.text)

        if not files:
            return await m.edit("❌ Failed to download Instagram post.")

        await m.edit(f"✅ Downloaded {len(files)} item(s)")

        for file in files:
            if file.endswith(".mp4"):
                await msg.reply_video(file)
            else:
                await msg.reply_photo(file)

            os.remove(file)
