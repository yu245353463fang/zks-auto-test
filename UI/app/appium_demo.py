from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
import unittest
from time import sleep


class AppiumOp(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor = 'http://localhost:4723/wd/hub',
            desired_capabilities = {
              'platformName': 'Android', # 被测手机是安卓
              'platformVersion': '10', # 手机安卓版本
              'deviceName': 'xxx', # 设备名，安卓手机可以随意填写
              'appPackage': 'tv.danmaku.bili', # 启动APP Package名称
              'appActivity': '.ui.splash.SplashActivity', # 启动Activity名称
              'unicodeKeyboard': False, # 使用自带输入法，输入中文时填True
              'resetKeyboard': True, # 执行完程序恢复原来输入法
              'noReset': True,       # 不要重置App
              'newCommandTimeout': 7000,
              'automationName' : 'UiAutomator2'
              # 'app': r'd:\apk\bili.apk',
            }
            )
        self.driver.implicitly_wait(6)

    def test_find_zkswap(self):
        # 如果有`青少年保护`界面，点击`我知道了`
        # Iknow = self.driver.find_elements_by_id("text3")
        # if Iknow:
        #     Iknow.click()

        # 根据id定位搜索位置框，点击
        self.driver.find_element_by_id("expand_search").click()

        # 根据id定位搜索输入框，点击
        sbox = self.driver.find_element_by_id('search_src_text')
        sbox.send_keys('zkswap')

        # 输入回车键，确定搜索
        self.driver.press_keycode(AndroidKey.ENTER)

        # 选择（定位）所有视频标题
        eles = self.driver.find_elements_by_id("title")
        for ele in eles:
            # 打印标题
            print(ele.text)

    def tearDown(self) -> None:
        sleep(1)
        #input('**** Press to quit..')
        #self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AppiumOp)
    unittest.TextTestRunner(verbosity=2).run(suite)