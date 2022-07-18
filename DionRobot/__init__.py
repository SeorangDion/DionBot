import os, logging
from telethon import TelegramClient

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

TOKEN = os.environ.get("TOKEN", None) # Your token bot, get one from t.me/botfather


dion = TelegramClient(
        "tgbot",
        api_id=6,
        api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e"
        ).start(
                bot_token=TOKEN
                )
