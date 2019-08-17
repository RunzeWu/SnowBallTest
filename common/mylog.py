'''
 @Time:         2019-08-17
 @Author:       吴润泽
'''
import logging
import logging.handlers
from common.config import ReadConfig
from common import contants

config = ReadConfig()


def get_logger(logger_name):
    logger = logging.getLogger(logger_name)
    if not logger.handlers:
        logger.setLevel('DEBUG')  # 直接设置为最低
        # 定义输出格式
        fmt = config.get_value("log", "formatter")
        formate = logging.Formatter(fmt)

        file_handler = logging.handlers.RotatingFileHandler(contants.log, maxBytes=20 * 1024 * 1024, backupCount=10,
                                                            encoding="utf-8")
        level = config.get_value('log', 'file_handler')
        file_handler.setLevel(level)
        file_handler.setFormatter(formate)

        console_handler = logging.StreamHandler()
        level = config.get_value('log', 'console_handler')
        console_handler.setLevel(level)
        console_handler.setFormatter(formate)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

