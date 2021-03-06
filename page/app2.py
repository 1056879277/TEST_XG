import datetime

from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from page.main_page_2 import MainPage


class App:

    driver:WebDriver = None
    @classmethod
    def start(cls):
        ''''
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "seveniruby"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        #caps["udid"] = "emulator-5556"
        caps["chromedriverExecutable"]="/Users/seveniruby/projects/chromedriver/2.20/chromedriver"
        caps["showChromedriverLog"]=True
        '''
        caps = {}
        caps["platformName"] = "iOS"
        caps["automationName"] = "xcuitest"
        caps["platformVersion"] = "14"
        caps["deviceName"] = "Memobird’s iPhone X"
        caps["udid"] = "9455a847b82870755a5c0626f9d8e2d8af7d74eb"
        # caps["bundleId"] = "com.example.apple-testUICatalog"
        caps["bundleId"] = "cn.memobird.study"
        caps["xcodeOrgId"] = "yi_zhaochen@outlook.com"
        caps["xcodeSigningId"] = "iPhone Developer"

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        cls.driver.implicitly_wait(10)

        # sleep(20)
        # if len(self.driver.find_elements_by_id("image_cancel")) >=1:
        #     self.driver.find_element_by_id("image_cancel").click()
        #
        #



        # WebDriverWait(self.driver, 15).until(
        #     expected_conditions.visibility_of_element_located((By.ID, "image_cancel"))
        # )

        # def loaded(driver):
        #     print(datetime.datetime.now())
        #     if len(cls.driver.find_elements_by_id("image_cancel")) >=1:
        #         cls.driver.find_element_by_id("image_cancel").click()
        #         return True
        #     else:
        #         return False
        #
        # try:
        #     WebDriverWait(cls.driver, 20).until(loaded)
        # except:
        #     print("no update")
        return MainPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()