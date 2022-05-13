import os
import logging

from telethon import TelegramClient

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


API_HASH = os.environ.get("API_HASH", None)
API_ID = os.environ.get("API_ID", None)
TOKEN = os.environ.get("TOKEN", None) # Your token bot, get one from t.me/botfather

dion = TelegramClient(
        "tgbot",
        api_id=API_ID,
        api_hash=API_HASH
        ).start(
                bot_token=TOKEN
                )
