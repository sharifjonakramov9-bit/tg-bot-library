from telegram.ext import (
    Updater, 
    CommandHandler, 
    MessageHandler,
    Filters, 
)
from handlers import (
    start, help, echo_text,
    echo_photo, send_products,
    main_menu,
) 


updater = Updater('7873555193:AAGYKz0La5tOy1bNGnTA5fw0g4RD8uuaTVA') 
dispatcher = updater.dispatcher

# command hendlers
dispatcher.add_handler(CommandHandler('start', start)) 
dispatcher.add_handler(CommandHandler('help', help))

# message handlers
dispatcher.add_handler(MessageHandler(Filters.text('Mahsulotlar'), send_products))
dispatcher.add_handler(MessageHandler(Filters.text('Bosh Sahifa'), main_menu))
dispatcher.add_handler(MessageHandler(Filters.text, echo_text))
dispatcher.add_handler(MessageHandler(Filters.photo, echo_photo)) 

# botni ishga tushurish
updater.start_polling()
updater.idle() 
