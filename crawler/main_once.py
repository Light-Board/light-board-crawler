# crawler
from sites.stack_overflow import StackOverFlow
from sites.indeed import Indeed
from sites.dice import Dice
from sites.flexjobs import FlexJobs

# log
from core.Logging import Logging
from core.database.Mongodb import DbCon

# util
import time

FIXED_KEYWORD = ["python"] #, "php", "java", "golang", "nest", "spring", "react", "vue"]

if __name__ == "__main__":

    # static
    main_logger = Logging("main")       # logger
    main_db_con = DbCon(main_logger)    # db connection

    # site list
    stack_overflow_crawler = StackOverFlow(main_logger)
    indeed_crawler = Indeed(main_logger)
    dice_crawler = Dice(main_logger)
    flexjobs_crawler = FlexJobs(main_logger)

    # list of data
    all_jobs = []

    start_time = time.time()
    for keyword in FIXED_KEYWORD:
        try: 
            main_logger.set_start_log(f"main : {keyword} crawl start")
            stack_overflow_jobs = stack_overflow_crawler.extract_jobs(keyword, 1)
            indeed_jobs = indeed_crawler.extract_jobs(keyword, 1)
            dice_jobs = dice_crawler.extract_jobs(keyword, 1)
            flexjobs_jobs = flexjobs_crawler.extract_jobs(keyword, 1)
        except Exception:
            pass

        all_jobs += (stack_overflow_jobs + indeed_jobs + dice_jobs + flexjobs_jobs)

    # db insert
    main_db_con.insert_crawler_data(all_jobs)

    end_time = time.time()
    main_logger.set_log(f"main crawl first page crawl time: {end_time - start_time}")




