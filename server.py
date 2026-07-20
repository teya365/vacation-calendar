from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__)

API_URL = "https://script.google.com/macros/s/AKfycbwfDEWx_lpPlJK3jJZdnrzcUaQi21oogv_Ytqs4cs8M5bv8Gbf77fdsqYkxzXDePTCfPg/exec"

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/add', methods=['POST'])
def add():
    data = request.json
    requests.post(API_URL, json=data)
    return 'ok'

@app.route('/list')
def list_data():
    res = requests.get(API_URL)
    return jsonify(res.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
