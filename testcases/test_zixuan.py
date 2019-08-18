# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-18
 @Author:       吴润泽 
'''
import pytest
import allure
from common.mylog import get_logger

logger = get_logger('test_自选')


@pytest.mark.usefixtures("start_app")
@pytest.mark.usefixtures("zixuan_fixture")
@allure.feature("测试雪球app的加自选的几种情况")
class TestZixuan:

    def test_add_collection(self,zixuan_fixture):
        search_page, zixuan_page = zixuan_fixture
        with allure.step("点击加自选"):
            search_page.click_collet_btn()
        with allure.step("判断按钮状态"):
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





