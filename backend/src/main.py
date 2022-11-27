from fastapi import FastAPI
from models import *


db.connect()
db.create_tables([Account, Event])
db.close()

app = FastAPI()


@app.get("/")
async def homepage():
    return "HELLO WORLD"


@app.post("/accounts/")
async def create_account(account: AccountModel):
    db.connect()
    newaccount = Account(username=account.username, firstname=account.firstname,
                         lastname=account.lastname, email=account.email)
    newaccount.save()
    db.close()
    return (201)


@app.get("/accounts/")
async def get_accounts():
    db.connect()
    query = list(Account.select().dicts())
    db.close()
    return query


@app.post("/events/")
async def create_event(event: EventModel):

    db.connect()
    id = Account.get(username=event.account.username)
    newevent = Event(account=id,name=event.name)
    newevent.save()
    db.close()
    return 201


@app.get("/events/")
async def get_event():
    db.connect()
    query = list(Event.select().dicts())
    result = []
    for event in query:
        result.append(Account.get_by_id(event["account"]))
    db.close()
    return result
