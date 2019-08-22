# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-17
 @Author:       吴润泽 
'''

from pages.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy


class SearchPage(BasePage):

    _search_input_loc = (MobileBy.ID, "com.xueqiu.android:id/search_input_text")
    _mes_get_loc = (MobileBy.ID, "com.xueqiu.android:id/name") # 预计默认取第一个索引

    _follow_btns = (MobileBy.ID, "com.xueqiu.android:id/follow_btn")
    _followed_btns = (MobileBy.ID, "com.xueqiu.android:id/followed_btn")
    # _add_collet_btns = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("加自选")')

    _cancle_loc = (MobileBy.ID,"com.xueqiu.android:id/action_close")

    def search(self, name):
        return self.send_keys(self._search_input_loc,name)

    def get_result(self):
        return self.get_text(self._mes_get_loc)

    def click_first_result(self):
        return self.click_element(self._mes_get_loc)

    def click_collet_btn(self):
        return self.click_first_of_elements(self._follow_btns)

    def is_added(self):
        text = self.get_element_text(self._followed_btns)
        if text == "已添加":
            return True
        else:
            return False

    def is_deleted(self):
        text = self.wait_elesVisible(self._follow_btns, model_name="test")[0].text
        if text == "加自选":
            return True
        else:
            return False

    def click_cancle(self):
        return self.click_element(self._cancle_loc)

    def is_add_toast(self):
        msg = self.get_toast_msg("添加成功")
        if msg:

            return True
        else:
            return False
