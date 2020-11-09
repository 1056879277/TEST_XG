from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from appium import webdriver
from page.base_page import BasePage
from page.search_page import SearchPage
from page.Login_page import LoginPage


class MainPage(BasePage):
    _search_locator = (By.ID, "com.xueqiu.android:id/home_search")
    _login = "//XCUIElementTypeButton[@name=\"登录\"]"


    def to_search(self):
        #todo: too slow
        self.find_element_and_click(self._search_locator)
        return SearchPage(self.driver)

    def to_Login(self):
            print("to_login1")
            self.find_element(self._login)
            return LoginPage(self.driver)

