from core.Crawler import Crawler


class BuiltIn(Crawler):

    def __init__(self):
        super().__init__("builtin", "https://builtin.com/jobs")
        self.origin_url = "https://builtin.com/jobs"

    def get_last_page(self, keyword):
        self.set_url(f"{self.origin_url}?search={keyword}")
        print(self.url)
        html = self.parsing_html()

        print(html)
        # pages = html.find("ul", {"class": "paginate"})
        # print(pages)
        # last_page = pages[-2].get_text(strip=True)
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
        jobs = []

        for page in range(last_page):
            print(f"Scrapping Dice Page : {page}")
            self.set_url(f"{self.origin_url}?q={keyword}&page={page + 1}&pageSize={LIMIT}")
            html = self.parsing_html()
            results = html.find_all("dhi-search-card")
            print(results)
            # for result in results:
            #     job = self.extract_job(result)
            #     jobs.append(job)

        return jobs

