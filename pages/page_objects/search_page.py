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

    def search(self, name):
        return self.send_keys(self._search_input_loc,name)

    def get_result(self):
        return self.get_text(self._mes_get_loc)