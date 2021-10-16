from .utilities.youtube_search import *
from .utilities.wolfram_alpha import *
from .fun_commands.yo_intro import *
from telegram.ext import *
import telegram

def boot():

##Bot_API
 updater = telegram.ext.Updater("BOT TOKEN HERE", use_context= True)
 dis = updater.dispatcher

#Command_handelers

 dis.add_handler(telegram.ext.CommandHandler("yo", yo))
 dis.add_handler(telegram.ext.CommandHandler("wolf", wolf))
 dis.add_handler(telegram.ext.CommandHandler("yt", youtube_search))

##Status
 print("SAGE is online!")


##Bot startup
 updater.start_polling()
 updater.idle()
