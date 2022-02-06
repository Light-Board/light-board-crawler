
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
# 참고로 BE와 Cralwer 가상환경은 분리되어 있음!
source .venv/bin/activate
python main.py
```

---
## [Nomad Crawler] Job 채용 웹 페이지

### 1. 자기소개

안녕하세요!

저희는 이제 막 대학교를 졸업하고 취업한 지 얼마 안 된 사회 초년생 개발자들입니다.

실무에서 회사 선배님들과 협업을 진행하면서 저희는 개발 능력이 부족하다고 느끼고 있었고, 부족한 부분을 채우기 위해 프로젝트를 진행하기로 했습니다. 어떤 주제에 대한 프로젝트를 진행할까 찾던 와중, 노마드코더에서 Job Scrapper 컨테스트를 진행하는 것을 알게 되었습니다.

이전에 노마드코더에서 학습을 통해 배운 것들과 실무에서 경험한 부분을 활용하여, Job Scrapper 프로젝트를 Product 단계와 같이 만들려고 노력한다면, 과정에서 개발자로서 많은 성장을 이뤄낼 수 있다고 생각하여 지원하게 되었습니다.

목표는 ***“누구나 쉽게 개발을 시작할 수 있는, 올인원 배포용 크롤러 앱 보일러 플레이트 만들기!! With 도커라이징!”*** 이었습니다!! 재사용 가능성을 최대한 열어두고 모두와 같이 기능을 하나씩 쌓아 올리고 싶었습니다. 


### 2. 서비스 소개

서비스 소개는 크게 기능 소개와 기술 소개로 2개로 나누어 소개하겠습니다!

#### 기능 소개

저희는 노마드코더에서 제공한 Job Scrapper와 비슷하게 검색 키워드에 따라, 직업 채용 정보를 4개 사이트(stackoverflow, indeed, dice ,flexjobs)에서 크롤링한 데이터를 기반으로 웹 페이지를 만들었습니다. 

그러나, 키워드 검색 뿐 아니라 기능을 추가한 부분이 크게 3가지가 있습니다!

1. **중요 키워드 버튼**입니다. 
    - 사용자들이 자주 검색할 키워드들 7가지를 선정했고, 해당 키워드들에 대한 데이터는 DB에 미리 저장시켜놓았습니다. 그래서 해당 키워드들로 검색 시에는 크롤링을 하지 않아 사용자들에게 직업 검색 결과를 바로 제공할 수 있도록 했습니다.

![사진](https://github.com/Light-Board/light-board-crawler/blob/develop/front-end/public/images/service_main_01.png?raw=true)

![사진](https://github.com/Light-Board/light-board-crawler/blob/develop/front-end/public/images/service_main_04.png?raw=true)

![사진](https://github.com/Light-Board/light-board-crawler/blob/develop/front-end/public/images/service_main_02.png?raw=true)


2. **페이지네이션**입니다.   
    - 저희는 위에 말씀드렸다시피 4개 사이트에서 데이터를 긁어오기 때문에 한 키워드에 대해 노출할 수 있는 데이터가 몇천건에 육박했습니다. 이를 한 화면에 보여주기에는 UI/UX 면에서 편리하지 않다고 생각하여, 한 페이지에 20개의 정보만 노출될 수 있도록 하였습니다.

![사진](https://github.com/Light-Board/light-board-crawler/blob/develop/front-end/public/images/service_main_03.png?raw=true)

3. **추천**입니다.
    - 인기 있는 채용 정보에 대한 노출은 다른 사용자들에게 편리함을 제공할 수 있다고 생각하여 채용 정보들 중 추천(`Recommend`)을 많이 받은 Top3 정보에 대해, 메인 페이지 상단에 노출되도록 하였습니다.
    - ip값과 job id값 기반으로 중복 추천 처리를 막았습니다!

![사진](https://github.com/Light-Board/light-board-crawler/blob/develop/front-end/public/images/service_main_05.png?raw=true)

![사진](https://github.com/Light-Board/light-board-crawler/blob/develop/front-end/public/images/service_main_06.png?raw=true)
  

#### 기술 소개

> 저희는 기술 stack으로 크게 FE, BE, Crontab, Database, Docker, AWS를 사용했습니다.


- FE
    - FE는 부트스트랩(html) + VanillaJavascript 으로 최대한 ES5+기준으로 나름 구조화 해서 만들었습니다. html을 이해해야 더 FE에 대한 깊은 이해를 할 수 있다는 부분, 동감했습니다!!
    - 그리고 최근에 노마드 형님이 올려주신 ```<datalist>``` 태그 활용을 했습니다!!
    - css/js/html을 나누고 js는 공통함수 common, API통신과 응답만 주는 store, 그리고 indexjs에서 모듈화된 함수를 활용하는 방식으로 사용했고 fetch와 async await를 최대한 활용했습니다.
    - 그리고 웹서버를 활용해 위 DOC 파일들을 Client에게 주었습니다!! nginx의 Conf를 제대로 활용해보는 경험이 너무나 좋았습니다.. 덤으로 404, 500 페이지를 비록 템플릿을 활용했지만, 웹서버 단에서 리턴해주는 방법을 활용했습니다!
    
    ![사진](https://github.com/Light-Board/light-board-crawler/blob/develop/front-end/public/images/service_main_07.png?raw=true)

    ![사진](https://github.com/Light-Board/light-board-crawler/blob/develop/front-end/public/images/service_main_08.png?raw=true)

- BE
    - Web Server로 nginx를 사용했고, WAS로서 flask를 활용해 rest api를 구축했습니다.

- Crawler
    - 저희는 사실 그냥 “1시간에 한 번 씩 어떻게 메인 크롤러만 돌려 DB업데이트 시켜서 FE에서 보여주자!“ 가 목표 였습니다. 어떤 방법을 쓰지? 결론은 리눅스의 크론탭 유틸 (데몬) 이었습니다.

    - 공통 부분을 core 로 모듈화 해서 나누고 각 사이트 마다 클래스 오브젝트를 만들어서 core의 함수를 오버라이딩 해서 파싱하는 방향으로 잡았습니다!

    - 데몬이 뭐고,, 크론탭이 뭐냐,, 부터 제로에서 시작하는 배움의 연속이었습니다. 마냥 python run! 으로는 가상 환경이나, 러닝 로그가 애매하더라고요! 그래서 해당 logging을 따로 하고 start shell을 .sh 로 만들었습니다! 저도 쉘 스크립트를 사용하는 순간이 오긴 오네요!!

- Database - MongoDB
    - DB는 긁어온 데이터를 쉽게, 다양한 형태로 저장하고 활용하기 위해 nosql - mongodb를 선택해 빠르게 개발에 착수했습니다. 
    - 각 페이지에서 부여하는 게시물 “id 값 기반 + 사이트이름” 을 db id값으로 잡아서 indexing 했고, 많은양 의 데이터 중 서치 속도를 조금이나마 향상 시킬 수 있었습니다.

    ![사진](https://github.com/Light-Board/light-board-crawler/blob/develop/front-end/public/images/service_main_09.png?raw=true)

- AWS
    - AWS를 한 번 도 써본 적 없는 저희는 서버도 호스팅 해버리자!! 그리고 보여주자!! 라는 일념으로 AWS를 1월 30일에 최초 회원가입해 EC2에 프리티어 인스턴스를 만들었습니다!! 그리고 인바운드 설정을 해매며 어찌 저찌 하고 난 뒤 공짜 도메인을 통해 DNS 설정까지 마무리 했습니다!! -> 도메인 네임은 [한국:내도메인](https://xn--220b31d95hq8o.xn--3e0b707e/) 이라는 곳을 활용했습니다!! 

- Docker

    - ~~역시 도커까지는 욕심이었나 싶었습니다.. compose 부터 하나하나 고생했습니다..~~

    - 크롤러는 어짜피 크론탭에 띄울꺼라, 메인 API 와는 개별적으로 돌아 도커라이징 대상에서는 제외했습니다.

    - Flask api app이 문제였습니다. 공식 python 이미지를 활용해 직접 api-app 이미지를 빌드하고 설정해야 했습니다. -> back-end의 Dockerfile 을 한 번 봐주세요 :)

    - nginx는 conf를 컨테이너에 접속해가며 변경하기는 싫었고, 그러다 보니 중요한 conf는 모두 밖으로 빼내 볼륨으로 잡아 줬고 FE는 빌드할 필요가 없는 static file로만 구성되어 있어서 바로 역시 볼륨으로 잡아 줬습니다. 

    - 그리고 ~/api/ 로 들어오는 요청은 3000번 포트 api(flask) 리버스 프록싱으로 처리했습니다. 이 한 마디가 굉장히 쉬워보였지만 직접 해보니까 진짜 쉽지 않더라고요. 처음엔 그냥 리다이렉션인가? 아니면 바이패스 개념인가? 굉장히 헷갈렸습니다. 그리고 로그도 바로바로 직접 보고 싶어 볼륨으로 잡아 줬습니다.

    - 가장 힘들었던 것은 mongodb였습니다. 에초에 conf 부터, 그 설정을 준 채로 도커이미지를 띄우는 것 조차 쉽지 않았습니다. 게다가 auth가 기본적으로 활성화 된 상태라 해당 설정을 disable한 상태로 띄워서 테스트하는게 말이 쉽지 모든게 익숙하지 않은 저희에게는 한 단계 단계 고비였습니다. 

    - 그렇게 해서 어떻게든 이미지를 띄웠더니!! mongodb auth 계정이 필요하다니! Auth 계정이 필요하다니!! 그래도 다행히 환경변수를 .env file로 바로 할 수 있는 방법을 깨닫고 바로 진행했습니다!!

    - 도커 컴포즈로 묶어서 도커 이미지를 돌리고 보니,, NAT 환경이 구성되어 각 이미지가 소통을 하려면 다른 네트워크로 (어쩌면 당연한 ㅠㅠ) 활성화 되더라고요!! 그래서 bridge network를 만들어서 각 이미지를 해당 네트워크를 이용하도록 했습니다!



### 3. 개발 과정 (어려웠던 점과 해결방법)

> 위에서 설명하면서 어느정도 말해버렸지만,, 직접 해보니까 매 순간이 어려웠습니다 ㅎㅎ :')

1. python으로 만든 restapi BE를 '배포'하려면 CGI interface개념이 필요하더라고요! WSGI등을 활용해서 배포해야 했는데, 이 부분은 앞으로 저희가 더 업그레이드 해 나갈 방향으로 잡았습니다! 우선 0.0.0.0으로 바인딩하고 app.py를 죽지 않게 살리는 방향으로 해결했습니다.

2. AWS 인스턴스를 실수로 중지 한 번 했다가 재가동 했더니 ip 할당이 바뀌는 것을 깨닫고 탄력적 IP 주소를 할당해서 다시 DNS에 등록해 마무리 했습니다! 그리고 EC2 인바운드 세팅을 통해 서버 방화벽의 존재를 다시금 깨달았습니다!

3. 로그인 등의 새션 없이 어떻게 '추천'을 쉽고 빠르게 만들까? 였습니다. 요청 client의 ip값고 고유한 job 게시글의 id를 활용했습니다! 

4. 도커라이징!!
    - mongodb의 도커라이징! 위 Docker에 대한 얘기를 했지만, mongodb의 기본 auth 접근 계정 설정도 참 많이 해멧습니다..
    - 각 컨테이너의 소통,, bridge network를 활용해서 해결했습니다!
    - 대표 이미지 외 직접 이미지화 해서 해당 이미지를 배포해야 하는 것도 어려웠습니다!

5. 기본 키워드 외 다른 키워드에 대한 검색 결과를 어떻게 빠르게 할 것인가? 
    - 고려한 방법은 'asyncio', 'multi-threading' 또는 'multi-processing' 이었습니다.
    - 제대로 이해하려면 생각보다 CS 기본 지식이 많이 필요하더라고요!! 덕분에 I/O Bound, CPU Bound를 고려하며 상황에 맞는 동시성 프로그래밍으로 접근을 해야 한다는 것을 깨달았습니다!
    - 우선 저희는 'asyncio'를 적용 시켰습니다! 

7. 빠르게 검색 결과를 가져오기 위해 DB 활용하고, 데이터를 가져왔는데 '어떻게 갱신하지'
    - 위 기술 소개에 언급 되었지만 간력하게 다시 말씀드리겠습니다!
    - 몇 분 당 한 번씩 타겟 페이지의 1페이지 정보만 가져와서 이미 있는 데이터와 비교하며 바뀐 것은 insert 치자!
    - 몇 분 당 한 번을 crontab으로 해결! crontab이라는 것을 깨닫고 실전에 돌입한 것은 처음이었습니다.. 사실 start shell을 구성하는 것 부터 고난이었습니다. 
    ```*/5 * * * * source /home/ubuntu/projects/light-board-crawler/crawler/script/run_shell.sh```

6. FE는 역시 어려워
    - 디자이너님은 신이십니다.
    - 동적으로 랜더링한 DOM object에 동적으로 EVENT를 바인딩하고 컨트롤하는 것이 어려웠습니다!
    - 나름 최대한 '관심사의 분리와 SPA'에 초점을 맞췃습니다.. 결국 조금 주먹 구구식이 된게 아쉽습니다. 


### 4. 앞으로 계획


약 2주간 해당 프로젝트를 친구와 함께 진행했는데요.

개발 진행하면서 개발 개념과 실력의 한계를 절실히 깨달으면서 앞으로 공부해야할 방향들이 더욱 명확해 지더라고요! “심플 노마드 크롤러 프로젝트!” 부터 여기까지 깨달음을 얻을 지 몰랐습니다. Clone code 방식으로 시작해 리뷰와 리팩토링을 하며 진짜 일취월장 했습니다. 항상 노마드 코더 덕분에 많은 것을 얻어 갈 수 있었어요!

프로젝트를 진행하면서 앞으로의 계획도 정해졌는데요~!

- 해당 프로젝트를 좀 더 고도화할 예정입니다! (이대로 두기에는 조금 아쉬운 감이 없지 않아 있네요 ㅠㅠ)
- 사용자들이 좀 더 편리하게 서비스를 사용할 수 있도록 초기 키워드 세팅을 동적으로 하고 데이터 초기화 부분을 좀 더 쉽게하려고 생각하고 있습니다 ㅎㅎ
- 또한, FE 쪽에 바벨링, webpack, lint 를 적용할 예정이고 Docker를 진행하면서 Kubernetes에 대해서도 알게 되었는데 추후에 Kuberentes를 적용하여 여러 컨테이너를 관리할 수 있도록 하면 좋겠다고 생각했습니다! (과정에서 헬스체크와 갑작스럽게 죽은 서버 관리, 모니터링 쪽에 대해서 추가적으로 다룰려고 생각하고 있습니다 ㅎㅎ)
- 그리고 진짜 초기 목표였던 ***“누구나 쉽게 개발을 시작할 수 있는, 올인원 배포용 크롤러 앱 보일러 플레이트 만들기!! With 도커라이징!”*** 꼭 이룰 수 있도록 범용성과 개발자를 위한 초기 개발 환경을 꼭 달성할 것입니!!

감사합니다!!

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

0. 공짜 도메인 설정하기! **[완/현우]**
    - https://xn--220b31d95hq8o.xn--3e0b707e/
    - nomad-crawl.kro.kr / www.nomad-crawl.kro.kr

1. front단 완성도 올리기
    - bootstrap 4 / vanilla javascript

2. 크롤러, 플라스크 DB 연동 **[완/현우]**
    - mongodb / pymongo: "ORM" -> "MVC" / model
    - 어떤 데이터를 저장할지 / 단일 collection 
    - "id, title, location, link" : 전체 공통
    - site(출처), created_at
    - id를 index로 잡고 -> 기본이 ObjectId
    - 하기 내용은 detail 정보에 추가해서 보여주기 
        - [company] flexjobs만 없음
        - [skillset] stack-overflow만 있음
    - collection 어떻게 나눌지 -> keyword 별로 나누는게 좋을 듯? 
        - 동적 collection name 받아오기
        - total, last_page DB 저장 로직 따로두기

3. 크론탭 설정 **[완/현우 등록만하면 끝]**
    - 데몬 프로세스
    - */20 * * * * run_shell.sh
    - cd + venv ~ active + nohup python 
    - logging -> 관리 대상 수준은 아닌듯

</details>



<details markdown="1">
<summary>2022.02.03 meet</summary>

1. front단 완성도 올리기
    - 기획 및 설계 완료, 작업 착수
    - bootstrap 4 / vanilla javascript

2. 크롤러 기초 데이터 구성하기
    - model(dict object)에 "heart" key 추가 

3. 따봉 로직
    - log collection에 ip 존재 여부 체크
    - 따봉 누른다 -> log collection에 ip + 따봉 누른 데이터 id값, 키워드 값 추가
    - keyword_jobs에 target id 값에 해당하는 heart 값 ++

4. 키워드 별 따봉 원탑 나열 API

5. 크론탭 설정 **[등록만하면 끝]**
    - */5 * * * * source /home/ubuntu/projects/light-board-crawler/crawler/script/run_shell.sh

</details>