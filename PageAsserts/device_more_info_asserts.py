# encoding:utf-8
# author:wangzhicheng
# time:2020/8/11 14:03
# file:device_more_info_asserts.py


from Common.mylogger import logger
from Common.handle_yaml import do_yaml
from Common.handle_mysql import HandleMysql
from Common.base_page_object import BasePageObject as BPO
from TestDatas.DeviceMoreInfoPageDatas import DeviceMoreInfoPageDatas as DMIPD
from PageLocations.device_more_info_locations import DeviceMoreInfoLocations as loc


class DeviceMoreInfoAssert(BPO):
    """设备更多信息页面断言"""

    def click_device_info_assert(self):
        logger.info("断言：点击更多-设备信息后页面跳转成功，本机信息和设备项元素可见，返回True or False")
        try:
            self.wait_element_visible(loc.local_device_info, module="更多-点击设备信息-本机信息可见")
            self.wait_element_visible(loc.local_device_setting, module="更多-点击设备信息-设置项可见")
        except:
            return False
        else:
            return True

    def click_refresh_button_assert(self):
        logger.info("断言：点击更多-设备信息,页面跳转成功，点击刷新按钮，刷新花朵元素可见，返回True or False")
        try:
            self.wait_element_visible(loc.refresh_flower, module="更多-点击设备信息-本机信息-点击刷新按钮")
        except:
            return False
        else:
            return True

    def click_local_device_info_assert(self):
        logger.info("断言：点击设备信息-本机信息-收回展示信息，收回后loc.ldi_fold元素存在 ，返回True or Fasle")

        try:
            self.wait_element_presence(loc.ldi_fold, module="点击本机信息-展示信息收回-loc.ldi_fold存在")
        except:
            return False
        else:
            return True

    def query_ldi_model_assert(self):
        logger.info("断言：本机信息-查询页面机型与数据库数据比较-返回True or Flase")

        value = self.get_element_text(loc.ldi_model, module="查询本机信息-机型型号")
        logger.info(f"---value-----{value}")

        db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_hardware_model_sql"), DMIPD.SN)[
            DMIPD.hardware_model]
        HandleMysql().close()
        logger.info(f"----db_value----{db_value}")

        if value == db_value:
            return True
        else:
            return False

    def query_ldi_sn_assert(self):
        logger.info("断言：本机信息-查询页面SN与给定SN比较-返回True or Flase")

        value = self.get_element_text(loc.ldi_sn, module="查询本机信息-SN号")
        logger.info(f"---value-----{value}")
        db_value = DMIPD.SN
        logger.info(f"----db_value----{db_value}")

        if value == db_value:
            return True
        else:
            return False

    def query_ldi_hardware_version_assert(self):
        logger.info("断言：本机信息-查询页面固件版本与数据库数据比较-返回True or Flase")

        value = self.get_element_text(loc.ldi_hardware_version, module="查询本机信息-固件版本")
        logger.info(f"---value-----{value}")

        db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_hardware_version_sql"), DMIPD.SN)[
            DMIPD.hardware_version]
        HandleMysql().close()

        db_value = "V" + db_value
        logger.info(f"----db_value----{db_value}")

        if value == db_value:
            return True
        else:
            return False

    def query_ldi_bootloader_version_assert(self):
        logger.info("断言：本机信息-查询页面bootloader版本与数据库数据比较-返回True or Flase")

        value = self.get_element_text(loc.ldi_bootloader_version, module='查询本机信息-bootloader版本')
        logger.info(f"---value-----{value}")

        db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_bootloader_version_sql"), DMIPD.SN)[
            DMIPD.bootloader_version]
        HandleMysql().close()

        db_value = "V" + db_value
        logger.info(f"----db_value----{db_value}")

        if db_value == value:
            return True
        else:
            return False

    def query_ldi_firware_version_assert(self):
        logger.info("断言：本机信息-查询页面固件版本与数据库数据比较-返回True or Flase")

        value = self.get_element_text(loc.ldi_firmware_version, module="查询本机信息-固件版本")
        logger.info(f"---value-----{value}")

        db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_firware_version_sql"), DMIPD.SN)[
            DMIPD.firmware_version]
        HandleMysql().close()

        db_value = "V" + db_value
        logger.info(f"----db_value----{db_value}")

        if db_value == value:
            return True
        else:
            return False

    def query_ldi_app_version_assert(self):
        logger.info("断言：本机信息-查询页面app版本与数据库数据比较-返回True or False")
        value = self.get_element_text(loc.ldi_app_version, module="查询本机信息-app版本")
        logger.info(f"---value-----{value}")

        db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_app_version_sql"), DMIPD.SN)[
            DMIPD.app_version]
        HandleMysql().close()

        db_value = "V" + db_value
        logger.info(f"----db_value----{db_value}")

        if db_value == value:
            return True
        else:
            return False

    def query_ldi_font_library_version_assert(self):
        logger.info("断言：本机信息-查询页面字库版本与数据库数据比较-返回True or False")
        value = self.get_element_text(loc.ldi_font_library_version, module="查询本机信息-字库版本")
        logger.info(f"---value-----{value}")
        db_value = "V" + \
                   HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_font_library_version_sql"), DMIPD.SN)[
                       DMIPD.font_library_version]
        logger.info(f"----db_value----{db_value}")

        if db_value == value:
            return True
        else:
            return False

    def query_ldi_tts_language_assert(self):
        logger.info("断言：本机信息-查询页面tts语言与数据库数据比较-返回True or False")

        value = self.get_element_text(loc.ldi_tts_language, module="查询本机信息-tts语言")
        value = value.split("(")[1].split(")")[0]
        logger.info(f"---value-----{value}")

        db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_tts_language_sql"), DMIPD.SN)[
            DMIPD.tts_language]
        logger.info(f"----db_value----{db_value}")

        if db_value == value:
            return True
        else:
            return False

    def query_ldi_tts_version_assert(self):
        logger.info("断言：本机信息-查询页面tts版本与数据库数据比较-返回True or False")
        value = self.get_element_text(loc.ldi_tts_language, module="查询本机信息-tts版本")
        value = value.split("(")[0]
        logger.info(f"---value-----{value}")

        db_value = "V" + HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_tts_version_sql"), DMIPD.SN)[
            DMIPD.tts_version]
        logger.info(f"----db_value----{db_value}")

        if db_value == value:
            return True
        else:
            return False

    def query_ldi_network_type_assert(self):
        logger.info("断言：本机信息-查询页面网络类型与数据库数据比较-返回True or False")
        value = self.get_element_text(loc.ldi_network_type, module="查询本机信息-网络类型版本")
        logger.info(f"---value-----{value}")

        db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_network_type_sql"), DMIPD.SN)[
            DMIPD.network_type]
        if db_value == 0:
            db_value = "GPRS"
        elif db_value == 1:
            db_value = "WIFI"
        logger.info(f"----db_value----{db_value}")

        if db_value == value:
            return True
        else:
            return False

    def click_mobile_net_info_assert(self):
        logger.info("断言：点击设备信息-点击移动网络信息-展开列表-信号强度元素可见")

        try:
            self.wait_element_visible(loc.mni_signal_strength, module="点击移动网络信息-展开列表-信号强度元素可见")
        except:
            return False
        else:
            return True

    def query_IMEI_assert(self):
        logger.info("断言：点击设备信息-移动网络-查询页面IMEI号，与数据库数据比较，返回True or Flase")

        value = self.get_element_text(loc.mni_IMEI, module="获取页面IMEI号")
        logger.info(f"---value-----:{value}")

        db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_imei_sql"), DMIPD.SN)[DMIPD.IMEI]

        if db_value == "":
            db_value = "--"
        logger.info(f"----db_value----:{db_value}")

        if db_value == value:
            return True
        else:
            return False

    def query_ICCID_assert(self):
        logger.info("断言：点击设备信息-移动网络-查询页面ICCID号，与数据库数据比较，返回True or Flase")

        value = self.get_element_text(loc.mni_ICCID, module="获取页面ICCID号")
        logger.info(f"---value-----:{value}")

        db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_iccid_sql"), DMIPD.SN)[DMIPD.ICCID]

        if db_value == "":
            db_value = "--"
        logger.info(f"----db_value----:{db_value}")

        if db_value == value:
            return True
        else:
            return False

    def query_longitude_latitude_assert(self):
        logger.info("断言：点击设备信息-移动网络-查询经纬度，与数据库数据比较，返回Ture or False")

        value = self.get_element_text(loc.mni_current_longitude_latitude, module="获取页面经纬度")
        logger.info(f"---value-----:{value}")

        db_value_longitude = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_lng_sql"), DMIPD.SN)[
            DMIPD.longitude]

        db_value_latitude = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_lat_sql"), DMIPD.SN)[
            DMIPD.latitude]

        HandleMysql().close()

        if str(db_value_longitude) == "0E-7":
            db_value_longitude = "0.00"
        else:
            db_value_longitude = "{:.2f}".format(db_value_longitude)

        if str(db_value_latitude) == "0E-7":
            db_value_latitude = "0.00"
        else:
            db_value_latitude = "{:.2f}".format(db_value_latitude)

        db_value = "Lat: " + db_value_latitude + " " + "Lon: " + db_value_longitude  # Lat: 0.00 Lon: 0.00
        logger.info(f"----db_value----:{db_value}")

        if db_value == value:
            return True
        else:
            return False

    def query_signal_strength_assert(self):
        logger.info("断言：点击设备信息-移动网络-查询信号强度，与数据库数据比较，返回Ture or False")

        value = self.get_element_text(loc.mni_signal_strength, module="获取当前移动网络信号强度")

        if "." not in value:
            value = value.replace("dB", ".0dB")
        logger.info(f"---value-----:{value}")

        try:
            db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_gprs_signal_sql"), DMIPD.SN)[
                DMIPD.gprs_signal]
        except:
            db_value = "--"
        else:
            db_value = str(db_value) + "dB"

        logger.info(f"----db_value----:{db_value}")

        if db_value == value:
            return True
        else:
            return False

    def click_wifi_info_assert(self):
        logger.info("断言:点击wifi信息-信息强度元素可见，返回True or False")

        try:
            self.wait_element_visible(loc.wifi_length, "WiFi信息-信号强度")
        except:
            return False
        else:
            return True

    def query_MAC_address_assert(self):
        logger.info("断言：点击wifi信息-查看页面mac地址，与数据库数据比对，返回True or False")

        value = self.get_element_text(loc.mac_address, module="查询页面MAC地址")
        logger.info(f"---value-----:{value}")

        db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_boot_mac_sql"), DMIPD.SN)[
            DMIPD.MAC_address]

        if db_value == None:
            db_value = "--"
        logger.info(f"----db_value----:{db_value}")

        HandleMysql().close()

        if db_value == value:
            return True
        else:
            return False

    def query_wifi_length_assert(self):
        logger.info("断言：点击wifi信息-查看页面wifi强度，与数据库数据比对，返回True or False")

        value = self.get_element_text(loc.wifi_length, module="查询页面wifi信号强度")

        if "." not in value:
            value = value.replace("dB", ".0dB")
        logger.info(f"---value-----:{value}")

        try:
            db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_wifi_length_sql"), DMIPD.SN)[
                DMIPD.wifi_length]
        except:
            db_value = "--"
        else:
            db_value = str(db_value) + "dB"

        logger.info(f"----db_value----:{db_value}")

        HandleMysql().close()

        if db_value == value:
            return True
        else:
            return False

    def click_printer_info_assert(self):
        logger.info("断言：点击打印信息-列表展开，打印头坏点元素可见，返回True or False")
        try:
            self.wait_element_visible(loc.printer_head_broken, module='打印信息-列表展开，打印头坏点元素可见')
        except:
            return False
        else:
            return True

    def query_printer_kilometer_assert(self):
        logger.info("断言：点击打印信息-查看页面打印公里数，与数据库数据比对，返回True or False")

        value = self.get_element_text(loc.printer_kilometer, module="查询页面打印机公里数")
        logger.info(f"---value-----:{value}")

        try:
            db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_printer_info_sql"), DMIPD.SN)[
                DMIPD.print_kilometer]
        except:
            db_value = "--"
        else:
            db_value = str(db_value / 1000) + "m"

        logger.info(f"----db_value----:{db_value}")

        if db_value == value:
            return True
        else:
            return False

    def query_open_money_box_assert(self):
        logger.info("断言：点击打印信息-查看页面开钱箱次数，与数据库数据比对，返回True or False")

        value = self.get_element_text(loc.money_box, module="查询页面开钱箱次数")
        logger.info(f"---value-----:{value}")

        db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_money_box_sql"), DMIPD.SN)[
            DMIPD.open_money_box]
        if db_value == None:
            db_value = "--"
        else:
            db_value = str(db_value) + "次"
        logger.info(f"----db_value----:{db_value}")

        if db_value == value:
            return True
        else:
            return False

    def query_need_paper_assert(self):
        logger.info("断言：点击打印信息-查看页面缺纸次数，与数据库数据比对，返回True or False")

        value = self.get_element_text(loc.need_paper, module="查询页面缺纸次数")
        logger.info(f"---value-----:{value}")

        db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_need_paper_sql"), DMIPD.SN)[
            DMIPD.need_paper]

        if db_value == None:
            db_value = "--"
        else:
            db_value = str(db_value) + "次"

        logger.info(f"----db_value----:{db_value}")

        if db_value == value:
            return True
        else:
            return False

    def query_printer_head_broken_assert(self):
        logger.info("断言：点击打印信息-查看页面打印头坏点，与数据库数据比对，返回True or False")

        value = self.get_element_text(loc.printer_head_broken, module="查询页面打印头坏点")
        logger.info(f"---value-----:{value}")

        try:
            db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_printer_head_broken_sql"), DMIPD.SN)[
                DMIPD.print_head_broken]
        except:
            db_value = "--"

        logger.info(f"----db_value----:{db_value}")

        if db_value == value:
            return True
        else:
            return False

    def click_set_the_item_assert(self):
        logger.info("断言:点击设置项-列表展开-打印浓度元素可见,返回True or False")

        try:
            self.wait_element_visible(loc.density, module="设置项-列表展开-打印浓度元素可见")
        except:
            return False
        else:
            return True

    def query_new_order_play_time_assert(self):
        logger.info("断言:设置项-查看页面新订单播报次数，与数据库数据比对，返回True or False")

        value = self.get_element_text(loc.new_order_play_time, module="设置项-新订单播报次数")
        logger.info(f"---value-----:{value}")

        try:
            db_value = str(
                HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_new_order_play_time_sql"), DMIPD.SN)[
                    DMIPD.new_order_play_time]) + "次"
        except:
            db_value = '1次'
        finally:
            HandleMysql().close()
        logger.info(f"----db_value----:{db_value}")

        if value == db_value:
            return True
        else:
            return False

    def query_new_order_contents_assert(self):
        logger.info("断言：设置项-查看页面新订单播报内容，与数据库比对，返回True or False")

        value = self.get_element_text(loc.new_order_contents, module="设置项-新订单播报内容")
        logger.info(f"---value-----:{value}")

        try:
            db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_new_order_contents_sql"), DMIPD.SN)[
                DMIPD.new_order_contents]
        except:
            db_value = "来源播报、备注播报"
        else:
            if db_value == "0,1,2,3":
                db_value = "来源播报、内容播报、金额播报、备注播报"
            elif db_value == "0,1,2":
                db_value = "来源播报、内容播报、金额播报"
            elif db_value == "0,1":
                db_value = "来源播报、内容播报"
            elif db_value == "0":
                db_value = "来源播报"
            elif db_value == "0,2":
                db_value = "来源播报、金额播报"
            elif db_value == "0,2,3":
                db_value = "来源播报、金额播报、备注播报"
            elif db_value == "0,3":
                db_value = "来源播报、备注播报"
            elif db_value == "1":
                db_value = "内容播报"
            elif db_value == "1,2":
                db_value = "内容播报、金额播报"
            elif db_value == "1,2,3":
                db_value = "内容播报、金额播报、备注播报"
            elif db_value == "1,3":
                db_value = "内容播报、备注播报"
            elif db_value == "2":
                db_value = "金额播报"
            elif db_value == "2,3":
                db_value = "金额播报、备注播报"
            elif db_value == "3":
                db_value = "备注播报"
            else:
                db_value = ""
        finally:
            HandleMysql().close()
            logger.info(f"----db_value----:{db_value}")

        if value == db_value:
            return True
        else:
            return False

    def query_cancle_order_play_time_assert(self):
        logger.info("断言：设置项-查看页面取消单播报次数，与数据库比对，返回True or False")
        value = self.get_element_text(loc.cancel_order_play_time, module="设置项-取消单播报次数")
        logger.info(f"---value-----:{value}")

        try:
            db_value = str(
                HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_cancel_order_play_time_sql"), DMIPD.SN)[
                    DMIPD.cancel_order_play_time]) + "次"
        except:
            db_value = "1次"
        finally:
            HandleMysql().close()
            logger.info(f"----db_value----:{db_value}")

        if value == db_value:
            return True
        else:
            return False

    def query_cancle_order_contents_assert(self):
        logger.info("断言：设置项-查看页面取消单播报内容，与数据库比对，返回True or False")

        value = self.get_element_text(loc.cancel_order_contents, module="设置项-取消单播报内容")
        logger.info(f"---value-----:{value}")

        try:
            db_value = \
                HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_cancel_order_contents_sql"), DMIPD.SN)[
                    DMIPD.cancel_order_contents]
        except:
            db_value = "来源播报、备注播报"
        else:
            if db_value == "0,1,3":
                db_value = "来源播报、内容播报、备注播报"
            elif db_value == "0,1":
                db_value = "来源播报、内容播报"
            elif db_value == "0":
                db_value = "来源播报"
            elif db_value == "0,3":
                db_value = "来源播报、备注播报"
            elif db_value == "1":
                db_value = "内容播报"
            elif db_value == "1,3":
                db_value = "内容播报、备注播报"
            elif db_value == "3":
                db_value = "备注播报"
            else:
                db_value = ""
        finally:
            HandleMysql().close()
            logger.info(f"----db_value----:{db_value}")

        if value == db_value:
            return True
        else:
            return False

    def query_rush_order_play_time_assert(self):
        logger.info("断言：设置项-查看页面催单播报次数，与数据库比对，返回True or False")
        value = self.get_element_text(loc.rush_order_play_time, module="设置项-催单播报次数")
        logger.info(f"---value-----:{value}")

        try:
            db_value = str(
                HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_rush_order_play_time_sql"), DMIPD.SN)[
                    DMIPD.rush_order_play_time]) + "次"
        except:
            db_value = "1次"
        finally:
            HandleMysql().close()
            logger.info(f"----db_value----:{db_value}")

        if value == db_value:
            return True
        else:
            return False

    def query_voice_connect_assert(self):
        logger.info("断言：设置项-查看页面网络连接播报次数，与数据库比对，返回True or False")
        value = self.get_element_text(loc.voice_connect, module="设置项-网络连接播报次数")
        logger.info(f"---value-----:{value}")

        try:
            db_value = str(HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_voice_connect_sql"), DMIPD.SN)[
                               DMIPD.voice_connect]) + "次"
        except:
            db_value = "1次"
        finally:
            HandleMysql().close()
            logger.info(f"----db_value----:{db_value}")

        if value == db_value:
            return True
        else:
            return False

    def query_voice_disconnect_assert(self):
        logger.info("断言：设置项-查看页面网络断开播报次数，与数据库比对，返回True or False")
        value = self.get_element_text(loc.voice_disconnect, module="设置项-网络断开播报次数")
        logger.info(f"---value-----:{value}")

        try:
            db_value = str(HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_voice_disconnect_sql"), DMIPD.SN)[
                               DMIPD.voice_disconnect]) + "次"
        except:
            db_value = "0次"
        finally:
            HandleMysql().close()
            logger.info(f"----db_value----:{db_value}")

        if value == db_value:
            return True
        else:
            return False

    def query_inspection_page_language_assert(self):
        logger.info("断言：设置项-查看页面自检页语言，与数据库比对，返回True or False")
        value = self.get_element_text(loc.inspection_page_language, module="设置项-自检页语言")
        logger.info(f"---value-----:{value}")

        try:
            db_value = \
                HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_inspection_page_language_sql"), DMIPD.SN)[
                    DMIPD.inspection_page_language]
        except:
            db_value = "简体中文"
        else:
            if db_value == 0:
                db_value = "简体中文"
            elif db_value == 1:
                db_value = "英文"
        finally:
            HandleMysql().close()
            logger.info(f"----db_value----:{db_value}")

        if value == db_value:
            return True
        else:
            return False

    def query_density_assert(self):
        logger.info("断言：设置项-查看页面打印浓度，与数据库比对，返回True or False")
        value = self.get_element_text(loc.density, module="设置项-打印浓度")
        logger.info(f"---value-----:{value}")

        try:
            db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_density_sql"), DMIPD.SN)[
                DMIPD.density]
        except:
            db_value = "100%"
        else:
            if db_value == 75:
                db_value = "75%"
            elif db_value == 85:
                db_value = "85%"
            elif db_value == 100:
                db_value = "100%"
            elif db_value == 125:
                db_value = "125%"
            elif db_value == 150:
                db_value = "150%"
        finally:
            HandleMysql().close()
            logger.info(f"----db_value----:{db_value}")

        if value == db_value:
            return True
        else:
            return False

    def query_cancel_order_copy_assert(self):
        logger.info("断言：设置项-查看页面取消单打印联数，与数据库比对，返回True or False")
        value = self.get_element_text(loc.cancel_order_copy, module="设置项-取消单打印联数")
        logger.info(f"---value-----:{value}")

        try:
            db_value = str(
                HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_cancel_order_copy_sql"), DMIPD.SN)[
                    DMIPD.cancel_order_copy]) + "张"
        except:
            db_value = "1张"
        finally:
            HandleMysql().close()
            logger.info(f"----db_value----:{db_value}")

        if value == db_value:
            return True
        else:
            return False

    def query_dialect_assert(self):
        logger.info("断言：设置项-查看页面语音方言，与数据库比对，返回True or False")
        value = self.get_element_text(loc.dialect, module="设置项-语音方言")
        logger.info(f"---value-----:{value}")

        try:
            db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_dialect_sql"), DMIPD.SN)[
                DMIPD.dialect]
        except:
            db_value = "普通话女声"
        else:
            if db_value == 0:
                db_value = "普通话男声"
            elif db_value == 1:
                db_value = "普通话女声"
            elif db_value == 2:
                db_value = "四川话"
            elif db_value == 3:
                db_value = "粤语"
        finally:
            HandleMysql().close()
            logger.info(f"----db_value----:{db_value}")

        if value == db_value:
            return True
        else:
            return False

    def query_voice_speed_assert(self):
        logger.info("断言：设置项-查看页面语音播报语速，与数据库比对，返回True or False")
        value = self.get_element_text(loc.voice_speed, module="设置项-语音播报语速")
        logger.info(f"---value-----:{value}")

        try:
            db_value = HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "query_voice_speed_sql"), DMIPD.SN)[
                DMIPD.voice_speed]
        except:
            db_value = "50%"
        else:
            if db_value == 20:
                db_value = "20%"
            elif db_value == 50:
                db_value = "50%"
            elif db_value == 80:
                db_value = "80%"
        finally:
            HandleMysql().close()
            logger.info(f"----db_value----:{db_value}")

        if value == db_value:
            return True
        else:
            return False
