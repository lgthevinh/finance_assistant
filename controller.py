import requests

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
