import os
import logging
from pyrogram import Client
from src.parser import Parser
from src.card import parseData

log = logging.getLogger('app')

@Client.on_message()
@Client.on_edited_message()
async def collector_message(client: Client, message):

    parser = Parser(message.text)
    card_parser = parseData(message.text)

    if parser.find_keyword() and card_parser['success']:
        log.info("Card found: %s", card_parser)
        log.info("Keyword: %s", parser.formated_keyword())
        await client.send_message(os.getenv('CHANNEL_ID'), f'Card found: {card_parser}\nResult: {parser.formated_keyword()}')
        with open('lives.txt', 'a') as f:
            del card_parser['success']
            f.write(f'{"|".join(card_parser.values())}|{parser.formated_keyword()}\n')