# encoding:utf-8
# author:wangzhicheng
# time:2020/5/26 17:46
# file:test_01_login_page.py

import pytest, time
from Common.mylogger import logger
from TestDatas.LoginPageDatas import LoginPageDatas as LPD


class TestLoginPage:
    """登录页面测试用例"""


    # 登录成功
    @pytest.mark.usefixtures("init_set")
    @pytest.mark.parametrize("text", LPD.text)
    def test_01_login_success(self, init_set, text):
        logger.info("正常用例---登录成功")

        init_set[1].login(text)
        time.sleep(3)

        # 断言：账号元素、iot设备管理元素 可见 为 True
        assert init_set[2].account_isvisible() == True
        assert init_set[2].iot_device_manage_isvisible() == True


if __name__ == '__main__':
    pytest.main()
