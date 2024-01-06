import telebot
import webbrowser
import sqlite3
import _mysql_connector

bot= telebot.TeleBot('6774993420:AAF2xadJGuqDP8qFmGh_mjUuAyXgZT4JWSk')
name = None

bot.remove_webhook()

updates = bot.get_updates(False)
print(updates)
@bot.message_handler(commands=['start','main'])
def main(chat):
    conn = sqlite3.connect('userseach.sql')
    cur= conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50), pass VARCHAR(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(chat.chat.id, "Привет сейчас вас зарегетрируем")
    bot.register_next_step_handler(chat, user_name)
def user_name(chat):
    global name
    name=message.text.strip() #del space user
    bot.send_message(chat.chat.id, "Введите пароль")
    bot.register_next_step_handler(chat, user_pass)
def user_pass(chat):
    password=message.text.strip() #del space user
    # bot.send_message(chat.chat.id, "Введите пароль")
    # bot.register_next_step_handler(chat, user_pass)
def user_pass(chat):
    conn = sqlite3.connect('userseach.sql')
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, pass) VALUES ('%s', '%s')",(name, password))
    conn.commit()
    cur.close()
    conn.close()
    bot.register_next_step_handler(chat, user_name)
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(chat.chat.id, "Пользователь зарегестрирован" , reply_markup=markup)
@bot.message_handler(commands=['site','webside'])
def side(message):
    webbrowser.open('https:/google.com')
    # """приветственное"""


@bot.message_handler(commands=['buy'])
def main(chat):
    bot.send_message(chat.chat.id,f'Прекрасный выбор, {chat.from_user.first_name} {chat.from_user.last_name}')

# @bot.message_handler(commands=['pay'])
# def main(paymant):
#     bot.send_message()
# """это хелп"""
@bot.message_handler(commands=['help'])
def main(chat):
    bot.send_message(chat.chat.id, 'вывожу доступные команды!', parse_mode='html')

# '''это обработка обычных сообщений '''
@bot.callback_query_handler(func=lambda call :True)
def callback(call):
    conn = sqlite3.connect('userseach.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users=cur.fetchall()
    info = ''
    for el in users:
        info+=f'Имя{el[1]}', 'пароль: {el[2]}\n'
    cur.close()
    conn.close()
    bot.send_message(call.message.chat.id, info)
@bot.message_handler()
def info(message):
    if message.text.lower()=='привет':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower()=='id':
        bot.reply_to(message, f'ID: {message.from_user.id}')
    elif message.text.lower()!='привет':
        bot.send_message(message.chat.id, f"sorry, I'm not undestand" )


    bot.polling()