# crawler
from sites.stack_overflow import StackOverFlow
from sites.indeed import Indeed
from sites.dice import Dice
from sites.flexjobs import FlexJobs

# util
from core.Logging import Logging        # log
from core.database.Mongodb import DbCon # DB
import time



if __name__ == "__main__":
    
    # static
    DEBUG = True
    FIXED_KEYWORD = ["python", "php", "java", "golang", "nest", "spring", "react", "vue"]
    main_logger = Logging("main") if DEBUG else Logging("main DEBUG")
    main_db_con = DbCon(main_logger)                               # db connection
    if not DEBUG: main_db_con.init_default_keyword(FIXED_KEYWORD)  # init keyword 
    
    # site list
    stack_overflow_crawler = StackOverFlow(main_logger)
    indeed_crawler = Indeed(main_logger)
    dice_crawler = Dice(main_logger)
    flexjobs_crawler = FlexJobs(main_logger)

    # list of data
    all_jobs = []

    if DEBUG:
        start_time = time.time()
        for keyword in FIXED_KEYWORD:
            try: 
                main_logger.set_start_log(f"main : {keyword} crawl total page start")
                stack_overflow_last_page = stack_overflow_crawler.get_last_page(keyword)
                main_logger.set_log(f"S.O lastpage : {stack_overflow_last_page}")
                stack_overflow_jobs = stack_overflow_crawler.extract_jobs(keyword, stack_overflow_last_page)

                indeed_last_page = indeed_crawler.get_last_page(keyword)
                main_logger.set_log(f"Indeed lastpage : {indeed_last_page}")
                indeed_jobs = indeed_crawler.extract_jobs(keyword, indeed_last_page)

                dice_last_page = dice_crawler.get_last_page(keyword)
                main_logger.set_log(f"Dice lastpage : {dice_last_page}")
                dice_jobs = dice_crawler.extract_jobs(keyword, dice_last_page)

                flexjobs_last_page = flexjobs_crawler.get_last_page(keyword)
                main_logger.set_log(f"FlexJobs lastpage : {flexjobs_last_page}")
                flexjobs_jobs = flexjobs_crawler.extract_jobs(keyword, flexjobs_last_page)
            except Exception:
                continue
            
            # insert data to keyword collection
            print(keyword, stack_overflow_jobs + indeed_jobs + dice_jobs + flexjobs_jobs)
            print("======================================================")

            main_db_con.insert_crawler_total_data(keyword, stack_overflow_jobs + indeed_jobs + dice_jobs + flexjobs_jobs)
            all_jobs += stack_overflow_jobs + indeed_jobs + dice_jobs + flexjobs_jobs
            time.sleep(1)

        end_time = time.time()
        main_logger.set_log(f"main DEBUG crawl total page crawl time: {end_time - start_time}, total data:{len(all_jobs)}")
    else:
        start_time = time.time()
        for keyword in FIXED_KEYWORD:
            try: 
                main_logger.set_start_log(f"main : {keyword} crawl total page start")
                stack_overflow_last_page = stack_overflow_crawler.get_last_page(keyword)
                main_logger.set_log(f"S.O lastpage : {stack_overflow_last_page}")
                stack_overflow_jobs = stack_overflow_crawler.extract_jobs(keyword, stack_overflow_last_page)

                indeed_last_page = indeed_crawler.get_last_page(keyword)
                main_logger.set_log(f"Indeed lastpage : {indeed_last_page}")
                indeed_jobs = indeed_crawler.extract_jobs(keyword, indeed_last_page)

                dice_last_page = dice_crawler.get_last_page(keyword)
                main_logger.set_log(f"Dice lastpage : {dice_last_page}")
                dice_jobs = dice_crawler.extract_jobs(keyword, dice_last_page)

                flexjobs_last_page = flexjobs_crawler.get_last_page(keyword)
                main_logger.set_log(f"FlexJobs lastpage : {flexjobs_last_page}")
                flexjobs_jobs = flexjobs_crawler.extract_jobs(keyword, flexjobs_last_page)
            except Exception:
                pass
            
            # insert data to keyword collection
            main_db_con.insert_crawler_total_data(keyword, stack_overflow_jobs + indeed_jobs + dice_jobs + flexjobs_jobs)
            all_jobs += stack_overflow_jobs + indeed_jobs + dice_jobs + flexjobs_jobs
            time.sleep(1)

        end_time = time.time()
        main_logger.set_log(f"main crawl total page crawl time: {end_time - start_time}, total data:{len(all_jobs)}")        