from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import write, helper
from datetime import datetime




def stoerender(update: Update, context: CallbackContext):
    array = update.message.text.split(" ")
    if len(array) <= 2:
        update.message.reply_text(f'Fehler. Es muss folgender Command sein: /stoer [start|stop] <Was> als einzelnes Wort.')
        update.message.reply_text(f'Es muss mindestens 2 Argumente dran sein.')
    else:
        datum = datetime.now().strftime("%d.%b.%Y  den %H:%M:%S")
        print(array)
        zu_schreiben = ""
        if array[1] == "start":
            zu_schreiben = "Am folgenden Tag {} fing folgendes: {} an".format(datum,array[2])
        elif array[1] == "stop":
            zu_schreiben = "Am folgenden Tag {} hörte folgendes: {} auf".format(datum,array[2])

        #Datei schreiben
        zu_schreiben = zu_schreiben + "\r\n"
        write.write_stoer(zu_schreiben)

        update.message.reply_text(f'Erledigt. Folgene Nachricht wurde im Log aufgenommen:')
        update.message.reply_text(f'{zu_schreiben}')

