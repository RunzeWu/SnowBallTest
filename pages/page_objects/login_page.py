# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-17
 @Author:       吴润泽 
'''
from pages.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy


class LoginPage(BasePage):
    # _mobile_icon_loc = (MobileBy.ID, "com.xueqiu.android:id/rl_login_phone")
    # _switch_log_with_pwd_loc = (MobileBy.ID, "com.xueqiu.android:id/tv_login_with_account")
    _mobile_input_loc = (MobileBy.ID, "com.xueqiu.android:id/login_account")
    _pwd_input_loc = (MobileBy.ID, "com.xueqiu.android:id/login_password")
    _login_btn_loc = (MobileBy.ID, "com.xueqiu.android:id/button_next")
    _wrong_mobile_text_loc = (MobileBy.ID, "com.xueqiu.android:id/md_content")
    _confirm_loc = (MobileBy.ID, "com.xueqiu.android:id/md_buttonDefaultPositive")

    def login(self,mobile,pwd):
        self.input_text(self._mobile_input_loc, mobile)
        self.input_text(self._pwd_input_loc, pwd)
        self.click_element(self._login_btn_loc)

    def get_info(self):
        info = self.get_text(self._wrong_mobile_text_loc)
        self.click_element(self._confirm_loc)
        return info


