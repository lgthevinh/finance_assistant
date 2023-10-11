from database import connect_db

db = connect_db()

def addToBalance(sender_id, ammount):
  return