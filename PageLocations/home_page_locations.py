# encoding:utf-8
# author:wangzhicheng
# time:2020/5/28 14:47
# file:home_page_locations.py


from selenium.webdriver.common.by import By


class HomePageLocations:
    """主界面的元素定位"""

    # 登录成功home界面账户元素
    account_element = (By.XPATH, "//a[@class='ant-dropdown-link ant-dropdown-trigger']")

    # IOT设备管理
    iot_device_manage = (By.XPATH, "//span[text()='IoT设备管理']")

    # IOT设备管理>>>设备管理元素
    device_manage = (By.XPATH, "//a[@to='/wireless/printer']")
