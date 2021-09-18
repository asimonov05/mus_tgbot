from flask import Flask, request, render_template
import requests
import os

token = os.environ.get('TOKEN')

app = Flask(__name__)

def send_message(chat_id, text):
    method = "sendMessage"
    global token
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        if request.json.get("message"):
            text = request.json["message"]["text"]
            chat_id = request.json["message"]["chat"]["id"]
            send_message(chat_id, text)
        print(request.json)
    return {"ok": True}

@app.route('/start_bot', methods = ["GET", "POST"])
def start_bot():
    global token
    if request.method == "POST":        
        url = request.form["url"]
        requests.post(f'https://api.telegram.org/bot{token}/setWebhook', data={"url": f"{url}"})
    return render_template("base.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)