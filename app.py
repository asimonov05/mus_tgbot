from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        print(request.json)
    return {"ok": True}

@app.route('/start_bot')
def start_bot():
    token = '2024499408:AAHWeU_4iRWurzzUMDLETBWmQ6h_amfY9Mg'
    url = "https://8c2b-109-252-124-11.ngrok.io"
    requests.post(f'https://api.telegram.org/bot{token}/setWebhook', data={"url": f"{url}"})
    return 'ok'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)