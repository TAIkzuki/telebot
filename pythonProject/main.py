import telebot
import webbrowser
bot= telebot.TeleBot('6774993420:AAF2xadJGuqDP8qFmGh_mjUuAyXgZT4JWSk')
bot.remove_webhook()
updates = bot.get_updates(False)
print(updates)

@bot.message_handler(commands=['site','webside'])
def side(message):
    webbrowser.open('https:/google.com')
    # """приветственное"""
@bot.message_handler(commands=['start','main'])
def main(chat):
    bot.send_message(chat.chat.id,f'Hello, {chat.from_user.first_name} {chat.from_user.last_name}')


@bot.message_handler(commands=['buy'])
def main(chat):
    bot.send_message(chat.chat.id,f'Hello, {chat.from_user.first_name} {chat.from_user.last_name}')

# @bot.message_handler(commands=['pay'])
# def main(paymant):
#     bot.send_message()
# """это хелп"""
@bot.message_handler(commands=['help'])
def main(chat):
    bot.send_message(chat.chat.id, 'help information!', parse_mode='html')

# '''это обработка обычных сообщений '''
@bot.message_handler()
def info(message):
    if message.text.lower()=='привет':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower()=='id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text.lower()!='привет':
        bot.send_message(message.chat.id, f"sorry, I'm not undestand" )
bot.polling(none_stop=True)