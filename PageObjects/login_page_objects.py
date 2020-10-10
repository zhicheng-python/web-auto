#encoding:utf-8
#author:wangzhicheng
#time:2020/5/26 17:35
#file:login_page_objects.py


from Common.base_page_object import BasePageObject as BPO
from PageLocations.login_page_locations import LoginPageLocations as loc


#继承basepageobject
class LoginPageObjects(BPO):
    """登录页面行为，操作过程"""

    #登录
    def login(self,text):
        #1.输入用户名
        #2.输入密码
        #3.点击登录

        self.input_text(loc.user_input_box_locator,module='登录页面_输入用户名',text=text["user"])
        self.input_text(loc.password_input_box_locator,module='登录页面_输入密码',text=text["passwd"])
        self.click_element(loc.login_button_locator,module='登录页面_点击登录按钮')




