# encoding:utf-8
# author:wangzhicheng
# time:2020/5/8 9:44
# file:mylogger.py


import logging
from Common.handle_path import do_path
from Common.handle_yaml import do_yaml


class HandleLogging:
    """处理日志"""

    def __init__(self, log_path=do_path.log_path):
        self.path = log_path
        self.fmt = do_yaml.read_yaml("logging", "fmt")
        self.name = do_yaml.read_yaml("logging", "name")
        self.datefmt = do_yaml.read_yaml("logging", "datefmt")
        self.output_level = do_yaml.read_yaml("logging", "output_level")
        self.collect_level = do_yaml.read_yaml("logging", "collect_level")

    def handle_logging(self):
        # 创建log收集器，设定收集最低级别
        logger = logging.getLogger(name=self.name)
        logger.setLevel(self.collect_level)

        # 创建log处理器,输出log到控制台，设定输出最低级别
        sh = logging.StreamHandler()
        sh.setLevel(self.output_level)

        # 创建log处理器,输出log到指定路径，设定输出最低级别
        fh = logging.FileHandler(filename=self.path, encoding="utf8")
        fh.setLevel(self.output_level)

        # 设置日志输出格式
        formatter = logging.Formatter(fmt=self.fmt, datefmt=self.datefmt)

        # 指定处理器输出格式
        sh.setFormatter(formatter)
        fh.setFormatter(formatter)

        # 收集器加载处理器
        logger.addHandler(sh)
        logger.addHandler(fh)

        return logger


logger = HandleLogging().handle_logging()

if __name__ == '__main__':
    logger.debug("---debug这是---")
    logger.info("---info我的---")
    logger.warning("--warning测试--")
    logger.error("--error结果--")
    logger.critical("--critical啊--")
