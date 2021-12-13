from telegram import Update
from telegram.ext import CallbackContext
import write
import subprocess

process = subprocess.Popen(["echo", "hi"])
externe_HDD = False

def backup(update: Update, context: CallbackContext) -> None:
    global process
    ids = f'{update.effective_user.id}'
    a = f'Anfrage von {ids} @ backup Extern'
    write.write_log(a)
    write.write_id(ids)
    if process.poll() == 0: 
      cmd = ["/media/HDD/Backup-New/intern.sh"]
      f = open("log.txt","w")
      process = subprocess.Popen(cmd,stdout=f)
      update.message.reply_text(f'Backup wurde gestartet.')
    else:
      update.message.reply_text(f'Backup läuft schon!')

def backup_extern(update: Update, context: CallbackContext) -> None:
    global externe_HDD
    ids = f'{update.effective_user.id}'
    a = f'Anfrage von {ids} @ backup Extern'
    write.write_id(ids)
    write.write_log(a)
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
     write.write_log(a)
     if process.poll() == 0:
        update.message.reply_text(f'Backup wurde nicht gestartet.')
        datei = open("log.txt","r")
        zahler = 0
        string_pa = ""
        for raw in datei:
           zahler = zahler + len(raw)
           string_pa = string_pa + raw + "\r\n"
           if zahler >= 250:
              update.message.reply_text(string_pa)
              string_pa = ""
              print("Zahler:",zahler)
              zahler = 0
              print("Schon gesendet")
        if zahler > 0:
          update.message.reply_text(string_pa)
        datei.close()
        print(zahler)
     else:
        update.message.reply_text(f'Backup läuft grade.')

def unlock(update: Update, context: CallbackContext) -> None:
    global externe_HDD
    a = f'Anfrgae von {update.effective_user.id} @ Unlock'
    write.write_log(a)
    externe_HDD = True
    update.message.reply_text(f'OK!')

def lock(update: Update, context: CallbackContext) -> None:
    global externe_HDD
    a = f'Anfrgae von {update.effective_user.id} @ Lock'
    write.write_log(a) 
    externe_HDD = False
    update.message.reply_text(f'OK!')
