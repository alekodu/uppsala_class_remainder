#!/usr/bin/python
import os

from twx.botapi import InputFileInfo, InputFile

from app import application
from app import bot


def init_heroku_logging():
    import logging
    stream_handler = logging.StreamHandler()
    application.logger.addHandler(stream_handler)
    application.logger.setLevel(logging.DEBUG)


def get_certificate():
    certificate_path = 'app/ssl-certificate.herokuapp-com.pem'
    fp = open(certificate_path, 'rb')
    file_info = InputFileInfo(
        file_name=certificate_path,
        fp=fp,
        mime_type='text/plain')
    return InputFile('certificate', file_info)


def init_bot(telegram_bot):
    telegram_bot.update_bot_info().wait()
    print('Starting bot %s' % telegram_bot.username)
    certificate = get_certificate()
    telegram_bot.set_webhook(
        url='https://morning-chamber-85976.herokuapp.com/incoming',
        certificate=certificate,
    ).wait()
    print('Webhook configured')


if os.environ.get('HEROKU') is not None:
    init_heroku_logging()

try:
    init_bot(bot)
except Exception as e:
    print(e)
