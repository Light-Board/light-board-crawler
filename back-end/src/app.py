from flask import (Flask, request, send_file, json)
from util.file_util import (save_csv, save_json)
import datetime

app = Flask("SuperScrapper")


# BE TEST PING 
@app.route("/api/ping", methods=['GET'])
def testPing():
    response = app.response_class(
        status=200,
        response=json.dumps({"test": "ok"}),
        mimetype='application/json'
    )
    return response



@app.route("/api/search", methods=['GET'])
def searchJobs():
    keyword = request.args.get('keyword')
    page = request.args.get('page')
    row = 20

    if not page:
        page = 1

    if keyword:
        keyword = keyword.lower()

    # 1. 해당 keyword가 DB에 존재하는가?

    # 1-1. 존재한다면 DB 데이터 조회해서 반환하기

    # 1-2. 존재하지 않는다면, 크롤링 진행 후 긁어온 데이터 DB 저장하고 반환하기


@app.route("/api/export", methods=['GET'])
def exportJobs():
    keyword = request.args.get('keyword')
    type = request.args.get('type')

    if not keyword:
        raise Exception()

    keyword = keyword.lower()

    # keyword에 대해, DB 조회
    jobs = [{"title": "python developer", "company": "naver", "location": "sungNam", "link": "https://www.naver.com"}]

    if not jobs:
        raise Exception()

    file_name = f"{keyword}_{datetime.datetime.now()}"

    if type == "csv":
        save_csv(file_name, ["Title", "Company", "Location", "Link"], jobs)
        return send_file(f"{file_name}.csv")
    elif type == "json":
        save_json(file_name, jobs)
        return send_file(f"{file_name}.json")


app.run(host='0.0.0.0', port=3000)
