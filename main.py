import os
import threading
from flask import Flask
from pyrogram import Client, filters
from pyrogram.types import Message

# ──────────────────────────────────────────────
# 🔑  ENV VARIABLES
# ──────────────────────────────────────────────
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Koyeb sets PORT automatically; default 8000 for local run
PORT = int(os.getenv("PORT", "8000"))

# ──────────────────────────────────────────────
# 🌐  Minimal Flask app for health-check
# ──────────────────────────────────────────────
flask_app = Flask(__name__)

@flask_app.route("/", methods=["GET", "HEAD"])
def index():
    return "✓ Bot is alive!", 200

def run_web():
    """Start Flask in a separate thread so it doesn't block the bot."""
    flask_app.run(host="0.0.0.0", port=PORT)

threading.Thread(target=run_web, daemon=True).start()

# ──────────────────────────────────────────────
# 🤖  Telegram Bot (Pyrogram)
# ──────────────────────────────────────────────
app = Client(
    "auto_reply_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

START_TEXT = """
👋 𝐇𝐞𝐥𝐥𝐨 {mention}!

আমি অটো-পোস্ট-জেনারেটর বট 🤖  
যে কোনো মুভি-টাইটেল বা ছবি পাঠালে নিজে থেকে ফরম্যাটেড পোস্ট বানিয়ে রেপ্লাই করবো।

• শুধু ছবি পাঠালে — সেই ছবিই থাকবে  
• শুধু টেক্সট পাঠালে — লোগো ছাড়া টেক্সট ফরম্যাট করবো  
"""

REPLY_TEMPLATE = """
🎬 @PrimeCineHub {caption}

━━━━━━━━━━━━━━━━━━
📥 ᴛᴇʟᴇɢʀᴀᴍ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ғɪʟᴇ 📥
━━━━❰ 📺 ᴠɪᴅᴇᴏ ǫᴜᴀʟɪᴛʏ 📺 ❱━━⊱

📁 480ᴘ
🔗 

📁 720ᴘ
🔗 

📁 1080ᴘ
🔗 

╭━❰ 📚 ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴛᴜᴛᴏʀɪᴀʟ ᴠɪᴅᴇᴏ 🎥 ❱━⊱
┃      <a href='https://t.me/Prime_Movie_Watch_Dawnload/71'>👉 🔴 ʜᴏᴡ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ 🔴 👈</a>
╰━━━━━━━━━━━━━━━━⊱

💬 ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ & ɢʀᴏᴜᴘꜱ
🔗✇ https://t.me/addlist/ceobDOjc7202ZmVl

━━━━━━━━━━━━━━━━━━
🔔 ꜱᴛᴀʏ ᴛᴜɴᴇᴅ ꜰᴏʀ ᴍᴏʀᴇ ᴜᴘᴅᴀᴛᴇꜱ
📽️ ɴᴇᴡ ᴍᴏᴠɪᴇꜱ, ꜱᴇʀɪᴇꜱ & ᴍᴏʀᴇ ᴇᴠᴇʀʏ ᴅᴀʏ!
📩 ᴡᴇ'ʀᴇ ʜᴇʀᴇ ᴛᴏ ᴅᴇʟɪᴠᴇʀ ᴛʜᴇ ʙᴇꜱᴛ ᴇɴᴛᴇʀᴛᴀɪɴᴍᴇɴᴛ!
"""

# ──────────────────────────────────────────────
# 📜  Handlers
# ──────────────────────────────────────────────

@app.on_message(filters.private & filters.command("start"))
async def start_cmd(_, message: Message):
    await message.reply_text(
        START_TEXT.format(mention=message.from_user.mention),
        disable_web_page_preview=True
    )

@app.on_message(filters.private & (filters.photo | filters.text))
async def auto_reply(_, message: Message):
    # Skip if this is the /start command itself
    if message.text and message.text.startswith("/"):
        return

    caption = (message.caption or message.text or "Untitled").strip()
    reply_text = REPLY_TEMPLATE.format(caption=caption)

    if message.photo:
        await message.reply_photo(message.photo.file_id, caption=reply_text)
    else:
        await message.reply_text(reply_text)

# ──────────────────────────────────────────────
# 🚀  Run bot
# ──────────────────────────────────────────────
app.run()
