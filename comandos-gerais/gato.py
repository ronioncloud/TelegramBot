@bot.message_handler(commands=['gato'])
def gatin(message):
    cat = requests.get('https://thatcopy.pw/catapi/rest')
    gato = cat.json()
    bot.send_photo(message.chat.id, gato['url'])
    # Kkkk eu tava quebrando a cabeça pra fazer download da url, sendo que poderia somente incorporar a URL :D
