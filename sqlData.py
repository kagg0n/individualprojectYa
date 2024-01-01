import sqlite3

# Устанавливаем соединение с базой данных
connectionUser = sqlite3.connect('mainDatabase.db')
cursorUser = connectionUser.cursor()

# Создаем таблицу Users
cursorUser.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,

tgId TEXT NOT NULL,
resultFishing INTEGER,
resultScam INTEGER,
resultVirus INTEGER,
resultPassword INTEGER

)

''')
# создаем таблицу вопросов
connectionUser.commit()
connectionUser.close()

