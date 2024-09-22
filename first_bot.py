import telebot
from telebot import types

TOKEN = '7213834309:AAFeuZxrFTLux2cezfVuWuyCITirjqsciYs'
bot = telebot.TeleBot(TOKEN)

# Хранение данных о пользователях и их ссылках
users = {}

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    # Генерация уникальной ссылки (для простоты используем user_id)
    invite_link = f"https://t.me/+pTtbxt8bxmNhZTJi?start={user_id}"
    users[user_id] = {'link': invite_link, 'requests': 0}

    bot.send_message(message.chat.id, f'Ваша личная ссылка для приглашения: {invite_link}\nЧтобы отслеживать количество заявок, нажмите "Информация".')

@bot.message_handler(func=lambda message: message.text == 'Информация')
def info(message):
    user_id = message.from_user.id
    if user_id in users:
        data = users[user_id]
        bot.send_message(message.chat.id, f'Ваша ссылка: {data["link"]}\nКоличество заявок: {data["requests"]}')
    else:
        bot.send_message(message.chat.id, "Вы не зарегистрированы.")

# Функция для увеличения количества заявок (должна вызываться по мере поступления заявок)
def increment_requests(user_id):
    if user_id in users:
        users[user_id]['requests'] += 1
        if users[user_id]['requests'] >= 100:
            bot.send_message(user_id, "Задание успешно выполнено и находится на рассмотрении.")

bot.polling()
