import pytest
import allure
from cases.conftest import api_data
from common.logger import logger
from api.price import Price


@allure.step("步骤1 ==>> 获取所有币种信息")
def step_1():
    logger.info("步骤1 ==>> 获取所有币种信息")

@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("获取币种信息模块")

class TestGetToken_Price():
    @allure.story("用例--获取全部币种信息")
    @allure.description("该用例是针对获取所有币种信息接口的测试")
    # @pytest.mark.parametrize("except_result, except_code, except_msg",
    #                          api_data["test_get_token_price"])
    # @allure.title(
    #     "测试数据：【 {username}，{password}，{telephone}，{sex}，{address}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    def test_price(self, res):
        logger.info("*************** 开始执行用例 ***************")
        res = Price.list_price()
        assert res.success == True


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_price.py"])