from core.Crawler import Crawler
import time

class StackOverFlow(Crawler):

    def __init__(self, logger):
        super().__init__("stack_overflow", "https://stackoverflow.com/jobs", logger)
        self.origin_url = "https://stackoverflow.com/jobs"


    def get_last_page(self, keyword):
        self.set_url(f"{self.origin_url}?q={keyword}")
        html = self.parsing_html()
        pages_link = html.find("div", {"class": "s-pagination"})
        if pages_link:
            pages = pages_link.find_all("a")
            return int(pages[-2].get_text(strip=True))
        else:
            return 1


    def extract_job(self, html):
        job_id = html["data-jobid"]
        title = html.find("h2").find("a")["title"]
        company, location = html.find("h3").find_all("span", recursive=False)
        company = company.get_text(strip=True)
        location = location.get_text(strip=True)

        primary_id = f"{self.site_name}-{job_id}"

        skills = html.find("div", {"class": "d-inline-flex gs4 fw-wrap"})
        if skills:
            skill_set = [skill.string for skill in skills if skill != '\n']
        else:
            skill_set = []

        # pay 정보 없음
        return {
            "id": primary_id, 
            "title": title, 
            "company": company, 
            "location": location,
            "link": f"{self.origin_url}/{job_id}", 
            "skill_set": skill_set
        }


    def extract_jobs(self, keyword, last_page):
        jobs = list()

        for page in range(1, last_page + 1):
            self.logger.set_log(f"Scrapping S.O {keyword} Page : {page} crawl")
            self.set_url(f"{self.origin_url}?q={keyword}&pg={page}")
            html = self.parsing_html()
            results = html.find_all("div", {"class": "-job"})
            for result in results:
                job = self.extract_job(result)
                jobs.append(job)

            time.sleep(3)

        return jobs
