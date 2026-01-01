from pyrogram import filters
import json
import os

# 🔴 CHANGE THIS TO YOUR TELEGRAM USER ID
OWNER_ID = 123456789  

USERS_FILE = "database/users.json"


# -------------------------
# Helpers
# -------------------------
def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)


def add_user(user_id):
    users = load_users()
    if user_id not in users:
        users.append(user_id)
        save_users(users)


# -------------------------
# Handlers
# -------------------------
def owner_handler(app):

    # 🔹 Track users (call this on any message)
    @app.on_message(filters.private)
    async def track_users(_, msg):
        add_user(msg.from_user.id)


    # 🔹 /stats
    @app.on_message(filters.command("stats") & filters.user(OWNER_ID))
    async def stats(_, msg):
        users = load_users()
        await msg.reply(
            f"📊 **Bot Stats**\n\n"
            f"👤 Total Users: `{len(users)}`"
        )


    # 🔹 /broadcast (reply based)
    @app.on_message(filters.command("broadcast") & filters.user(OWNER_ID))
    async def broadcast(_, msg):

        if not msg.reply_to_message:
            return await msg.reply(
                "❌ **Usage:** Reply to a message and type `/broadcast`"
            )

        users = load_users()
        success = 0
        failed = 0

        for user_id in users:
            try:
                await msg.reply_to_message.copy(user_id)
                success += 1
            except:
                failed += 1

        await msg.reply(
            f"📣 **Broadcast Completed**\n\n"
            f"✅ Sent: `{success}`\n"
            f"❌ Failed: `{failed}`"
        )
