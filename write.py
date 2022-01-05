from helper import delete_file
from datetime import datetime

path = "/var/log/telegrambot/"

def write_log(text):
    print(text)
    datei_log = open(path+'telegrambot.log','a')
    datei_log.write(text + "\n")
    datei_log.flush()
    datei_log.close()

def write_id(ids):
    file_name = 'empf.id'
    delete_file(file_name)
    datei_id = open(file_name,'a')
    datei_id.write(ids)
    datei_id.flush()
    datei_id.close()

def write_stoer(text):
    filename = "storender.txt"
    datei = open(filename,"a")
    datei.write(text+"\r\n")
    datei.flush()
    datei.close()

def getLogLine(uid,functionname) -> str:
   return f'[{str(datetime.now().strftime("%H:%M:%S %d.%m.%Y"))}] Anfrage von {uid} @ {functionname}'