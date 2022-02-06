# crawler
from sites.stack_overflow import StackOverFlow
from sites.indeed import Indeed
from sites.dice import Dice
from sites.flexjobs import FlexJobs

# util
import time
from core.Logging import Logging        # log


def crawler(keyword):

    main_logger = Logging("main")  # logger

    # site list
    stack_overflow_crawler = StackOverFlow(main_logger)
    indeed_crawler = Indeed(main_logger)
    dice_crawler = Dice(main_logger)
    flexjobs_crawler = FlexJobs(main_logger)

    # list of data
    all_jobs = []

    start_time = time.time()

    try:
        main_logger.set_start_log(f"main : {keyword} crawl start")
        stack_overflow_jobs = stack_overflow_crawler.extract_jobs(keyword, 1)
        indeed_jobs = indeed_crawler.extract_jobs(keyword, 1)
        dice_jobs = dice_crawler.extract_jobs(keyword, 1)
        flexjobs_jobs = flexjobs_crawler.extract_jobs(keyword, 1)

    except Exception:
        pass

    all_jobs += (stack_overflow_jobs + indeed_jobs + dice_jobs + flexjobs_jobs)

    end_time = time.time()
    main_logger.set_log(f"main crawl first page crawl time: {end_time - start_time}, total data:{len(all_jobs)}")

    return all_jobs







