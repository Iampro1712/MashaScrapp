import os
from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.enums import ParseMode
import logging
from pyrogram import filters
from src.custom import custom_keywords

load_dotenv()  # take environment variables from .env.

log = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO)

try:
    app = Client(
        "scrapper",
        api_id=int(os.environ['API_ID']),
        api_hash=os.environ['API_HASH'],
        phone_number=os.environ['PHONE_NUMBER'],
        parse_mode=ParseMode.MARKDOWN
    )

    @app.on_message(filters.chat())
    @app.on_edited_message()
    async def collector_message(client, message):
        try:
            upper_text = message.text.upper()
        except AttributeError:
            log.info("Message not text: %s", message.text)
            return
        
        if any(keyword in upper_text for keyword in custom_keywords) == True:
            log.info("Found message with keywork: %s", message.text)
            with open('messages.txt', 'a') as f:
                f.write(f'{message.text}\n')

        log.info("Found message: %s", message.text)

    app.run()
except KeyboardInterrupt:
    log.info("Shutting Down...")
    exit()