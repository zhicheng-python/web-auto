#encoding:utf-8
#author:wangzhicheng
#time:2020/5/28 14:46
#file:home_page_asserts.py

from Common.mylogger import logger
from Common.base_page_object import BasePageObject as BPO
from PageLocations.home_page_locations import HomePageLocations as loc


#这个分层是从操作过程中分离出来的，需要导入的部分其他内容和Objects文件夹下一致


class HomePageAsserts(BPO):
    """主界面操作-断言用"""

    #主界面账户元素是否可见，  return ：True or  False

    def account_isvisible(self):
        logger.info("断言：主界面账户元素是否可见")

        try:
            self.wait_element_visible(loc.account_element,module="主界面_等待账户元素可见")
        except:
            return False
        else:
            return True


    #主界面iot设备管理元素是否可见：

    def iot_device_manage_isvisible(self):
        logger.info("断言：主界面iot设备管理元素是否可见")

        try:
            self.wait_element_visible(loc.iot_device_manage,module="主界面_等待iot设备管理元素可见")
        except:
            return False
        else:
            return True






