import logging

from telethon import TelegramClient
from DionRobot.config import Config

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

dion = TelegramClient(
        "tgbot",
        api_id=14624642,
        api_hash="23c93aa64d16911f521bd0b16291af57"
        ).start(
                bot_token=TOKEN
                )
