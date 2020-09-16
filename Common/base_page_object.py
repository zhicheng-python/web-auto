# encoding:utf-8
# author:wangzhicheng
# time:2020/5/26 14:57
# file:base_page_object.py



import datetime, time
from Common.mylogger import logger
from Common.handle_path import do_path
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePageObject:
    """页面基础动作，点击，截图，等待..."""

    def __init__(self, driver: WebDriver):
        self.driver = driver  # 引入WebDriver的目的是，后面保证所有操作都是在同一个driver下，会传入一个driver，这里可以让driver.（点）时候弹出它的方法

    # 截图
    def screen_shots(self, module, path=do_path.screen_shots_path):
        """
        :param module:  页面+页面操作行为
        :param path:  图片保存路径
        :return: 无
        """
        time = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d%H%M%S")
        # 图片命名格式： 时间_页面_页面操作行为.png
        picture_name = f"{time}_{module}.png"
        # 图片绝对路径
        file_path = path + "\\" + picture_name

        logger.info("...开始截图...")
        try:
            self.driver.save_screenshot(file_path)
        except:
            logger.exception("...截图失败...")
            raise
        else:
            logger.info(f"...截图成功...图片保存路径为：{file_path}")

    # 等待元素可见
    def wait_element_visible(self, loc, module, timeout=20, poll_frequency=0.5):
        """
        :param loc:  元素定位
        :param module: 页面+页面操作行为
        :param timeout: 超时时限
        :param poll_frequency: 轮询时间
        :return: 无
        """
        logger.info(f"等待元素{loc}可见...")
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))
        except:
            logger.exception("等待元素可见失败...")
            # 出错后截图
            self.screen_shots(module)
            raise

    # 等待元素存在
    def wait_element_presence(self, loc, module, timeout=20, poll_frequency=0.5):
        """
          :param loc:  元素定位
          :param module: 页面+页面操作行为
          :param timeout: 超时时限
          :param poll_frequency: 轮询时间
          :return: 无
          """
        logger.info(f"等待元素{loc}存在...")
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(loc))
        except:
            logger.exception("等待元素存在失败...")
            # 出错后截图
            self.screen_shots(module)
            raise


    #判断元素是否不存在
    def wait_element_invisibility(self,loc,module,timeout=20,poll_frequency=0.5):
        """
          :param loc:  元素定位
          :param module: 页面+页面操作行为
          :param timeout: 超时时限
          :param poll_frequency: 轮询时间
          :return: 无
          """
        logger.info(f"判断元素是否不存在")
        try:
            WebDriverWait(self.driver,timeout,poll_frequency).until(EC.invisibility_of_element_located(loc))
        except:
            logger.exception(f"{loc}元素存在")
            self.screen_shots(module)
            raise


    # 获取元素
    def get_element(self, loc, module, timeout=20, poll_frequency=0.5):
        """
        :param loc:  元素定位
        :param module: 页面+页面操作行为
        :param timeout: 超时时限
        :param poll_frequency: 轮询时间
        :return: 元素
        """
        logger.info(f"{module}→→→开始获取元素:{loc}")
        try:
            ele = self.driver.find_element(*loc)
        except:
            logger.exception("元素获取失败...")
            # 出错后截图
            self.screen_shots(module)
            raise
        else:
            return ele

    # 输入文本信息
    def input_text(self, loc, module, text, timeout=20, poll_frequency=0.5):
        """
        :param loc: 元素定位
        :param module: 页面+页面操作行为
        :param text: 输入的文本
        :param timeout: 超时时限
        :param poll_frequency: 轮询时间
        :return: 无
        """
        # 1.等待元素可见
        # 2.获取该元素
        # 3.输入文本信息
        self.wait_element_visible(loc, module, timeout, poll_frequency)
        ele = self.get_element(loc, module, timeout, poll_frequency)

        logger.info(f"{module}→→→开始输入文本信息：{text}")
        try:
            ele.send_keys(text)
        except:
            logger.exception("文本信息输入失败...")
            # 出错后截图
            self.screen_shots(module)
            raise

    # 点击元素
    def click_element(self, loc, module, timeout=20, poll_frequency=0.5):
        """
        :param loc:  元素定位
        :param module: 页面+页面操作行为
        :param timeout: 超时时限
        :param poll_frequency: 轮询时间
        :return: 元素
        """

        # 1.等待元素可见
        # 2.获取该元素
        # 3.点击元素
        self.wait_element_visible(loc, module, timeout, poll_frequency)
        ele = self.get_element(loc, module, timeout, poll_frequency)

        logger.info(f"{module}→→→开始点击元素：{loc}")
        try:
            ele.click()
        except:
            logger.exception("点击元素失败...")
            # 出错后截图
            self.screen_shots(module)
            raise

    # 获取元素文本信息
    def get_element_text(self, loc, module, timeout=20, poll_frequency=0.5):
        """
        :param loc:  元素定位
        :param module: 页面+页面操作行为
        :param timeout: 超时时限
        :param poll_frequency: 轮询时间
        :return: 文本信息
        """

        # 1.等待元素可见
        # 2.获取该元素
        # 3.获取该元素文本信息

        self.wait_element_visible(loc, module, timeout, poll_frequency)
        ele = self.get_element(loc, module, timeout, poll_frequency)

        # 有的元素有时候获取不到文本，等待一秒后获取
        time.sleep(1)

        logger.info(f"{module}→→→获取元素文本信息：{loc}")
        try:
            text = ele.text
        except:
            logger.exception("元素文本信息获取失败...")
            # 出错后截图
            self.screen_shots(module)
            raise
        else:
            return text

    # 获取元素属性值
    def get_element_attribute(self, loc, module, attribute_name, timeout=20, poll_frequency=0.5):
        """
        :param loc: 元素定位
        :param module: 页面+页面操作行为
        :param attribute_name: 元素属性名称
        :param timeout: 超时时限
        :param poll_frequency: 轮询时间
        :return: 无
        """

        # 1.等待元素可见
        # 2.获取该元素
        # 3.获取元素属性值

        self.wait_element_visible(loc, module, timeout, poll_frequency)
        ele = self.get_element(loc, module, timeout, poll_frequency)

        logger.info(f"{module}→→→获取元素属性值：{loc}")
        try:
            attribute_text = ele.get_attribute(attribute_name)
        except:
            logger.exception("元素属性值获取失败...")
            # 出错后截图
            self.screen_shots(module)
            raise
        else:
            return attribute_text

    # 键盘事件
    def click_keyboard(self, loc, module, text, timeout=20, poll_frequency=0.5):
        """
        :param loc:
        :param module:
        :param timeout:
        :param poll_frequency:
        :return:
        """
        # 1.等待元素可见
        # 2.获取该元素
        # 3.键盘操作
        self.wait_element_visible(loc, module, timeout, poll_frequency)
        ele = self.get_element(loc, module, timeout, poll_frequency)
        logger.info(f"键盘操作：{text}")
        try:
            if len(text) == 1:
                ele.send_keys(text)
            else:
                ele.send_keys(text[0], text[1])
        except:
            logger.Exception("键盘操作失败...")
            raise
