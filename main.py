from flask import Flask, request
from api import getIncome, spendIncome
import controllers.messenger.messenger_utils as messenger_utils

app = Flask(__name__)
app.debug = True

ALLOWED_USER = ['6913965595292111']

def getAndResponse(sender_id, text):
  print(text)
  if "CONNECT" == text[:7]:
    message = "Fina bot has connected to your account"
    response = messenger_utils.sendTextMessage(sender_id, message)
  if "GET" == text[:3]:
    print(text)
    try:
      message = getIncome(text)
    except Exception as e:
      message = f'Error occured while adding income with error: {e}, please try again.'
    response = messenger_utils.sendTextMessage(sender_id, message)
    return response
  if "SPEND" == text[:5]:
    message = spendIncome(text)
    response = messenger_utils.sendTextMessage(sender_id, message)
    return response
  if "BALANCE" == text[:7]:
    response = messenger_utils.sendTextMessage(sender_id, "Your current balance is {}")
    return response
  return "Invalid command"


@app.route("/", methods=['GET'])
def fbverify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        print("Verifying webhook")
        if not request.args.get("hub.verify_token") == "ngf73hsd8":
            print("Verification token missmatch")
            return "Verification token missmatch", 403
        print("Verification successful")
        return request.args['hub.challenge'], 200
    return "Hello world", 200

@app.route("/", methods=['POST'])
def fbwebhook():
    # Extract data from request
    data = request.get_json()
    sender_id = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']
    print(data , sender_id)
    getAndResponse(sender_id, message['text'])
    return data

if __name__ == "__main__":
    app.run(debug=True, port=3000)
    