from peewee import *

db = SqliteDatabase('cashball.db')

class Cashball(Model):
    casino = CharField()
    datetime = CharField()
    dollar = IntegerField()

    class Meta:
        database = db

db.connect()
db.create_tables([Cashball])
db.close()