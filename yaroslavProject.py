#--------EXTERNAL LIBRARIES-------

import telebot
from telebot import types

import sqlite3

#-------PRESETS AND VARIABLES-----

bot = telebot.TeleBot('6652275990:AAF9kBBdNLicha65GICiHHYIhQCxitLF9Lc')



#global previousFishingStep

global step
global rightAnswers
global switch
switch = 0
rightAnswers = 0
step = 0

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
                  ["Утечка данных", "Попадание к мошенникам", "Все перечисленное"]]

virusTestVar = [["Программа для заражения компьтеров","ПО, увеличивающее скорость ПК", "ПО для усиления безопасности"],
                ["Файлы из Интернета","Спутниковое телевидение","Почта"],
                ["Троянский конь","Рекламное ПО", "Вирус-червь"],
                ["Взлом банковских счетов","Противодействие доступа к компьютерам","Получение доступа к данным"],
                ["Социальный вирус","Вирус-червь","Рекламное ПО"],
                ["Установка антвирусов","Обслуживание ПК","Использование общего Wifi"],
                ["Сканирует на наличие вирусов","Проводит каптчу","Улучшает ПК"],
                ["ПО, требующее выкуп","Крупная атака хакеров","Задача разработчика вируса"],
                ["Взлом почтовых ящиков","ПО предоставляющее доступ к ПК","Антивирусное ПО"],
                ["Передача шпионской информации", "Взлом паролей","Аттака для отключения сервера"],
                ["Исправляют недочеты в ОС","Удаляют вирусы с ПК","Замедляют работу ПК"],
                ["Вирус,скрывающий активность","ПО для производительности","Система безопасноти ПК",],
                ["Запах гари при включении","Изображение котенка на рабочем столе","Медленная работа ПК"],
                ["Выключить компьютер","Ничего не делать","Запустить антивирус"],
                ["ПО для защиты ПК","ПО для увеличения скорости","Игры, зараженные вирусами"]]


passwordTestVar = [["Перебор паролей","Вид мошенничества","Компьютерный вирус"],
                   ["123456","Состоящий из имени","Состоящий из случайной комбинации"],
                   ["Предоставить пароль","Если оф.источник, то предоставить","Не предоставлять"],
                   ["Использовать одно и то же слово","Использовать личные данные","Использовать уникальные комбинации"],
                   ["Подтверждение двумя паролями","Идентификация двумя формами","Метод связи двух банков"],
                   ["Использовать простые комбинации","Использовать одинаковые пароли","Все перечисленное"],
                   ["Изменение пароля спецалгоритмом","Публичное раскрытие пароля","Удаление пароля из системы"],
                   ["Имя и фамилия","Название улицы","Случайная комбинация"],
                   ["Проигнорировать","Поменять пароль и написать в поддержку","Поделиться с друзьями"],
                   ["Пароль, который долго не используется","Пароль на носимом устройстве","Одноразовый пароль"],
                   ["Запись пароля на видном месте","Использование парольных мессенджеров","Хранение в облаке"],
                   ["Использовать одинаковый пароль","Использовать разные пароли","Распространять пароли"],
                   ["Поделиться личными данными","Перебирать пароли","Использовать восстановление"],
                   ["Легко запоминаемый пароль","Пароль, состоящий из цифр","Пароль,состоящий из комбинаций"],
                   ["Сохранение в открытом виде","Использование парольного мессенджера","Сообщение пароля по почте"]]


scamTestVar = [["Метод рыбалки","Вид мошенничества","Очистка рыбы"],
               ["Номер паспорта","Имя и фамилия","Любимый жанр музыки"],
               ["Номер телефона","Пароль от электронной почты","Все перечисленное"],
               ["Предоставить пароль","Если оф.запрос, то предоставить","Никогда не предоставлять"],
               ["Обновлять антивирус","Оставлять личные данные","Использовать общий Wifi"],
               ["Однофакторная аутентификация","Двухфакторная аутентификация","Бесфакторная аутентификация"],
               ["Находиться в панике","Связаться с правохранительными органами","Игнорировать происшествие"],
               ["Имя домашнего питомца","Дата рождения","Произвольная комбинация"],
               ["Обновлять пароли","Предоставлять банковскую информацию","Оставаться на данном сайте"],
               ["Предоставить информацию","Перезвонить в банк","Заблокировать номер"],
               ["Лекарство от болезни","Вредоносная программа","Что-то полезное для ПК"],
               ["Нежелательная почта","Американские консервы","Блокировщик рекламы"],
               ["Обновить антивирус","Ничего не делать","Выключить ПК"],
               ["Пользоваться общим Wifi для покупок","Покупать товары со странных сайтов","Пользоваться HTTPS"],
               ["Предоставить персональные данные","Использовать антивирус","Щелкать по спам-ссылкам"]]





@bot.message_handler(commands=['start'])

