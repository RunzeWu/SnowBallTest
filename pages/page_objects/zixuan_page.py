# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-18
 @Author:       吴润泽 
'''
from pages.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy


class ZixuanPage(BasePage):
    _search_icon_loc = (MobileBy.ID, "com.xueqiu.android:id/action_search")
    _collet_loc = (MobileBy.ID,"com.xueqiu.android:id/portfolio_stockName")
    _delete_collet_loc = (MobileBy.XPATH, "//*[@text='删除']")

    def click_search_icon(self):
        return self.click_element(self._search_icon_loc)

    def long_press_collect(self):
        ele = self.get_element(self._collet_loc)
        self.long_press(ele, duration=2000)

    def get_collection_name(self):
        return self.get_attribute(self._collet_loc,"text")

    def click_delete(self):
        return self.click_element(self._delete_collet_loc)

    def is_toast_exits(self):
        msg = self.get_toast_msg("已从自选删除")
        if msg:
            return True
        else:
            return False


