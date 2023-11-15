from structure import History
from database import connect_db
from datetime import datetime
db = connect_db()

def deposit(sender_id, ammount):
  query = {"sender_id": sender_id}
  user = db["user"].find_one(query)
  if user:
    history = History(1, "deposit", ammount, datetime.now())
    db["user"].update_one(query,{"$set": {"current_balance": user["current_balance"] + ammount}})
    db["user"].update_one(query,{"$push": {"histories": history()}})
    user = db["user"].find_one(query)
    return user
  else:
    return "User doesn't exist", 502

def withdraw(sender_id, ammount):
  query = {"sender_id": sender_id}
  user = db["user"].find_one(query)
  if user:
    db["user"].update_one(query,{"$set": {"current_balance": user["current_balance"] - ammount}})
    user = db["user"].find_one(query)
    return user
  else:
    return "User doesn't exist", 502
  
def getCurrentBalance(sender_id):
  try:
    current_balance = db["user"].find_one({"sender_id": sender_id})["current_balance"]
    return current_balance
  except:
    return "Can't get current balance", 502

def getHistory(sender_id, numbers):
  try:
    history = db["user"].find_one({"sender_id": sender_id})["history"]
    return history[:numbers+1]
  except:
    return "Can't get histories", 502