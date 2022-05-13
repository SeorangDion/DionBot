import os

class Config(object):
    TOKEN = os.environ.get("TOKEN", None)
