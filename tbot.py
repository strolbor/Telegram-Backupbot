from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import config as cf
import write, helper, commands_backup as cmdbck, commands_stor as cmdsto

# pip install python-telegram-bot

#process = subprocess.Popen(['echo'])
#print("Poll",process.poll())
externe_HDD = False

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


def main():
    updater = Updater(cf.TOKEN)

    # normale Commands
    updater.dispatcher.add_handler(CommandHandler('start', hello))
    updater.dispatcher.add_handler(CommandHandler('backup', cmdbck.backup))
    updater.dispatcher.add_handler(CommandHandler('extern', cmdbck.backup_extern))
    updater.dispatcher.add_handler(CommandHandler('status', cmdbck.status))

    # Störende Commands
    updater.dispatcher.add_handler(CommandHandler('stoer', cmdsto.stoerender, pass_args=True))
    #updater.dispatcher.add_handler(CommandHandler('status', status))

    # Debug Commands
    updater.dispatcher.add_handler(CommandHandler('unlock', cmdbck.unlock))
    updater.dispatcher.add_handler(CommandHandler('lock', cmdbck.lock))
    updater.dispatcher.add_handler(CommandHandler('test', test))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()