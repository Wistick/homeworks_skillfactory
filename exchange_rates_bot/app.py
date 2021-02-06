from extensions import *
from config import rates, TOKEN

import telebot


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def bot_help(message: telebot.types.Message):
    text = '<b>Добро пожаловать в Exchange бот!</b>\n\nВведите:\nНазвание валюты\n' \
           'Название валюты в которой надо узнать цену\n' \
           'Количество первой валюты\n\nНапример: <b>евро рубль 100</b>\n\n' \
           'Наберите /values для того, чтобы увидеть список всех доступных валют.\n'
    bot.reply_to(message, text, parse_mode='html')


@bot.message_handler(commands=['values', ])
def bot_values(message: telebot.types.Message):
    text = '<b>Доступные валюты:</b>'
    for key in rates:
        text = '\n'.join((text, key))
    bot.reply_to(message, text, parse_mode='html')


@bot.message_handler(content_types=['text', ])
def bot_convert(message: telebot.types.Message):
    message.text = message.text.replace(',', '.')
    message.text = message.text.title()
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Слишком много или мало параметров!')

        base, quote, amount = values

        total = ExchangeAPI.get_rate(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Нынешний курс {amount} {rates[base]} в {rates[quote]}  —  <b>{total}</b>'
        bot.send_message(message.chat.id, text, parse_mode='html')


bot.polling(none_stop=True)
