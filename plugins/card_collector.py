import logging
from pyrogram import Client
from pyrogram import filters
from src.custom import custom_keywords

log = logging.getLogger('app')

@Client.on_message()
@Client.on_edited_message()
async def collector_message(client, message):
    try:
        upper_text = message.text.upper()
    except AttributeError:
        log.info("Message not text: %s", message.text)
        return
        
    if any(keyword in upper_text for keyword in custom_keywords) == True:
        log.info("Card found: %s", message.text)
        with open('messages.txt', 'a') as f:
            f.write(f'{message.text}\n')

    log.info("Found message: %s", message.text)