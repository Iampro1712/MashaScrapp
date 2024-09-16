import logging
from pyrogram import Client
from src.parser import Parser
from src.card import parseData
from src.sender import send

log = logging.getLogger('app')

msg_fr = None

@Client.on_message()
@Client.on_edited_message()
async def collector_message(client: Client, message):
    global msg_fr

    parser = Parser(message.text)
    card_parser = parseData(message.text)

    if parser.find_keyword() and card_parser['success']:
        log.info("Card found: %s", card_parser)
        log.info("Keyword: %s", parser.formated_keyword())
        with open('lives.txt', 'a') as f:
            del card_parser['success']
            f.write(f'{"|".join(card_parser.values())}|{parser.formated_keyword()}\n')

    log.info("\nFound message: %s", message.text)
    msg_fr = message.text
    await send(client, msg_fr)
