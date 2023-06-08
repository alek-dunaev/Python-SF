import telebot
from config import keys, TOKEN
from extensions import APIException, СurrencyConverter


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message):
    bot.send_message(message.chat.id, f'Welcome, {message.chat.username}')
    text = 'Для того чтобы начать работу введите команду боту в следующем формате: \n <Имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты> \nУвидеть список доступных валют: /values'

    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def handle_values(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException('Проблемы с параметрами')

        quote, base, amount = values
        text = СurrencyConverter.convert(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')
    else:
        final_text = f'Цена {amount} {quote} в {base} - {text}'
        bot.send_message(message.chat.id, final_text)


bot.polling()
