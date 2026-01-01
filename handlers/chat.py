from pyrogram import filters
from utils.replies import smart_reply

def chat_handler(app):
    @app.on_message(filters.text & ~filters.command(["start", "caption"]))
    async def chat(_, msg):
        reply = smart_reply(msg.text)
        if reply:
            await msg.reply(reply)