def start(message):
    separated_list = []
    global chatId
    global InlineStartMarkup


    InlineStartMarkup = types.InlineKeyboardMarkup(row_width=2)

    moreInfoButton = types.InlineKeyboardButton("Узнать больше", callback_data="узнать больше")

    KeyboardMarkup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    InlineStartMarkup.add(moreInfoButton)
    bot.send_message(message.from_user.id, "👋Приветствую, я чат-бот, созданный для повышения уровня квалификации пенсионеров в области компьютерной безопасности")

    connectionUser = sqlite3.connect('mainDatabase.db')
    cursorUser = connectionUser.cursor()
    
    userData = cursorUser.execute('SELECT tgId FROM Users')
    user = userData.fetchall()
    chatId = message.chat.id

    for separator in user:
        separated_list.extend(separator)
    
    if str(chatId) not in separated_list:
            cursorUser.execute('INSERT INTO Users  (tgId) VALUES (?)', (chatId,))
            connectionUser.commit()

    else:
        results_raw = cursorUser.execute('SELECT tgId,resultFishing,resultScam,resultVirus,resultPassword FROM Users ')
        results = results_raw.fetchall()
        connectionUser.commit()
        for i in range(len(results) - 1):
            if str(chatId) == results[i][0]:
                resultFishing = results[i][1]
                resultsScam = results[i][2]
                resultVirus = results[i][3]
                resultPassword = results[i][4]
                bot.send_message(message.from_user.id,("Ваши результаты по тестам: "))
                bot.send_message(message.from_user.id,("Тест по фишингу: "+ str(resultFishing)))
                bot.send_message(message.from_user.id,("Тест по интернет-мошенникам: "+ str(resultsScam)))
                bot.send_message(message.from_user.id,("Тест по вирусам: "+ str(resultVirus)))
                bot.send_message(message.from_user.id,("Тест по паролям: "+ str(resultPassword)))


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
                InlineTestmarkup = types.InlineKeyboardMarkup(row_width=2)
                testButton = types.InlineKeyboardButton("Запустить тест", callback_data="virusTest")

                InlineTestmarkup.add(testButton)

                bot.send_message(call.message.chat.id, text, reply_markup=InlineBackMarkup)
                bot.send_message(call.message.chat.id,"Вы можете пройти тест по теме",reply_markup=InlineTestmarkup)

                file.close()

        elif call.data == "мошенники":
            with open("scamInfo.txt", "r", encoding="utf-8") as file:
                text = file.read()
                addBackButton()
                InlineTestmarkup = types.InlineKeyboardMarkup(row_width=2)
                testButton = types.InlineKeyboardButton("Запустить тест", callback_data="scamTest")
                InlineTestmarkup.add(testButton)

                bot.send_message(call.message.chat.id, text, reply_markup=InlineBackMarkup)
                bot.send_message(call.message.chat.id,"Вы можете пройти тест по теме",reply_markup=InlineTestmarkup)
                file.close()

        elif call.data == "пароли":
            with open("passwdInfo.txt", "r", encoding="utf-8") as file:
                text = file.read()
                addBackButton()
                InlineTestmarkup = types.InlineKeyboardMarkup(row_width=2)
                testButton = types.InlineKeyboardButton("Запустить тест", callback_data="passwdTest")
                InlineTestmarkup.add(testButton)

                bot.send_message(call.message.chat.id, text, reply_markup=InlineBackMarkup)
                bot.send_message(call.message.chat.id,"Вы можете пройти тест по теме",reply_markup=InlineTestmarkup)
                file.close()


        if call.data == "fishingTest":
            global answer
            global question
            global switch
            #fishingStep = 0
            connection= sqlite3.connect('Questions.db')
            cursor = connection.cursor()
            cursor.execute('SELECT txtvalue FROM Questions WHERE Qid > ?', (0,))
            question = cursor.fetchall()
            cursor.execute('SELECT answer FROM Questions WHERE Qid > ?', (0,))
            answer = cursor.fetchall()
            connection.close()
            switch = "fishing"
            startTest(call)

        elif call.data == "virusTest":
            
            connection= sqlite3.connect('Questions1.db')
            cursor = connection.cursor()
            cursor.execute('SELECT txtvalue FROM Questions WHERE Qid > ?', (0,))
            question = cursor.fetchall()
            cursor.execute('SELECT answer FROM Questions WHERE Qid > ?', (0,))
            answer = cursor.fetchall()
            connection.close()
            switch = "virus"
            startTest(call)

        elif call.data == "scamTest":

            connection= sqlite3.connect('Questions3.db')
            cursor = connection.cursor()
            cursor.execute('SELECT txtvalue FROM Questions WHERE Qid > ?', (0,))
            question = cursor.fetchall()
            cursor.execute('SELECT answer FROM Questions WHERE Qid > ?', (0,))
            answer = cursor.fetchall()
            connection.close()
            switch = "scam"
            startTest(call)

        elif call.data == "passwdTest":

            connection= sqlite3.connect('Questions2.db')
            cursor = connection.cursor()
            cursor.execute('SELECT txtvalue FROM Questions WHERE Qid > ?', (0,))
            question = cursor.fetchall()
            cursor.execute('SELECT answer FROM Questions WHERE Qid > ?', (0,))
            answer = cursor.fetchall()
            connection.close()
            switch = "password"
            startTest(call)

        
            
        if call.data == "1" or call.data == "2" or call.data == "3":
          
            answer_verif(call)
           
    except Exception as e:
         print(repr(e))
    if call.data == "возврат":
        returnMenu(call)


