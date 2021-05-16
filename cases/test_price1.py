import pytest
import allure
import os
from common.logger import logger
from common.read_data import data


BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]

@allure.feature('api_test')
@allure.story('验证获取币种价格')
class TestTokenPrice(object):
    @allure.feature('获取币种价格')
    @allure.story('获取成功')
    def test_get_price_success(self):
        return self
        logger.info("********** 开始执行用例 **************")
        assert 1 == 1


    @allure.feature('币种信息错误')
    @allure.story('获取不到币种信息')
    def test_get_price_fail(self):
        return self
        logger.info("********** 用例执行结束 **************")
        assert 4 == 3



if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_price1.py"])