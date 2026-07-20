from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__)

# ✅ 본인 Apps Script URL
API_URL = "https://script.google.com/macros/s/AKfycbwfDEWx_lpPlJK3jJZdnrzcUaQi21oogv_Ytqs4cs8M5bv8Gbf77fdsqYkxzXDePTCfPg/exec"

@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# ✅ 데이터 추가 (구글시트 저장)
@app.route('/add', methods=['POST'])
def add():
    data = request.json
    
    # ✅ Apps Script는 form 방식이 안정적
    requests.post(API_URL, data={
        "name": data.get("name"),
        "date": data.get("date"),
        "type": data.get("type")
    })

    return 'ok'

# ✅ 데이터 조회 (구글시트 → 사이트)
@app.route('/list')
def list_data():
    res = requests.get(API_URL)
    return jsonify(res.json())

# ✅ Render용 실행
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
