from datetime import datetime
import locale

from controllers.google.google_utils import * # Import all functions from google_utils.py
import controllers.messenger.messenger_utils as messenger_utils

locale.setlocale(locale.LC_ALL, 'vi_VN') # Set locale to Vietnamese

COMMANDS = [
  "CONNECT",  # Check Messenger connection
  "GET",      # Add income
  "SPEND",    # Add expense
  "BALANCE"   # Get balance
  ]

try: 
  creds = create_creds()
  service = build_service(creds)
  print("Service built successfully")
except Exception as e:
  print(f'Error occured while building service with error: {e}')

def fetch_balance():
  try:
    current_year = str(datetime.now().strftime("%Y"))
    result = get_values(service, SPREEDSHEET_ID, current_year+BALANCE_RANGE)
    balance = result['values'][0][0] # Get the first value of the first row
    message = f'Your current balance is {balance} on {datetime.now().strftime("%H:%M, %d-%m-%Y")}' # No need to format balance because it's already formatted in Google Sheet
  except Exception as e:
    message = f'Error occured while fetching balance with error: {e}'
  return message

def get_income(text: str):
  try:
    current_year = str(datetime.now().strftime("%Y"))
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
      append_values(service, SPREEDSHEET_ID, current_year+RANGE_NAME, "USER_ENTERED", [[datetime.now().strftime("%d/%m"), "IN", name, category, amount]])
      message = f'You have received {locale.currency('%d', amount, grouping=True)} on {name} at {datetime.now().strftime("%H:%M, %d-%m-%Y")}'
  except Exception as e:
    # If error, return error message
    message = f'Error occured while adding income with error: {e}, please try again.'
  return message

def spend_income(text: str):
  try:
    current_year = str(datetime.now().strftime("%Y"))
    # Data manipulation
    data = text.replace(" ", "_").split("_")
    name = str(data[1])
    category = str(data[2])
    amount = int(data[3]) * 1000
    # Check if category is valid
    if category not in CATEGORY:
      message = 'Invalid category, please choose one of these category: ' + ', '.join(CATEGORY)
    else: # If valid, append to Google Sheet
      append_values(service, SPREEDSHEET_ID, current_year+RANGE_NAME, "USER_ENTERED", [[datetime.now().strftime("%d/%m"), "OUT", name, category, amount]])
      message = f'You have spent {locale.currency(amount, grouping=True)} on {name} at {datetime.now().strftime("%H:%M, %d-%m-%Y")}'
  except Exception as e:
    # If error, return error message
    message = f'Error occured while adding expense with error: {e}, please try again.'
  return message

def get_and_response(sender_id, text):
  command = text.replace(" ", "_").split("_")
  if command[0] in COMMANDS:
    try:
      if command[0] == "CONNECT":
        message = "Fina bot has connected to your account"
      if command[0] == "GET":
        message = get_income(text)
      if command[0] == "SPEND":
        message = spend_income(text)
      if command[0] == "BALANCE":
        message = fetch_balance()
    except Exception as e:
      message = f'Error occured while processing command with error: {e}, please try again.'
  else:
    message = "Invalid command, please try again."
  return messenger_utils.sendTextMessage(sender_id, message)
