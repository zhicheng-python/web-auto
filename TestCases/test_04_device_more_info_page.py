# encoding:utf-8
# author:wangzhicheng
# time:2020/8/11 14:01
# file:test_04_device_more_info_page.py

import pytest
from Common.mylogger import logger


class TestDeviceMoreInfoPage:
    """设备更多信息页面测试用例"""

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info")
    def test_24_click_device_info_success(self, device_more_info):
        logger.info("正常用例-点击设备信息-成功展开信息")
        device_more_info[7].click_device_info_obj()
        assert device_more_info[6].click_device_info_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_25_click_refresh_button(self, device_more_info_device_info):
        logger.info("正常用例-点击设备信息-本机信息-点击刷新按钮")
        # 点击刷新按钮
        device_more_info_device_info[7].click_refresh_button_obj()
        assert device_more_info_device_info[6].click_refresh_button_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_26_click_local_device_info(self, device_more_info_device_info):
        logger.info("正常用例-点击设备信息-点击本机信息-展示信息收回")
        device_more_info_device_info[7].click_local_device_info_obj()
        assert device_more_info_device_info[6].click_local_device_info_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_27_query_ldi_model(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看本机信息1）机型")
        assert device_more_info_device_info[6].query_ldi_model_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_28_query_ldi_sn(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看本机信息2）SN 号")
        assert device_more_info_device_info[6].query_ldi_sn_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_29_query_ldi_hardware_version(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看本机信息3）硬件版本")
        assert device_more_info_device_info[6].query_ldi_hardware_version_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_30_query_ldi_bootloader_version(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看本机信息4）bootloader版本")
        assert device_more_info_device_info[6].query_ldi_bootloader_version_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_31_query_ldi_firware_version(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看本机信息5）固件版本")
        assert device_more_info_device_info[6].query_ldi_firware_version_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_32_query_ldi_app_version(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看本机信息6）app版本")
        assert device_more_info_device_info[6].query_ldi_app_version_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_33_query_ldi_font_library_version(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看本机信息7）字库版本")
        assert device_more_info_device_info[6].query_ldi_font_library_version_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_34_query_ldi_tts_language(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看本机信息8）TTS方言")
        assert device_more_info_device_info[6].query_ldi_tts_language_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_35_query_ldi_tts_version(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看本机信息9）TTS字库版本")
        assert device_more_info_device_info[6].query_ldi_tts_version_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_36_query_ldi_network_type(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看本机信息10）网络类型")
        assert device_more_info_device_info[6].query_ldi_network_type_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_37_click_mobile_net_info(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-点击移动网络信息-展开列表")
        device_more_info_device_info[7].click_mobile_net_info_obj()
        assert device_more_info_device_info[6].click_mobile_net_info_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_38_query_IMEI(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看移动网络信息-查看IMEI号")
        device_more_info_device_info[7].click_mobile_net_info_obj()
        assert device_more_info_device_info[6].query_IMEI_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_39_query_ICCID(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看移动网络信息-查看ICCID号")
        device_more_info_device_info[7].click_mobile_net_info_obj()
        assert device_more_info_device_info[6].query_ICCID_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_40_query_longitude_latitude(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看移动网络信息-当前经纬度")
        device_more_info_device_info[7].click_mobile_net_info_obj()
        assert device_more_info_device_info[6].query_longitude_latitude_assert() == True

    @pytest.mark.test
    def test_41_query_signal_strength(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看移动网络信息-当前信号强度")
        device_more_info_device_info[7].click_mobile_net_info_obj()
        assert device_more_info_device_info[6].query_signal_strength_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_42_click_refresh_button_mobile_net(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-点击移动网络信息-点击刷新按钮")
        device_more_info_device_info[7].click_mobile_net_info_obj()
        device_more_info_device_info[7].click_mobile_net_info_refresh_button_obj()
        assert device_more_info_device_info[6].click_refresh_button_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_43_click_WIFI_info(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-点击WIFI信息-展开列表")
        device_more_info_device_info[7].click_wifi_info_obj()
        assert device_more_info_device_info[6].click_wifi_info_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_44_query_MAC_address(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看WIFI信息-MAC地址")
        device_more_info_device_info[7].click_wifi_info_obj()
        assert device_more_info_device_info[6].query_MAC_address_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_45_query_wifi_length(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看WIFI信息-信号强度")
        device_more_info_device_info[7].click_wifi_info_obj()
        assert device_more_info_device_info[6].query_wifi_length_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_46_click_printer_info(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-点击打印信息-展开")
        device_more_info_device_info[7].click_printer_info_obj()
        assert device_more_info_device_info[6].click_printer_info_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_47_query_printer_kilometer(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看打印公里数")
        device_more_info_device_info[7].click_printer_info_obj()
        assert device_more_info_device_info[6].query_printer_kilometer_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_48_open_money_box(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看开钱箱次数")
        device_more_info_device_info[7].click_printer_info_obj()
        assert device_more_info_device_info[6].query_open_money_box_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_49_query_need_paper(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看缺纸次数")
        device_more_info_device_info[7].click_printer_info_obj()
        assert device_more_info_device_info[6].query_need_paper_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_50_query_printer_head_broken(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看打印头坏点")
        device_more_info_device_info[7].click_printer_info_obj()
        assert device_more_info_device_info[6].query_printer_head_broken_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_51_click_set_the_item(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-点击设置项展开信息")
        device_more_info_device_info[7].click_set_the_item_obj()
        assert device_more_info_device_info[6].click_set_the_item_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_52_query_new_order_play_time(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看设置项-新订单播报次数")
        device_more_info_device_info[7].click_set_the_item_obj()
        assert device_more_info_device_info[6].query_new_order_play_time_assert() == True

    @pytest.mark.test
    @pytest.mark.db
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_53_query_new_order_contents(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看设置项-新订单播报内容")
        device_more_info_device_info[7].click_set_the_item_obj()
        assert device_more_info_device_info[6].query_new_order_contents_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_54_query_cancle_order_play_time(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看设置项-取消单播报次数")
        device_more_info_device_info[7].click_set_the_item_obj()
        assert device_more_info_device_info[6].query_cancle_order_play_time_assert() == True

    @pytest.mark.test
    @pytest.mark.db
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_55_query_cancle_order_contents(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看设置项-取消单播报内容")
        device_more_info_device_info[7].click_set_the_item_obj()
        assert device_more_info_device_info[6].query_cancle_order_contents_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_56_query_rush_order_play_time(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看设置项-催单播报次数")
        device_more_info_device_info[7].click_set_the_item_obj()
        assert device_more_info_device_info[6].query_rush_order_play_time_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_57_query_voice_connect(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看设置项-网络连接播报次数")
        device_more_info_device_info[7].click_set_the_item_obj()
        assert device_more_info_device_info[6].query_voice_connect_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_58_query_voice_disconnect(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看设置项-网络断开播报次数")
        device_more_info_device_info[7].click_set_the_item_obj()
        assert device_more_info_device_info[6].query_voice_disconnect_assert() == True

    @pytest.mark.test
    @pytest.mark.db
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_59_query_inspection_page_language(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看设置项-自检页语言")
        device_more_info_device_info[7].click_set_the_item_obj()
        assert device_more_info_device_info[6].query_inspection_page_language_assert() == True

    @pytest.mark.test
    @pytest.mark.db
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_60_query_density(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看设置项-打印浓度")
        device_more_info_device_info[7].click_set_the_item_obj()
        assert device_more_info_device_info[6].query_density_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_61_query_cancel_order_copy(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看设置项-取消单打印联数")
        device_more_info_device_info[7].click_set_the_item_obj()
        assert device_more_info_device_info[6].query_cancel_order_copy_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_62_query_dialect(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看设置项-语音方言")
        device_more_info_device_info[7].click_set_the_item_obj()
        assert device_more_info_device_info[6].query_dialect_assert() == True

    @pytest.mark.test
    @pytest.mark.db
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_63_query_voice_speed(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-查看设置项-语音播报语速")
        device_more_info_device_info[7].click_set_the_item_obj()
        assert device_more_info_device_info[6].query_voice_speed_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_64_click_refresh_button_set_the_item(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-点击设置项旁的刷新按钮")
        device_more_info_device_info[7].click_set_the_item_obj()
        device_more_info_device_info[7].click_set_the_item_refresh_button_obj()
        assert device_more_info_device_info[6].click_refresh_button_assert() == True

    @pytest.mark.test
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_65_click_refresh_button_WIFI_info(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-点击wifi信息旁的刷新按钮")
        device_more_info_device_info[7].click_wifi_info_obj()
        device_more_info_device_info[7].click_wifi_info_refresh_button_obj()
        assert device_more_info_device_info[6].click_refresh_button_assert() == True

    # @pytest.mark.db
    @pytest.mark.usefixtures("device_more_info_device_info")
    def test_66_click_refresh_button_printer_info(self, device_more_info_device_info):
        logger.info("正常用例：点击设备信息-点击打印信息旁的刷新按钮")
        device_more_info_device_info[7].click_printer_info_obj()
        device_more_info_device_info[7].click_printer_info_refresh_button_obj()
        assert device_more_info_device_info[6].click_refresh_button_assert() == True
