import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from __init__ import create_creds

SPREEDSHEET_ID = "1OW96c4zdAHSr2zmQuEjS9JIgbF6BJ1BL7QooLMJ8e3w"
RANGE_NAME = "2024!A2:D1000"

creds = create_creds()
service = build("sheets", "v4", credentials=creds)

def get_values(spreadsheet_id, range_name):
  """
  Creates the batch_update the user has access to.
  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """
  # pylint: disable=maybe-no-member
  try:
    result = (service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute())
    rows = result.get("values", [])
    print(f"{len(rows)} rows retrieved")
    return result
  except HttpError as error:
    print(f"An error occurred: {error}")
    return error
  
def batch_update_values(spreadsheet_id, range_name, value_input_option, values):
  """
  Creates the batch_update the user has access to.
  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """
  # pylint: disable=maybe-no-member
  try:
    data = [{"range": range_name, "values": values}] # Additional ranges to update.
    body = {"valueInputOption": value_input_option, "data": data}
    result = (service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute())
    print(f"{(result.get('totalUpdatedCells'))} cells updated.")
    return result
  except HttpError as error:
    print(f"An error occurred: {error}")
    return error

def append_values(spreadsheet_id, range_name, value_input_option, values):
  """
  Append values of user written.
  Load pre-authorized user credentials from the environment.
  TODO(developer) - See https://developers.google.com/identity
  for guides on implementing OAuth2 for the application.
  """
  # pylint: disable=maybe-no-member
  try:
    body = {
      "majorDimension": "ROWS",
      "values": values,
    }
    result = (service.spreadsheets().values().append(
      spreadsheetId=spreadsheet_id, 
      range=range_name, 
      valueInputOption=value_input_option,
      insertDataOption="INSERT_ROWS",
      body=body,
    ).execute())
    print(f'{result.get("updates").get("updatedCells")} cells appended.')
    return result
  except HttpError as error:
    print(f"An error occurred: {error}")
    return error

# DEBUG MODE
# if __name__ == "__main__":
#   # Pass: spreadsheet_id, range_name value_input_option and _values
#   append_values(
#       SPREEDSHEET_ID,
#       '2024!A2',
#       "USER_ENTERED",
#       [["27/11", "Test", "Shopping", 100000]],  
#   )
