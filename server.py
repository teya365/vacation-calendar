from datetime import datetime

@app.route('/add', methods=['POST'])
def add():
    data = request.json

    # ✅ 날짜 포맷 변환
    raw_date = data.get("date")
    try:
        date = datetime.strptime(raw_date, "%Y-%m-%d").strftime("%Y-%m-%d")
    except:
        date = raw_date

    requests.get(API_URL, params={
        "name": data.get("name"),
        "date": date,
        "type": data.get("type")
    })

    return 'ok'
