from pymongo.mongo_client import MongoClient

USER = "lgthevinh"
PASSWORD = "ibuErFWW0OK4zXYD"

def connect_db():
  uri = "mongodb+srv://lgthevinh:ibuErFWW0OK4zXYD@project-a.auwb3mk.mongodb.net/?retryWrites=true&w=majority"
  # Create a new client and connect to the server
  client = MongoClient(uri)
  # Send a ping to confirm a successful connection
  try:
      client.admin.command('ping')
      print("Pinged your deployment. You successfully connected to MongoDB!")
      my_db = client["fina_bot"]
      print(client.list_database_names())
      return my_db
  except Exception as e:
      print(e)
      return e