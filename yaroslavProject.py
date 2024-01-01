#--------EXTERNAL LIBRARIES-------

import telebot
from telebot import types

import sqlite3

#-------PRESETS AND VARIABLES-----

bot = telebot.TeleBot('6652275990:AAF9kBBdNLicha65GICiHHYIhQCxitLF9Lc')



#global previousFishingStep
global rightFishingAnswers
global fishingStep
fishingStep = 0
rightFishingAnswers = 0

userId = 0

fishingTestVar = [["Ссылка на рыбалку","Вредоносный сайт","Ссылка на онлайн магазин"],
                  ["Для привлечения посетителей на сайт","Для защиты от вирусов","Для кражи личной информации"],
                  ["Подписки на новости","Логины и пароли","История покупок"],
                  ["По длине","По наличию защищенного соединения","По названию сайта"],
                  ["Перейти по ссылке", "Ничего не делать", "Удалить письмо или сообщение"],
                  ["Сайт-конкурент","Дубликат сайта","Недоработанная версия"],
                  ["Ввести данные", "Позвонить в поддержку", "Ничего не делать"],
                  ["Фин.учереждения","Гос.учреждения","Все перечисленное"],
                  ["Не обращать внимания", "Обратиться за помощью", "Рассказать друзьям"],
                  ["Хакеры","Кардеры","Криптоторговцы"],
                  ["Антивирус","Обновление паролей","Оба варианта"],
                  ["Никогда не проверять", "Раз в месяц","Каждый раз"],
                  ["Грамматические ошибки","Странная ссылка","Все перечисленное"],
                  ["Удалить сообщения", "Поменять все пароли","Не делать ничего"],
                  ["Утечка данных", "Попадание к мошенникам", "Все перечисленное"]
]
@bot.message_handler(commands=['start'])

def start(message):
    separated_list = []
    global chatId
    global InlineStartMarkup
    #print(userId)

    InlineStartMarkup = types.InlineKeyboardMarkup(row_width=2)

    moreInfoButton = types.InlineKeyboardButton("Узнать больше", callback_data="узнать больше")

    KeyboardMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #updateData = types.InlineKeyboardButton("Обновить данные",callback_data = "Обновить данные")



    InlineStartMarkup.add(moreInfoButton)
    bot.send_message(message.from_user.id, "👋Приветствую, я чат-бот, созданный для повышения уровня квалификации пенсионеров в области компьютерной безопасности")
    #previousMessage = message
    connectionUser = sqlite3.connect('mainDatabase.db')
    cursorUser = connectionUser.cursor()
    userId = bot.user.id
    
    userData = cursorUser.execute('SELECT tgId FROM Users')
    user = userData.fetchall()
    chatId = message.chat.id
    print(chatId)
    for separator in user:
        separated_list.extend(separator)
    print(separated_list)
    if str(chatId) not in separated_list:
            cursorUser.execute('INSERT INTO Users  (tgId) VALUES (?)', (chatId,))
            connectionUser.commit()
    connectionUser.close()
    bot.send_message(message.from_user.id, "Если хотите узнать подробнее, нажмите на кнопку внизу",reply_markup=InlineStartMarkup)

@bot.callback_query_handler(func = lambda call: True)
def get_callback(call):

    try:
        if call.data == "узнать больше":
            Inlinemarkup = types.InlineKeyboardMarkup(row_width=2)

            passwordButton = types.InlineKeyboardButton("Защита паролей", callback_data="пароли")
            fishingButton = types.InlineKeyboardButton("Фишинговые ссылки", callback_data="фишинг")
            virusButton = types.InlineKeyboardButton("Вирусы", callback_data="вирусы")
            scamButton = types.InlineKeyboardButton("Интернет-мошенники", callback_data="мошенники")

            Inlinemarkup.add(passwordButton)
            Inlinemarkup.add(fishingButton)
            Inlinemarkup.add(virusButton)
            Inlinemarkup.add(scamButton)


            with open("info1.txt", "r", encoding="utf-8") as file:
                text = file.read()
                bot.send_message(call.message.chat.id, text, reply_markup=Inlinemarkup)
                file.close()

        elif call.data == "фишинг":
            with open("fishingInfo.txt", "r", encoding="utf-8") as file:
                text = file.read()
                addBackButton()
                InlineTestmarkup = types.InlineKeyboardMarkup(row_width=2)
                testButton = types.InlineKeyboardButton("Запустить тест", callback_data="fishingTest")
                InlineTestmarkup.add(testButton)

                bot.send_message(call.message.chat.id, text, reply_markup=InlineBackMarkup)
                bot.send_message(call.message.chat.id,"Вы можете пройти тест по теме",reply_markup=InlineTestmarkup)
                file.close()

        elif call.data == "вирусы":
            with open("virusInfo.txt", "r", encoding="utf-8") as file:
                text = file.read()
                addBackButton()
                bot.send_message(call.message.chat.id, text, reply_markup=InlineBackMarkup)
                file.close()

        elif call.data == "мошенники":
            #with open("scamInfo.txt", "r", encoding="utf-8") as file:
                #text = file.read()
            addBackButton()
            bot.send_message(call.message.chat.id, "Текст отсутсвует", reply_markup=InlineBackMarkup)
                #file.close()

        elif call.data == "пароли":
            with open("passwdInfo.txt", "r", encoding="utf-8") as file:
                text = file.read()
                addBackButton()
                bot.send_message(call.message.chat.id, text, reply_markup=InlineBackMarkup)
                file.close()
        if call.data == "fishingTest":
            global answer
            global question
            fishingStep = 0
            connection= sqlite3.connect('Questions.db')
            cursor = connection.cursor()
            cursor.execute('SELECT txtvalue FROM Questions WHERE Qid > ?', (fishingStep,))
            question = cursor.fetchall()
            print(question)
            cursor.execute('SELECT answer FROM Questions WHERE Qid > ?', (fishingStep,))
            answer = cursor.fetchall()
            print(answer)
            connection.close()
            startFishingTest(call)
            
        if call.data == "1" or call.data == "2" or call.data == "3":
            answer_verif(call)
            #call.data == '0'
        #-------------MAIN MENU--------------------------------

    except Exception as e:
         print(repr(e))
    if call.data == "возврат":
        returnMenu(call)


