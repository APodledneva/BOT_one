import telebot, wikipedia, re
from telebot import types
import random

wikipedia.set_lang("ru")

f = open('anek.txt', 'r', encoding='UTF-8')
jokes = f.read().split('/')
f.close()

f = open('wolf.txt', 'r', encoding='UTF-8')
ayf_facts = f.read().split('/')
f.close()

bot = telebot.TeleBot('5714195121:AAE1Z6_wTkv5i5a_kJlsV-xHl867kVW-yiI')


def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'У меня нет такой информации, воспользуйся гуглом'


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Привет")
    btn2 = types.KeyboardButton("Давай веселиться")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Я учебный бот".format(
                         message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Привет"):
        bot.send_message(message.chat.id, text="Доброго времени суток! Спасибо, за посещение!"
                                               "\nЭто небольшой расслабляющий бот."
                                               "\nТы можешь попросить у меня небольшую статью из Википедии, "
                                               "просто напиши любое слово.")

    elif (message.text == "Давай веселиться"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Хочу анекдот")
        btn2 = types.KeyboardButton("Расскажи мудрую мысль")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Что рассказать?", reply_markup=markup)

    elif (message.text == "Хочу анекдот"):
        bot.send_message(message.chat.id, random.choice(jokes))

    elif (message.text == "Расскажи мудрую мысль"):
        bot.send_message(message.chat.id, random.choice(ayf_facts))

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Привет")
        button2 = types.KeyboardButton("Давай веселиться")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
        bot.send_message(message.chat.id, getwiki(message.text))

bot.polling(none_stop=True)
