import telebot
from config import token
from telebot import types
from random import randint
import fact

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def button_click(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    weather = types.KeyboardButton('Сайт погоды в Челябинске', )
    random_butt = types.KeyboardButton('Рандомное число')
    help_info = types.KeyboardButton('Инструкция')
    id_info = types.KeyboardButton('Ваш ID')
    fact = types.KeyboardButton('Узнать факт')
    jok_land_rover = types.KeyboardButton('Шутка про Lend Rover')
    markup.add(weather, random_butt, help_info, id_info, fact, jok_land_rover)
    bot.send_message(message.chat.id, 'Нажми на кнопки и приготовься увидеть чудо ;D', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mes_test(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, f"Привет, {message.from_user.first_name}")
    elif message.text == 'Как дела?':
        markup = types.InlineKeyboardMarkup(row_width=5)
        good = types.InlineKeyboardButton('Хорошо', callback_data='Good')
        not_bad = types.InlineKeyboardButton('Не плохо', callback_data='not bad')
        markup.add(good, not_bad)
        bot.send_message(message.chat.id, 'У меня отлично, а у вас?', reply_markup=markup)
    elif message.text == 'Ваш ID':
        bot.send_message(message.chat.id, f'Ваш ID: {message.from_user.id}')
    elif message.text == 'Шутка про Lend Rover':
        bot.send_message(message.chat.id, f'{fact.joke()}')
    elif message.text == 'Узнать факт':
        bot.send_message(message.chat.id, f'{fact.fact()}')
    elif message.text == "Сайт погоды в Челябинске":
        bot.send_message(message.chat.id, "https://www.gismeteo.ru/weather-chelyabinsk-4565/")
    elif message.text == 'Рандомное число':
        bot.send_message(message.chat.id, f'{randint(-10000, 10000)}')
    elif message.text == 'Инструкция':
        bot.send_message(message.chat.id, 'Поздороваться - "Привет"\n'
                                          'Спросить как у бота дела "Как дела?"\n'
                                          'если нет кнопок, введи "/start"')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'Good':
            bot.send_message(call.message.chat.id, 'Супер!')
        elif call.data == 'not bad':
            bot.send_message(call.message.chat.id, 'Бывает.')


bot.infinity_polling(none_stop=True)
