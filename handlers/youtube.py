from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.yt import download_youtube
import os

def yt_handler(app):

    # Step 1: When user sends YouTube link
    @app.on_message(filters.text & filters.regex("youtube.com|youtu.be"))
    async def yt_link(_, msg):
        url = msg.text.strip()

        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("🎥 Video", callback_data=f"yt_video|{url}"),
                InlineKeyboardButton("🎧 Audio", callback_data=f"yt_audio|{url}")
            ]
        ])

        await msg.reply(
            "👇 **Choose download format**",
            reply_markup=keyboard
        )

    # Step 2: Handle button click
    @app.on_callback_query(filters.regex("^yt_"))
    async def yt_callback(_, cq):
        data = cq.data.split("|")
        mode = data[0].replace("yt_", "")
        url = data[1]

        await cq.message.edit("⏳ Downloading...\nIt may take some time 🫠\nPlease wait....\n\nᴩᴏᴡᴇʀᴇᴅ ʙʏ: @jb_links")

        file = download_youtube(url, mode=mode)

        if not file or not os.path.exists(file):
            return await cq.message.edit("❌ Download failed")

        if mode == "audio":
            await cq.message.reply_audio(file)
        else:
            await cq.message.reply_video(file)

        os.remove(file)
