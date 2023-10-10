import requests
from datetime import datetime

#This is PAGE ACCESS TOKEN (get from Facebook Developer console)
PAGE_ACCESS_TOKEN = "EAAORjZCyWfKcBOZBZAliLlH80RgbukyrjZAugw5vIWJ8lksBkZCNcce5b2t7bVsPNsoqvXSDdhSaJjqjs5LWFVTCY1TSQm60X3e3BcBmQQZAuKlW2r5JKCcyHqMnlL5cdFx8s9YEEibOZCBXJZCjDrGM100wZCEZBCgHdtF6mvuzB5814ruZC1j4lTYfWg5srjg"
#This is API Key for Facebook messenger
API = "https://graph.facebook.com/v2.6/me/messages"

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
    if type(data[1]) is int:
      message = "You have received {} at {}, your current balance is {}".format(data[1], datetime.now().strftime("%I:%M %p, %d %b %Y"), 200 + int(data[1]))
    else:
      message = "Wrong command, please check."
    response = sendTextMessage(sender_id, message)
    print(response)
    return response
  return "Invalid command", 403