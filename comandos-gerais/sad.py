frases_desmotivacionais = ['Você não pode mudar o seu passado, mas pode estragar o seu futuro.','Você é mais fraco do que pensa.','É uma fase ruim, logo vai piorar.','O caminho é longo, mas a derrota é certa.','Nada como um dia pior que outro.','Não pare faça até dar errado.','No teatro da vida, o papel de trouxa é seu.','Dividir para fracassar.','Seja o protagonista do seu fracasso.','Nunca foi azar, sempre foi incompetência.','No começo é difícil, mas no final dará errado.','Coisas ruins se vão para que piores possam vir.','Seu problema é você.','Acredite, você nasceu para conquistar grandes fracassos.','Você não é incrível.','Acreditar que você pode ja é meio caminho errado.','Tudo dando errado conforme esperado.','O não você já tem, busque a humilhação.','Quando tudo estiver dando errado, acostume-se']
bot.message_handler(commands=['sad'])
def sad(message):
  bot.reply_to(message, text=f'<b>{random.choice(frases_desmotivacionais)}</b>')
  # kkkkkk só isso? kskskkss
