from crawler.core.Crawler import Crawler
import time

LIMIT = 50

class Indeed(Crawler):

    def __init__(self):
        super().__init__("indeed", "https://www.indeed.com/jobs")
        self.origin_url = "https://www.indeed.com/jobs"

    def get_last_page(self, keyword):
        self.set_url(f"{self.origin_url}?q={keyword}&limit={LIMIT}")
        print(self.url)
        html = self.parsing_html()
        pagination = html.find("div", {"class": "pagination"})

        links = pagination.find_all('a')
        last_button = links[-1]["aria-label"]
        current_last_page = 1

        while last_button == "Next":
            current_last_page = int(links[-2].string)
            self.set_url(f"{self.origin_url}?q={keyword}&limit={LIMIT}&start={current_last_page * LIMIT}")
            print(self.url)
            html = self.parsing_html()
            pagination = html.find("div", {"class": "pagination"})
            links = pagination.find_all('a')
            last_button = links[-1]["aria-label"]

        return int(current_last_page)

    def extract_job(self, job_id, html):
        data = html.find("td", {"class": "resultContent"})
        title = data.find("h2", {"class": "jobTitle"}).find_all("span")[-1]["title"]
        company = data.find("span", {"class": "companyName"}).string
        location = data.find("div", {"class": "companyLocation"})

        location_data = []
        for x in location.contents:
            if str(type(x)) == "<class 'bs4.element.Tag'>":
                temps = x.contents
                for z in temps:
                    if str(type(z)) != "<class 'bs4.element.Tag'>":
                        if str(z).strip() != '':
                            location_data.append(str(z))
            elif str(type(x)) == "<class 'bs4.element.Comment'>":
                if str(x.string).strip() != '':
                    location_data.append(str(x.string))
            else:
                if str(x).strip() != '':
                    location_data.append(str(x))

        # skill_set을 가져올 수 있는 정보가 없음
        # pay 정보도 있는게 있고 없는 것도 있음
        return {"id": f"{self.site_name}-{job_id}", 'title': title, 'company': company,
                'location': ''.join(location_data), 'link': f"https://www.indeed.com/viewjob?jk={job_id}"}

    def extract_jobs(self, keyword, last_page):
        jobs = []

        for page in range(1, last_page + 1):
            print(f"Scrapping Indeed Page : {page}")
            
            self.set_url(f"{self.origin_url}?q={keyword}&start={page * LIMIT}")
            html = self.parsing_html()
            jobs_link = html.find_all("a", {"class": "tapItem"})
            for job_data in jobs_link:
                job_id = job_data["data-jk"]
                job_detail = job_data.find("div", {"class": "job_seen_beacon"})
                jobs.append(self.extract_job(job_id, job_detail))

            time.sleep(3)

        return jobs
