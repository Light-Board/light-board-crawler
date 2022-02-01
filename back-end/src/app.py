
# module 
from util.file_util import (save_csv, save_json)
from util.Mongodb import (DbCon)
import pymongo

# python lib
from flask import (Flask, request, send_file, json, jsonify)
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
        result = main_db_con.get_init_data("init_keyword")
        response = app.response_class(
            status=200,
            response=json.dumps({"data": result}),
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
    
    # mongodb connection
    db = main_db_con.get_con()

    keyword = request.args.get('keyword', "all").lower() 
    page = int(request.args.get('page', 1))
    row = 20

    # 1. 해당 keyword가 DB에 존재하는가? -> collection 존재 여부 체크
    # 1-1. 존재한다면 DB 데이터 조회해서 반환하기
    if main_db_con.is_coll_exists(f"{keyword}_jobs"):
        total_count = db[f"{keyword}_jobs"].count_documents({})
        results = db[f"{keyword}_jobs"].find({},{"_id":0}).sort("id", pymongo.ASCENDING).skip((row * page) - row).limit(row)
        result_list = list()
        for r in results:
            result_list.append(r)

        response = app.response_class(
            status=200,
            response=json.dumps({
                "total_count": total_count,
                "data": result_list,
            }),
            mimetype='application/json'
        )
    # 1-2. 존재하지 않는다면, 크롤링 진행 후 긁어온 데이터 DB 저장하고 반환하기 -> 흠 이건 너무 작업이 해비함
    else: 
        response = app.response_class(
            status=400,
            response=json.dumps({"error": f"there is no any data"}),
            mimetype='application/json'
        )

    return response

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


app.run(host='0.0.0.0', port=3000, debug=True)
