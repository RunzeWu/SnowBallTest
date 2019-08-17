# -*- coding: utf-8 -*-
'''
 @Time:         2019-08-17
 @Author:       吴润泽 
'''
import pytest
import allure
from testdata.search_data import search_data
from common.mylog import get_logger

logger = get_logger('test_search')


@pytest.mark.usefixtures("start_app")
@pytest.mark.usefixtures("search_env")
@allure.feature("测试首页搜索框")
class TestLogin:

    @pytest.mark.parametrize("value", search_data)
    @allure.story("参数化，用例合一")
    def test_wrong_login(self, value, search_env):
        with allure.step("读取conftest中前后置条件"):
            search_page = search_env
        with allure.step("读取测试数据"):
            name = value["name"]
            expected = value["expected"]
        with allure.step("搜索相应的公司"):
            search_page.search(name=name)
        with allure.step("获得搜索结果"):
            res = search_page.get_result()

        try:
            with allure.step("断言"):
                assert expected == res
            logger.info("用例执行成功")
        except AssertionError as e:
            logger.error("用力执行失败")
            allure.attach(search_page.get_windows_img())
            raise e