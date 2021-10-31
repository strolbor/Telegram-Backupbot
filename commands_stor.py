from telegram import Update
from telegram.ext import CallbackContext
import write
from datetime import datetime




def stoerender(update: Update, context: CallbackContext):
    array = update.message.text.split(" ")
    if len(array) <= 2:
        update.message.reply_text(f'Fehler. Es muss folgender Command sein: /stoer [start|stop] <Was> als einzelnes Wort.')
        update.message.reply_text(f'Es muss mindestens 3 Argumente dran sein.')
    else:
        datum = datetime.now().strftime("%d.%b.%Y  um %H:%M:%S")
        print(array)
        zweiter_teil = False
        zu_schreiben = ""
        if array[1] == "start":
            zu_schreiben = "Am folgenden Tag {} fing folgendes: >{}< an".format(datum,array[2:])
            zweiter_teil = True
        elif array[1] == "stop":
            zu_schreiben = "Am folgenden Tag {} hörte folgendes: >{}< auf".format(datum,array[2:])
            zweiter_teil = True
        elif array[1] == "moment":
            zweiter_teil = True
            zu_schreiben = "Am folgenden Tag {} hörte man folgendes: >{}<".format(datum,array[2:])
        else:
            update.message.reply_text(f'Fehler das zweite Argument muss entweder "start" oder "stop" sein.')

        if zweiter_teil:
            #Datei schreiben
            zu_schreiben = zu_schreiben 

            write.write_stoer(zu_schreiben)
            print(zu_schreiben)

            # Nachricht schreiben
            update.message.reply_text(f'Erledigt. Folgene Nachricht wurde im Log aufgenommen:')
            update.message.reply_text(f'{zu_schreiben}')

