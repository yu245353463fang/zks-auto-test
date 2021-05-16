from selenium import webdriver
from time import sleep
import unittest


class SeleniumOp(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://forum.zks.org/')
        #浏览器窗口最大化
        self.driver.maximize_window()

    def test_create_forum(self):
        login_button = self.driver.find_element_by_xpath("/html/body/section/div/div[1]/header/div/div/div[2]/span/button[2]/span")
        login_button.click()
        sleep(2)

        login_name_input = self.driver.find_element_by_xpath('//*[@id="login-account-name"]')
        login_name_input.send_keys('fangyulong@zks.org')
        sleep(2)

        login_password = self.driver.find_element_by_xpath('//*[@id="login-account-password"]')
        login_password.send_keys('qweQWE123..,,')
        sleep(2)

        login = self.driver.find_element_by_xpath('/html/body/section/div/div[5]/div/div/div/div[3]/div[1]/div[1]/div[2]/button[1]/span')
        login.click()
        sleep(2)

        create = self.driver.find_element_by_xpath('/html/body/section/div/div[3]/div[3]/div/section/div/button/span')
        create.click()
        self.driver.implicitly_wait(2)

        title = self.driver.find_element_by_xpath('//*[@id="reply-title"]')
        title.send_keys('ZKS to the moon!乌拉！')
        sleep(2)

        content = self.driver.find_element_by_xpath('//*[@id="ember237"]')
        content.send_keys('zkswap作为Layer2 赛道的先驱者，有责任和义务推动Layer2技术的发展，让交易更丝滑，让手续费更低廉！')
        self.driver.implicitly_wait(2)

    def tearDown(self) -> None:
        sleep(2)
        #self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SeleniumOp)
    unittest.TextTestRunner(verbosity=2).run(suite)

