from core.Crawler import Crawler

LIMIT = 100


class Dice(Crawler):

    def __init__(self):
        super().__init__("dice", "https://www.dice.com/jobs")
        self.origin_url = "https://www.dice.com/jobs"

    def get_last_page(self, keyword):
        self.set_url(f"{self.origin_url}?q={keyword}")
        print(self.url)
        cookie = '__uzma=4d492ca1-7d5e-44ed-88c5-c4ff5085ac6c; __uzmb=1642699708; _ga=GA1.2.460607658.1642699709; _gid=GA1.2.2075492022.1642699709; _gcl_au=1.1.981770744.1642699709; _rdt_uuid=1642699709501.4d57d6d3-4b5a-4d6c-9ca3-f708b97524a4; _mkto_trk=id:318-VQK-428&token:_mch-dice.com-1642699709615-50883; _gaexp=GAX1.2.Sh_4hXkUSsuaDyYXXmPLAQ.19027.3; DGL="{\"country\":\"Korea (south)\",\"city\":\"Gohyeon-dong\",\"state\":\"Gyeongsangnam-do\",\"stateCode\":\"\",\"zipCode\":\"656-304\",\"latitude\":\"34.88064\",\"longitude\":\"128.62108\",\"joblocation\":\"Gohyeon-dong\"}"; _clck=g5lsjy|1|eya|0; __ssid=a6b6012ee7a9f511f50e4848f4b0610; searchexp=control; __gads=ID=22bf6a0008ae7f3c:T=1642699921:S=ALNI_MZWdvh38YdOYc9fNX1IhteIDPvhZA; _ccid=1642699923060414hf77qx; JSESSIONID=51D4FAEB21D4F3DCB9C6E7504806495B; AWSELB=415901FD02F1450C4C37AB8D4D1C9AEA73CE1DCC2FD2D8F8C21863BF676C67D8A94137E145B69A1D9ABB7D0F6B6B4459D8F1EC2606742FAF74F0DBF81CCF447D503DEA427243B232528AD113B04407679AEF7F6594; __uzmc=689066464663; uzdbm_a=f370b010-ba35-b79a-9c71-d5521b0732f5; __uzmd=1642703227; _uetsid=622493d07a1611ecb4906baca0db9b33; _uetvid=6224e1107a1611ec880891a7bccc8c9d; searchBackURL=/jobs?q=python&countryCode=US&radius=30&radiusUnit=mi&page=1&pageSize=20&language=en&eid=S2Q_,AQ_3; _clsk=kzonhb|1642703228605|1|1|h.clarity.ms/collect; _gat_UA-45084316-1=1'
        html = self.parsing_html(cookie=cookie)
        print(html)
        # pages = html.find("ul", {"class": "pagination"})
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
        return {"id": primary_id, "title": title, "company": company, "location": location,
                "link": f"{self.origin_url}/{job_id}", "skill_set": skill_set}

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