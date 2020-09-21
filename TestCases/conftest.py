# encoding:utf-8
# author:wangzhicheng
# time:2020/5/26 17:48
# file:conftest.py


import pytest
from time import sleep
from selenium import webdriver
from Common.common_datas import CommonDatas as CD
from PageObjects.login_page_objects import LoginPageObjects
from PageAsserts.home_page_asserts import HomePageAsserts
from PageObjects.home_page_objects import HomePageObjects
from TestDatas.DeviceManageSubPageDatas import DeviceManageSubPageDatas as DMSPD
from PageAsserts.device_manage_subpage_asserts import DeviceManageSubPageAsserts
from PageObjects.device_manage_subpage_objects import DeviceManageSubPageObjects
from PageAsserts.device_more_info_asserts import DeviceMoreInfoAssert
from PageObjects.device_more_info_page_objects import DeviceMoreInfoPageObjects
from selenium.webdriver.chrome.options import Options

"""存放用例的前置/后置条件"""


# 前置条件-打开浏览器，最大化，打开网址
@pytest.fixture
def init_set():
    # 前置条件
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # 无图模式
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    # driver = webdriver.Chrome()
    # 窗口最大化
    driver.maximize_window()
    # 打开网址
    driver.get(CD.login_url)

    # 登录界面，主界面，设备管理子界面等等类实例化
    LPO = LoginPageObjects(driver)
    HPA = HomePageAsserts(driver)
    HPO = HomePageObjects(driver)
    DMSPA = DeviceManageSubPageAsserts(driver)
    DMSPO = DeviceManageSubPageObjects(driver)
    DMIPA = DeviceMoreInfoAssert(driver)
    DMIPO = DeviceMoreInfoPageObjects(driver)

    yield driver, LPO, HPA, HPO, DMSPA, DMSPO, DMIPA, DMIPO
    # 后置条件
    sleep(3)
    driver.quit()


# 前置条件-登录成功
@pytest.fixture(scope='function')
def login_success(init_set):
    # 有时候网站打不开，等待1秒后，刷新页面
    sleep(1)
    init_set[0].refresh()

    # 输入用户名密码
    init_set[1].login(CD.correct_account)

    yield init_set


# 前置条件-登录成功-进入设备管理子界面
@pytest.fixture(scope='function')
def click_device_manage(login_success):
    # 点击iot设备管理-点击设备管理
    login_success[3].click_IOT_device_manage()
    yield login_success


# 前置条件-登录成功-进入设备子界面-指定SN-更多
@pytest.fixture(scope="function")
def device_more_info(click_device_manage):
    # 输入指定SN,点击查询
    click_device_manage[5].input_SN_and_find(DMSPD.SN)

    sleep(1)
    # 点击更多
    click_device_manage[5].click_device_more_info_obj()

    yield click_device_manage


# 前置条件--登录成功-进入设备子界面-指定SN-更多-点击设备信息
@pytest.fixture(scope="function")
def device_more_info_device_info(device_more_info):
    # 点击设备信息
    device_more_info[7].click_device_info_obj()
    yield device_more_info


@pytest.fixture()
def device_more_info_device_log(device_more_info):
    pass


@pytest.fixture()
def device_more_info_device_reboot(device_more_info):
    pass


@pytest.fixture()
def device_more_info_withdraw_business(device_more_info):
    pass


@pytest.fixture()
def device_more_info_order_log(device_more_info):
    pass


# 筛选用例，标记名处理
def pytest_configure(config):
    marker_list = ["smoke", "test", "uat", "db"]

    for i in marker_list:
        config.addinivalue_line(
            "markers", i  # smoke 是标签名
        )
