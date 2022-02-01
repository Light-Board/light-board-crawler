
# module 
from util.file_util import (save_csv, save_json)
from util.Mongodb import (DbCon)

# python lib
from flask import (Flask, request, send_file, json)
from bson import json_util  # for mongodb result return 
import datetime

# static
app = Flask("SuperScrapper")
main_db_con = DbCon() # db connection


# BE TEST PING 
@app.route("/api/ping", methods=['GET'])
def testPing():
    response = app.response_class(
        status=200,
        response=json.dumps({"test": "ok"}),
        mimetype='application/json'
    )
    return response


# 등록된 키워드 리스트 가져오기
@app.route("/api/keyword", methods=['GET'])
def getKeywords():
    try:
        result = list(main_db_con.get_init_data("init_keyword"))
        response = app.response_class(
            status=200,
            response=json.dumps(result, default=json_util.default),
            mimetype='application/json'
        )
    except Exception as e:
        response = app.response_class(
            status=500,
            response=json.dumps({"error": f"server error: {e}"}),
            mimetype='application/json'
        )
    return response


# 메인 API, 검색 결과 얻어오기
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

    # 1-2. 존재하지 않는다면, 크롤링 진행 후 긁어온 데이터 DB 저장하고 반환하기 -> 노노 이건 너무 작업이 해비함


# 검색 결과 추출 
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
