import json

from machine import pdf_

def start(update, context):
    update.message.reply_text('''Hi! It's pdfify here. I can make your boring pdf to an awesome audiobook..
Just upload the pdf after this message.
    ''')


def help(update, context):
    update.message.reply_text('Help is always there')


def echo(update, context):
    chat_id = update["message"]["chat"]["id"]

    update.message.reply_text('The pdf file is recieved. I am working on it.')
    context.bot.get_file(update.message.document).download(custom_path=r'X:\Code\Python\pdfify\db\main.pdf')
    pdf_()
    update.message.reply_text('Your audio file is ready')
    context.bot.send_audio(chat_id=chat_id, audio=open('X:\Code\Python\pdfify\output\generatedspeech.mp3','rb'))
    