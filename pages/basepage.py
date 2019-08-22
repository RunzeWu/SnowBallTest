'''
 @Time:         2019-08-17
 @Author:       吴润泽
'''
import time
import allure
from appium.webdriver import WebElement
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import contants
from common.contants import screenshot_dir
from common.mylog import get_logger
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium import webdriver

logger = get_logger("basepage")


class BasePage:

    def __init__(self, driver: webdriver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, locator, timeout=30, poll_frequency=0.5, model_name="model") -> WebElement:
        logger.info("等待元素可见：{}".format(locator))
        try:
            wait_start_time = time.time()
            ele = WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 获取结束等待的时间
            wait_end_time = time.time()
            # 获取等待的总时长 - 以秒为单位
            wait_time = wait_end_time - wait_start_time
            logger.info("元素已可见。等待元素可见总时长:{}".format(wait_time))
            return ele
        except:
            # 写进日志
            logger.exception("等待元素可见超时。")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    def wait_elesVisible(self, locator, timeout=30, poll_frequency=0.5, model_name="model") -> WebElement:
        logger.info("等待元素可见：{}".format(locator))
        try:
            wait_start_time = time.time()
            ele = WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_any_elements_located(locator))
            # 获取结束等待的时间
            wait_end_time = time.time()
            # 获取等待的总时长 - 以秒为单位
            wait_time = wait_end_time - wait_start_time
            logger.info("元素已可见。等待元素可见总时长:{}".format(wait_time))
            return ele
        except:
            # 写进日志
            logger.exception("等待元素可见超时。")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    # 查找元素
    def get_element(self, locator, model_name="model") -> WebElement:
        logger.info("查找模块：{}下的元素：{}".format(model_name, locator))
        try:
            ele = self.driver.find_element(*locator)
            logger.info("查找到元素成功")
            return ele
        except:
            # 写进日志
            logger.exception("查找元素失败。")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    def get_elements(self, locator, model_name="model"):
        logger.info("查找模块：{}下的元素：{}".format(model_name, locator))
        try:
            ele = self.driver.find_elements(*locator)
            logger.info("查找到元素成功")
            return ele
        except:
            # 写进日志
            logger.exception("查找元素失败。")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    # 点击元素
    def click_element(self, locator, model_name="model"):
        # 元素查找
        ele = self.wait_eleVisible(locator, model_name=model_name)
        # 元素操作
        logger.info("点击操作：模块 {} 下的元素 {}".format(model_name, locator))
        try:
            ele.click()
        except:
            # 写进日志
            logger.exception("点击元素操作失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    def click_first_of_elements(self, locator, model_name="model"):
        # 元素查找
        ele = self.wait_elesVisible(locator, model_name=model_name)[0]
        # 元素操作
        logger.info("点击操作：模块 {} 下的元素 {}".format(model_name, locator))
        try:
            ele.click()
        except:
            # 写进日志
            logger.exception("点击元素操作失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    # 输入内容
    def input_text(self, locator, value, model_name="model"):
        # 元素查找
        ele = self.get_element(locator, model_name)
        # 元素操作
        logger.info("输入操作：模块 {} 下的元素 {}输入文本 {}".format(model_name, locator, value))
        try:
            ele.clear()
            ele.send_keys(value)
        except:
            # 写进日志
            logger.exception("元素输入操作失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    def clear_input(self, locator, model_name):
        ele = self.get_element(locator, model_name="model")
        return ele.clear()

    # 获取元素的属性
    def get_element_attribute(self, locator, attr, model_name="model"):
        # 元素查找
        ele = self.get_element(locator, model_name)
        # 元素操作
        logger.info("获取元素属性：模块 {} 下的元素 {} 的属性 {}".format(model_name, locator, attr))
        try:
            return ele.get_attribute(attr)
        except:
            # 写进日志
            logger.exception("获取元素属性失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    # 获取元素的文本内容
    def get_element_text(self, locator, model_name="model"):
        # 元素查找
        ele = self.get_element(locator, model_name)
        # 元素操作
        logger.info("获取元素文本值：模块 {} 下的元素 {}".format(model_name, locator))
        try:
            return ele.text
        except:
            # 写进日志
            logger.exception("获取元素文本值失败：")
            # 截图 - 直接通过图片名称就知道截的是什么图。
            self.save_webImg(model_name)
            raise

    def save_webImg(self, model_name):
        # 文件名称=模块名称_当前时间.png
        filePath = screenshot_dir + "/{0}_{1}.png".format(model_name,
                                                          time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        try:
            self.driver.save_screenshot(filePath)
            logger.info("截图成功，文件路径为：{}".format(filePath))
        except Exception as e:
            logger.exception("截图失败！！")
            raise e

    # 获取设备大小
    def get_device_size(self):
        try:
            return self.driver.get_window_size()
        except Exception as e:
            logger.error("获取设备大小失败！")
            raise e

    # 滑屏操作 - 左右、上下
    # 左右,默认向左
    def swipe_left_right(self, start_per=0.9, end_per=0.1):
        size = self.get_device_size()
        self.driver.swipe(size["width"] * start_per, size["height"] * 0.5, size["width"] * end_per,
                          size["height"] * 0.5, 200)
        time.sleep(0.5)

    # 上下滑动，默认向上滑
    def swipe_up_down(self, start_per=0.9, end_per=0.1):
        size = self.get_device_size()
        self.driver.swipe(size["width"] * 0.5, size["height"] * start_per, size["width"] * 0.5,
                          size["height"] * end_per, 200)
        time.sleep(0.5)

    # 列表滑动到底部
    def scroll_list_to_bottom(self):
        new = self.driver.page_source
        old = ''
        while old != new:
            old = new
            self.swipe_up_down()
            new = self.driver.page_source

    def scroll_list_to_top(self):
        new = self.driver.page_source
        old = ''
        while old != new:
            old = new
            self.swipe_up_down(start_per=0.1, end_per=0.9)
            new = self.driver.page_source

    # 翻页查找某个字符串
    def scroll_find(self, str):
        new = self.driver.page_source
        old = ''

        while old != new:
            old = new
            self.swipe_up_down()
            new = self.driver.page_source
            if new.find(str):
                locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("{}")'.format(str))
                return self.wait_eleVisible(locator)
                # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR,
                #                                                                   'new UiSelector().text("逻辑思维题")')))
                # driver.find_element_by_android_uiautomator('new UiSelector().text("逻辑思维题")').click()

    # toast获取
    def get_toast_msg(self, text):
        # xpath表达式 -- 文本匹配去获取
        ele_loc = '//*[contains(@text,"{}")]'.format(text)
        # uiautomator2
        # 等待元素存在，而不是元素可见。
        WebDriverWait(self.driver, 10, 0.01).until(EC.presence_of_element_located((MobileBy.XPATH, ele_loc)))
        text = self.get_element((MobileBy.XPATH, ele_loc)).text
        WebDriverWait(self.driver, 10, 0.01).until(EC.invisibility_of_element((MobileBy.XPATH, ele_loc)))
        return text

    # h5切换
    def switch_to_H5(self, h5_name, model_name="model"):
        try:
            self.driver.switch_to.context(h5_name)
            current = self.driver.current_context
            logger.info("切换H5页面成功，h5：{}".format(current))
        except Exception as e:
            logger.error("切换失败")
            self.save_webImg(model_name)

    def switch_to_native(self, model_name="model"):
        try:
            self.driver.switch_to.default_content()
            logger.info("切换原生页面成功")
        except Exception as e:
            logger.error("切换原生页面失败")
            self.save_webImg(model_name)

    # appium 封装了 关于键盘的操作
    def hide_keyboard(self):
        self.driver.hide_keyboard()

    def long_press(self, locator, duration=1000):
        ta = TouchAction(self.driver)
        ta.long_press(locator, duration=duration).perform()

    def tab_srceen(self, ele=None):
        ta = TouchAction(self.driver)
        ta.tap(element=ele).perform()

        '''
        以上为appium原生操作，以下为H5页面操作
        '''

    def get_visible_element(self, locator, eqc=20) -> WebElement:
        '''
        定位元素，参数locator为元祖类型
        :param locator:
        :param eqc:
        :return:
        '''
        try:
            ele = WebDriverWait(self.driver, timeout=eqc).until(
                EC.visibility_of_element_located(locator))
            logger.info('获取{}元素成功'.format(locator))
            return ele
        except:
            logger.error("相对时间内没有定位到{}元素".format(locator))
            allure.attach(self.get_windows_img())

    def get_presence_element(self, locator, eqc=10):
        """
        定位一组元素
        :param locator:
        :param eqc:
        :return:
        """
        try:
            ele = WebDriverWait(self.driver, timeout=eqc).until(
                EC.presence_of_element_located(locator))
            logger.info('获取{}元素成功'.format(locator))
            return ele
        except:
            logger.error("相对时间内没有定位到{}元素".format(locator))
            allure.attach(self.get_windows_img())

    def get_clickable_element(self, locator, eqc=20):
        try:
            ele = WebDriverWait(self.driver, timeout=eqc).until(
                EC.element_to_be_clickable(locator))
            logger.info('获取{}元素成功'.format(locator))
            return ele
        except:
            logger.error("相对时间内没有定位到{}元素".format(locator))
            allure.attach(self.get_windows_img())

    def send_keys(self, locator, text):
        '''
        发送文本，清空后输入
        locator = ('id','xxx')
        element.send_keys(locator,text)
        '''

        element = self.get_visible_element(locator)
        element.clear()
        element.send_keys(text)
        logger.info('SendKeys %s in %s success.' % (text, locator))

    def is_text_in_element(self, locator, text, timeout=10):
        '''
        判断文本在元素里，没有元素返回false打印日志，定位到返回判断结果的布尔值
        result = driver.text_in_element(locator,text)
        '''

        try:
            result = WebDriverWait(
                self.driver, timeout, 1
            ).until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            logger.info('No location to the element.')
            allure.attach(self.get_windows_img())
            return False
        else:
            return result

    def is_text_in_value(self, locator, value, timeout=10):
        '''
        判断元素的value值，没定位到元素返回false，定位到返回判断结果布尔值
        result = dirver.text_to_be_present_in_element_value(locator,text)
        '''

        try:
            result = WebDriverWait(
                self.driver, timeout, 1
            ).until(EC.text_to_be_present_in_element_value(locator, value))
        except TimeoutException:
            logger.info('No location to the element.')
            allure.attach(self.get_windows_img())
            return False
        else:
            return result

    def is_title(self, title, timeout=10):
        '''
        判断元素的title是否完全等于
        '''

        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.title_is(title))
        return result

    def is_title_contains(self, title, timeout=10):
        '''
        判断元素的title是否包含
        '''

        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.title_contains(title))
        return result

    def is_selected(self, locator, timeout=10):
        '''
        判断元素是否被选中
        '''

        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.element_located_to_be_selected(locator))
        return result

    def is_selected_be(self, locator, selected=True, timeout=10):
        '''
        判断元素的状态是不是符合期望的状态，selected是期望的状态
        '''

        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.element_located_selection_state_to_be(locator, selected))
        return result

    def is_alert_present(self, timeout=10):
        '''
        判断页面是否有alert,有的话返回alert，没有返回False
        '''

        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.alert_is_present())
        return result

    def is_visibility(self, locator, timeout=10):
        '''
        元素可见，返回本身，不可见返回False
        '''

        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.visibility_of_element_located(locator))
        return result

    def is_invisibility(self, locator, timeout=10):
        '''
        元素可见返回本身，不可见返回Ture,没有找到元素也返回Ture
        '''

        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.invisibility_of_element_located(locator))
        return result

    def is_clickable(self, locator, timeout=10):
        '''
        元素可以点击is_enabled返回本身，不可点击返回False
        '''

        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.element_to_be_clickable(locator))
        return result

    def is_located(self, locator, timeout=10):
        '''
        判断元素有没有被定位到(并不意味着可见),定位到返回element，没有定位到返回False
        '''

        result = WebDriverWait(
            self.driver, timeout, 1
        ).until(EC.presence_of_all_elements_located(locator))
        return result

    def move_to_element(self, locator):
        '''
        鼠标悬停操作
        locator=('id','xxx')
        driver.move_to_element(locator)
        '''

        element = self.get_visible_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()
        # logger.info('ActionChins move to %s' % locator)

    def back(self):
        self.driver.back()

        logger.info('back driver!')

    def forward(self):
        self.driver.forward()

        logger.info('forward driver!')

    def close(self):
        self.driver.close()

        logger.info('close driver!')

    def refresh(self):
        return self.driver.refresh()

    def get_title(self):
        '''
        获取title
        '''

        logger.info('git dirver title.')
        return self.driver.title()

    def get_text(self, locator):
        '''
        获取文本
        '''

        element = self.get_visible_element(locator)
        # logger.info('get text in %s' % locator)
        text = element.text
        return text

    def get_attribute(self, locator, name):
        '''
        获取属性
        '''

        element = self.get_visible_element(locator)
        logger.info('get attribute in %s' % str(locator))
        return element.get_attribute(name)

    def js_execute(self, js):
        '''
        执行js
        '''

        try:
            logger.info('Execute js.%s' % js)
            return self.driver.execute_script(js)
        except:
            allure.attach(self.get_windows_img())
            logger.info('failed to excute js')

    def js_focus_element(self, locator):
        '''
        聚焦元素
        '''

        target = self.get_visible_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''
        滚动到顶部
        '''

        js = 'window.scrollTo(0,0)'
        self.js_execute(js)
        logger.info('Roll to the top!')

    def js_scroll_end(self):
        '''
        滚动到底部
        '''

        js = "window.scrollTo(0,document.body.scrollHight)"
        self.js_execute(js)
        logger.info('Roll to the end!')

    def get_windows_img(self):
        try:
            file_name = contants.screenshot_img
            self.driver.get_screenshot_as_file(file_name)
            logger.info('Had take screenshot and save to folder:output/screenshots')
        except NameError as e:
            logger.info('Failed to take the screenshot!%s' % e)
            self.get_windows_img()
        return file_name

    def switch_window(self, name=None, fqc=20):
        """
        切换窗口，有name切换至该name的窗口，没有则切换最新
        :param name:
        :param fqc:
        :return:
        """
        if name is None:
            current_handle = self.driver.current_window_handle
            WebDriverWait(self.driver, fqc).until(EC.new_window_is_opened(current_handle))
            handles = self.driver.window_handles
            return self.driver.switch_to.window(handles[-1])
        return self.driver.switch_to.window()
