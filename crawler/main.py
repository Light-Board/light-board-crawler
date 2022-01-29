# crawler
from sites.stack_overflow import StackOverFlow
from sites.indeed import Indeed
from sites.dice import Dice
from sites.flexjobs import FlexJobs

# log
from core.Logging import Logging

# util
import time

FIXED_KEYWORD = ["python", "php", "java", "golang", "nest", "spring", "react", "vue"]

if __name__ == "__main__":
    
    # logging
    main_logger = Logging("main")

    # site list
    stack_overflow_crawler = StackOverFlow()
    indeed_crawler = Indeed()
    dice_crawler = Dice()
    flexjobs_crawler = FlexJobs()

    # list of data
    all_jobs = []

    start_time = time.time()
    for keyword in FIXED_KEYWORD:
        main_logger.set_start_log(f"main : {keyword} crawl total page start")
        stack_overflow_last_page = stack_overflow_crawler.get_last_page(keyword)
        main_logger.set_log(f"S.O lastpage : {stack_overflow_last_page}")
        stack_overflow_jobs = stack_overflow_crawler.extract_jobs(keyword, stack_overflow_last_page)

        indeed_last_page = indeed_crawler.get_last_page(keyword)
        main_logger.set_log(f"Indeed lastpage : {stack_overflow_last_page}")
        indeed_jobs = indeed_crawler.extract_jobs(keyword, indeed_last_page)

        dice_last_page = dice_crawler.get_last_page(keyword)
        main_logger.set_log(f"Dice lastpage : {stack_overflow_last_page}")
        dice_jobs = dice_crawler.extract_jobs(keyword, dice_last_page)

        flexjobs_last_page = flexjobs_crawler.get_last_page(keyword)
        main_logger.set_log(f"FlexJobs lastpage : {stack_overflow_last_page}")
        flexjobs_jobs = flexjobs_crawler.extract_jobs(keyword, flexjobs_last_page)

        all_jobs += (stack_overflow_jobs + indeed_jobs, dice_jobs, flexjobs_jobs)

    end_time = time.gmtime(time.time())
    main_logger.set_log(f"main crawl total page crawl time: {end_time - start_time}")    
    print(len(all_jobs))
