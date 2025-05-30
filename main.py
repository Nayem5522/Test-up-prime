from pyrogram import Client, filters
from pyrogram.types import Message
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("auto_reply_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

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

@app.on_message(filters.private & (filters.photo | filters.text))
async def auto_reply(client: Client, message: Message):
    caption = message.caption or message.text or "No Title Found"
    reply_text = REPLY_TEMPLATE.format(caption=caption.strip())

    if message.photo:
        await message.reply_photo(photo=message.photo.file_id, caption=reply_text)
    else:
        await message.reply_text(reply_text)

app.run()
