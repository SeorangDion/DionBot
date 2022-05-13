import logging

from telethon import TelegramClient
from DionRobot.config import Config

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

dion = TelegramClient(
        "tgbot",
        api_id=APP_ID,
        api_hash=API_HASH
        ).start(
                bot_token=BOT_TOKEN
                )
