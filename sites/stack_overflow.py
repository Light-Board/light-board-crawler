from core.Crawler import Crawler


class StackOverFlow(Crawler):

    def __init__(self):
        super().__init__("stack_overflow", "https://stackoverflow.com/jobs")
        self.origin_url = "https://stackoverflow.com/jobs"

    def get_last_page(self, keyword):
        self.set_url(f"{self.origin_url}?q={keyword}")
        print(self.url)
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
        return {"id": primary_id, "title": title, "company": company, "location": location,
                "link": f"{self.origin_url}/{job_id}", "skill_set": skill_set}

    def extract_jobs(self, keyword, last_page):
        jobs = []

        for page in range(last_page):
            print(f"Scrapping SO Page : {page}")

            self.set_url(f"{self.origin_url}?q={keyword}&pg={page + 1}")
            html = self.parsing_html()
            results = html.find_all("div", {"class": "-job"})
            for result in results:
                job = self.extract_job(result)
                jobs.append(job)

        return jobs
