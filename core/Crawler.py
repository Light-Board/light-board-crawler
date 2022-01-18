
# python module
from bs4 import BeautifulSoup

# other core module
from core.Request import Request
from core.Logging import set_start_log

class Crawler(Request):

    # 생성자, 부모 생성자 주의
    def __init__(self, site_name, url) -> None:
        super().__init__(site_name, url)


    # HTML 파일 data parsing
    def parsing_html(self, **kwargs):
        headers = self.get_headers(**kwargs)
        html = self.get_html("GET", headers, "")


    # 저장 필요한 데이터 핸들링 - DB or Static file
    def save_target_data(self):
        pass
    

    # 크롤링 하는 메인 부분
    def crawler_main(self):
        set_start_log(self.site_name)
        self.parsing_html()
        self.save_target_data()