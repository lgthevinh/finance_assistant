import sys
sys.path.append('../config')

from config.config_project import PAGE_ACCESS_TOKEN
import requests

# This is API Key for Facebook messenger
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
