from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__)

API_URL = "https://script.google.com/macros/s/AKfycbyrUQjHLgpo6aminWudHWfbR3eztVV1ehUpPYAIGGC7CtHwhTGqf6TIc27PYE4Qv-55/exec"

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# ✅ 데이터 추가
@app.route('/add', methods=['POST'])
def add():
    data = request.json

    requests.get(API_URL, params={
        "name": data.get("name"),
        "date": data.get("date"),
        "type": data.get("type")
    })

    return 'ok'

# ✅ 데이터 조회
@app.route('/list')
def list_data():
    res = requests.get(API_URL)
    return jsonify(res.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
