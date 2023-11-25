import requests
from datetime import datetime

from utils import getIncome, spendIncome

# This is PAGE ACCESS TOKEN (get from Facebook Developer console)
PAGE_ACCESS_TOKEN = "EAAORjZCyWfKcBOZBIy1G55u20JF0fr3ZBKsExlNF6CAvQ0bwFs6ZCbL8212eZBUcutGaiyXbYwZBfImwIwiPfcYozkH5Dx539ZCGLl3mShmQnLf5SqE8kVAnTMjXtmox1kNgIxPijdFdZCdF7pLoUSmN2FwLqG5RIkFO6DsLt00doZAZAY93PrhQy3A3WWi9uW"
#This is API Key for Facebook messenger
API = "https://graph.facebook.com/v18.0/me/messages"

# Messenger API
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
  try:
    response = requests.post(API, json=payload)
    return response.json()
  except Exception as e:
    print(f'Failed to send message to {recipient} with error {e}')
    return 'Failed'

def getCommand(sender_id, text):
  if "GET" == text[:4]:
    message = getIncome(text)
    response = sendTextMessage(sender_id, message)
    return response

  if "SPEND" == text[:6]:
    message = spendIncome(text)
    response = sendTextMessage(sender_id, message)
    return response

  if "BALANCE" == text[:8]:
    response = sendTextMessage(sender_id, "Your current balance is {}")
    return response
  
  return "Invalid command"

