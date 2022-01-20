from sites.stack_overflow import StackOverFlow
from sites.indeed import Indeed
from sites.dice import Dice
from sites.builtin import BuiltIn

FIXED_KEYWORD = ["python", "php", "java", "golang", "nest", "spring", "react", "vue"]

if __name__ == "__main__":

    stack_overflow_crawler = StackOverFlow()
    indeed_crawler = Indeed()

    '''
    # 각 사이트 Crawler 인스턴스 생성
    builtin_crawler = BuiltIn()
    dice_crawler = Dice()
    '''

    # 테스트 코드

    # (stack_overflow 구현 완)
    stack_overflow_last_page = stack_overflow_crawler.get_last_page('python')
    stack_overflow_jobs = stack_overflow_crawler.extract_jobs("python", 1)

    # (indeed 구현 완)
    indeed_last_page = indeed_crawler.get_last_page('python')
    indeed_jobs = indeed_crawler.extract_jobs('python', 1)

    print(stack_overflow_jobs + indeed_jobs)

    '''
    # (builtin 구현 진행)
    # 해당 검색 페이지 화면을 가져올 수 없음
    builtin_last_page = builtin_crawler.get_last_page('python')
    # builtin_jobs = build_in_crawler.extract_jobs('python', 1)
    
    # (dice 구현 진행)
    # 키워드로 검색된 html을 가져올 수 없음 > 확인 필요
    # 검색된 html이 아닌, default html을 가져오고 있음
    dice_last_page = dice_crawler.get_last_page('python')
    dice_jobs = dice_crawler.extract_jobs('python', 1)
    '''

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



