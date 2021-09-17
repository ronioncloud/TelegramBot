import random
import telebot
import json
import requests
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
yuu = telebot.TeleBot('1894877321:AAFDTv470mmfVlXAGHLk36DZZr9NSbgUj80', parse_mode='html')

@yuu.message_handler(commands=['gato', 'gatin'])
def enviar_foto_de_gato(message):
    cat = requests.get('https://thatcopy.pw/catapi/rest')
    cat2 = cat.json()
    b = cat2['url']
    yuu.send_message(message.chat.id, text=f'<a href="{b}">Gatinho</a>', parse_mode='HTML')
    del cat
    del cat2
    del b


@yuu.message_handler(commands=['dolar'])
def dolar(message):
    requisicao = requests.get('https://economia.awesomeapi.com.br/all/USD-BRL')
    cotacao = requisicao.json()
    yuu.reply_to(message, text=f"<b>Moeda:</b> {cotacao['USD']['name']}\n<b>Data:</b> {cotacao['USD']['create_date']}\n<b>Valor atual:</b> R${cotacao['USD']['bid']}")
    del cotacao
    del requisicao
frases = ['Com vontade de trair hoje','Tríste hoje','Azarado(a) hoje','Louco(a) hoje','Doido(a) hoje','Com vontade de teclar hoje','Dengoso(a) hoje','Irritado(a) hoje','Ostentando hoje','Sem vontade de se jogar da ponte hoje','Com vontade de dar risadas hoje','Com vontade de conversar hoje','Solteiro(a) hoje','Assanhado(a) hoje','Sem animo hoje','Com ódio hoje','Sem vontade de brincar hoje','Sem assunto hoje','Rabugento(a) hoje','Estressado(a) hoje','Doido(a) hoje','Irado(a) hoje','Sem assunto hoje','Com vontade de ouvir musicas hoje','Com vontade de viajar hoje','Revoltado(a) hoje','Pirado(a) hoje','Com vontade de passear com alguém do grupo hoje','Com cheiro ruim hoje','Com vontade de beijar hoje','Com fome hoje','Assanhado(a) hoje','Sedutor(a) hoje','Gostoso(a) hoje','Sem vontade de brincar hoje','Confuso(a) hoje','Romântico(a) hoje','Embabacado(a) hoje','Sem vontade de se jogar da ponte hoje','Com vontade de cantar hoje','vontade de dormir de conchinha','vontade de tomar café','vontade de morrer', 'vontade de mandar o ademiro pro inferno', 'vontade de namorar', 'vontade de ser banido', 'vontade de comer algo ou alguém']
@yuu.message_handler(commands=['yo'])
def yep(messagem):
    verificar_grupo = messagem.chat.type
    if verificar_grupo == 'supergroup':
      # nick = messagem
      porcentagem = random.randint(1,100)
      yuu.reply_to(messagem, text=f'Você está {porcentagem}% <b>{random.choice(frases)}</b>')
      del porcentagem
      # del verificar_grupo
      # yuu.get_chat_member(user_id=messagem.user.id)
frases_desmotivacionais = ['Você não pode mudar o seu passado, mas pode estragar o seu futuro.','Você é mais fraco do que pensa.','É uma fase ruim, logo vai piorar.','O caminho é longo, mas a derrota é certa.','Nada como um dia pior que outro.','Não pare faça até dar errado.','No teatro da vida, o papel de trouxa é seu.','Dividir para fracassar.','Seja o protagonista do seu fracasso.','Nunca foi azar, sempre foi incompetência.','No começo é difícil, mas no final dará errado.','Coisas ruins se vão para que piores possam vir.','Seu problema é você.','Acredite, você nasceu para conquistar grandes fracassos.','Você não é incrível.','Acreditar que você pode ja é meio caminho errado.','Tudo dando errado conforme esperado.','O não você já tem, busque a humilhação.','Quando tudo estiver dando errado, acostume-se']
@yuu.message_handler(commands=['sad'])
def yep2(message):
  yuu.reply_to(message, text=f'<b>{random.choice(frases_desmotivacionais)}</b>')
 
@yuu.message_handler(commands=['help','ajuda'])
def vrum(a):
  yuu.reply_to(a, text=f'''
  <b><i>Olá, bem vindo ao bot do Sr. Yuu</i></b>

<i>O bot ainda esté em desenvolvimento em prol do estudo de Python do Yuu</i>
  
  <b>Lista de comandos:</b>
  <i>/help</i> ou <i>/ajuda</i> -> Esta mensagem 
  <i>/yo</i> -> Mostra uma frase aleatória sobre seu estado atual
  <i>/sad</i> -> Exibe uma frase desmotivacional
  <i>/dolar</i> -> Exibe valor atual do dólar em BRL
  <i>/gato</i> ou <i>/gatin</i> -> Envia foto aleatória de gato
  <i>/autor</i> -> Se tiver ideas para o bot, use esse comando :D
  
  Mais comando serão adicionados com o tempo :D
  ''')


# Botão de url
@yuu.message_handler(commands=['autor'])
def autor(message):
    markup = InlineKeyboardMarkup()
    btn_meu_user= InlineKeyboardButton(text='Visitar Autor', url='https://t.me/Sr_Yuu')
    markup.add(btn_meu_user)
    yuu.send_message(message.chat.id, text=f'''<b>Autor do Bot Inútil</b>
    
Olá!! Desejas fazer <b>expressar suas ideias</b> para o bot, <b>fazer reclamações</b>, ou até mesmo <b>elogiar</b>
    
Sinta-se livre para ir no perfil do autor :D''', reply_markup = markup)

yuu.polling(non_stop=True)
