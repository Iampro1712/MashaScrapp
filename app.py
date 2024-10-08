import os
from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.enums import ParseMode
import logging

load_dotenv(dotenv_path="PATH")  # take environment variables from .env.

log = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

try:
    app = Client(
        "scrapper",
        api_id=int(os.environ['API_ID']),
        api_hash=os.environ['API_HASH'],
        phone_number=os.environ['PHONE_NUMBER'],
        parse_mode=ParseMode.MARKDOWN,
        plugins=dict(
            root="plugins"
        )
    )

    log.info("Running...")
    app.run()
except KeyboardInterrupt:
    log.info("Shutting Down...")
    exit()