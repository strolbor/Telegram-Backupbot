from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

import os
import subprocess

import config as cf

#pip install python-telegram-bot

process = subprocess.Popen(['ls'])
print("Poll",process.poll())
externe_HDD = False

def write_log(text):
    print(text)
    datei_log = open('telegrambot.log','a')
    datei_log.write(text + "\n")
    datei_log.flush()
    datei_log.close()

def hello(update: Update, context: CallbackContext) -> None:
    a = f'Anfrgae von {update.effective_user.id} @ hello'
    write_log(a)
    update.message.reply_text(f'Hallo {update.effective_user.first_name}! ')

def backup(update: Update, context: CallbackContext) -> None:
    global process
    a = f'Anfrgae von {update.effective_user.id} @ backup'
    write_log(a)
    if process.poll() == 0: 
      cmd = ["/media/HDD/Backup-New/intern.sh"]
      process = subprocess.Popen(cmd)
      update.message.reply_text(f'Backup wurde gestartet.')
    else:
      update.message.reply_text(f'Backup läuft schon!')

def backupExtern(update: Update, context: CallbackContext) -> None:
    global externe_HDD
    a = f'Anfrage von {update.effective_user.id} @ backup Extern'
    write_log(a)
    global process
    if externe_HDD:
       if process.poll() == 0:
          cmd = ["/media/HDD/Backup-New/extern.sh"]
          process = subprocess.Popen(cmd)
          update.message.reply_text(f'Backup wurde gestartet.')
       else:
          update.message.reply_text(f'Backup läuft schon!')
    else:
       update.message.reply_text(f'Dieser Command ist gesperrt.')


def status(update: Update, context: CallbackContext) -> None:
     global process
     a = f'Anfrage von {update.effective_user.id} @ status'
     write_log(a)
     if process.poll() == 0:
        update.message.reply_text(f'Backup wurde nicht gestartet.')
     else:
        update.message.reply_text(f'Backup läuft schon.')

def unlock(update: Update, context: CallbackContext) -> None:
    global externe_HDD
    a = f'Anfrgae von {update.effective_user.id} @ Unlock'
    write_log(a)
    externe_HDD = True
    update.message.reply_text(f'OK!')

def lock(update: Update, context: CallbackContext) -> None:
    global externe_HDD
    a = f'Anfrgae von {update.effective_user.id} @ Lock'
    write_log(a) 
    externe_HDD = False
    update.message.reply_text(f'OK!')

updater = Updater(cf.TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', hello))
updater.dispatcher.add_handler(CommandHandler('backup', backup))
updater.dispatcher.add_handler(CommandHandler('extern', backupExtern))
updater.dispatcher.add_handler(CommandHandler('status', status))


updater.dispatcher.add_handler(CommandHandler('unlock', unlock))
updater.dispatcher.add_handler(CommandHandler('lock', lock))
updater.start_polling()
updater.idle()
