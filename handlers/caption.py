from pyrogram import filters
from utils.captions import generate_caption

def caption_handler(app):
    @app.on_message(filters.command("caption"))
    async def caption(_, msg):
        topic = " ".join(msg.command[1:])
        if not topic:
            return await msg.reply("❌ Usage: /caption travel")
        await msg.reply(generate_caption(topic))
