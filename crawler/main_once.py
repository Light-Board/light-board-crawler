# crawler
from sites.stack_overflow import StackOverFlow
from sites.indeed import Indeed
from sites.dice import Dice
from sites.flexjobs import FlexJobs

# log
from core.Logging import Logging

FIXED_KEYWORD = ["python", "php", "java", "golang", "nest", "spring", "react", "vue"]

if __name__ == "__main__":

    # logging
    main_logger = Logging("main")

    # site list
    stack_overflow_crawler = StackOverFlow(main_logger)
    indeed_crawler = Indeed(main_logger)
    dice_crawler = Dice(main_logger)
    flexjobs_crawler = FlexJobs(main_logger)

    # list of data
    all_jobs = []

    
    for keyword in FIXED_KEYWORD:
        main_logger.set_start_log(f"main : {keyword} crawl start")
        stack_overflow_jobs = stack_overflow_crawler.extract_jobs(keyword, 1)
        indeed_jobs = indeed_crawler.extract_jobs(keyword, 1)
        dice_jobs = dice_crawler.extract_jobs(keyword, 1)
        flexjobs_jobs = flexjobs_crawler.extract_jobs(keyword, 1)

        all_jobs += (stack_overflow_jobs + indeed_jobs + dice_jobs + flexjobs_jobs)

    print(len(all_jobs))





