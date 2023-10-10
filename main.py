from flask import Flask, request
from controller import sendTextMessage, getCommand

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
    sender_id = data['entry'][0]['messaging'][0]['sender']['id']
    if sender_id == '6913965595292111':
        message = data['entry'][0]['messaging'][0]['message']
        if message['text'] == "test":
            response = sendTextMessage(sender_id, "test")
            print(response)
            return response
        else:
            response = getCommand(sender_id, message['text'])
            print(response)
            return response
if __name__ == "__main__":
    app.run(debug=True, port=3000)
    