
# 1328469542:AAF8lEz4WqqbG9QSBHCJLTve5IFOW5vxzJI
# 1300551587:AAEG_T2VW-cTow3MvNAXu8OBZuBgrNCvXYY code of elaman


import telebot
from telebot import types

name = ''
surname = ''
age = 0

bot = telebot.TeleBot("1328469542:AAF8lEz4WqqbG9QSBHCJLTve5IFOW5vxzJI")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi, welcome to the chat!")


# name = ['Elaman', 'Azim', 'beka']
# for i in name:
#     print(i)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == 'Hello!':
        bot.reply_to(message, 'Hello, clever person!')
    elif message.text == 'Hi':
        bot.reply_to(message, 'Hello, clever person!')
    elif message.text == 'hi':
        bot.reply_to(message, 'Hello, clever person!')
    elif message.text == 'hello':
        bot.reply_to(message, 'Hello, clever person!')
    elif message.text == 'hello!':
        bot.reply_to(message, 'Hello, clever person!')
    elif message.text == 'Who are you?':
        bot.reply_to(message, 'My name is HELPER! ')
    elif message.text == 'What is your name?':
        bot.reply_to(message, 'My name is HELPER! ')
    elif message.text == 'what is your name?':
        bot.reply_to(message, 'My name is HELPER! ')
    elif message.text == 'What is your name':
        bot.reply_to(message, 'My name is HELPER! ')
    elif message.text == 'Can I ask something?':
        bot.reply_to(message, 'Of course, But we have some problem, my information can follow only students of international university Alatoo! Are you student of Alatoo?')
    elif message.text == 'Can you help me?':
        bot.reply_to(message, 'Of course, But we have some problem, my information can follow only students of international university Alatoo! Are you student of Alatoo?')
    elif message.text == 'yes':
        bot.reply_to(
            message, 'Woww, it is very great! Can you write you name? becouse I need check')
    elif message.text1 == '':
        if message.text1 in i:
            bot.reply_to(
                message, 'welcome!')
    elif message.text == 'no':
        bot.reply_to(
            message, 'I am sorry! you cant!')
    else:
        bot.reply_to('please write a some words!')

        # if message.text == 'yes':
        # bot.reply_to(message, 'Woww, it is very great! Can you write you name? becouse I need check')

        # else:
        #     bot.reply_to(message, 'I am sorry, you cant!')

        # bot.send_message(
        #     message.from_user.id, "Of course, But we have some problem, my informayion can follow only students of international university Alatoo! Are you student of Alatoo? ")
        #    if message.text == 'yes':
        #         bot.send_message(
        #             message.from_user.id, "Woww, it is very good! Can you write you name? becouse i need check?")
        #     else:
        #         bot.send_message(
        #             message.from_user.id, "I am sorry, this is bot can work only students of alatoo! Or check you name")
        # else:
        #     bot.reply_to(message, 'Write a good word!')
        bot.register_next_step_handler(message, reg_name)

    # bot.reply_to(message, message.text)


# def reg_name(message):
#     global name
#     name=message.text
#     bot.send_message(message.from_user.id, "Какая у вас фамилия?")
#     bot.register_next_step_handler(message, reg_surname)


# def reg_surname(message):
#     global surname
#     surname=message.text
#     bot.send_message(message.from_user.id, "Сколько вам лет?")
#     bot.register_next_step_handler(message, reg_age)


# def reg_age(message):
#     global age
#     # age = message.text
#     while age == 0:
#         try:
#             age=int(message.text)
#         except Exception:
#             bot.send_message(message.from_user.id, "Вводите цифрами!")

    # keyboard = types.InlineKeyboardMarkup()
    # key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    # keyboard.add(key_yes)
    # key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    # keyboard.add(key_no)
    # question = 'Тебе ' + str(age) + ' лет? И тебя зовут: ' + \
    #     name + ' ' + surname + '?'
    # bot.send_message(message.from_user.id, text=question,
    #                  reply_markup=keyboard)

# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     if call.data == "yes":
#         bot.send_message(call.message.chat.id,
#                          "Приятно познакомиться! Теперь запишу в БД!")
#     elif call.data == "no":
#         bot.send_message(call.message.chat.id, "Попробуем еще раз!")
#         bot.send_message(call.message.chat.id,
#                          "Привет! Давай познакомимся! Как тебя зовут?")
#         bot.register_next_step_handler(call.message, reg_name)


bot.polling()
