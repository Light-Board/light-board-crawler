
import logging
import datetime


class Logging:
    
    def __init__(self, process_name) -> None:
        self.logger = self.setup_log(process_name)

    # set start log
    def setup_log(self, process_name):
        # logging setting
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s — %(message)s',
            datefmt='%Y-%m-%d_%H:%M:%S',
            handlers=[logging.FileHandler(f'{process_name}.log', encoding='utf-8')]
        )
        logging.getLogger("requests").setLevel(logging.WARNING)
        logging.getLogger("urllib3").setLevel(logging.WARNING)
        return logging


    # 루프 구간 또는 main 구간에서 찍을 로그 
    def set_start_log(self, process_name):
        # logging
        logging.info("======================================================")
        logging.info(f"{process_name} STARTED AT {datetime.datetime.now()}")
        logging.info("======================================================")


    # 로그 찍기 
    def set_log(self, log_msg, log_type="info"):
        if log_type == "info": logging.info(log_msg)
        else: logging.error(log_msg)
