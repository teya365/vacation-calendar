from flask import Flask, request, jsonify, send_from_directory
import json
import os

app = Flask(__name__)

FILE = 'data.json'

if os.path.exists(FILE):
    with open(FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
else:
    data = []

def save():
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

@app.route('/add', methods=['POST'])
def add():
    data.append(request.json)
    save()
    return 'ok'

@app.route('/delete', methods=['POST'])
def delete():
    idx = request.json['index']
    if 0 <= idx < len(data):
        data.pop(idx)
        save()
    return 'ok'

@app.route('/list')
def list_data():
    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
