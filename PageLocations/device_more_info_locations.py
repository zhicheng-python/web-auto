# encoding:utf-8
# author:wangzhicheng
# time:2020/8/11 14:02
# file:device_more_info_locations.py

from selenium.webdriver.common.by import By


class DeviceMoreInfoLocations:
    """更多页面元素定位"""

    # 更多-设备信息
    more_info_device_info = (By.XPATH, "//div[text()='设备信息']")
    # 更多-设备LOG
    more_info_device_log = (By.XPATH, "//div[text()='设备LOG']")
    # 更多-设备重启
    more_info_device_reboot = (By.XPATH, "//div[text()='设备重启']")
    # 更多-解除业务
    more_info_relieve = (By.XPATH, "//div[text()='解除业务']")
    # 更多-订单日志
    more_info_order_log = (By.XPATH, "//div[text()='订单日志']")

    # 更多-设备信息-本机信息
    local_device_info = (By.XPATH, "//div[@class='ant-collapse-header' and text()='本机信息']")
    # 更多-设备信息-设置项
    local_device_setting = (By.XPATH, "//div[@class='ant-collapse-header' and text()='设置项']")

    # 设备信息-刷新按钮
    refresh_button = (By.XPATH, "//i[@class='anticon anticon-reload']")
    # 刷新时转动的花圈
    refresh_flower = (By.XPATH, "//span[@class='ant-spin-dot']")

    # 设备信息-本机信息：local_device_info>>>>>>ldi
    # 本机信息展开后-展开
    # ldi_unfold = (By.XPATH, "//div[@class='ant-collapse-content ant-collapse-content-active']")
    # 本机信息展开后-折叠
    ldi_fold = (By.XPATH, "//div[@class='ant-collapse-content ant-collapse-content-inactive']")
    # 机型：
    ldi_model = (By.XPATH, "//div[@class='ant-col-12' and text()='机型：']//following-sibling::div[@class='ant-col-12']")
    # SN
    ldi_sn = (By.XPATH, "//div[@class='ant-col-12' and text()='SN号：']//following-sibling::div[@class='ant-col-12']")
    # 硬件版本
    ldi_hardware_version = (
        By.XPATH, "//div[@class='ant-col-12' and text()='硬件版本：']//following-sibling::div[@class='ant-col-12']")
    # bootloader版本
    ldi_bootloader_version = (
        By.XPATH, "//div[@class='ant-col-12' and text()='Bootloader版本：']//following-sibling::div[@class='ant-col-12']")
    # 固件版本
    ldi_firmware_version = (
        By.XPATH, "//div[@class='ant-col-12' and text()='固件版本：']//following-sibling::div[@class='ant-col-12']")
    # app版本
    ldi_app_version = (
        By.XPATH, "//div[@class='ant-col-12' and text()='APP0版本：']//following-sibling::div[@class='ant-col-12']")
    # 字库版本
    ldi_font_library_version = (
        By.XPATH, "//div[@class='ant-col-12' and text()='字库版本：']//following-sibling::div[@class='ant-col-12']")
    # TTS方言、TTS库版本
    ldi_tts_language = (
        By.XPATH, "//div[@class='ant-col-12' and text()='TTS库版本：']//following-sibling::div[@class='ant-col-12']")
    # 网络类型
    ldi_network_type = (
        By.XPATH, "//div[@class='ant-col-12' and text()='网络类型：']//following-sibling::div[@class='ant-col-12']")

    # 设备信息-移动网络信息 mobile_net_info>>>>>>mni
    # 移动网络信息
    mobile_net_info = (By.XPATH, "//div[@class='ant-collapse-header' and text()='移动网络信息']")

    # IMEI号
    mni_IMEI = (By.XPATH, "//div[@class='ant-col-12' and text()='IMEI号：']//following-sibling::div[@class='ant-col-12']")
    # ICCID号
    mni_ICCID = (
        By.XPATH, "//div[@class='ant-col-12' and text()='ICCID号：']//following-sibling::div[@class='ant-col-12']")
    # 当前经纬度
    mni_current_longitude_latitude = (
        By.XPATH, "//div[@class='ant-col-12' and text()='当前经纬度：']//following-sibling::div[@class='ant-col-12']")
    # 信号强度
    mni_signal_strength = (
        By.XPATH, "//div[@class='ant-col-12' and text()='信号强度：']//following-sibling::div[@class='ant-col-12']")
    # 移动网络-刷新按钮
    mni_refresh_button = (By.XPATH,
                          "//div[contains(text(),'移动网络信息')]//following-sibling::div[@class='ant-collapse-content ant-collapse-content-active']//div[@class='_1cPNS31EYYNrgxahIuu97Q']")

    # 设备信息-wifi信息 wifi_info
    # wifi信息
    wifi_info = (By.XPATH, "//div[@class='ant-collapse-header' and text()='WIFI信息']")
    # mac地址
    mac_address = (
        By.XPATH, "//div[@class='ant-col-12' and text()='MAC地址：']//following-sibling::div[@class='ant-col-12']")
    # wifi信号强度
    wifi_length = (
        By.XPATH, "//div[@class='ant-col-12' and text()='信号强度：']//following-sibling::div[@class='ant-col-12']")
    # wifi信息-刷新按钮
    wifi_info_refresh_button = (By.XPATH,
                                "//div[contains(text(),'WIFI信息')]//following-sibling::div[@class='ant-collapse-content ant-collapse-content-active']//div[@class='_1cPNS31EYYNrgxahIuu97Q']")

    # 设备信息-打印信息 printer_info
    # 打印信息
    printer_info = (By.XPATH, "//div[@class='ant-collapse-header' and text()='打印信息']")
    # 打印公里数
    printer_kilometer = (
        By.XPATH, "//div[@class='ant-col-12' and text()='打印公里数：']//following-sibling::div[@class='ant-col-12']")
    # 开钱箱次数
    money_box = (
        By.XPATH, "//div[@class='ant-col-12' and text()='开钱箱次数：']//following-sibling::div[@class='ant-col-12']")
    # 缺纸次数
    need_paper = (
        By.XPATH, "//div[@class='ant-col-12' and text()='缺纸次数：']//following-sibling::div[@class='ant-col-12']")
    # 打印头坏点
    printer_head_broken = (
        By.XPATH, "//div[@class='ant-col-12' and text()='打印头坏点：']//following-sibling::div[@class='ant-col-12']")
    # 打印信息-刷新按钮
    printer_info_refresh_button = (By.XPATH,
                                   "//div[contains(text(),'打印信息')]//following-sibling::div[@class='ant-collapse-content ant-collapse-content-active']//div[@class='_1cPNS31EYYNrgxahIuu97Q']")

    # 设备信息-设置项 set_the_item
    # 设置项
    set_the_item = (By.XPATH, "//div[@class='ant-collapse-header' and text()='设置项']")
    # 新订单播报次数
    new_order_play_time = (
        By.XPATH, "//div[@class='ant-col-12' and text()='新订单播报次数：']//following-sibling::div[@class='ant-col-12']")
    # 新订单播报内容
    new_order_contents = (
        By.XPATH, "//div[@class='ant-col-12' and text()='新订单播报内容：']//following-sibling::div[@class='ant-col-12']")
    # 取消单播报次数
    cancel_order_play_time = (
        By.XPATH, "//div[@class='ant-col-12' and text()='取消单播报次数：']//following-sibling::div[@class='ant-col-12']")
    # 取消单播报内容
    cancel_order_contents = (
        By.XPATH, "//div[@class='ant-col-12' and text()='取消单播报内容：']//following-sibling::div[@class='ant-col-12']")
    # 催单播报次数
    rush_order_play_time = (
        By.XPATH, "//div[@class='ant-col-12' and text()='催单播报次数：']//following-sibling::div[@class='ant-col-12']")
    # 网络连接播报次数
    voice_connect = (
        By.XPATH, "//div[@class='ant-col-12' and text()='网络连接播报次数：']//following-sibling::div[@class='ant-col-12']")
    # 网络断开播报次数
    voice_disconnect = (
        By.XPATH, "//div[@class='ant-col-12' and text()='网络断开播报次数：']//following-sibling::div[@class='ant-col-12']")
    # 自检页语言
    inspection_page_language = (
        By.XPATH, "//div[@class='ant-col-12' and text()='自检页语言：']//following-sibling::div[@class='ant-col-12']")
    # 打印浓度
    density = (By.XPATH, "//div[@class='ant-col-12' and text()='打印浓度：']//following-sibling::div[@class='ant-col-12']")
    # 取消单打印联数
    cancel_order_copy = (
        By.XPATH, "//div[@class='ant-col-12' and text()='取消单打印联数：']//following-sibling::div[@class='ant-col-12']")
    # 语音方言
    dialect = (By.XPATH, "//div[@class='ant-col-12' and text()='语音方言：']//following-sibling::div[@class='ant-col-12']")
    # 语音播报语速
    voice_speed = (
        By.XPATH, "//div[@class='ant-col-12' and text()='语音播报语速：']//following-sibling::div[@class='ant-col-12']")
    # 设置项-刷新按钮
    set_the_item_refresh_button = (By.XPATH,
                                   "//div[contains(text(),'设置项')]//following-sibling::div[@class='ant-collapse-content ant-collapse-content-active']//div[@class='_1cPNS31EYYNrgxahIuu97Q']")

    # 设备log
    device_log = (By.XPATH, "//div[text()='设备LOG']")
    # log开关
    device_log_on_off = (By.XPATH, "//span[text()='log开关']")

    # log开按钮
    # device_log_button_on =(By.XPATH,"//span[contains(@class,'ant-switch-checked')")
    device_log_button_on = (By.CSS_SELECTOR, ".ant-switch-checked")

    # log关按钮
    # device_log_button_off = (By.XPATH,"//span[@class='_2RVDfaIJYqrl11hwAEYNo8 ant-switch']")
    device_log_button_off = (By.CSS_SELECTOR, ".ant-switch")

    # 跳至
    device_log_jump_to = (By.XPATH, "//div[@class='_2Cac_zWmhjWM4jyTs7b_24']//following::div[text()='跳至']")
