
from core.Crawler import Crawler

class StackOverFlow(Crawler):
    
    # 오버라이딩
    def parsing_html(self, **kwargs):
        headers = self.get_headers(**kwargs)
        html = self.get_html("GET", headers, "")
        print(html)
        # temp = html.find('div', {'class': 'listResults'})
        
        # # 데이터 파싱
        # for div in temp.find_all('div'):
        #     try:
        #         print(div.find('h2').get_text())
        #     except Exception:
        #         continue
