import datetime

def getIncome(text: str):
  data = text.replace(" ", "_").split("_")
  try:
    amount = int(data[1]) * 1000
    message = f'You have received {amount} at {datetime.now().strftime("%I:%M %p, %d %b %Y")})'
  except Exception as e:
    message = 'Invalid amount, type amount with numbers, not text.'
  return message

def spendIncome(text: str):
  data = text.replace(" ", "_").split("_")
  try:
    amount = int(data[1]) * 1000
    message = f'You have received {amount} at {datetime.now().strftime("%I:%M %p, %d %b %Y")})'
  except Exception as e:
    message = 'Invalid amount, type amount with numbers, not text.'
  return message