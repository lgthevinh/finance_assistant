import requests
from datetime import datetime
from controller import deposit, withdraw, getCurrentBalance

#This is PAGE ACCESS TOKEN (get from Facebook Developer console)
PAGE_ACCESS_TOKEN = "EAAORjZCyWfKcBOZBIy1G55u20JF0fr3ZBKsExlNF6CAvQ0bwFs6ZCbL8212eZBUcutGaiyXbYwZBfImwIwiPfcYozkH5Dx539ZCGLl3mShmQnLf5SqE8kVAnTMjXtmox1kNgIxPijdFdZCdF7pLoUSmN2FwLqG5RIkFO6DsLt00doZAZAY93PrhQy3A3WWi9uW"
#This is API Key for Facebook messenger
API = "https://graph.facebook.com/v18.0/me/messages"

#Messenger API
def sendTextMessage(recipient, text):
  payload = {
    "recipient": {
      "id": recipient
    },
    "messaging_type": "RESPONSE",
    "message": {
      "text": text
    },
    "access_token": PAGE_ACCESS_TOKEN
  }
  response = requests.post(API, json=payload)
  return response.json()

def getCommand(sender_id, text):
  if "GET" == text[:4]:
    data = text.replace(" ", "_").split("_")
    try:
      ammount = int(data[1]) * 1000
      user = deposit(sender_id, ammount)
      message = "You have received {} at {}, your current balance is {}".format(ammount, datetime.now().strftime("%I:%M %p, %d %b %Y"), user["current_balance"])
    except Exception as e:
      print(e)
      message = "Wrong command, please check."
    response = sendTextMessage(sender_id, message)
    return response

  if "SPEND" == text[:6]:
    data = text.replace(" ", "_").split("_")
    try:
      ammount = int(data[1]) * 1000
      user = withdraw(sender_id, ammount)
      message = "You have spent {} at {}, your current balance is {}".format(ammount, datetime.now().strftime("%I:%M %p, %d %b %Y"), user["current_balance"])
    except Exception as e:
      print(e)
      message = "Wrong command, please check."
    response = sendTextMessage(sender_id, message)
    return response

  if "BALANCE" == text[:8]:
    response = sendTextMessage(sender_id, "Your current balance is {}".format(getCurrentBalance(sender_id)))
    return response
  
  return "Invalid command"

