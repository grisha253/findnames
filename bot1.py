# coding=utf-8
##import telebot
##import random
##telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}
##token = "888041305:AAHtiYrbwdvfGLdIPwXH5xcUaimj0zbIFLQ"
##bot = telebot.TeleBot(token=token)
##@bot.message_handler(commands=['help'])
##def help(message):
##    user = message.chat.id
##    bot.send_message(user,'Это бот выдаёт анекдоты просто введи /anek')
##@bot.message_handler(commands=['anek'])
##def anek(message):
##    print(message)
##    user = message.chat.id
##    a = random.randint(1,3)3
##    if(a == 1):
##        bot.send_message (user,'Колобок повесился')
##    if(a == 2):
##        bot.send_message (user,'Русалка села на шпагат')
##    if(a == 3):
##        bot.send_message (user,'Буратина утонул')
##bot.polling(none_stop=True)
##
##
import telebot

token = "888041305:AAHtiYrbwdvfGLdIPwXH5xcUaimj0zbIFLQ"
telebot.apihelper.proxy = {'https': 'socks5h://geek:socks@t.geekclass.ru:7777'}
bot = telebot.TeleBot(token=token)


niks = ['@roctbb', '@griglit', '@flyted', '@valentin_denisov', '@prplkn']
names = ['Ростислав Бородин', 'Grisha Litvinenko', 'Fedor Falkovsky', 'Valentin Denisov', 'Alexei']

@bot.message_handler(content_types=['text'])
def echo(message):
    text = message.text
    user = message.chat.id
    if text in niks:
        bot.send_message(user, names[niks.index(text)])
    elif text in names:
        bot.send_message(user, niks[names.index(text)])
    else:
        bot.send_message(user,
                         'привет, меня зовут Nowitwork, я знаю, как зовут по именам участников летней смены школы GOTO' + ' я не знаю, кто это: <' + text + '>')
        start(message)


name = ''
surname = ''


@bot.message_handler(content_types=['text'], commands=['/reg'])
def start(message):
    user = message.chat.id
    if message.text == '/reg':
        bot.send_message(user, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name);
    else:
        bot.send_message(user, 'Напиши' + '/reg');


def get_name(message):
    user = message.chat.id
    global name;
    name = message.text;
    bot.send_message(user, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);


def get_surname(message):
    user = message.chat.id
    global surname;
    surname = message.text;
    bot.send_message(user, ' Tебя зовут ' + name + ' ' + surname + '?')
    bot.register_next_step_handler(message, dailinet);


def dailinet(message):
    global niks
    global names
    user = message.chat.id
    text = message.text
    if text == "да":
        bot.send_message(user, 'Запомню : )')
        print(names)
        print(niks)
        names.append(name + " " + surname)
        niks.append("@"+message.chat.username)
        print(names)
        print(niks)
    elif text == 'нет':
        bot.send_message(user, 'переспрашиваю')
        start(message)


bot.polling(none_stop=True)
