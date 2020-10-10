#encoding:utf-8
#author:wangzhicheng
#time:2020/8/12 15:12
#file:DeviceMoreInfoPageDatas.py




class DeviceMoreInfoPageDatas:
    """设备更多页面测试数据"""

    #指定查询的SN
    # SN = "N301P98Q40093"
    SN = "N301P9WZC0193"
    # SN = "testWap4"

    #数据库查询后key值
    #本机信息
    hardware_model = "hardware_model"   #小机型
    hardware_version = "hardware_version" #硬件版本
    bootloader_version = "bootloader_version" #bootloader版本
    firmware_version = "firmware_version" #固件版本
    app_version = "app_version" #app版本
    font_library_version = "font_library_version" #字库版本
    tts_language = "tts_language" #tts方言
    tts_version = "tts_version" #tts版本
    network_type = "network_type" #网络类型

    #数据库查询后key值
    #移动网络信息
    IMEI = "imei" #imei
    ICCID = "sim" #iccid
    longitude = "lng" #经度
    latitude = "lat"  #维度
    gprs_signal = "gprs_length" #GPRS信号强度

    #数据库查询后key值
    #WIFI信息
    MAC_address= "boot_mac" #MAC地址
    wifi_length = "wifi_length" #WIFI信号强度

    #数据库查询后key值
    #打印信息
    print_kilometer = 'printer_kilometre' #打印公里数
    open_money_box = "sum(money_box)" #开钱箱次数
    need_paper = "sum(need_paper)" #缺纸总次数
    print_head_broken = "printer_head_broken" #打印头坏点


    # 数据库查询后key值
    #设置项
    new_order_play_time = "new_order_play_time" #新订单播报次数
    new_order_contents="new_order_contents" #新订单播报内容  --[来源播报、内容播报、金额播报、备注播报] 0,1,2,3
    cancel_order_play_time= "cancel_order_play_time" #取消单播报次数
    cancel_order_contents= "cancel_order_contents" #取消单播报内容--[来源播报、内容播报、备注播报] 0,1,3
    rush_order_play_time ="rush_order_play_time" #催单播报次数
    voice_connect = "voice_connect" #网络连接播报次数
    voice_disconnect="voice_disconnect" #网络断开播报次数
    inspection_page_language="inspection_page_language" #自检页语言
    density="density" #打印浓度
    cancel_order_copy = "cancel_order_copy" #取消单打印联数
    dialect = "dialect" #语音方言  0,1,2,3,4   普通话男声,普通话女声,四川话,粤语,  ----英语字段没加
    voice_speed="voice_speed" #语音播报语速





















