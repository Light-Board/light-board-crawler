
# Python module
import json
import os
import time
from dotenv import load_dotenv
from pymongo import MongoClient

# 환경변수값 세팅을
load_dotenv()

class DbCon:

    def __init__(self, logger) -> None:
        self.main_client = self.get_main_client()
        self.logger = logger


    # get connection
    def get_main_client(self):
        port = int(os.environ.get('MONGO_PORT'))
        user = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
        password = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')
        db = os.environ.get('MONGO_INITDB_DATABASE')

        client = MongoClient(
            'localhost', 
            port, 
            connect=False,
            username=user,
            password=password,
            authSource='admin')

        return client[f'{db}']


    # 크롤링 데이터 new data insert - main_once
    def insert_crawler_new_data(self, keyword: str, jobs: list):
        self.main_client[f'{keyword}_jobs'].create_index(("id"))         # mongodb collection index
        for job in jobs:
            try:
                target = self.main_client[f'{keyword}_jobs'].find_one({"id": job.get('id')})
                
                # new things! 
                if not target:
                    self.main_client[f'{keyword}_jobs'].insert_one(job)
                    self.logger.set_log(f"insert_crawler_new_data get new data! {job}")
            except Exception as e:
                self.logger.set_log(f"insert_crawler_new_data error: {job}, {type(e).__name__}, {type(e)}", "error")
                continue

    
    # 크롤링 데이터 전체 이니셜라이징 - main
    def insert_crawler_total_data(self, keyword: str, jobs: list):
        self.main_client[f'{keyword}_jobs'].create_index(("id"))         # mongodb collection index
        for job in jobs:
            try:
                self.main_client[f'{keyword}_jobs'].insert_one(job)
            except Exception as e:
                self.logger.set_log(f"insert_crawler_total_data error: {job}, {type(e).__name__}, {type(e)}", "error")
                continue


    # keyword 이니셜라이징
    def init_default_keyword(self, init_keyword: list):
        if not self.main_client.system_data.find_one({"type": "init_keyword"}):
            self.main_client.system_data.insert_one({ 
                "type": "init_keyword",
                "keywords": init_keyword
            })


    # system_data 얻어오기 - 이니셜라이징 데이터
    def get_init_data(self, _type: str):
        return self.main_client.system_data.find_one({"type": _type})