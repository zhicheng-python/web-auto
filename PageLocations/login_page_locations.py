# encoding:utf-8
# author:wangzhicheng
# time:2020/5/26 15:10
# file:login_page_locations.py


from selenium.webdriver.common.by import By


class LoginPageLocations:
    """登录页面元素定位"""

    # 用户名输入框定位
    user_input_box_locator = (By.XPATH, "//input[@type='text']")

    # 密码输入框定位
    password_input_box_locator = (By.XPATH, "//input[@type='password']")

    # 登录按钮定位
    login_button_locator = (By.XPATH, "//button[@type='button']")
