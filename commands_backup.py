from telegram import Update
from telegram.ext import CallbackContext
import write
import subprocess

process = subprocess.Popen(["echo", "hi"])
externe_HDD = False

def backup(update: Update, context: CallbackContext) -> None:
   """Interne Backup Funktion"""
   global process
   write.write_log(write.getLogLine(update.effective_user.id,"Backup intern"))
   write.write_id(update.effective_user.id)
   if process.poll() == 0: 
      cmd = ["/media/HDD/Backup-New/intern.sh"]
      f = open(write.path+"intern.log","w")
      process = subprocess.Popen(cmd,stdout=f)
      update.message.reply_text(f'Backup wurde gestartet.')
   else:
      update.message.reply_text(f'Backup läuft schon!')

def backup_extern(update: Update, context: CallbackContext) -> None:
   """ Externes Backup Funktion"""
   global externe_HDD, process
   write.write_id(update.effective_user.id)
   write.write_log(write.getLogLine(update.effective_user.id,"Backup extern"))
   if externe_HDD:
      if process.poll() == 0:
         cmd = ["/media/HDD/Backup-New/extern.sh"]
         f = open(write.path+"extern.log","w")
         process = subprocess.Popen(cmd,stdout=f)
         update.message.reply_text(f'Backup wurde gestartet.')
      else:
         update.message.reply_text(f'Backup läuft schon!')
   else:
      update.message.reply_text(f'Dieser Command ist gesperrt.')

def status(update: Update, context: CallbackContext) -> None:
   array = update.message.text.split(" ")
   if len(array) > 1:
      if array[1] == "cron" or array[1] == "cronjob":
         status_main(update, context,write.path+"backup.txt")
      if array[1] == "extern":
         status_main(update, context,write.path+"extern.log")
      if array[1] == "intern":
         status_main(update, context,write.path+"intern.log")
   else:
      update.message.reply_text(f'Bitte als Option [cron|intern|extern] hinschreiben.')

def status_main(update: Update, context: CallbackContext,file_name_log):
     global process
     a = write.getLogLine(update.effective_user.id,"Status")
     write.write_log(a)
     write.write_id(update.effective_user.id)
     if process.poll() == 0:
        update.message.reply_text(f'Backup wurde nicht gestartet.')

        datei = open(file_name_log,"r")
        zaehler = 0
        string_pa = ""
        for raw in datei:
           zaehler = zaehler + len(raw)
           string_pa = string_pa + raw + "\r\n"
           if zaehler >= 700:
              update.message.reply_text(string_pa)
              string_pa = ""
              zaehler = 0
        if zaehler > 0:
          update.message.reply_text(string_pa)
        datei.close()
     else:
        update.message.reply_text(f'Backup läuft grade.')
        write.write_log(write.getLogLine(update.effective_user.id,"Status: Backup läuft grade."))

def unlock(update: Update, context: CallbackContext) -> None:
    global externe_HDD
    a = write.getLogLine(update.effective_user.id,"Unlock")
    write.write_log(a)
    externe_HDD = True
    update.message.reply_text(f'Fertig entsperrt!')

def lock(update: Update, context: CallbackContext) -> None:
    global externe_HDD
    a = write.getLogLine(update.effective_user.id,"Unlock")
    write.write_log(a)
    externe_HDD = False
    update.message.reply_text(f'Fertig gesperrt!')
