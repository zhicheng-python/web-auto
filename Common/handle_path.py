# encoding:utf-8
# author:wangzhicheng
# time:2020/5/8 9:44
# file:handle_path.py


import os


class HandlePath:
    """处理所有路径"""

    # 项目路径：
    basic_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 配置文件路径：
    config_file_path = os.path.join(basic_path, "Common", "config.yaml")

    # 测试log路径：
    log_path = os.path.join(basic_path, "TestResults", "logs", "logs.log")

    # 截图路径：
    screen_shots_path = os.path.join(basic_path, "TestResults", "screenshots")

    # 测试报告路径：
    report_path = os.path.join(basic_path, "TestResults", "reports", "report.html")

    #allure文件路径：
    allure_path =os.path.join(basic_path,"TestResults","reports","my_allure_results")

    # allure_html报告路径：
    allure_html = os.path.join(basic_path, "TestResults", "reports", "allure_html")


#实例化
do_path = HandlePath()

if __name__ == '__main__':
    print(do_path.basic_path,do_path.log_path, do_path.report_path, do_path.screen_shots_path,
          do_path.config_file_path)
