from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

import configparser
bot_config = configparser.ConfigParser()
bot_config.read('BotConfig.ini')

updater = Updater( bot_config['ACCESS']['token'],
                  use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text( "Hi there! I'm " +
        bot_config['BOT']['name'] +
        ". Type /help for more info on what I can do. ")

def help(update: Update, context: CallbackContext):
    update.message.reply_text(bot_config['BOT']['help_text'])


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry, I can't figure out what you just said : '%s'" % update.message.text)

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry, '%s' is not a valid command" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
