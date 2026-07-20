from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__)

API_URL = "https://script.google.com/macros/s/AKfycbxN4e2qVbIw5m3FLkaVVb8_mzj3vdtxQCGGloC0n7s_4b7ud1HxfoK_7zmYvPM_DCmi/exec"

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# ✅ 데이터 추가 (구글시트 저장)
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
