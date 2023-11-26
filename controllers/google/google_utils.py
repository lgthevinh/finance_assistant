import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# This is SPREADSHEET ID (get from Google Sheet URL), RANGE_NAME is the sheet name and range data
SPREEDSHEET_ID = "1OW96c4zdAHSr2zmQuEjS9JIgbF6BJ1BL7QooLMJ8e3w"
RANGE_NAME = "2024!A2:D1000"

# This is the category of the income and expense
CATEGORY = ["Shopping", "Education", "Food", "Healthcare", "Transportation"]

# Google API

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# This function is used to create the credentials
def create_creds():
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("./config/token.json"):
    creds = Credentials.from_authorized_user_file("./config/token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "./config/credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("./config/token.json", "w") as token:
      token.write(creds.to_json())
  return creds

def build_service(creds):
  """Builds the service for the Sheets API.
  """
  # pylint: disable=maybe-no-member
  service = build("sheets", "v4", credentials=creds)
  return service

def get_values(service, spreadsheet_id, range_name):
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
  
def batch_update_values(service, spreadsheet_id, range_name, value_input_option, values):
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

def append_values(service, spreadsheet_id, range_name, value_input_option, values):
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