def returnMenu(call):
    connectionUser = sqlite3.connect('mainDatabase.db')
    cursorUser = connectionUser.cursor()
    chatId = call.message.chat.id
    try:
        results_raw = cursorUser.execute('SELECT tgId,resultFishing,resultScam,resultVirus,resultPassword FROM Users ')
        results = results_raw.fetchall()
        connectionUser.commit()
        connectionUser.close()
        for i in range(len(results) - 1):
            if str(chatId) == results[i][0]:
                resultFishing = results[i][1]
                resultsScam = results[i][2]
                resultVirus = results[i][3]
                resultPassword = results[i][4]
                bot.send_message(call.message.chat.id,("Ваши результаты по тестам: "))
                bot.send_message(call.message.chat.id,("Тест по фишингу: "+ str(resultFishing)))
                bot.send_message(call.message.chat.id,("Тест по интернет-мошенникам: "+ str(resultsScam)))
                bot.send_message(call.message.chat.id,("Тест по вирусам: "+ str(resultVirus)))
                bot.send_message(call.message.chat.id,("Тест по паролям: "+ str(resultPassword)))
        

    except Exception as e:
        print(repr(e))

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
def startTest(call):
    global step
    global rightAnswers
    global answer
    global question
    global switch


    #step = 0

    if step >= len(question):
        bot.send_message(call.message.chat.id,"Вы прошли тест, результаты сохранены и указаны ниже:")
        bot.send_message(call.message.chat.id,(str(rightAnswers) +"/" + str(len(question))))
        userId = call.message.chat.id
        connectionUser = sqlite3.connect('mainDatabase.db')
        cursorUser = connectionUser.cursor()
        if switch == "fishing":
            cursorUser.execute('UPDATE Users SET resultFishing = ? WHERE tgId = ?', (rightAnswers, userId))

        if switch == "virus":
            cursorUser.execute('UPDATE Users SET resultVirus = ? WHERE tgId = ?', (rightAnswers, userId))

        if switch == "scam":
            cursorUser.execute('UPDATE Users SET resultScam = ? WHERE tgId = ?', (rightAnswers, userId))
        
        if switch == "password":
            cursorUser.execute('UPDATE Users SET resultPassword = ? WHERE tgId = ?', (rightAnswers, userId))

        connectionUser.commit()
        connectionUser.close()

        returnMenu(call)

        step = 0
    else:
        localMarkup = types.InlineKeyboardMarkup(row_width=1)
        
        if switch == "fishing":
            frstButton = types.InlineKeyboardButton((fishingTestVar[step][0]),callback_data='1')
            scndtButton = types.InlineKeyboardButton((fishingTestVar[step][1]),callback_data='2')
            thrdButton = types.InlineKeyboardButton((fishingTestVar[step][2]),callback_data='3')

        elif switch == "virus":
            frstButton = types.InlineKeyboardButton((virusTestVar[step][0]),callback_data='1')
            scndtButton = types.InlineKeyboardButton((virusTestVar[step][1]),callback_data='2')
            thrdButton = types.InlineKeyboardButton((virusTestVar[step][2]),callback_data='3')

        elif switch == "scam":
            frstButton = types.InlineKeyboardButton((scamTestVar[step][0]),callback_data='1')
            scndtButton = types.InlineKeyboardButton((scamTestVar[step][1]),callback_data='2')
            thrdButton = types.InlineKeyboardButton((scamTestVar[step][2]),callback_data='3')
        
        elif switch == "password":
            frstButton = types.InlineKeyboardButton((passwordTestVar[step][0]),callback_data='1')
            scndtButton = types.InlineKeyboardButton((passwordTestVar[step][1]),callback_data='2')
            thrdButton = types.InlineKeyboardButton((passwordTestVar[step][2]),callback_data='3')

                        
        localMarkup.add(frstButton)
        localMarkup.add(scndtButton)
        localMarkup.add(thrdButton)

        bot.send_message(call.message.chat.id,question[step],reply_markup=localMarkup)

        step = step + 1

    
def answer_verif(call):
    global switch
    global rightAnswers
    global step

    if (step - 1) >= (len(answer)):

        rightAnswers= 0
        
    
    elif int(call.data) == answer[step - 1][0]:
        rightAnswers = rightAnswers + 1

    startTest(call)  


bot.polling(none_stop=True, interval=0)
