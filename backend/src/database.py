from playhouse.cockroachdb import CockroachDatabase
from dotenv import load_dotenv
import os
from peewee import *
load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
db = CockroachDatabase(DATABASE_URL)


class BaseModel(Model):
    class Meta:
        database=db

class Account(BaseModel):
    username= CharField(unique=True)
    firstname=CharField()
    lastname=CharField()
    email=CharField(unique=True)


class Event(BaseModel):
    account=ForeignKeyField(Account)

db.connect()
db.drop_tables([Account,Event])
db.create_tables([Account,Event])
account = Account(username="meow",firstname="meowmeow",lastname="meowmeowmeow",email="meow@meow.com")
account.save()
db.close()
