from telegram import Update
from telegram.ext import CallbackContext
import write

def hello(update: Update, context: CallbackContext) -> None:
    a = f'Anfrgae von {update.effective_user.id} @ hello'
    write.write_log(a)
    update.message.reply_text(f'Hallo {update.effective_user.first_name}! ')

def test(update: Update, context: CallbackContext) -> None:
    ids = f'{update.effective_user.id}'
    a = f'Anfrage von {ids} @ test'
    write.write_log(a)
    write.write_id(ids)
    update.message.reply_text(f'OK! Fertig simuliert')
