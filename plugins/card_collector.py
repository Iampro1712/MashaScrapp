import logging
from pyrogram import Client
from src.parser import Parser
from src.card import parseData

log = logging.getLogger('app')

@Client.on_message()
@Client.on_edited_message()
async def collector_message(client, message):
        
    parser = Parser(message.text)
    card_parser = parseData(message.text)

    if parser.find_keyword() and card_parser['success']:
        log.info("Card found: %s", card_parser)
        log.info("Keyword: %s", parser.formated_keyword())
        # TODO: create database by using mongodb
        with open('lives.txt', 'a') as f:
            del card_parser['success']
            f.write(f'{"|".join(card_parser.values())}|{parser.formated_keyword()}\n')

    log.info("Found message: %s", message.text)