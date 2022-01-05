from telegram import Update, Bot
from telegram.ext import CallbackContext
import write

def hello(update: Update, context: CallbackContext) -> None:
    a = write.getLogLine(update.effective_user.id,"Begrüßung")
    write.write_log(a)
    update.message.reply_text(f'Hallo {update.effective_user.first_name}! ')

def test(update: Update, context: CallbackContext) -> None:
    a = write.getLogLine(update.effective_user.id,"Test Command")
    write.write_log(a)
    write.write_id(f'{update.effective_user.id}')
    update.message.reply_text(f'OK! Fertig simuliert')
