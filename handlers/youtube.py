from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.yt import download_youtube
import os

def yt_handler(app):

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

    @app.on_callback_query(filters.regex("^yt_"))
    async def yt_callback(_, cq):
        mode, url = cq.data.split("|")

        mode = mode.replace("yt_", "")
        await cq.message.edit("⏳ Downloading...")

        file = download_youtube(url, mode)

        if not file or not os.path.exists(file):
            return await cq.message.edit("❌ Download failed")

        if mode == "audio":
            await cq.message.reply_audio(file)
        else:
            await cq.message.reply_video(file)

        os.remove(file)
