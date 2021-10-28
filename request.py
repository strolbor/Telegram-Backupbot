import requests as r
import config as cf
import sys

TELEGRAM_BOT_URL = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"

#TEXT  = "Backup ist fertig"
TEXT = sys.argv[1]

r.post(TELEGRAM_BOT_URL.format(cf.TOKEN,cf.EMPF,TEXT))
