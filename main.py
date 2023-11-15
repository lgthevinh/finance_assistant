from flask import Flask, request
from controllers.api import sendTextMessage, getCommand

app = Flask(__name__)
app.debug = True

ALLOWED_USER = ['6913965595292111']

@app.route("/", methods=['GET'])
def fbverify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "nmHwa2":
            print("Verification token missmatch")
            return "Verification token missmatch", 403
        return request.args['hub.challenge'], 200
    return "Hello world", 200

@app.route("/", methods=['POST'])
def fbwebhook():
    data = request.get_json()
    sender_id = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']
    print(data , sender_id)
    if message['text'] == "CONNECTION":
        response = sendTextMessage(sender_id, f'Finabot has connected to Meta Webhooks')
        print(response)
        return response
    if sender_id in ALLOWED_USER:
        response = getCommand(sender_id, message['text'])
        return response
    return data

if __name__ == "__main__":
    app.run(debug=True, port=3000)
    