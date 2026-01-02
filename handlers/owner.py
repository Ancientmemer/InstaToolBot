from pyrogram import filters
from pymongo import MongoClient
import os

# 🔴 CHANGE THIS
OWNER_ID = 8336106518  # your Telegram ID

# 🔴 MongoDB URI (add in env)
MONGO_URI = os.getenv("MONGO_URI")

# -------------------------
# MongoDB Setup
# -------------------------
mongo = MongoClient(MONGO_URI)
db = mongo["instatoolbot"]
users_col = db["users"]


def owner_handler(app):

    # -------------------------
    # AUTO SAVE USERS
    # -------------------------
    @app.on_message(filters.private)
    async def save_user(_, msg):
        user_id = msg.from_user.id
        users_col.update_one(
            {"user_id": user_id},
            {"$set": {"user_id": user_id}},
            upsert=True
        )

    # -------------------------
    # /stats
    # -------------------------
    @app.on_message(filters.command("stats") & filters.user(OWNER_ID))
    async def stats(_, msg):
        total = users_col.count_documents({})
        await msg.reply(
            f"📊 **Bot Statistics**\n\n"
            f"👤 Total Users: `{total}`"
        )

    # -------------------------
    # /broadcast (reply based)
    # -------------------------
    @app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
    async def broadcast(_, msg):

        if not msg.reply_to_message:
            return await msg.reply(
                "❌ **Reply to a message and use `/broadcast`**"
            )

        sent = 0
        failed = 0

        for user in users_col.find({}):
            try:
                await msg.reply_to_message.copy(user["user_id"])
                sent += 1
            except:
                failed += 1

        await msg.reply(
            f"📣 **Broadcast Completed**\n\n"
            f"✅ Sent: `{sent}`\n"
            f"❌ Failed: `{failed}`"
        )
