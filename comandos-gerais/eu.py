import random
import telebot
token = 'TOKEN'
bot = telebot.TeleBot(token)

frases = ['Com vontade de trair hoje','Tríste hoje','Azarado(a) hoje','Louco(a) hoje','Doido(a) hoje','Com vontade de teclar hoje','Dengoso(a) hoje','Irritado(a) hoje','Ostentando hoje','Sem vontade de se jogar da ponte hoje','Com vontade de dar risadas hoje','Com vontade de conversar hoje','Solteiro(a) hoje','Assanhado(a) hoje','Sem animo hoje','Com ódio hoje','Sem vontade de brincar hoje','Sem assunto hoje','Rabugento(a) hoje','Estressado(a) hoje','Doido(a) hoje','Irado(a) hoje','Sem assunto hoje','Com vontade de ouvir musicas hoje','Com vontade de viajar hoje','Revoltado(a) hoje','Pirado(a) hoje','Com vontade de passear com alguém do grupo hoje','Com cheiro ruim hoje','Com vontade de beijar hoje','Com fome hoje','Assanhado(a) hoje','Sedutor(a) hoje','Gostoso(a) hoje','Sem vontade de brincar hoje','Confuso(a) hoje','Romântico(a) hoje','Embabacado(a) hoje','Sem vontade de se jogar da ponte hoje','Com vontade de cantar hoje','vontade de dormir de conchinha','vontade de tomar café','vontade de morrer', 'vontade de mandar o ademiro pro inferno', 'vontade de namorar', 'vontade de ser banido', 'vontade de comer algo ou alguém']
@bot.message_handler(commands=['eu'])
def eu_estou(messagem):
      porcentagem = random.randint(1,100)
      bot.reply_to(messagem, text=f'Você está {porcentagem}% <b>{random.choice(frases)}</b>', parse_mode='HTML')
      del porcentagem

bot.polling()
