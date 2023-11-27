from flask import Flask, request
from api import get_and_response

app = Flask(__name__)
app.debug = True

ALLOWED_USER = ['6913965595292111']

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
    get_and_response(sender_id, message['text'])
    return data

if __name__ == "__main__":
    app.run(debug=True, port=3000)
    