# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-17
 @Author:       吴润泽 
'''
import time

from pages.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy


class SearchPage(BasePage):

    _search_input_loc = (MobileBy.ID, "com.xueqiu.android:id/search_input_text")
    _mes_get_loc = (MobileBy.ID, "com.xueqiu.android:id/name") # 预计默认取第一个索引

    _add_collet_btns = (MobileBy.XPATH, "//*[contains(@resource-id, 'follow_btn')]")
    # _add_collet_btns = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("加自选")')

    _cancle_loc = (MobileBy.ID,"com.xueqiu.android:id/action_close")

    def search(self, name):
        return self.send_keys(self._search_input_loc,name)

    def get_result(self):
        return self.get_text(self._mes_get_loc)

    def click_first_result(self):
        return self.click_element(self._mes_get_loc)

    def click_collet_btn(self):
        self.hide_keyboard()
        time.sleep(2)
        return self.click_element(self._add_collet_btns)

    def is_added(self):
        ele = self.get_elements(self._add_collet_btns)
        if ele.text == "已添加":
            return True
        else:
            return False

    def click_cancle(self):
        return self.click_element(self._cancle_loc)