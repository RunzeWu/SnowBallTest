'''
 @Time:         2019-08-17
 @Author:       吴润泽
'''
import pytest
import allure
from testdata.login_data import wrong_login
from common.mylog import get_logger

logger = get_logger('test_login')


@pytest.mark.usefixtures("start_app")
@pytest.mark.usefixtures("login_env")
@pytest.mark.run
@allure.feature("测试雪球app的两种异常登录情况")
class TestLogin:

    @allure.story("参数化，将两种异常情况放在一个用例")
    @pytest.mark.parametrize("value", wrong_login)
    def test_wrong_login(self, value, login_env):
        with allure.step("从文件中读取测试数据"):
            mobile = value['mobile']
            pwd = value['pwd']
            msg = value['expected']

        with allure.step("执行conftest中前后置条件"):
            login_page = login_env

        with allure.step("输入用户名密码"):
            login_page.login(mobile, pwd)

        with allure.step("获取报错信息"):
            actual = login_page.get_info()

        try:
            with allure.step("比较断言结果"):
                assert msg == actual
            logger.info('获取info:{}成功'.format(actual))
        except AssertionError as e:
            logger.error('Failed, 没有获取到toast')
            allure.attach(login_page.get_windows_img())
            raise e


if __name__ == '__main__':
    pytest.main()