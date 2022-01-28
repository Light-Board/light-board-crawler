from core.Crawler import Crawler

class FlexJobs(Crawler):

    def __init__(self):
        super().__init__("flexjobs", "https://www.flexjobs.com/search")
        self.origin_url = "https://www.flexjobs.com"

    def get_last_page(self, keyword):
        self.set_url(f"{self.origin_url}/search?page=2&search={keyword}")
        print(self.url)
        html = self.parsing_html()
        pagination = html.find("ul", {"class": "pagination"})
        links = pagination.find_all('li')
        last_page = links[-2].string
        print(last_page)
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
        # return {
        #     'id': target_data.get('id', "null"),
        #     'title': target_data.get('title', "null"), 
        #     'company': target_data.get('companyName', "null"),
        #     'location': "null" if target_data.get('jobLocation', "null") == "null" else target_data.get('jobLocation').get('displayName'), 
        #     'link': target_data.get('detailsPageUrl', "null")
        #     # skill_set 관련 내용은 서머리에 있음,, 해당 서머리는 long text
        # }


    # 
    def extract_jobs(self, keyword, last_page):
        jobs = []

        for page in range(1, last_page + 1):
            print(f"Scrapping FlexJobs Page : {page}")
            target_html = self.parsing_html(search=keyword, page=page)
            jobs += (self.extract_job(target_html))
                
        return jobs