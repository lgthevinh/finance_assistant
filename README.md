# Fina Bot (2023)

Fina Bot is a financial assistance bot designed to help manage your finances.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Built With

* [Python](https://www.python.org/) - The programming language used.
* [Google Sheets API](https://developers.google.com/sheets/api) - Used to store and retrieve data.

## Code Overview

### main.py

#### Overview

This is the main entry point of the application.

#### Code Explanation

This Python script uses the Flask web framework to create a webserver interact with Facebook's Messenger Platform. Here's a breakdown of what each part does:

```python
from flask import Flask, request
from api import get_and_response

app = Flask(__name__)
app.debug = True

ALLOWED_USER = ['6913965595292111']
```
This part imports necessary modules and sets up a new Flask web application. ALLOWED_USER is a list of user IDs that are allowed to interact with the bot.

```python
@app.route("/", methods=['GET'])
def fbverify():
    ...
```
This function handles GET requests to the root URL ("/"). It's used by Facebook to verify your webhook. Facebook sends a GET request with specific parameters, and your server must respond correctly to verify the webhook.

```python
@app.route("/", methods=['POST'])
def fbwebhook():
    ...
```
This function handles POST requests to the root URL. These requests are sent by Facebook when a user sends a message to your bot. The function extracts the sender ID and message text from the request, and passes them to get_and_response to generate a response.

```python
if __name__ == "__main__":
    app.run(debug=True, port=3000)
```
This part runs the Flask server when the script is run directly (not imported as a module). The server runs in debug mode on port 3000.

### api.py

#### Overview

This file contains the main logic of the bot. It includes functions for handling income, spending, and fetching balance. It interacts with Google Sheets to store and retrieve data.

#### Code Explanation

This file contains the main logic of the Fina Bot. It includes functions for handling income, spending, and fetching balance. It interacts with Google Sheets to store and retrieve data.

```python
from datetime import datetime
import locale

from controllers.google.google_utils import * # Import all functions from google_utils.py
import controllers.messenger.messenger_utils as messenger_utils

locale.setlocale(locale.LC_ALL, 'vi_VN') # Set locale to Vietnamese
```
The above code imports necessary modules and sets the locale to Vietnamese.

```python
COMMANDS = [
  "CONNECT",  # Check Messenger connection
  "GET",      # Add income
  "SPEND",    # Add expense
  "BALANCE"   # Get balance
  ]
```
The COMMANDS list contains all the commands that the bot can handle.

```python
try: 
  creds = create_creds()
  service = build_service(creds)
  print("Service built successfully")
except Exception as e:
  print(f'Error occured while building service with error: {e}')
```
The above code tries to create credentials and build the service for Google Sheets. If there's an error, it prints the error message.

```python
def fetch_balance():
  ...
def get_income(text: str):
  ...
def spend_income(text: str):
  ...
```
These functions handles BALANCE, GET, SPEND commands

```python
def get_and_response(sender_id, text):
  ...
```
The get_and_response function processes the command from the user and sends a response back.

## Authors

* **Luong The Vinh** - *University of Engineering and Technology (UET-VNU)* - [lgthevinh](https://github.com/lgthevinh)

## License

This project is licensed under the MIT License - see the [MIT LICENSE](LICENSE) file for details