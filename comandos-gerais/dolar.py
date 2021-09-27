import telebot
token = 'TOKEN'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['dolar'])
def dolar(message):
    requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
    cotacao = requisicao.json()
    bot.reply_to(message, text=f"""
<b>Moeda:</b> {cotacao['USD']['name']}
<b>Data:</b> {cotacao['USD']['create_date']}
<b>Valor atual:</b> R${cotacao['USD']['bid']}
""", parse_mode='HTML')
    
bot.polling(non_stop=True)
