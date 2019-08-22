# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-18
 @Author:       吴润泽 
'''
import pytest
import allure
from common.mylog import get_logger
from appium import webdriver
from desired_caps.get_desired_caps import desired_caps
from pages.page_objects.search_page import SearchPage
from pages.page_objects.zixuan_page import ZixuanPage
from pages.page_objects.index_page import IndexPage

logger = get_logger('test_自选')


@allure.feature("测试雪球app的加自选的几种情况")
@pytest.mark.zixuan
class TestZixuan:

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def teardown_class(self):
        self.driver.close_app()
        self.driver.quit()

    def test_add_collection(self):
        driver = self.driver
        with allure.step("前提步骤"):
            index_page = IndexPage(driver=driver)
            search_page = SearchPage(driver=driver)
            zixuan_page = ZixuanPage(driver=driver)
            index_page.click_zixuan()
            zixuan_page.click_search_icon()
            search_page.search("alibaba")
            search_page.click_first_result()
        with allure.step("点击加自选"):
            logger.info("点击加自选")
            search_page.click_collet_btn()
        with allure.step("断言toast"):
            assert search_page.is_add_toast() is True
        with allure.step("断言按钮状态"):
            flag = search_page.is_added()
        try:
            with allure.step("如果状态为真则初步判断加自选成功"):
                assert flag is True
        except AssertionError as e:
            logger.error("用例执行失败")
            allure.attach(search_page.get_windows_img())
            raise e

        with allure.step("返回自选页"):
            search_page.click_cancle()

        with allure.step("获取当前收藏名"):
            name = zixuan_page.get_collection_name()

        try:
            with allure.step("获取当前收藏名"):
                assert name == "阿里巴巴"
                logger.info("用例执行成功")
        except AssertionError as e:
            logger.error("用例执行失败")
            allure.attach(search_page.get_windows_img())
            raise e

    def test_delete_collection(self):
        driver = self.driver
        with allure.step("前提步骤"):
            search_page = SearchPage(driver=driver)
            zixuan_page = ZixuanPage(driver=driver)
            zixuan_page.long_press_collect()
            zixuan_page.click_delete()
            zixuan_page.click_search_icon()
            search_page.search("alibaba")
            search_page.click_first_result()

        with allure.step("断言按钮状态"):
            flag = search_page.is_deleted()
        try:
            with allure.step("如果状态为真则初步判断删除成功"):
                assert flag is True
        except AssertionError as e:
            logger.error("用例执行失败")
            allure.attach(search_page.get_windows_img())
            raise e