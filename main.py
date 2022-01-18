

from threading import Thread
from sites.stack_overflow import StackOverFlow


if __name__ == "__main__":

    stack_overflow = StackOverFlow("stack_overflow", "https://stackoverflow.com/jobs")

    site_lists = list()
    site_lists.append(stack_overflow)

    # 크롤링 메인 호출
    for site in site_lists:
        site.crawler_main()