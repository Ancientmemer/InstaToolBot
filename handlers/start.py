from pyrogram import filters

def start_handler(app):
    @app.on_message(filters.command("start"))
    async def start(_, msg):
        await msg.reply(
            "🔥 **Multi Social media downloader**\n\n"
            "📥 Instagram Reel/Post Downloader\n"
            "▶️ Youtube Video downloader\n"
            "🏷️ Instagram Caption + Hashtag Generator Use /caption\n"
            "🤖 Smart Auto Reply\n\n"
            "Send a link to begin!\n\n"
            "ᴩᴏᴡᴇʀᴇᴅ ʙʏ: @jb_links
        )
