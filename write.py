from helper import delete_file
from datetime import datetime
import os

path = "/var/log/telegrambot/"

def write_log(text):
    init()
    datei_log = open(path+'telegrambot.log','a')
    datei_log.write(text + "\n")
    datei_log.flush()
    datei_log.close()

def write_id(ids):
    init()
    file_name = 'empf.id'
    delete_file(file_name)
    datei_id = open(file_name,'a')
    datei_id.write(str(ids))
    datei_id.flush()
    datei_id.close()

def write_txt(ids):
    init()
    file_name = 'save.txt'
    datei_id = open(file_name,'a')
    datei_id.write(str(ids))
    datei_id.flush()
    datei_id.close()

def write_stoer(text):
    """ Logschreiber des Nervens"""
    init()
    filename = path+"storender.txt"
    datei = open(filename,"a")
    datei.write(text+"\r\n")
    datei.flush()
    datei.close()


def init():
    """ Ordner Initalisierung"""
    if not os.path.exists(path):
        os.makedirs(path)

def getLogLine(uid,functionname) -> str:
   return f'[{str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))}] Anfrage von {uid} @ {functionname}'