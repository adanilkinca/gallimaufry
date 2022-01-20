#weatheradviserBot2.py
#weater module from https://github.com/csparpa/pyowm
#bot from https://pypi.org/project/pyTelegramBotAPI/

from pyowm import OWM
owm = OWM('9d539ba42681da0689a38c727fe8a122')
mgr = owm.weather_manager()
import telebot
bot = telebot.TeleBot("5152221695:AAEXGq8yn1MfmXw0UjIkl2Pl0RtKdylw_io")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message, 'Where are you want to know weater? Enter city name: ')

@bot.message_handler(content_types=['text'])
def echo_all(message):
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	temp = w.temperature('celsius')['temp']

	answer = 'There is ' + w.detailed_status + ' in ' + message.text + ' now' + '\n'
	answer += 'The temperature is ' + str(temp) + '\n\n'

	if temp < 0:
		answer +='It\'s below zero now, wear something warm'
	elif 0 < temp < 10:
		answer +='Not bad. It might be worse'
	else:
		answer +='If water do not feeze, then and you\'re too'

	bot.send_message(message.chat.id, answer)

bot.infinity_polling()
