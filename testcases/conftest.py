'''
 @Time:         2019-08-17
 @Author:       吴润泽
'''
import pytest
from appium import webdriver
from desired_caps.get_desired_caps import desired_caps
from pages.page_objects.search_page import SearchPage
from pages.page_objects.index_page import IndexPage
from pages.page_objects.login_page import LoginPage
from pages.page_objects.zixuan_page import ZixuanPage
from common.mylog import get_logger

logger = get_logger("conftest")


# 根据测试用例需求，动态配置启动参数。
def basedriver(noReset=None, port=4723, **kwargs):
    if noReset is not None:
        desired_caps["noReset"] = noReset
    if kwargs:
        # 修改从配置文件当中读取出来的desired_caps.
        for key, value in kwargs:
            desired_caps[key] = value
    # 启动appium会话 - 连接appium server  端口号
    driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(port), desired_caps)
    return driver


@pytest.fixture(scope="class")
def start_app():
    driver = basedriver(noReset=True)
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def login_env(start_app):
    # 启动App后检查登录，已登录退出登录
    driver = start_app
    index_page = IndexPage(driver=driver)
    index_page.go_to_login()
    login_page = LoginPage(driver=driver)
    yield login_page
    driver.close_app()


@pytest.fixture(scope="class")
def search_env(start_app):
    driver = start_app
    index_page = IndexPage(driver=driver)
    search_page = SearchPage(driver=driver)
    index_page.click_search_input()
    yield search_page
    driver.close_app()


# @pytest.fixture(scope="class")
# def zixuan_fixture():
#     driver = basedriver(noReset=True)
#     index_page = IndexPage(driver=driver)
#     search_page = SearchPage(driver=driver)
#     zixuan_page = ZixuanPage(driver = driver)
#     index_page.click_zixuan()
#     zixuan_page.click_search_icon()
#     search_page.search("alibaba")
#     search_page.click_first_result()
#     # search_page.click_collet_btn()
#     yield search_page, zixuan_page
#     # driver.close_app()
#     # driver.quit()