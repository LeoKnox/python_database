import sqlalchemy as db

engine = db.create_engine('sqlite:///intro.db')

connection = engine.connect()

metadata = db.MetaData()

intro = db.Table('Intro', metadata, autoload=True, autoload_with=engine)

query = db.select([intro])

result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()

print(result_set[0])
print(result_set[:2])

query = db.select([intro]).where(intro.columns.char_race == 'Elf')

result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()

print(result_set[0])

query = intro.insert().values(Name="Ynzon",char_class="Barbarian",char_race="Orc",level=4)

connection.execute(query)

query = db.select([intro])

result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()

print(result_set)