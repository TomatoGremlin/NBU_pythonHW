'''  
Напишете програма, която създава нова SQLite база данни и създайте таблица food, 
която да бъде със структура като тази на първите пет атрибута в таблицата в текстовия файл retn5_dat.txt. 
Колоните на таблицата food трябва да са съответно code, descript, nmbr, nutname, retention.
Parse-вайки файла retn5_dat.txt попълнете таблицата с данните от него.
Името на базата данни трябва да е от вида fxxxxx-food.db, където XXXXX е вашият факултетен номер. 
Програмата с име FXXXXX_L12_T1.py, където XXXXX е вашият факултетен номер, 
да получава параметър от командния ред (със sys.argv, не от клавиатурата) символен низ със заявка, 
която връща само един ред.
Извеждайте на екрана само резултата от заявката. 
'''


import sqlite3
import sys


def createDatabase(database_name):

    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS food(
        code TEXT,
        descript TEXT, 
        nmbr TEXT, 
        nutname TEXT,
        retention TEXT)
        ''')

    conn.commit()
    conn.close()



def fillTable(database_name, input_file):
    
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    with open(input_file, 'r') as file:
        for line in file:
            fields = line.strip().split('^')

            code = fields[0].strip('~')
            descript = fields[1].strip('~')
            nmbr = fields[2].strip('~')
            nutname = fields[3].strip('~')
            retention = fields[4].strip('~')

            cursor.execute('INSERT INTO food VALUES (?, ?, ?, ?, ?)', (code, descript, nmbr, nutname, retention))

    conn.commit()
    conn.close()


def executeQuery(database_name, query):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    cursor.execute(query)
    result = cursor.fetchone()

    conn.close()
    return result


query = sys.argv[1]
#query = " SELECT * FROM food WHERE descript LIKE '%VEAL%' "


database_name = 'f104331-food.db' 
input_file = 'retn5_dat.txt'  
createDatabase(database_name)
fillTable(database_name, input_file)

result = executeQuery(database_name, query)
print(result)




    



