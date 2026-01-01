from pyrogram import filters

def start_handler(app):
    @app.on_message(filters.command("start"))
    async def start(_, msg):
        await msg.reply(
            "🔥 **InstaToolBot**\n\n"
            "📥 Instagram Reel/Post Downloader\n"
            "🏷️ Caption + Hashtag Generator Use /caption\n"
            "🤖 Smart Auto Reply\n\n"
            "Send an instagram link to begin!"
        )
