import os
from pyrogram import Client
from dotenv import load_dotenv

load_dotenv()

ch_id = os.environ("CHANNEL_ID")

async def send(client: Client, message: str):
    await client.send_message(ch_id, message)
