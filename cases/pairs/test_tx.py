import pytest
import allure
from cases.conftest import api_data
from common.logger import logger


@allure.step("步骤1 ==>> 获取所有币种信息")
def step_1():
    logger.info("步骤1 ==>> 获取所有币种信息")

@allure.severity(allure.severity_level.TRIVIAL)
@allure.epic("针对单个接口的测试")
@allure.feature("获取币种信息模块")
class TestTx:
    """获取用户信息模块"""

    @allure.story("用例--获取全部币种信息")
    @allure.description("该用例是针对获取所有币种信息接口的测试")
    @pytest.mark.single
    def test_tx_changepubkey(self, type, accountId, account, newPkHash, nonce, ethSignature ,signature, fastProcessing, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = (type, accountId, account, newPkHash, nonce, ethSignature ,signature, fastProcessing)
        step_1(type, accountId, account, newPkHash, nonce, ethSignature ,signature, fastProcessing)
        # assert result.success == except_result, result.error
        # assert result.response.status_code == 200
        # assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_tx.py"])