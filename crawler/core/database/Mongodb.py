
# Python module
import json
import os
from dotenv import load_dotenv
from pymongo import MongoClient

# 환경변수값 세팅을
load_dotenv()
mySecret = os.environ.get('MySecret')


class DbCon:

    def __init__(self, logger) -> None:
        self.main_client = self.get_main_client()
        self.logger = logger


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


    # 크롤링 데이터 Total Insert
    def insert_crawler_data(self, all_jobs: list):
        self.main_client.jobs.create_index(("id"))         # mongodb collection index
        for job in all_jobs:
            try:
                self.main_client.jobs.insert_one(job)
            except Exception as e:
                self.logger.set_log(f"insert_crawler_data error: {job}, {type(e).__name__}, {type(e)}", "error")
                continue