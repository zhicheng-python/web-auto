# encoding:utf-8
# author:wangzhicheng
# time:2020/5/26 14:40
# file:main.py


import pytest, os
from Common.handle_path import do_path

if __name__ == '__main__':
    # #执行前先清空文件夹中文件
    # dir_path= do_path.allure_path
    # path=os.listdir(dir_path)
    #
    #
    #
    # for file_name in path:
    #     file_path=os.path.join(dir_path,file_name)
    #     os.remove(file_path)


    # pytest.main(["-s","--reruns", "1", "--reruns-delay", "3", "--alluredir=TestResults/reports/my_allure_results"])
    # pytest.main(["--reruns", "1","-v", "-s","--reruns-delay", "1", "--alluredir=TestResults/reports/my_allure_results","-m","smoke"])
    # pytest.main(["--reruns", "3", "-s", "--alluredir=TestResults/reports/my_allure_results"])
    # pytest.main(["--reruns","1","-s","--alluredir=TestResults/reports/my_allure_results","-m","test"])
    pytest.main(["--reruns","1","-s","--alluredir=TestResults/reports/my_allure_results","-m","db"])
    # pytest.main(["--reruns","1","-v","-s","--alluredir=TestResults/reports/my_allure_results","-m","uat","-n","auto"])
