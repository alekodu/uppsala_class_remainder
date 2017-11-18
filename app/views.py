import time
from flask import render_template, request, Response
from twx.botapi import Message
from app import application
from app import bot
import json

def process_text(message):
    incomming_text = message.text
    # Your code goes here
    my_response = incomming_text
    return my_response


@application.route('/')
def index():
    return "Hej"


@application.route('/time')
def show_time():
    return render_template(
        'time.html',
        now=time.strftime("%c")
    )


@application.route('/incoming', methods=['POST'])
def incoming():
    j = json.loads(request.get_data())
    m = j['message']
    msg = Message.from_result(m)
    print('Raw message:', msg)
    try:
        print('Received this message from user %d (%s): %s' % (msg.sender.id, msg.sender.first_name, msg.text))
        chat_id = msg.chat.id
        print('Responding to chat %i using token %s' % (chat_id, bot.token))
        response_text = process_text(msg)
        resp = bot.send_message(
            chat_id=chat_id,
            text=response_text,
            parse_mode=None,
            disable_web_page_preview=None,
            reply_to_message_id=None,
            reply_markup=None,
            disable_notification=False).wait()
    except Exception as e:
        print("ERROR: ", e.message)

    print("send_message returned ", resp)

    return Response(status=200)



