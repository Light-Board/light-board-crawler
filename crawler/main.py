from crawler.core.util import csv_util
from crawler.sites.stack_overflow import StackOverFlow
from crawler.sites.indeed import Indeed
from crawler.sites.dice import Dice
from crawler.sites.flexjobs import FlexJobs
from crawler.sites.builtin import BuiltIn

# FIXED_KEYWORD = ["python", "php", "java", "golang", "nest", "spring", "react", "vue"]
FIXED_KEYWORD = ["python"]

if __name__ == "__main__":

    stack_overflow_crawler = StackOverFlow()
    indeed_crawler = Indeed()
    dice_crawler = Dice()
    flexjobs_crawler = FlexJobs()

    all_jobs = []
    for keyword in FIXED_KEYWORD:
        stack_overflow_last_page = stack_overflow_crawler.get_last_page(keyword)
        stack_overflow_jobs = stack_overflow_crawler.extract_jobs(keyword, stack_overflow_last_page)

        indeed_last_page = indeed_crawler.get_last_page(keyword)
        indeed_jobs = indeed_crawler.extract_jobs(keyword, indeed_last_page)

        dice_last_page = dice_crawler.get_last_page(keyword)
        dice_jobs = dice_crawler.extract_jobs(keyword, dice_last_page)

        flexjobs_last_page = flexjobs_crawler.get_last_page(keyword)
        flexjobs_jobs = flexjobs_crawler.extract_jobs(keyword, flexjobs_last_page)

        all_jobs += (stack_overflow_jobs + indeed_jobs, dice_jobs, flexjobs_jobs)

    print(len(all_jobs))
