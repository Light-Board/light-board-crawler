
# 채용 사이트 크롤러

> 노마드 코더 ***"금 한 돈 프로젝트"***

## getting start

```bash
# Python 3.7.3 version 이상
# Pip 21.3.1 version 이상

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements_v(최신).txt

```

---

## Test running

```bash
# 프로젝트 경로 이동 - main.py 실행 
source .venv/bin/activate
python main.py
```

---

## Daily ToDo


<details markdown="1">
<summary>2022.01.26 meet</summary>

1. last_page 어떻게 구할 것인지 **[완]**
    - 각 키워드 별로 페이지 수 구하고 단발 배치성
    - 최초 크롤링 시 page마다 sleep 주고 last page까지 가보기


2. 첫 페이지만 크롤링하는 파일이랑, 라스트 페이지까지 모두 크롤링하는 파일이랑 분리 필요 **[완]**
    - 메인으로 분리해서, 단발 배치성 메인과 크론탭 첫 페이지
    - 메인 파일 완성하기


3. python 경량 서버 구축 **[완/세영]**
    - web server(nginx, 80 port)
        - /api/ -> restapi (3000)
        - /media/ -> file 접근
    - BE flask restapi (3000 port) / 하단에 API end point List / [27일까지 Flask 세영]
        - /api/search?keyward={}&page={}
        - /api/export?keyward={}&type={}
            - filename: keyward-createdat-random_seq.type
            - csv, json
            - DB에서 "keyward = site" query -> 결과 모두 추출
        - jwt + OAuth [option]


4. front단 구축 **[완/현우]**
    - bootstrap 4 / vanilla javascript
    - SPA
    - html의 환장의 콜라보 


5. DB 연동
    - mongodb / pymongo: "ORM" -> "MVC" / model
    - 어떤 데이터를 저장할지 / 단일 collection 
    - "id, title, location, link" : 전체 공통
    - site(출처), created_at
    - id를 index로 잡고 -> 기본이 ObjectId
    - 하기 내용은 detail 정보에 추가해서 보여주기 
        - [company] flexjobs만 없음
        - [skillset] stack-overflow만 있음


6. 크론탭 설정
    - 데몬 프로세스
    - */20 * * * * run_shell.sh
    - cd + venv ~ active + nohup python 
    - logging -> 관리 대상 수준은 아닌듯


7. infra **[완/현우]**
    - server 구축
    - docker, docker compose
    - DNS 오또케? free dns 있으면 쓰고 없으면 재끼고
</details>


<details markdown="1">
<summary>2022.01.29 meet</summary>

1. front단 완성도 올리기
    - bootstrap 4 / vanilla javascript

2. 크롤러, 플라스크 DB 연동
    - mongodb / pymongo: "ORM" -> "MVC" / model
    - 어떤 데이터를 저장할지 / 단일 collection 
    - "id, title, location, link" : 전체 공통
    - site(출처), created_at
    - id를 index로 잡고 -> 기본이 ObjectId
    - 하기 내용은 detail 정보에 추가해서 보여주기 
        - [company] flexjobs만 없음
        - [skillset] stack-overflow만 있음

3. 크론탭 설정
    - 데몬 프로세스
    - */20 * * * * run_shell.sh
    - cd + venv ~ active + nohup python 
    - logging -> 관리 대상 수준은 아닌듯

</details>