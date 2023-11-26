from datetime import datetime
from controllers.google.google_utils import append_values, build_service, create_creds
import controllers.messenger.messenger_utils as messenger_utils

# This is SPREADSHEET ID (get from Google Sheet URL), RANGE_NAME is the sheet name and range data
SPREEDSHEET_ID = "1OW96c4zdAHSr2zmQuEjS9JIgbF6BJ1BL7QooLMJ8e3w"
RANGE_NAME = "2024!A2:D1000"

# This is the category of the income and expense
CATEGORY = ["Shopping", "Education", "Food", "Healthcare", "Transportation", "Work", "Family"]

try: 
  creds = create_creds()
  service = build_service(creds)
  print("Service built successfully")
except Exception as e:
  print(f'Error occured while building service with error: {e}')

def getIncome(text: str):
  try:
    # Data manipulation
    data = text.replace(" ", "_").split("_")
    name = str(data[1])
    category = str(data[2])
    amount = int(data[3]) * 1000
    print("Data manipulated successfully")
    # Check if category is valid
    if category not in CATEGORY:
      message = 'Invalid category, please choose one of these category: ' + ', '.join(CATEGORY)
      return message
    else: # If valid, append to Google Sheet
      append_values(service, SPREEDSHEET_ID, RANGE_NAME, "USER_ENTERED", [[datetime.now().strftime("%d/%m"), "IN", name, category, amount]])
      message = f'You have received {amount} on {name} at {datetime.now().strftime("%I:%M %p, %d %b %Y")}'
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
    else: # If valid, append to Google Sheet
      append_values(service, SPREEDSHEET_ID, RANGE_NAME, "USER_ENTERED", [[datetime.now().strftime("%d/%m"), "OUT", name, category, amount]])
      message = f'You have spent {amount} on {name} at {datetime.now().strftime("%I:%M %p, %d %b %Y")}'
  except Exception as e:
    # If error, return error message
    message = f'Error occured while adding expense with error: {e}, please try again.'
  return message

def getAndResponse(sender_id, text):
  if "CONNECT" == text[:7]:
    message = "Fina bot has connected to your account"
    response = messenger_utils.sendTextMessage(sender_id, message)
  if "GET" == text[:4]:
    try:
      message = getIncome(text)
    except Exception as e:
      message = f'Error occured while adding income with error: {e}, please try again.'
    response = messenger_utils.sendTextMessage(sender_id, message)
    return response
  if "SPEND" == text[:6]:
    try:
      message = spendIncome(text)
    except Exception as e:
      message = f'Error occured while adding expense with error: {e}, please try again.'
    return response
  if "BALANCE" == text[:8]:
    response = messenger_utils.sendTextMessage(sender_id, "Your current balance is {}")
    return response
  return "Invalid command"
