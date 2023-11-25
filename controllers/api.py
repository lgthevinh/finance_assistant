import requests
import datetime 
from google_utils import append_values, get_values, SPREEDSHEET_ID, RANGE_NAME, CATEGORY
from messenger_utils import sendTextMessage

def getIncome(text: str):
  try:
    # Data manipulation
    data = text.replace(" ", "_").split("_")
    name = str(data[1])
    category = str(data[2])
    amount = int(data[3]) * 1000
    # Check if category is valid
    if category not in CATEGORY:
      message = 'Invalid category, please choose one of these category: ' + ', '.join(CATEGORY)
      return message
    # If valid, append to Google Sheet
    append_values(SPREEDSHEET_ID, RANGE_NAME, [[datetime.now().strftime("%d/%m"), "IN", name, category, amount]])
    message = f'You have received {amount} at {datetime.now().strftime("%I:%M %p, %d %b %Y")})'
  except Exception as e:
    # If error, return error message
    message = f'Error occured while adding income with error: {e}, please try again.'
  return message

def spendIncome(text: str):
  try:
    # Data manipulation
    data = text.replace(" ", "_").split("_")
    name = str(data[1])
    category = str(data[2])
    amount = int(data[3]) * 1000
    # Check if category is valid
    if category not in CATEGORY:
      message = 'Invalid category, please choose one of these category: ' + ', '.join(CATEGORY)
      return message
    # If valid, append to Google Sheet
    append_values(SPREEDSHEET_ID, RANGE_NAME, [[datetime.now().strftime("%d/%m"), "OUT", name, category, amount]])
    message = f'You have spent {amount} at {datetime.now().strftime("%I:%M %p, %d %b %Y")})'
  except Exception as e:
    # If error, return error message
    message = f'Error occured while adding expense with error: {e}, please try again.'
  return message

def getAndResponse(sender_id, text):
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
