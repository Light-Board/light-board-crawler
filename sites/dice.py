from core.Crawler import Crawler

class Dice(Crawler):

    def __init__(self):
        super().__init__("dice", "https://job-search-api.svc.dhigroupinc.com/v1/dice/jobs/search")
        self.origin_url = "https://job-search-api.svc.dhigroupinc.com/v1/dice/jobs/search"


    # 오버라이딩
    def parsing_html(self, **kwargs):
        header_append_dict = {
            "origin": "https://www.dice.com",
            "referer": "https://www.dice.com/",
            "authority": "job-search-api.svc.dhigroupinc.com",
            "x-api-key": "1YAt0R9wBg4WfsF9VB2778F5CHLAPMVW3WAZcKd8",
        }
        querystring = {
            "q":f"{kwargs.get('search', '')}",
            "countryCode2":"US","radius":"30","radiusUnit":"mi","page":f"{kwargs.get('page', '1')}","pageSize":"20",
            "facets":"employmentType|postedDate|workFromHomeAvailability|employerType|easyApply|isRemote",
            "fields":"id|jobId|summary|title|postedDate|modifiedDate|jobLocation.displayName|detailsPageUrl|salary|clientBrandId|companyPageUrl|companyLogoUrl|positionId|companyName|employmentType|isHighlighted|score|easyApply|employerType|workFromHomeAvailability|isRemote",
            "culture":"en","recommendations":"true","interactionId":"0","fj":"true","includeRemote":"true",
            "eid":"a6zd7NUgR0Wy8Tzf36TS2Q_|Sh_4hXkUSsuaDyYXXmPLAQ_2"
        }        
        headers = self.get_headers(**header_append_dict)
        result_json = self.get_html("GET", headers, "", querystring=querystring, is_json=True)
        return result_json['data']



    # 
    def extract_job(self, target_data):
        return {
            'id': f"{self.site_name}-{target_data.get('id', 'null')}",
            'title': target_data.get('title', "null"), 
            'company': target_data.get('companyName', "null"),
            'location': "null" if target_data.get('jobLocation', "null") == "null" else target_data.get('jobLocation').get('displayName'), 
            'link': target_data.get('detailsPageUrl', "null")
            # skill_set 관련 내용은 서머리에 있음,, 해당 서머리는 long text
        }


    # 
    def extract_jobs(self, keyword, last_page):
        jobs = []

        for page in range(1, last_page + 1):
            target_data_list = self.parsing_html(search=keyword, page=page)
            print(f"Scrapping DICE Page : {page}")

            for target_data in target_data_list:
                jobs.append(self.extract_job(target_data))
                
        return jobs