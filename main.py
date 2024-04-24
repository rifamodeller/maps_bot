from telebot import types
import telebot
from geo import geocode, load_map
import random
import csv

bot = telebot.TeleBot('6753251878:AAH5FRbpYaGDbC7FhysCcMRydZ3q2BpSKWQ')

capitals_europe = []
cities_europe = []
information = ''
otvets = 0
goagain = True
true_otvets = 0
usage_capitals = []
information_2 = ''

with open('capitals.csv', encoding='utf8') as file:
    reader = csv.reader(file, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        capitals_europe.append(row[0])
        cities_europe.append(row[1])


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    yess = types.KeyboardButton('/Давай начнем')
    no = types.KeyboardButton('/Позже')
    markup.add(yess, no)
    mess = f'''Привет, {message.from_user.first_name}.
Я хочу помочь тебе выучить страны и столицы мира'''
    bot.send_message(message.chat.id, mess, reply_markup=markup)
    # bot.register_next_step_handler(message, start_otvet)


# @bot.message_handler()
# def start_otvet(message):
#         bot.send_message(message.chat.id, "Хорошо", reply_markup=types.ReplyKeyboardRemove(),
#         parse_mode='Markdown')

@bot.message_handler()
def text(message):
    global usage_capitals
    global otvets
    global true_otvets
    if message.text == '/Давай начнем':
        otvets = 0
        true_otvets = 0
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        y1 = types.KeyboardButton('/Страны')
        y2 = types.KeyboardButton('/Столицы')
        y3 = types.KeyboardButton('/Страны и столицы')
        markup.add(y1, y2, y3)
        bot.send_message(message.chat.id, 'Хорошо, я попрошу тебя выбрать тип вопросов',
                         reply_markup=markup)
    if message.text == '/Позже':
        bot.send_message(message.chat.id, 'Прискорбно, тогда увидимся потом',
                         reply_markup=types.ReplyKeyboardRemove())
    if message.text == '/Страны':
        usage_capitals = []
        while otvets < 10:
            if otvets < 10:
                if goagain:
                    yes(message)
        bot.send_message(message.chat.id, f'Ты дал {true_otvets}/10 верных ответов')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        y1 = types.KeyboardButton('/Давай начнем')
        markup.add(y1)
        bot.send_message(message.chat.id, 'Попробуем снова?', reply_markup=markup)
    if message.text == '/Столицы':
        usage_capitals = []
        while otvets < 10:
            if otvets < 10:
                if goagain:
                    yes1(message)
        bot.send_message(message.chat.id, f'Ты дал {true_otvets}/10 верных ответов')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        y1 = types.KeyboardButton('/Давай начнем')
        markup.add(y1)
        bot.send_message(message.chat.id, 'Попробуем снова?', reply_markup=markup)
    if message.text == '/Страны и столицы':
        usage_capitals = []
        while otvets < 10:
            if otvets < 10:
                if goagain:
                    yes2(message)
        bot.send_message(message.chat.id, f'Ты дал {true_otvets}/10 верных ответов')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        y1 = types.KeyboardButton('/Давай начнем')
        markup.add(y1)
        bot.send_message(message.chat.id, 'Попробуем снова?', reply_markup=markup)


@bot.message_handler()
def returnn(message):
    global true_otvets
    global otvets
    global goagain
    if information.lower() == message.text.lower():
        bot.send_message(message.chat.id, 'Ответ верен')
        otvets += 1
        goagain = True
        true_otvets += 1
    else:
        bot.send_message(message.chat.id, 'Ответ неверен')
        bot.send_message(message.chat.id, f'Правильный ответ - {information}')
        otvets += 1
        goagain = True


@bot.message_handler()
def yes(message):
    global goagain
    global usage_capitals
    goagain = False
    bot.send_message(message.chat.id, 'Как называется эта страна?',
                     reply_markup=types.ReplyKeyboardRemove())
    global information
    while True:
        i = random.randint(0, 30)
        if capitals_europe[i] not in usage_capitals:
            information = capitals_europe[i]
            usage_capitals.append(capitals_europe[i])
            break
    bot.send_message(message.chat.id,
                     f'Столицей этой страны является {cities_europe[i]}')
    # print(information)
    load_map(geocode(capitals_europe[i]))
    with open('map.png', 'rb') as file:
        bot.send_photo(message.chat.id, file)
    bot.register_next_step_handler(message, returnn)


@bot.message_handler()
def yes1(message):
    global goagain
    global usage_capitals
    goagain = False
    bot.send_message(message.chat.id, 'Как называется столица этой страны?',
                     reply_markup=types.ReplyKeyboardRemove())
    global information
    while True:
        i = random.randint(0, 30)
        if capitals_europe[i] not in usage_capitals:
            information = cities_europe[i]
            usage_capitals.append(capitals_europe[i])
            break
    bot.send_message(message.chat.id, f'Эта страна называется {capitals_europe[i]}')
    # print(information)
    load_map(geocode(capitals_europe[i]))
    with open('map.png', 'rb') as file:
        bot.send_photo(message.chat.id, file)
    bot.register_next_step_handler(message, returnn)


@bot.message_handler()
def yes2(message):
    global goagain
    global usage_capitals
    global information_2
    goagain = False
    bot.send_message(message.chat.id, 'Назовите сначала страну, а затем её столицу',
                     reply_markup=types.ReplyKeyboardRemove())
    global information
    while True:
        i = random.randint(0, 30)
        if capitals_europe[i] not in usage_capitals:
            information = capitals_europe[i]
            information_2 = cities_europe[i]
            usage_capitals.append(capitals_europe[i])
            break
    # print(information)
    load_map(geocode(capitals_europe[i]))
    with open('map.png', 'rb') as file:
        bot.send_photo(message.chat.id, file)
    bot.register_next_step_handler(message, returnn1_1)


@bot.message_handler()
def returnn1_1(message):
    global true_otvets
    global otvets
    global goagain
    if information.lower() == message.text.lower():
        bot.send_message(message.chat.id, 'Название страны верно, теперь назовите её столицу')
        bot.register_next_step_handler(message, returnn1_2)
    else:
        bot.send_message(message.chat.id, 'Ответ неверен')
        bot.send_message(message.chat.id,
                         f'Эта страна называется {information}, а её столица называется {information_2}')
        goagain = True


@bot.message_handler()
def returnn1_2(message):
    global true_otvets
    global otvets
    global goagain
    if information_2.lower() == message.text.lower():
        bot.send_message(message.chat.id, 'Ответ верен')
        true_otvets += 1
        otvets += 1
        goagain = True
    else:
        bot.send_message(message.chat.id, 'Ответ неверен')
        bot.send_message(message.chat.id,
                         f'Эта страна называется {information}, а её столица называется {information_2}')
        goagain = True


bot.polling(none_stop=True)
