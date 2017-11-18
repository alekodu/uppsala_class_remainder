import os

from flask import Flask
from twx.botapi import TelegramBot

bot_api_key = os.environ.get('TELEGRAM_BOT_APIKEY')

bot = TelegramBot(bot_api_key)

application = Flask(__name__)

from app import views

if os.environ.get('HEROKU') is not None:
    import logging

    stream_handler = logging.StreamHandler()
    application.logger.addHandler(stream_handler)
    application.logger.setLevel(logging.DEBUG)
