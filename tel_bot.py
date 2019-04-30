from telegram.ext import Updater , CommandHandler
import requests
import re
catapi = "https://random.dog/woof.json"

def return_url():
	url = requests.get(catapi).json()['url']
	return url

def send(bot , update):
	url = return_url()
	print(url)
	chat_id = update.message.chat_id
	bot.send_photo(chat_id = chat_id , photo = url)

def command_nilesh(bot , update):
	chat_id = update.message.chat_id
	bot.send_message(chat_id = chat_id , text = 'creator of the group')

def command_anmol(bot , update):
	chat_id = update.message.chat_id
	bot.send_message(chat_id = chat_id , text = 'chutiya aadmi')

def command_ashutosh(bot , update):
	chat_id = update.message.chat_id
	bot.send_message(chat_id = chat_id , text = 'andha vella aadmi')

def command_manas(bot , update):
	chat_id = update.message.chat_id
	bot.send_message(chat_id = chat_id , text = 'andha vella aadmi')

def send_image():
	updater = Updater('843445997:AAHrbSPNH0WTkKhzyRyJ_DA1N203rW5Q71g')
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('shoot' , send))
	dp.add_handler(CommandHandler('nilesh' , command_nilesh))
	dp.add_handler(CommandHandler('anmol' , command_anmol))
	dp.add_handler(CommandHandler('ashutosh' , command_ashutosh))
	dp.add_handler(CommandHandler('manas' , command_manas))
	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	send_image()
