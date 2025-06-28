from PURVIMUSIC import app
from pyrogram import Client
from pyrogram.raw import functions
from pyrogram.raw.types import UpdateGroupCallParticipants
from pyrogram.types import Message
import asyncio

@app.on_raw_update()
async def video_chat_join_raw_handler(client: Client, update):
    if isinstance(update, UpdateGroupCallParticipants):
        chat_id = update.chat_id

        for participant in update.participants:
            if not participant.user_id:
                continue  # skip bots or unknowns

            try:
                user = await client.get_users(participant.user_id)
                name = user.first_name or "Unknown"
                username = f"@{user.username}" if user.username else "No username"
                user_id = user.id

                text = f"""📹 𝐕𝐢𝐝𝐞𝐨 𝐂𝐡𝐚𝐭 𝐉𝐨𝐢𝐧𝐞𝐝!

👤 Nᴀᴍᴇ : {name}
🔗 Username : {username}
🆔 ID : {user_id}"""

                # send message in group where VC is happening
                sent: Message = await client.send_message(chat_id, text)
                await asyncio.sleep(6)
                await sent.delete()

            except Exception as e:
                print(f"[VideoChat RAW Handler Error] {e}")

