import telebot
from datetime import datetime
import random

TOKEN = '8127468822:AAFQ5E6W7fDV1p6qYXhEaNM92mF7bv9ww5E'

bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
button_time = telebot.types.KeyboardButton('Узнать время')
button_random = telebot.types.KeyboardButton('Рандомное число')
button_id = telebot.types.KeyboardButton('Мой ID')
keyboard.add(button_time, button_random, button_id)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Выбери действие:', reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == 'Узнать время':
        current_time = datetime.now().strftime('%H:%M:%S')
        bot.reply_to(message, f'Текущее московское время: {current_time}')

    elif message.text == 'Рандомное число':
        number = random.randint(1, 100)
        bot.reply_to(message, f'Ваше случайное число: {number}')

    elif message.text == 'Мой ID':
        user_id = message.from_user.id
        bot.reply_to(message, f"Ваш ID: {user_id}")

    else:
        bot.reply_to(message, 'Извините, такой команды нет. Используйте доступные кнопки.')


if __name__ == '__main__':
    print("Бот запущен!")
    bot.polling()