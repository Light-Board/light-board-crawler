import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

class Request:

    # 생성자
    def __init__(self, site_name, url, logger) -> None:
        self.site_name = site_name
        self.url = url
        self.logger = logger

    # url set
    def set_url(self, url):
        self.url = url

    # HTTP 요청에 필요한 header setting
    def get_headers(self, **kwargs) -> dict:

        # 민간함 해더 값 
        origin = kwargs.get('origin', self.url)
        referer = kwargs.get('referer', 'https://google.com')
        ua = UserAgent()
        
        headers = {
            "authority": "stackoverflow.com",
            "pragma": "no-cache",
            "cache-control": "no-cache",
            "sec-ch-ua": '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            "sec-ch-ua-mobile": "?0",
            "upgrade-insecure-requests": "1",
            "accept": "application/json, text/plain, */*",
            "user-Agent": ua.random,
            "origin": origin,
            "referer": referer,
            "sec-fetch-site": "cross-site",
            "sec-fetch-mode": "cors",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "empty",
            "accept-language": "en,ko-KR;q=0.9,ko;q=0.8,en-US;q=0.7"            
        }

        # 추가 헤더 값 체크
        if kwargs.get('cookie', None) is not None:
            headers['cookie'] = kwargs.get('cookie')
        if kwargs.get('x-api-key', None) is not None:
            headers['x-api-key'] = kwargs.get('x-api-key')
        if kwargs.get('authority', None) is not None:
            headers['authority'] = kwargs.get('authority')            

        return headers

    # 실제 request 던지는 부분
    # 쿼리 파라미터로 붙은 놈들은 url에 포함 시켜서 사용, body값 (json, multipart ...)
    def get_html(self, method_type: str, headers, data, querystring=None, is_json=False):
        try:
            res = requests.request(method_type, self.url, data=data, headers=headers, params=querystring)
            if res.status_code != 200:
                raise Exception(f"res status code is not 200 - {res.status_code}")
            if is_json:
                return res.json()
            else:
                return BeautifulSoup(res.content, 'lxml')
        except requests.Timeout:
            self.logger.set_log(f"{self.site_name} get_html error: 요청 일시 벤 먹음", "error")
        except requests.exceptions.ProxyError:
            self.logger.set_log(f"{self.site_name} get_html error: 프록시 일시 벤 먹음", "error")
        except requests.exceptions.ConnectionError:
            self.logger.set_log(f"{self.site_name} get_html error: 요청 일시 벤 먹음", "error")
        except requests.exceptions.ChunkedEncodingError:
            self.logger.set_log(f"{self.site_name} get_html error: 요청 일시 벤 먹음", "error")
        except requests.exceptions.TooManyRedirects:
            self.logger.set_log(f"{self.site_name} get_html error: 요청 거부 당함", "error")
        except Exception as e:
            self.logger.set_log(f"{self.site_name} get_html error: {e}, {type(e).__name__}, {type(e)}", "error")
