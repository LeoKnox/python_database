import sqlite3
connection = sqlite3.connect('intro.db')

cursor = connection.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS Intro (Name TEXT, char_class TEXT,
    char_race TEXT, level INT)''')

connection.commit()
connection.close()