# encoding:utf-8
# author:wangzhicheng
# time:2020/8/11 14:02
# file:device_more_info_page_objects.py

import time
from Common.base_page_object import BasePageObject as BPO
from PageLocations.device_more_info_locations import DeviceMoreInfoLocations as loc


class DeviceMoreInfoPageObjects(BPO):
    """设备更多信息页面操作过程"""

    # 点击设备信息进行跳转
    def click_device_info_obj(self):
        self.click_element(loc.more_info_device_info, module="更多界面-点击设备信息")
        time.sleep(1)

    # 点击本机信息收回展示信息
    def click_local_device_info_obj(self):
        self.click_element(loc.local_device_info, module='设备信息-点击本机信息')
        time.sleep(1)

    # 点击设备信息-移动网络信息
    def click_mobile_net_info_obj(self):
        # 这里总是报错，多加一个步骤，先收回本机信息列表
        self.click_local_device_info_obj()
        self.click_element(loc.mobile_net_info, module="设备信息-点击移动网络信息")
        time.sleep(1)

    # 点击设备信息-wifi信息
    def click_wifi_info_obj(self):
        self.click_element(loc.wifi_info, module="设备信息-点击WIFI信息")
        time.sleep(1)

    # 点击设备信息-打印机信息
    def click_printer_info_obj(self):
        self.click_element(loc.printer_info, module="设备信息-点击打印信息")
        time.sleep(1)

    # 点击设备信息-设置项
    def click_set_the_item_obj(self):
        self.click_element(loc.set_the_item, module="设备信息-点击设置项")
        time.sleep(1)

    # 点击本机信息-刷新按钮
    def click_refresh_button_obj(self):
        self.click_element(loc.refresh_button, module="设备信息-本机信息-点击刷新按钮")

    # 点击移动网络信息-刷新按钮
    def click_mobile_net_info_refresh_button_obj(self):
        self.click_element(loc.mni_refresh_button, module="设备信息-移动网络信息-点击刷新按钮")

    # 点击WIFI信息-刷新按钮
    def click_wifi_info_refresh_button_obj(self):
        self.click_element(loc.wifi_info_refresh_button, module="设备信息-WIFI信息-点击刷新按钮")

    # 点击打印信息-刷新按钮
    def click_printer_info_refresh_button_obj(self):
        self.click_element(loc.printer_info_refresh_button, module="设备信息-打印信息-点击刷新按钮")

    # 点击设置项-刷新按钮
    def click_set_the_item_refresh_button_obj(self):
        self.click_element(loc.set_the_item_refresh_button, module="设备信息-设置项-点击刷新按钮")
