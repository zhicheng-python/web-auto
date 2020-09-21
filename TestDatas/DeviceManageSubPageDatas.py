# encoding:utf-8
# author:wangzhicheng
# time:2020/6/9 17:22
# file:DeviceManageSubPageDatas.py

import math
from Common.handle_yaml import do_yaml
from Common.handle_mysql import HandleMysql
from selenium.webdriver.common.keys import Keys


class DeviceManageSubPageDatas:
    """设备子界面测试数据"""

    # 存在的完整的渠道名称
    complete_channel = '阿爸'
    complete_channel_2 = 'zzzz'
    # 存在的不完整的渠道名称
    notcomplete_channel = '阿'
    # 存在的完整的SN
    # SN = "N301P98Q40093"
    SN = "N301P9WZC0193"
    # SN = "testWap4"
    #存在的不完整的sn
    no_complete_SN = "40093"
    # 不存在的SN 、渠道
    no_exist_SN = "N111111111111111111111"
    no_exist_channel = "mmmaassqqqwqwqwqw"

    # td所在的索引位置 0 开始
    hareware_model_td_index = 1  # 机型
    SN_td_index = 2  # SN
    channel_td_index = 3  # 渠道
    last_connect_td_index = 5  # 上次连入
    last_disconnect_td_index = 6  # 上次断开
    log_switch_td_index = 7  # log开关

    # 可选择的机型
    device_model_NT211 = "NT211"
    device_model_NT212 = "NT212"
    device_model_NT211_S = "NT211_S"
    device_model_NT212_S = "NT212_S"
    device_model_NT213 = "NT213"

    # 页面跳转输入框 输入的页面数字
    jump_to_page_number = 10
    # 页面跳转输入框中输入的错误数字列表 (参数化用)
    jump_to_error_page = [0, -1]
    # 键盘操作，enter键
    enter_keyboard = (Keys.ENTER)
    # 当前共多少页设备（设备总数/10 向上取整）
    current_page_number = math.ceil(
        int(HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_device_count_sql"))["count(msn)"]) / 10)

    # 大于当前最大页
    out_of_largest_page_number = current_page_number + 10



    #查询数据库数据key值
    is_online = "is_online"
    hardware_model = "hardware_model"
    connect_time = "connect_time"
    disconnect_time = "disconnect_time"
    log_switch = "log_switch"
    count_is_online = "count(is_online)"
    count_msn = "count(msn)"

