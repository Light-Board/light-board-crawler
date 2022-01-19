## 1. Crontab

- 활용
    - 파이썬 파일 실행하여, 특정 키워드로 채용 사이트에서 크롤링하여 데이터베이스에 데이터 저장
- 사용
    ```
    $ crontab -e
    $ 10 * * * * {execute_file_path}/main.py
    ```
    - crontab 로그 남길 것인지 고민 > 주기적으로 로그 삭제하는 crontab도 등록해야 함
- 특이사항
    - 크롤링할 대상 키워드에 대해 첫 페이지만 크롤링 해서 DB에 데이터 저장하기
        - 특정 사이트의 특정 키워드에 대해 2page~lastpage 까지는 미리 크롤링해서 저장해놓기

<br/>

## 2. Python Crawling

- 활용
    - 검색 키워드로 채용 정보를 각기 다른 채용 사이트에서 정보를 취합하기
    - 검색 데이터를 CSV 파일로 제공 (JSON은 굳이 제공 안해도 될 것 같음)
- 크롤링 대상 사이트
    - 사이트마다, 일일이 크롤러 코드 작성해야 하기 때문에 3~4개가 적당할 것 같음
    - stackoverflow (https://stackoverflow.com/jobs)
    - indeed (https://www.indeed.com/jobs?)
    - dice (https://www.dice.com/jobs)
    - build-in (https://builtin.com/jobs)
- 검색 키워드
    - 무슨 키워드 할 것인지 정하기
    - python
    - php
    - java
    - golang
    - nest
    - spring
    - react
    - vue
    - 등등..
- 주의 사항
    - 검색하는 키워드가 crontab으로 데이터를 크롤링하는 키워드라면?
        - DB 데이터를 조회하여 보여주기
    - 검색하는 키워드가 crontab으로 데이터를 크롤링하는 키워드가 아니라면?
        - 바로 Crawling을 수행하여 DB에 저장 후, 보여주기
        - 여러 개 사이트 크롤링하면, 대기 시간 길 것 같은데 이 부분은 어떻게 해결할지? 아니면 해결하지 않을 것인지?

<br/>

## 3. Database (MySQL)
- schema
    - 스키마 이름 : crawler
- table
    - keyword 
        - 키워드 목록 관리
        ```
            CREATE TABLE IF NOT EXISTS `crawler`.`keyword` (
             `keyword` VARCHAR(30) NOT NULL,
             PRIMARY KEY (`keyword`))
             ENGINE = InnoDB
             DEFAULT CHARACTER SET = utf8;
        ```
    - job
        - 채용 정보 관리
        ```
            CREATE TABLE IF NOT EXISTS `crawler`.`job` (
             `link` VARCHAR(1000) NOT NULL,
             `title` VARCHAR(100) NOT NULL,
             `company` VARCHAR(1000),
             `skill` VARCHAR(1000),
             `location` VARCHAR(1000) NOT NULL,
             `pay` VARCHAR(1000) NOT NULL,     
             PRIMARY KEY (`link`))
             ENGINE = InnoDB
             DEFAULT CHARACTER SET = utf8;
        ```
<br/>

## 4. Server (python Flask)

- 활용
    - 사용자가 특정 domain으로 접속했을 때, 취합한 데이터 정보로 View를 제공
- API 종류
    - 제공해야할 path 기준으로 생각
    - home API
        - 키워드를 검색할 수 있는 메인 페이지
        - path : `"/home"`
    - search API
        - 사용자가 키워드 입력하여, 채용 정보 검색
        - path : `"/search"`
        - param
            - `keyword`
    - job API
        - 특정 키워드에 대한, 채용 정보 보여주는 페이지
            - pagination으로 제공
        - path : `"/job"`
        - param
            - `keyword`
            - `pageNumber`
            - `row`
    - csv API
        - 특정 키워드에 대한, 채용 정보를 CSV 파일로 추출
        - path : `"/export"`
        - param
            - `keyword`
<br/>


## 5. Front (react.js)
- 활용
    - 사용자에게 보여질 페이지    
- View 
    - home
        - 검색창
        - 가지고 있는 데이터 그래프로 표현
        - 나머지는 잘 꾸미기 
    - job
        - 키워드로 검색된 채용 정보
            - 페이지네이션 적용
        - CSV 파일 추출 버튼   
<br/>
