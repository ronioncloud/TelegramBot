import requests
import telebot
bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['gato'])
def gatin(message):
    cat = requests.get('https://thatcopy.pw/catapi/rest')
    gato = cat.json()
    bot.send_photo(message.chat.id, gato['url'])

bot.polling(non_stop=True)
