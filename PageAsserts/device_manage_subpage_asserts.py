# encoding:utf-8
# author:wangzhicheng
# time:2020/6/9 14:21
# file:device_manage_subpage_asserts.py

from Common.mylogger import logger
from Common.handle_yaml import do_yaml
from Common.handle_mysql import HandleMysql
from Common.switch_timestamp import switch_timestamp
from Common.base_page_object import BasePageObject as BPO
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestDatas.DeviceManageSubPageDatas import DeviceManageSubPageDatas as DMSPD
from PageLocations.device_manage_subpage_locations import DeviceManageSubPageLocations as loc


class DeviceManageSubPageAsserts(BPO):
    """设备管理子界面断言"""

    def find_button_isvisible(self):
        logger.info("断言：设备管理子界面_等待查询按钮是否可见,返回True or False")
        try:
            self.wait_element_visible(loc.find_button, module="设备管理子界面_等待查询按钮可见")
        except:
            return False
        else:
            return True

    def jump_to_isvisible(self):
        logger.info("断言：设备管理子界面_跳至元素是否可见,返回True or False")
        try:
            self.wait_element_visible(loc.find_button, module="设备管理子界面_跳至元素可见")
        except:
            return False
        else:
            return True

    def channel_name_iscorrect(self, channel_name, td_index):
        logger.info("断言：查询到的所有渠道名是否正确,返回True or False")

        # 获取所有的tr 对象 为一个列表
        tr_list = self.get_element(loc.table_tbody, module="获取所有tr为一个列表").find_elements_by_tag_name("tr")

        channle_list = []

        # 遍历 tr 列表
        for tr in tr_list:
            # 获取每个tr下所有td的对象 为一个列表
            td_list = tr.find_elements_by_tag_name("td")
            # 在td的对象列表中获取指定位置的td值并添加到空列表中
            channle_list.append(td_list[td_index].text)

        logger.info("已获取的一列渠道名称列表{}".format(channle_list))

        # 遍历 td 值的列表,如果列表中的值与指定的值相等就在新列表中加"false"
        list_value = []
        for td_value in channle_list:
            if (td_value != channel_name):
                list_value.append("false")
                break

        if "false" in list_value:
            return False
        else:
            return True

    def channel_name_iscontain(self, channel_name, td_index):
        logger.info("断言：查询到的所有渠道名是否包含输入内容,返回True or False")

        # 获取所有的tr 对象 为一个列表
        tr_list = self.get_element(loc.table_tbody, module="获取所有tr为一个列表").find_elements_by_tag_name("tr")

        channel_list = []

        # 遍历 tr 列表
        for tr in tr_list:
            # 获取每个tr下所有td的对象 为一个列表
            td_list = tr.find_elements_by_tag_name("td")
            # 在td的对象列表中获取指定位置的td的值并添加到空列表中
            channel_list.append(td_list[td_index].text)

        logger.info("已获取的一列渠道名称列表{}".format(channel_list))

        # 遍历 td 值的列表 进行比对,如果某一个字符串中不包含指定的值，则在list_value列表中添加"false"
        list_value = []
        for td_value in channel_list:
            if (td_value.find(channel_name) == -1):
                list_value.append("false")
                break

        if "false" in list_value:
            return False
        else:
            return True

    def SN_iscorrect(self, SN, td_index):
        logger.info("断言：查询到的SN是否正确,返回True or False")

        # 获取所有的tr 对象 为一个列表
        tr_list = self.get_element(loc.table_tbody, module="获取所有tr为一个列表").find_elements_by_tag_name("tr")

        SN_list = []

        # 遍历 tr 列表
        for tr in tr_list:
            # 获取每个tr下所有td的对象 为一个列表
            td_list = tr.find_elements_by_tag_name("td")
            # 在td的对象列表中获取指定位置的td的值并添加到空列表中
            SN_list.append(td_list[td_index].text)

        logger.info("已获取的一列SN列表{}".format(SN_list))

        if (SN_list[0] != SN):
            return False
        else:
            return True

    def SN_number_isone(self):
        logger.info("断言：查询到的SN数量只有一个,返回True or False")

        # 获取所有的tr 对象 为一个列表
        tr_list = self.get_element(loc.table_tbody, module="获取所有tr为一个列表").find_elements_by_tag_name("tr")

        if (len(tr_list) == 1):
            return True
        else:
            return False

    def SN_iscontain(self, SN, td_index):
        logger.info("断言：查询到的SN是否包含输入内容,返回True or False")

        # 获取所有的tr 对象 为一个列表
        tr_list = self.get_element(loc.table_tbody, module="获取所有tr为一个列表").find_elements_by_tag_name("tr")

        SN_list = []

        # 遍历 tr 列表
        for tr in tr_list:
            # 获取每个tr下所有td的对象 为一个列表
            td_list = tr.find_elements_by_tag_name("td")
            # 在td的对象列表中获取指定位置的td的值并添加到空列表中
            SN_list.append(td_list[td_index].text)

        logger.info("已获取的一列SN列表{}".format(SN_list))

        # 遍历 td 值的列表 进行比对,如果某一个字符串中不包含指定的值，则在list_value列表中添加"false"
        list_value = []
        for i in SN_list:
            if i.find(SN) == -1:
                list_value.append("false")
                break

        if "false" in list_value:
            return False
        else:
            return True

    def content_is_no_exist(self):
        logger.info("断言：查询不存在的内容,返回True or False")
        # 如果SN不存在则查询内容为空
        try:
            self.wait_element_visible(loc.no_data, module="查询不存在的内容")
        except:
            return False
        else:
            return True

    def select_device_model_and_find_NT211_assert(self, td_index, device_model):
        logger.info("断言：选择小机型点击查询，查询出来的SN机型为NT211,返回True or False")

        tr_list = self.get_element(loc.table_tbody, module="获取所有tr存进一个列表中").find_elements_by_tag_name("tr")

        model_list = []
        for i in tr_list:
            td_list = i.find_elements_by_tag_name("td")
            model_list.append(td_list[td_index])
            # logger.info(f"-------1-------{td_list[td_index].text}")

        list_value = []
        for i in model_list:
            if i.text != device_model:
                list_value.append("false")
                break

        if "false" in list_value:
            return False
        else:
            return True

    def select_device_model_and_find_NT212_assert(self, td_index, device_model):
        logger.info("断言：选择小机型点击查询，查询出来的SN机型为NT212,返回True or False")

        tr_list = self.get_element(loc.table_tbody, module="获取所有tr存进一个列表中").find_elements_by_tag_name("tr")

        model_list = []
        for i in tr_list:
            td_list = i.find_elements_by_tag_name("td")
            model_list.append(td_list[td_index])
            # logger.info(f"-------2-------{td_list[td_index].text}")

        list_value = []
        for i in model_list:
            if i.text != device_model:
                list_value.append("false")
                break

        if "false" in list_value:
            return False
        else:
            return True

    def device_current_state(self):
        logger.info("断言：查询页面SN的当前状态,与数据库数据比对，返回True or False")
        # 查看离线状态的元素存不存在，如果存在则返回0 ，不存在则返回1
        try:
            WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(loc.device_offline))
        except:
            value = 1
        else:
            value = 0

        value_db = (HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_state_sql"), DMSPD.SN))[DMSPD.is_online]
        # 关闭数据库
        HandleMysql().close()

        if value == value_db:
            return True
        else:
            return False

    def device_current_hardware_model(self, td_index):
        logger.info("断言：查询页面SN的小机型,并与数据库数据比对,返回True or False")
        # 获取所有的tr 对象 为一个列表
        tr_list = self.get_element(loc.table_tbody, module="获取tr为一个列表").find_elements_by_tag_name("tr")

        td_list = tr_list[0].find_elements_by_tag_name("td")

        hardware_model = td_list[td_index].text
        logger.info(f"--hardware_model:--{hardware_model}")

        # 从数据库中获取数据
        value = (HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_hardware_model_sql"), DMSPD.SN))[
            DMSPD.hardware_model]
        # 关闭数据库
        HandleMysql().close()
        logger.info(f"---value:---{value}")

        if hardware_model == value:
            return True
        else:
            return False

    def device_current_connect_time(self, td_index):
        logger.info("断言：查询页面SN的上次连入时间,并与数据库数据比对,返回True or False")

        # 从页面获取时间
        # 获取所有的tr 对象 为一个列表
        tr_list = self.get_element(loc.table_tbody, module="获取tr为一个列表").find_elements_by_tag_name("tr")
        td_list = tr_list[0].find_elements_by_tag_name("td")
        connect_time = td_list[td_index].text
        logger.info(f"--connect_time:--{connect_time}")

        # 从数据库中获取连接时间
        value = (HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_connect_time_sql"), DMSPD.SN))[
            DMSPD.connect_time]
        # 关闭数据库
        HandleMysql().close()

        # 转换时间戳为需要格式
        connect_time_db = switch_timestamp(value)
        logger.info(f"--connect_time_db:--{connect_time_db}")

        if connect_time == connect_time_db:
            return True
        else:
            return False

    def device_current_disconnect_time(self, td_index):
        logger.info("断言：查询页面SN的断开连接时间，并与数据库数据比对，返回True or False")

        # 从页面获取时间
        tr_list = self.get_element(loc.table_tbody, module="获取tr为一个列表").find_elements_by_tag_name("tr")
        td_list = tr_list[0].find_elements_by_tag_name("td")
        value = td_list[td_index].text
        logger.info(f"---value:---{value}")

        # 从数据库获取断连时间
        value_db = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_disconnect_time_sql"), DMSPD.SN)
        HandleMysql().close()

        value_db = value_db[DMSPD.disconnect_time]
        # 转换时间戳为需要格式
        value_db = switch_timestamp(value_db)
        logger.info(f"---value_db:---{value_db}")

        if value == value_db:
            return True
        else:
            return False

    def device_log_state(self, td_index):
        logger.info("断言：查询页面的设备log开关状态，并与数据库数据比对，返回True or False")

        # 从页面获取log开关状态
        tr_list = self.get_element(loc.table_tbody, "获取tr为一个列表").find_elements_by_tag_name("tr")
        td_list = tr_list[0].find_elements_by_tag_name("td")
        log_state = td_list[td_index].text

        # 从数据库获取log开关状态
        value_db = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_log_switch_sql"), DMSPD.SN)[
            DMSPD.log_switch]
        HandleMysql().close()

        if log_state == "关":
            value = 0
        else:
            value = 1

        logger.info(f"---value:---{value}")
        logger.info(f"---value_db:---{value_db}")

        if value == value_db:
            return True
        else:
            return False

    def online_devices_number(self, ):
        logger.info("断言：查询页面在线打印机总数，并与数据库数据比对，返回True or False")

        # 从页面获取在线打印机总数
        online_devices_number = self.get_element_text(loc.device_count_and_online_number, "设备子界面-在线打印机总数")
        online_devices_number = online_devices_number.split("/")[1]

        logger.info(f"--------online_devices_number------{online_devices_number}")

        # 从数据库获取在线打印机数据
        db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_online_devices_number_sql"))[
            DMSPD.count_is_online]
        db_value = "在线" + str(db_value) + "台"

        logger.info(f"--------db_value------{db_value}")

        HandleMysql().close()

        if online_devices_number == db_value:
            return True
        else:
            return False

    def device_count(self):
        logger.info("断言：查询页面打印机总数，并与数据库数据比对，返回True or False")

        # 从页面获取打印机总数
        value = self.get_element_text(loc.device_count_and_online_number, "设备子界面-打印机总数")
        value = value.split("/")[0]
        logger.info(f"--------value------{value}")

        # 从数据库获取打印机总数数据
        db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_device_count_sql"))[
            DMSPD.count_msn]
        db_value = "共" + str(db_value) + "台"

        logger.info(f"--------db_value------{db_value}")
        HandleMysql().close()

        if value == db_value:
            return True
        else:
            return False

    def click_fourth_page_assert(self):
        logger.info("断言: 点击第4页进行跳页，第4页框框被选中，被选中后的元素可见 返回True 否则返回 False")

        try:
            self.wait_element_visible(loc.selected_fourth_page, module="子界面-被选中的第四页框框")
        except:
            return False
        else:
            return True

    def jump_tenth_page_assert(self):
        logger.info("断言：跳转框输入10，跳转到第10页，第10页框框被选中，元素可见返回 True 否则返回False")

        try:
            self.wait_element_visible(loc.selected_tenth_page, module="子界面-被选中的第10页框框")
        except:
            return False
        else:
            return True

    def jump_error_page_assert(self):
        logger.info("断言：跳转框输入不存在的页面数，点击enter键，页面不变动，第1页框框被选中，元素可见返回 True 否则返回False")

        try:
            self.wait_element_visible(loc.selected_first_page, module="子界面-被选中的第一页框框")
        except:
            return False
        else:
            return True

    def input_out_of_largest_page_assert(self):
        logger.info("断言：跳转框输入大于当前最大页面的页面数，跳到最后一页，最后一页框框被选中，元素可见返回True，否则False")

        try:
            self.wait_element_visible(loc.selected_end_page, module="子界面-被选中最后一页框框")
        except:
            return False
        else:
            return True

    def click_device_more_info_assert(self):
        logger.info("断言：点击设备更多按钮，设备信息元素可见，订单日志元素可见,可见返回True 否则返回False")

        try:
            self.wait_element_visible(loc.more_info_order_log, module="订单日志元素存在")
            self.wait_element_visible(loc.more_info_device_info, module="设备信息元素存在")
        except:
            return False
        else:
            return True
