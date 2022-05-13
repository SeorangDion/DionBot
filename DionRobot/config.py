import os

class Config(object):
    APP_ID = os.environ.get("APP_ID", None)
    API_HASH = os.environ.get("API_HASH", None)
    TOKEN = os.environ.get("TOKEN", None)
