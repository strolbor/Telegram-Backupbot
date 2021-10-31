from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import config as cf
import write, helper, commands_backup as cmdbck, commands_stor as cmdsto, commands as cmd

# pip install python-telegram-bot




def main():
    updater = Updater(cf.TOKEN)

    # normale Commands
    updater.dispatcher.add_handler(CommandHandler('start', cmd.hello))
    updater.dispatcher.add_handler(CommandHandler('backup', cmdbck.backup))
    updater.dispatcher.add_handler(CommandHandler('extern', cmdbck.backup_extern))
    updater.dispatcher.add_handler(CommandHandler('status', cmdbck.status))

    # Störende Commands
    updater.dispatcher.add_handler(CommandHandler('stoer', cmdsto.stoerender, pass_args=True))
    #updater.dispatcher.add_handler(CommandHandler('status', status))

    # Debug Commands
    updater.dispatcher.add_handler(CommandHandler('unlock', cmdbck.unlock))
    updater.dispatcher.add_handler(CommandHandler('lock', cmdbck.lock))
    updater.dispatcher.add_handler(CommandHandler('test', cmd.test))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()