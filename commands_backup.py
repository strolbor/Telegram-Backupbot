from telegram import Update
from telegram.ext import CallbackContext
import write
import subprocess
import os


process = subprocess.Popen(["echo", "hi"])
externe_HDD = False

def backup(update: Update, context: CallbackContext) -> None:
   """Interne Backup Funktion"""
   global process
   a = write.getLogLine(update.effective_user.id,"Backup intern")
   write.write_log(a)
   write.write_id(update.effective_user.id)
   if process.poll() == 0: 
      cmd = ["/media/HDD/Backup-New/intern.sh"]
      f = open("log.txt","w")
      process = subprocess.Popen(cmd,stdout=f)
      update.message.reply_text(f'Backup wurde gestartet.')
   else:
      update.message.reply_text(f'Backup läuft schon!')

def backup_extern(update: Update, context: CallbackContext) -> None:
   """ Externes Backup Funktion"""
   global externe_HDD
   a = write.getLogLine(update.effective_user.id,"Backup extern")
   write.write_id(update.effective_user.id)
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
     a = write.getLogLine(update.effective_user.id,"Status")
     write.write_log(a)
     write.write_id(update.effective_user.id)
     if process.poll() == 0:
        update.message.reply_text(f'Backup wurde nicht gestartet.')
        path = "/var/log/telegrambot/"
        if not os.path.exists(path):
           os.makedirs(path)
        datei = open(path+"log.txt","r")
        zahler = 0
        string_pa = ""
        for raw in datei:
           zahler = zahler + len(raw)
           string_pa = string_pa + raw + "\r\n"
           if zahler >= 700:
              update.message.reply_text(string_pa)
              string_pa = ""
              zahler = 0
        if zahler > 0:
          update.message.reply_text(string_pa)
        datei.close()
     else:
        update.message.reply_text(f'Backup läuft grade.')
        a = write.getLogLine(update.effective_user.id,"Status: Backup läuft grade.")
        write.write_log(a)

def unlock(update: Update, context: CallbackContext) -> None:
    global externe_HDD
    a = write.getLogLine(update.effective_user.id,"Unlock")
    write.write_log(a)
    externe_HDD = True
    update.message.reply_text(f'Fertig entsperrt!')

def lock(update: Update, context: CallbackContext) -> None:
    global externe_HDD
    a = getLogLine(update.effective_user.id,"Unlock")
    write.write_log(a)
    externe_HDD = False
    update.message.reply_text(f'Fertig gesperrt!')
