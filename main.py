from flask import Flask, request
import requests
from controller import sendTextMessage

app = Flask(__name__)
app.debug = True

@app.route("/", methods=['GET'])
def fbverify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "vri3aSD":
            print("Verification token missmatch")
            return "Verification token missmatch", 403
        return request.args['hub.challenge'], 200
    return "Hello world", 200

@app.route("/", methods=['POST'])
def fbwebhook():
    data = request.get_json()
    print(data)
    message = data['entry'][0]['messaging'][0]['message']
    sender_id = data['entry'][0]['messaging'][0]['sender']['id']
    if message['text'] == "test":
        response = sendTextMessage(sender_id, "test")
        print(response)
        return response
if __name__ == "__main__":
    app.run(debug=True, port=3000)
    