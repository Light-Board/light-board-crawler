from core.Request import Request


class Crawler(Request):

    # 생성자, 부모 생성자 주의
    def __init__(self, site_name, url, logger) -> None:
        super().__init__(site_name, url, logger)

    # HTML 파일 data parsing
    def parsing_html(self, **kwargs):
        headers = self.get_headers(**kwargs)
        html = self.get_html("GET", headers, "")
        return html

    def get_last_page(self, keyword: str) -> int:
        """Overrides get_last_page()"""
        pass

    def extract_jobs(self, keyword: str, last_page: int) -> list:
        """Overrides extract_jobs()"""
        pass
