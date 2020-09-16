#encoding:utf-8
#author:wangzhicheng
#time:2020/5/28 14:47
#file:home_page_objects.py


import time
from Common.base_page_object import BasePageObject as BPO
from PageLocations.home_page_locations import HomePageLocations as loc


class HomePageObjects(BPO):
    """主界面的操作过程"""

    #点击IOT设备管理-点击设备管理
    def click_IOT_device_manage(self):
        #1.点击IOT设备管理
        #2.点击设备管理

        self.click_element(loc.iot_device_manage,timeout=30,module='主界面-点击IOT设备管理')
        time.sleep(1)
        self.click_element(loc.device_manage,module='主界面-IOT设备管理-点击设备管理',timeout=30)


    #