import requests as r
import config as cf
import argparse
from datetime import datetime


TELEGRAM_BOT_URL = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
def sendmsg(receiver: str, text: str):
   # 1. Nachricht senden
   r.post(TELEGRAM_BOT_URL.format(cf.TOKEN,receiver,text))



if __name__ == '__main__':
   # Arugument PArser initalisieren
   all_args = argparse.ArgumentParser()
   # Telegram ID angeben
   all_args.add_argument("-id", "--telegram-id", required=True,
      help="Telegram")
      # Nachrichten Text eingabe in ""
   all_args.add_argument("-txt", "--text", required=True,
      help='Diese Telegram Nachricht muss in "" stehen.')
      #Debug Mode aktivieren

   #Arugment zu dict Objekt
   args = vars(all_args.parse_args())

   # Arguemente sortieren
   TEXT = str(args['text'])
   EMPFÄNGER = str(args['telegram_id'])
   sendmsg(EMPFÄNGER,TEXT)