from pyrogram import filters

def start_handler(app):
    @app.on_message(filters.command("start"))
    async def start(_, msg):
        await msg.reply(
            "🔥 **InstaToolBot**\n\n"
            "📥 Instagram Reel/Post Downloader\n"
            "▶️ YouTube Video/Audio Downloader\n"
            "🏷️ Caption + Hashtag Generator\n"
            "🤖 Smart Auto Reply\n\n"
            "Send a link or use commands!"
        )
