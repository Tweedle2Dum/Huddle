from playhouse.cockroachdb import CockroachDatabase
from dotenv import load_dotenv
import os
from peewee import *
import peewee
load_dotenv()
import pydantic
from typing import List,Any,Union
from pydantic.utils import GetterDict

DATABASE_URL = os.getenv('DATABASE_URL')
db = CockroachDatabase(DATABASE_URL)

class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res

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
    name=CharField()



class AccountModel(pydantic.BaseModel):
    
    username:pydantic.constr()
    firstname:pydantic.constr()
    lastname:pydantic.constr()
    email:pydantic.constr()

    class Config:
        orm_mode=True
        getter_dict=PeeweeGetterDict


class EventModel(pydantic.BaseModel):
    
    account:AccountModel
    name:pydantic.constr()

    class Config:
        orm_mode=True
        getter_dict=PeeweeGetterDict


 


