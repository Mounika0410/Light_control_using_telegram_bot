from Adafruit_IO import Client,Data
import os
x = os.getenv('x') #ADAFRUIT_IO_USERNAME
y = os.getenv('y') #ADAFRUIT_IO_KEY


from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
import requests
def turnon(bot,update):
 
    chat_id = update.message.chat_id
    bot.send_message(chat_id,text="Light turned on")
    bot.send_photo(chat_id,photo='https://images.app.goo.gl/vboPtjpGbD3iUTrf6')
def turnoff(bot,update):
 
    chat_id = update.message.chat_id
    bot.send_message(chat_id,text="Light turned off")
    bot.send_photo(chat_id,photo='https://images.app.goo.gl/cU8fsGt7sSjdKS4b8')
    
def input_message(bot,update):
   text=update.message.text
   if text == 'turn on':
      chat_id = update.message.chat_id
      bot.send_message(chat_id,text="Light turned on")
      bot.send_photo(chat_id,photo='https://images.app.goo.gl/vboPtjpGbD3iUTrf6')
      feed = aio.feeds('lightbot')
      aio.send_data(feed.key,1)
      
      
   elif text=='turn off':
      chat_id = update.message.chat_id
      bot.send_message(chat_id,text="Light turned off")
      bot.send_photo(chat_id,photo='https://images.app.goo.gl/cU8fsGt7sSjdKS4b8')
      feed = aio.feeds('lightbot')
      aio.send_data(feed.key,0)
      
Token=os.getenv('Token')   
u = Updater('Token')
dp = u.dispatcher
dp.add_handler(CommandHandler('turnon',turnon))
dp.add_handler(CommandHandler('turnoff',turnoff))
dp.add_handler(MessageHandler(Filters.text & (~Filters.command),input_message))
u.start_polling()
u.idle() 
