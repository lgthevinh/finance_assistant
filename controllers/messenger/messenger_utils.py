import requests

# This is PAGE ACCESS TOKEN (get from Facebook Developer console)
PAGE_ACCESS_TOKEN = "EAAORjZCyWfKcBO2yuPukZBsEBUPJcwddVGyNyNwW7XTm6ZBhKFZCU7IZChJk9o9AEHZBejBCeEwXkzXJNgkpF8MTSiLYSa7otTFibgIiutIiltjMtQqVXK0exr5DUeWidORU54W5jpjUIumu0UkuEqmWvj90Oifekv7YkTlK70dRIPAZBLivGDe8ieJfV4ZC"
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
