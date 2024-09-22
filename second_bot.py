import telebot

TOKEN = '7219757150:AAF9eTqQ1JLRnjwuO_sHFfaZoVSWBUEgHOc'
bot = telebot.TeleBot(TOKEN)

# Хранение данных о заявках
applications = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать! Вы можете просмотреть заявки.")

@bot.message_handler(commands=['view_applications'])
def view_applications(message):
    if not applications:
        bot.send_message(message.chat.id, "Нет заявок на рассмотрение.")
        return

    for user_id, status in applications.items():
        bot.send_message(message.chat.id, f'Пользователь: {user_id}, Статус: {status}')

# Функция для добавления заявки
def add_application(user_id):
    applications[user_id] = 'На рассмотрении'

# Функция для обновления статуса заявки
def update_application(user_id, status):
    if user_id in applications:
        applications[user_id] = status

bot.polling()
