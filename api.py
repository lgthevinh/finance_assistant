import requests
from datetime import datetime

#This is PAGE ACCESS TOKEN (get from Facebook Developer console)
PAGE_ACCESS_TOKEN = "EAAORjZCyWfKcBOZBIy1G55u20JF0fr3ZBKsExlNF6CAvQ0bwFs6ZCbL8212eZBUcutGaiyXbYwZBfImwIwiPfcYozkH5Dx539ZCGLl3mShmQnLf5SqE8kVAnTMjXtmox1kNgIxPijdFdZCdF7pLoUSmN2FwLqG5RIkFO6DsLt00doZAZAY93PrhQy3A3WWi9uW"
#This is API Key for Facebook messenger
API = "https://graph.facebook.com/v18.0/me/messages"

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
  if "#thu" == text[0:4]:
    data = text.replace(" ", "_").split("_")
    if type(int(data[1])) is int:
      message = "You have received {} at {}, your current balance is {}".format(data[1], datetime.now().strftime("%I:%M %p, %d %b %Y"), 200 + int(data[1]))
    else:
      message = "Wrong command, please check."
    response = sendTextMessage(sender_id, message)
    return response
  if "#chi" == text[0:4]:
    data = text.replace(" ", "_").split("_")
    if type(int(data[1])) is int:
      message = "You have spent {} at {}, your current balance is {}".format(data[1], datetime.now().strftime("%I:%M %p, %d %b %Y"), 200 - int(data[1]))
    else:
      message = "Wrong command, please check."
    response = sendTextMessage(sender_id, message)
    return response
  else:
    return "Invalid command", 200