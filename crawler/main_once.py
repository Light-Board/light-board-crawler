from crawler.sites.stack_overflow import StackOverFlow
from crawler.sites.indeed import Indeed
from crawler.sites.dice import Dice
from crawler.sites.flexjobs import FlexJobs

FIXED_KEYWORD = ["python", "php", "java", "golang", "nest", "spring", "react", "vue"]

if __name__ == "__main__":
    stack_overflow_crawler = StackOverFlow()
    indeed_crawler = Indeed()
    dice_crawler = Dice()
    flexjobs_crawler = FlexJobs()

    all_jobs = []

    for keyword in FIXED_KEYWORD:
        stack_overflow_jobs = stack_overflow_crawler.extract_jobs(keyword, 1)
        indeed_jobs = indeed_crawler.extract_jobs(keyword, 1)
        dice_jobs = dice_crawler.extract_jobs(keyword, 1)
        flexjobs_jobs = flexjobs_crawler.extract_jobs(keyword, 1)

        all_jobs += (stack_overflow_jobs + indeed_jobs + dice_jobs + flexjobs_jobs)

    print(len(all_jobs))





