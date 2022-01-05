from telegram import Update
from telegram.ext import CallbackContext
import write
from datetime import datetime




def stoerender(update: Update, context: CallbackContext):
    array = update.message.text.split(" ")
    if len(array) <= 2:
        update.message.reply_text(f'Fehler. Es muss folgender Command sein: /stoer [start|stop|moment] <Was> als einzelnes Wort.')
        update.message.reply_text(f'Es muss mindestens 3 Argumente dran sein.')
    else:
        datum = update.message.date.strftime("%H:%M:%S %d.%m.%Y")
        zweiter_teil = False
        zu_schreiben = ""
        if array[1] == "start":
            zu_schreiben = "[{}] fing folgendes: {} an.".format(datum,array[2:])
            zweiter_teil = True
        elif array[1] == "stop":
            zu_schreiben = "[{}] hörte folgendes: {} auf.".format(datum,array[2:])
            zweiter_teil = True
        elif array[1] == "moment":
            zweiter_teil = True
            zu_schreiben = "[{}] hörte man folgendes: {}.".format(datum,array[2:])
        else:
            update.message.reply_text(f'Fehler das zweite Argument muss entweder "start" oder "stop" sein.')
        if zweiter_teil:
            #Datei schreiben
            write.write_stoer(zu_schreiben)
            # Nachricht schreiben
            update.message.reply_text(f'Erledigt. Folgene Nachricht wurde im Log aufgenommen: {zu_schreiben}')

