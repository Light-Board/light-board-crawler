from core.Crawler import Crawler
import time

class FlexJobs(Crawler):

    def __init__(self, logger):
        super().__init__("flexjobs", "https://www.flexjobs.com/search", logger)
        self.origin_url = "https://www.flexjobs.com"

    def get_last_page(self, keyword):
        html = self.parsing_html(search=keyword, page=1)
        pagination = html.find("ul", {"class": "pagination"})
        links = pagination.find_all('li')
        last_page = links[-2].string
        return int(last_page)


    # 오버라이딩
    def parsing_html(self, **kwargs):
        header_append_dict = {
            "origin": self.origin_url,
            "authority": "www.flexjobs.com"
        }
        querystring = {
            "search":f"{kwargs.get('search', '')}",
            "page":f"{kwargs.get('page', '1')}"
        }        
        headers = self.get_headers(**header_append_dict)
        html = self.get_html("GET", headers, "", querystring=querystring)
        return html


    # 
    def extract_job(self, target_data):
        warpper = target_data.find('div', {'class': 'job-category-jobs'}).find('ul')
        warpper = warpper.find_all('li')
        return_list = list()
        for li in warpper:
            return_dict = dict()

            try:
                return_dict['id'] = f"{self.site_name}-{li.get('data-job')}"
                return_dict['title'] = li.get('data-title')
                return_dict['location'] = li.find('div', {'class':'job-locations'}).get_text().strip()
                return_dict['link'] = f"{self.origin_url}{li.get('data-url')}"
            except Exception:
                continue
            
            return_list.append(return_dict)
        
        return return_list

    # 
    def extract_jobs(self, keyword, last_page):
        jobs = []

        for page in range(1, last_page + 1):
            self.logger.set_log(f"Scrapping FlexJobs {keyword} Page : {page} crawl")
            target_html = self.parsing_html(search=keyword, page=page)
            jobs += (self.extract_job(target_html))

            time.sleep(3)
                
        return jobs
