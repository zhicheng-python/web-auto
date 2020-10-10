# encoding:utf-8
# author:wangzhicheng
# time:2020/6/9 14:23
# file:device_manage_subpage_objects.py


import time
from Common.base_page_object import BasePageObject as BPO
from PageLocations.device_manage_subpage_locations import DeviceManageSubPageLocations as loc


class DeviceManageSubPageObjects(BPO):
    """设备管理子界面操作过程"""

    # 输入渠道名，点击查询
    def input_channle_and_find(self, text):
        self.input_text(loc.name_input_box, module='子界面-输入渠道名', text=text)
        time.sleep(1)
        self.click_element(loc.find_button, module='子界面-点击查询按钮')

    # 输入SN，点击查询
    def input_SN_and_find(self, text):
        self.input_text(loc.sn_input_box, module='子界面-输入SN', text=text)
        time.sleep(1)
        self.click_element(loc.find_button, module='子界面-点击查询按钮')

    # 选择设备小机型NT211型号，点击查询
    def select_device_model_and_find_NT211(self):
        self.click_element(loc.device_module_select_button, module="子界面-选择机型查询")
        time.sleep(1)
        self.click_element(loc.device_NT211, module="子界面-点击NT211机型")
        time.sleep(1)
        self.click_element(loc.find_button, module='子界面-点击查询按钮')

    # 选择设备小机型NT212型号，点击查询
    def select_device_model_and_find_NT212(self):
        self.click_element(loc.device_module_select_button, module="子界面-选择机型查询")
        time.sleep(1)
        self.click_element(loc.device_NT212, module="子界面-点击NT211机型")
        time.sleep(1)
        self.click_element(loc.find_button, module='子界面-点击查询按钮')

    # 点击第4页进行页面跳转
    def click_fourth_page_obj(self):
        self.click_element(loc.fourth_page_box, module="子界面-点击第4页进行页面跳转")
        time.sleep(1)

    # 跳转输入框输入页面数字10，点击enter键进行跳转
    def input_page_number_jump_obj(self, text, content):
        # 输入页面数字
        self.input_text(loc.jump_to_input_box, module="页面跳转输入框，输入页面数字", text=text)
        time.sleep(1)
        # 键盘操作enter键
        self.click_keyboard(loc.jump_to_input_box, module="子界面-页面跳转输入框-键盘操作enter键", text=content)

    # 点击更多按钮
    def click_device_more_info_obj(self):
        # 点击更多按钮
        self.click_element(loc.more_info, module="子界面-点击更多按钮")
        time.sleep(1)
