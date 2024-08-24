import os
from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.enums import ParseMode
import logging

load_dotenv()  # take environment variables from .env.

log = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

try:
    app = Client(
        "scrapper",
        api_id=int(os.environ['API_ID']),
        api_hash=os.environ['API_HASH'],
        bot_token=os.environ['BOT_TOKEN'],
        parse_mode=ParseMode.MARKDOWN
    )

    app.run()
except KeyboardInterrupt:
    log.info("Shutting Down...")
    exit()