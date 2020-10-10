# encoding:utf-8
# author:wangzhicheng
# time:2020/6/9 14:22
# file:device_manage_subpage_locations.py

from selenium.webdriver.common.by import By
from TestDatas.DeviceManageSubPageDatas import DeviceManageSubPageDatas as DMSPD


class DeviceManageSubPageLocations:
    # 设备管理子界面元素定位

    # sn 输入框
    sn_input_box = (By.ID, "sn")

    # 渠道名输入框
    name_input_box = (By.ID, "channel")

    # homepage_IOT设备管理_设备管理_查询按钮
    find_button = (By.XPATH, "//button[@type='button']")

    # 输入sn点击查询后出现的sn信息列表
    input_sn_printer_info_list = (By.XPATH, "//tr[@class='ant-table-row  ant-table-row-level-0']")

    # 输入指定sn N301P98Q40093 点击查询后出现的sn信息
    input_sn_printer_info = (By.XPATH, "//td[text()='N301P98Q40093']")

    # 指定SN查询后统计查询到的设备数量
    count_device = (By.XPATH, "//li[@class='ant-pagination-total-text']/span")

    # 输入渠道名点击查询后出现渠道信息
    input_name_printer_info = (By.XPATH, "//td[text()='N666D96D46666']//following-sibling::td[text()='阿爸']")

    # 查询为空时 暂无数据
    no_data = (By.XPATH, "//div[@class='ant-table-placeholder']")

    # 机型选择下拉按钮
    device_module_select_button = (By.XPATH, "//div[@class='ant-select-lg ant-select ant-select-enabled']")

    # NT211机型

    device_NT211 = (By.XPATH, "//li[text()='NT211']")

    # NT212机型
    device_NT212 = (By.XPATH, "//li[text()='NT212']")

    # 搜索完整的渠道名
    channel_name = (By.XPATH, "//td[text()='zzzz']")

    channel_name1 = (By.XPATH, "//td[text()='阿爸']")

    # 表格 tbody
    table_tbody = (By.XPATH, "//tbody[@class='ant-table-tbody']")

    # 设备离线状态定位
    device_offline = (By.XPATH, "//div[@class='_1nnCGGJ6QCmiDBXq_P_-q']")

    # 设备在线状态定位
    device_online = (By.XPATH, "//div[@class='_2YUb-ZeSBp06lV0F07j_iK']")

    # 设备总计、在线设备总计
    device_count_and_online_number = (By.XPATH, "//li[@class='ant-pagination-total-text']/span")

    # 第四页框框
    fourth_page_box = (By.XPATH, '//li[@class="ant-pagination-item ant-pagination-item-4"]')

    # 第1页框框被选中
    selected_first_page = (
    By.XPATH, "//li[@class='ant-pagination-item ant-pagination-item-1 ant-pagination-item-active']")

    # 第四页框框被选中
    selected_fourth_page = (
        By.XPATH, "//li[@class='ant-pagination-item ant-pagination-item-4 ant-pagination-item-active']")

    # 第10页框框被选中
    selected_tenth_page = (
    By.XPATH, "//li[@class='ant-pagination-item ant-pagination-item-10 ant-pagination-item-active']")

    # 最后一页框框被选中
    selected_end_page = (By.XPATH,
                         f"//li[@class='ant-pagination-item ant-pagination-item-{DMSPD.current_page_number} ant-pagination-item-active']")

    # 跳至
    jump_to = (By.XPATH, "//div[text()='跳至']")

    # 跳页输入框
    jump_to_input_box = (By.XPATH, '//div[@class="ant-pagination-options-quick-jumper"]//input[@type="text"]')

    # 指定SN信息-更多
    more_info = (By.XPATH, "//a[@class='ant-dropdown-link ant-dropdown-trigger' and text()='更多']")

    # 更多-设备信息
    more_info_device_info = (By.XPATH, "//div[text()='设备信息']")

    # 更多-订单日志
    more_info_order_log = (By.XPATH, "//div[text()='订单日志']")
