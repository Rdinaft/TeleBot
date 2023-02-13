import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename = 'bot.log', format = '%(asctime)s - %(message)s', level=logging.INFO)

def begin(update, context):
    print('Вызван /start')
    update.message.reply_text('Поздравляю, бот запущен!')

def talking(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', begin))
    dp.add_handler(MessageHandler(Filters.text, talking))

    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()
