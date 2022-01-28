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

    '''
    아래코드는 테스트용
    '''
    # stack_overflow_last_page = stack_overflow_crawler.get_last_page('python')
    # stack_overflow_jobs = stack_overflow_crawler.extract_jobs("python", 1)

    for keyword in FIXED_KEYWORD:
        indeed_last_page = indeed_crawler.get_last_page(keyword)
        print('낑', indeed_last_page)

    # indeed_jobs = indeed_crawler.extract_jobs('python', 1)

    # dice_jobs = dice_crawler.extract_jobs("python", 5)
    #
    # flexjobs_jobs = flexjobs_crawler.extract_jobs("python", 3)

    # print("==================================================================")
    # print(stack_overflow_jobs)
    # print("==================================================================")

    # print("==================================================================")
    # print(dice_jobs)
    # print("==================================================================")
    # print(flexjobs_jobs)

    '''
    # 처음에 전체 페이지 크롤링할 때, 사용할 코드
    stack_overflow_jobs = []
    for keyword in FIXED_KEYWORD:
        stack_overflow_last_page = stack_overflow_crawler.get_last_page(keyword)
        stack_overflow_jobs.append(stack_overflow_crawler.extract_jobs(keyword, stack_overflow_last_page))
        indeed_last_page = indeed_crawler.get_last_page(keyword)
        indeed_jobs = indeed_crawler.extract_jobs(keyword, indeed_last_page)
    '''

    '''
    # crontab 통해서 첫 페이지만 크롤링할 경우 사용하는 코드
    stack_overflow_jobs = []
    for keyword in FIXED_KEYWORD:
        stack_overflow_jobs.append(stack_overflow_crawler.extract_jobs(keyword, 1))
        indeed_jobs.append(indeed_crawler.extract_jobs(keyword, 1))
    '''



