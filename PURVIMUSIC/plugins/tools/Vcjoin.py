from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated
import asyncio
from SONALI import app

@app.on_chat_member_updated()
async def handle_video_chat_join(client: Client, update: ChatMemberUpdated):
    if update.new_chat_member is None:
        return
    
    user = update.new_chat_member.user
    if user.is_bot:
        return

    chat_id = update.chat.id
    name = user.first_name or "Unknown"
    username = f"@{user.username}" if user.username else "No username"
    user_id = user.id

    text = f"""📹 𝐕𝐢𝐝𝐞𝐨 𝐂𝐡𝐚𝐭 𝐉𝐨𝐢𝐧𝐞𝐝!

👤 Nᴀᴍᴇ : {name}
🔗 Username : {username}
🆔 ID : {user_id}"""

    try:
        sent = await client.send_message(chat_id, text)
        await asyncio.sleep(5)
        await sent.delete()
    except Exception as e:
        print(f"[Error] Video chat join log: {e}")
