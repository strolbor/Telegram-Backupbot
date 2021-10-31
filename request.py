import requests as r
import config as cf
import argparse
from datetime import datetime


TELEGRAM_BOT_URL = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"

# Arugument PArser initalisieren
all_args = argparse.ArgumentParser()
# Telegram ID angeben
all_args.add_argument("-id", "--telegram-id", required=True,
   help="Telegram")
   # Nachrichten Text eingabe in ""
all_args.add_argument("-txt", "--text", required=True,
   help='Diese Telegram Nachricht muss in "" stehen.')
   #Debug Mode aktivieren
all_args.add_argument("-debug", "--debugging", required=False,
   help="Sendet eine 2. Nachricht an den in der Config stehenden Empfänger.")

#Arugment zu dict Objekt
args = vars(all_args.parse_args())

# Arguemente sortieren
TEXT = str(args['text'])
EMPFÄNGER = str(args['telegram_id'])
# 1. Nachricht senden
first = r.post(TELEGRAM_BOT_URL.format(cf.TOKEN,EMPFÄNGER,TEXT))

# Debug Nachricht senden
if str(args['debugging']) != "None":
  datum = datetime.now().strftime("%d.%b.%Y um %H %M %S")
  DEBUG_TXT = "Die Nachricht vom {} an die ID {} ergab folgenden Statuscode: {}.".format(datum,EMPFÄNGER,first.status_code)
  
  ras = r.post(TELEGRAM_BOT_URL.format(cf.TOKEN,cf.EMPF,DEBUG_TXT))
