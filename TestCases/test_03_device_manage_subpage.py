# encoding:utf-8
# author:wangzhicheng
# time:2020/6/9 14:23
# file:test_03_device_manage_subpage.py



import pytest, time
from Common.mylogger import logger
from TestDatas.DeviceManageSubPageDatas import DeviceManageSubPageDatas as DMSPD


class TestDeviceManageSubPage:
    """设备管理子界面测试用例"""

    pytestmark = pytest.mark.uat

    # 输入完整的渠道阿爸，点击查询成功
    @pytest.mark.usefixtures("click_device_manage")
    def test_03_input_complete_channel(self, click_device_manage):
        logger.info("正常用例-输入完整的渠道名阿爸，点击查询成功")

        click_device_manage[5].input_channle_and_find(DMSPD.complete_channel)
        time.sleep(2)

        assert click_device_manage[4].channel_name_iscorrect(DMSPD.complete_channel, DMSPD.channel_td_index) == True

    # 输入完整的渠道zzzz，点击查询成功
    @pytest.mark.usefixtures("click_device_manage")
    def test_04_input_complete_channel(self, click_device_manage):
        logger.info("正常用例-输入完整的渠道名zzzz，点击查询成功")

        click_device_manage[5].input_channle_and_find(DMSPD.complete_channel_2)
        time.sleep(2)

        assert click_device_manage[4].channel_name_iscorrect(DMSPD.complete_channel_2, DMSPD.channel_td_index) == True

    # 输入不完整的存在的渠道-阿，点击查询成功
    @pytest.mark.usefixtures("click_device_manage")
    def test_05_input_incomplete_channel(self, click_device_manage):
        logger.info("正常用例-输入不完整的存在渠道-阿，点击查询成功")

        click_device_manage[5].input_channle_and_find(DMSPD.notcomplete_channel)
        time.sleep(2)

        assert click_device_manage[4].channel_name_iscontain(DMSPD.notcomplete_channel, DMSPD.channel_td_index) == True

    # 输入完整的SN，点击查询成功
    @pytest.mark.usefixtures("click_device_manage")
    def test_06_input_SN(self, click_device_manage):
        logger.info("正常用例-输入完整的SN，点击查询成功")
        click_device_manage[5].input_SN_and_find(DMSPD.SN)
        time.sleep(2)
        assert click_device_manage[4].SN_iscorrect(DMSPD.SN, DMSPD.SN_td_index) == True
        assert click_device_manage[4].SN_number_isone() == True

    # 输入不完整的SN，点击查询成功
    @pytest.mark.usefixtures("click_device_manage")
    def test_07_input_incomplete_SN(self, click_device_manage):
        logger.info("正常用例-输入不完整的SN，点击查询成功")
        click_device_manage[5].input_SN_and_find(DMSPD.no_complete_SN)
        time.sleep(2)
        assert click_device_manage[4].SN_iscontain(DMSPD.no_complete_SN, DMSPD.SN_td_index) == True

    # 输入不存在的SN，点击查询
    @pytest.mark.usefixtures("click_device_manage")
    def test_08_input_inexistence_SN(self, click_device_manage):
        logger.info("异常用例-输入不存在的SN，点击查询")
        click_device_manage[5].input_SN_and_find(DMSPD.no_exist_SN)
        time.sleep(2)
        assert click_device_manage[4].content_is_no_exist() == True

    # 输入不完整的存在的渠道，点击查询
    @pytest.mark.usefixtures("click_device_manage")
    def test_09_input_inexistence_channel(self, click_device_manage):
        logger.info("异常用例-输入不存在的渠道，点击查询")
        click_device_manage[5].input_channle_and_find(DMSPD.no_exist_channel)
        time.sleep(2)
        assert click_device_manage[4].content_is_no_exist() == True

    # 选择机型NT211,点击查询
    # @pytest.mark.smoke
    @pytest.mark.usefixtures("click_device_manage")
    def test_10_select_device_model_find(self, click_device_manage):
        logger.info("正常用例-选择机型NT211，点击查询")
        click_device_manage[5].select_device_model_and_find_NT211()
        time.sleep(2)
        assert click_device_manage[4].select_device_model_and_find_NT211_assert(DMSPD.hareware_model_td_index,
                                                                                DMSPD.device_model_NT211) == True

    # 选择机型NT211,点击查询
    # @pytest.mark.smoke
    @pytest.mark.usefixtures("click_device_manage")
    def test_11_select_device_model_find(self, click_device_manage):
        logger.info("正常用例-选择机型NT212，点击查询")
        click_device_manage[5].select_device_model_and_find_NT212()
        time.sleep(2)
        assert click_device_manage[4].select_device_model_and_find_NT212_assert(DMSPD.hareware_model_td_index,
                                                                                DMSPD.device_model_NT212) == True

    # 输入完整的SN查看当前状态
    # @pytest.mark.smoke
    @pytest.mark.usefixtures("click_device_manage")
    def test_12_query_device_current_state(self, click_device_manage):
        logger.info("正常用例-查询单台设备的当前状态")
        click_device_manage[5].input_SN_and_find(DMSPD.SN)
        time.sleep(1)
        assert click_device_manage[4].device_current_state() == True

    # 输入完整的SN查看小机型hardware_model
    # @pytest.mark.smoke
    @pytest.mark.usefixtures("click_device_manage")
    def test_13_query_device_current_hardware_model(self, click_device_manage):
        logger.info("正常用例-查询单台设备的小机型")
        click_device_manage[5].input_SN_and_find(DMSPD.SN)
        time.sleep(1)
        assert click_device_manage[4].device_current_hardware_model(DMSPD.hareware_model_td_index) == True

    # 输入完整的SN查看上次连入时间
    # @pytest.mark.smoke
    @pytest.mark.usefixtures("click_device_manage")
    def test_14_query_device_connect(self, click_device_manage):
        logger.info("正常用例-查询单台设备的上次连入时间")
        click_device_manage[5].input_SN_and_find(DMSPD.SN)
        time.sleep(1)
        assert click_device_manage[4].device_current_connect_time(DMSPD.last_connect_td_index) == True

    # 输入完整的SN查看上次断开时间
    # @pytest.mark.smoke
    @pytest.mark.usefixtures("click_device_manage")
    def test_15_query_device_disconnect(self, click_device_manage):
        logger.info("正常用例-输入完整的SN查询机器上次断开时间")
        click_device_manage[5].input_SN_and_find(DMSPD.SN)
        time.sleep(1)
        assert click_device_manage[4].device_current_disconnect_time(DMSPD.last_disconnect_td_index) == True

    # 输入完整的SN查看机器log开关状态
    # @pytest.mark.smoke
    @pytest.mark.usefixtures("click_device_manage")
    def test_16_query_device_log_state(self, click_device_manage):
        logger.info("正常用例-输入完整的SN查询机器log开关状态")
        click_device_manage[5].input_SN_and_find(DMSPD.SN)
        time.sleep(1)
        assert click_device_manage[4].device_log_state(DMSPD.log_switch_td_index) == True

    # 查看当前在线打印机台数
    # @pytest.mark.smoke
    @pytest.mark.usefixtures("click_device_manage")
    def test_17_query_online_devices_number(self, click_device_manage):
        logger.info("正常用例-获取在线打印机台数")
        assert click_device_manage[4].online_devices_number() == True

    # 查看打印机总数
    # @pytest.mark.smoke
    @pytest.mark.usefixtures("click_device_manage")
    def test_18_query_device_count(self, click_device_manage):
        logger.info("正常用例-获取打印机台数")
        assert click_device_manage[4].device_count() == True

    # 点击第四页进行跳页
    # @pytest.mark.smoke
    @pytest.mark.usefixtures("click_device_manage")
    def test_19_click_fourth_page(self, click_device_manage):
        logger.info("正常用例-点击第4页，页面跳转成功")
        click_device_manage[5].click_fourth_page_obj()
        assert click_device_manage[4].click_fourth_page_assert() == True

    # 跳转输入框中输入数字，进行页面跳转
    # @pytest.mark.smoke
    @pytest.mark.usefixtures("click_device_manage")
    def test_20_input_page_jump(self, click_device_manage):
        logger.info("正常用例-输入页面数字10-跳转页面成功")
        click_device_manage[5].input_page_number_jump_obj(DMSPD.jump_to_page_number, DMSPD.enter_keyboard)
        assert click_device_manage[4].jump_tenth_page_assert() == True

    # 输入不存在的页面数字 0，-1，页面不会发生跳转
    # @pytest.mark.smoke
    @pytest.mark.usefixtures("click_device_manage")
    @pytest.mark.parametrize("value", DMSPD.jump_to_error_page)
    def test_21_page_jump_failure(self, click_device_manage, value):
        logger.info(f"异常用例-输入不存的页面数字{value}，页面跳转失败")

        click_device_manage[5].input_page_number_jump_obj(value, DMSPD.enter_keyboard)
        assert click_device_manage[4].jump_error_page_assert() == True

    # @pytest.mark.smoke
    @pytest.mark.usefixtures("click_device_manage")
    def test_22_page_out_of_largest(self, click_device_manage):
        logger.info("异常用例-输入大于当前最大页面的数字，页面跳转至最后一页")

        click_device_manage[5].input_page_number_jump_obj(DMSPD.out_of_largest_page_number, DMSPD.enter_keyboard)
        assert click_device_manage[4].input_out_of_largest_page_assert() == True

    @pytest.mark.usefixtures("click_device_manage")
    # @pytest.mark.smoke
    def test_23_click_device_more_info(self, click_device_manage):
        logger.info("正常用例-指定SN查询后点击更多按钮成功")

        click_device_manage[5].input_SN_and_find(DMSPD.SN)
        time.sleep(1)
        click_device_manage[5].click_device_more_info_obj()
        assert click_device_manage[4].click_device_more_info_assert() == True
