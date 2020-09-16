# encoding:utf-8
# author:wangzhicheng
# time:2020/5/28 14:48
# file:test_02_home_page.py



import pytest, time
from Common.mylogger import logger


class TestHomePage:
    """主界面测试用例"""


    # 点击iot设备管理-点击设备管理成功进入子界面
    @pytest.mark.usefixtures("login_success")
    def test_02_click_device_manage_success(self, login_success):
        logger.info("正常用例---点击设备管理元素成功进入子界面")

        login_success[3].click_IOT_device_manage()
        time.sleep(3)

        assert login_success[4].find_button_isvisible() == True
        assert login_success[4].jump_to_isvisible() == True


if __name__ == '__main__':
    pytest.main(["--reruns", "2", "--reruns-delay", "2"])
