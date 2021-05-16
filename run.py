import pytest
import os


if __name__ == '__main__':
    # pytest.main(['-s','./cases/test_price1.py','--alluredir','./allure-results',])
    pytest.main(['-s', './cases/test_price1.py', '--alluredir', './allure-results' ,' -c ./reports'])
    os.system('allure generate ./allure-results  -o ./reports  -c ./reports' )
    # os.system('allure serve./reports/html')



