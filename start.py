import sqlite3
connection = sqlite3.connect('intro.db')

cursor = connection.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS Intro (Name TEXT, char_class TEXT,
    char_race TEXT, level INT)''')

#cursor.execute("INSERT INTO Intro VALUES ('Xingu', 'Fighter', 'Human', 3)")

ourChars = [('Colette', 'Rogue', 'Elf', 2),
    ('Aelien', 'Mage', 'Daemon', 2)]

#cursor.executemany('Insert INTO Intro VALUES (?,?,?,?)', ourChars)
our_list = cursor.execute("SELECT * FROM Intro")

for our in our_list:
    if our[3] == 3:
        print(our)

cursor.execute("SELECT * FROM Intro")

print(cursor.fetchall())

connection.commit()
connection.close()