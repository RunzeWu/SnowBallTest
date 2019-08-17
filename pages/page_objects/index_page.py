# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-17
 @Author:       吴润泽 
'''
from pages.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy


class IndexPage(BasePage):
    _profile_icon_loc = (MobileBy.ID, "com.xueqiu.android:id/user_profile_icon")
    _search_input_loc = (MobileBy.ID, "com.xueqiu.android:id/tv_search")
    _mobile_icon_loc = (MobileBy.ID, "com.xueqiu.android:id/rl_login_phone")
    _switch_log_with_pwd_loc = (MobileBy.ID, "com.xueqiu.android:id/tv_login_with_account")

    def go_to_login(self):
        self.click_element(self._profile_icon_loc)
        self.click_element(self._mobile_icon_loc)
        self.click_element(self._switch_log_with_pwd_loc)

    def click_search_input(self):
        return self.click_element(self._search_input_loc)