def returnMenu(call):
    try:
        Inlinemarkup = types.InlineKeyboardMarkup(row_width=2)

        passwordButton = types.InlineKeyboardButton("Защита паролей", callback_data="пароли")
        fishingButton = types.InlineKeyboardButton("Фишинговые ссылки", callback_data="фишинг")
        virusButton = types.InlineKeyboardButton("Вирусы", callback_data="вирусы")
        scamButton = types.InlineKeyboardButton("Интернет-мошенники", callback_data="мошенники")

        Inlinemarkup.add(passwordButton)
        Inlinemarkup.add(fishingButton)
        Inlinemarkup.add(virusButton)
        Inlinemarkup.add(scamButton)

        bot.send_message(call.message.chat.id, "Вы вернулись в главное меню", reply_markup=Inlinemarkup)
    except Exception as e:
         print(repr(e))


def addBackButton():
    global InlineBackMarkup
    InlineBackMarkup = types.InlineKeyboardMarkup(row_width=2)

    backButton= types.InlineKeyboardButton("Вернуться назад", callback_data="возврат")

    KeyboardMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    return InlineBackMarkup.add(backButton)


@bot.callback_query_handler(func = lambda callback: True)
def startFishingTest(call):
    global fishingStep
    global answer
    global question
    global rightFishingAnswers


    #step = 0

    if fishingStep >= len(question):
        bot.send_message(call.message.chat.id,"Вы прошли тест, результаты сохранены и указаны ниже:")
        bot.send_message(call.message.chat.id,(str(rightFishingAnswers) +"/" + str(len(question))))
        userId = call.message.chat.id
        connectionUser = sqlite3.connect('mainDatabase.db')
        cursorUser = connectionUser.cursor()
        cursorUser.execute('UPDATE Users SET resultFishing = ? WHERE tgId = ?', (rightFishingAnswers, userId))
        rightFishingAnswers = 0
        connectionUser.commit()
        connectionUser.close()

        #userId = bot.user.id
        #cursorUser.execute()

        returnMenu(call)

        fishingStep = 0
    else:
        localMarkup = types.InlineKeyboardMarkup(row_width=2)
        frstButton = types.InlineKeyboardButton((fishingTestVar[fishingStep][0]),callback_data='1')
        scndtButton = types.InlineKeyboardButton((fishingTestVar[fishingStep][1]),callback_data='2')
        thrdButton = types.InlineKeyboardButton((fishingTestVar[fishingStep][2]),callback_data='3')
                        
        localMarkup.add(frstButton)
        localMarkup.add(scndtButton)
        localMarkup.add(thrdButton)
        bot.send_message(call.message.chat.id,question[fishingStep],reply_markup=localMarkup)

        fishingStep = fishingStep + 1

    

#@bot.callback_query_handler(func=lambda call: True)
#print(call.data)

def answer_verif(call):
    global rightFishingAnswers
    if (fishingStep - 1) >= len(answer):
        rightFishingAnswers = 0
        
    #print(fishingStep) 
    
    elif int(call.data) == answer[fishingStep - 1][0]:
        rightFishingAnswers = rightFishingAnswers + 1
    startFishingTest(call)  

    

#@bot.callback_query_handler(func = lambda call: True)




bot.polling(none_stop=True, interval=0)
