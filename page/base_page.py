from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from appium import webdriver

class BasePage:
    _logout_1 = "//XCUIElementTypeButton[@name=\"我的\"]"   #点击我的
    _logout_2 = "(//XCUIElementTypeButton[@name=\"appSetting\"])[1]"
    _logout_3 = "//XCUIElementTypeButton[@name=\"退出\"]"

    _black_list = [
        ("//XCUIElementTypeButton[@name=\"以后\"]"),
        ("//XCUIElementTypeButton[@name=\"ico close unchecked\"]")

    ]
    def __init__(self, driver:WebDriver):
        self.driver = driver
        print("222222222")

    def find_element(self, *locator):
        try:
            print(locator)
            print("11111")
            return self.driver.find_element_by_xpath(*locator)
        except:
            print("异常处理")
            self.handle_exception()
            # self.find_element(locator)
            return self.find_element()

    def find_element_and_click(self, *locator):
        print("click")
        print(locator)
        try:
            #如果click也有异常，可以这样处理
            return self.driver.find_element_by_xpath(*locator).click()
        except:
            self.handle_exception()
            #return self.driver.find_element_by_xpath(*locator).click()
            return self.find_element_and_click()
    def handle_exception(self):
        print(":exception")
        self.driver.implicitly_wait(10)
        for locator in range(len(self._black_list)):
            print(locator)
            print(locator, self._black_list[locator])
            str_locator = self._black_list[locator]
            elements = self.driver.find_element_by_xpath(*str_locator)

            if len(elements) >= 1:
                #todo: 不是所有的弹框处理都是要点击弹框，可根据业务需要自行封装
                print("找到元素")
                elements[0].click()
            else:
                print("%s not found" % str(locator))

            #todo: 私用page source会更快的定位

            # page_source=self.driver.page_source
            # if "image_cancel" in page_source:
            #     self.driver.find_element(*locator).click()
            # elif "tips" in page_source:
            #     pass
        print("异常结束")
        self.driver.implicitly_wait(10)

    def Log_out(self):
         self.find_element(self._logout_1)


        #self.find_element_and_click(self._logout_2)
        #self.find_element_and_click(self._logout_3)