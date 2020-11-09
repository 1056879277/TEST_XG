from selenium.webdriver.common.by import By
from page.base_page_2 import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
class LoginPage(BasePage):

    _login = "//XCUIElementTypeButton[@name=\"登录\"]"
    _login_password = "//XCUIElementTypeButton[@name=\"账号密码登录\"]"
    _login_verification = "//XCUIElementTypeButton[@name=\"验证码登录\"]"
    _login_password_1 = "//XCUIElementTypeButton[@name=\"以后\"]"


    usernameInput = "//XCUIElementTypeApplication[@name=\"咕咕机Pro\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTextField"
    passwordInput = "//XCUIElementTypeApplication[@name=\"咕咕机Pro\"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeSecureTextField"
    submitLogin = "//XCUIElementTypeButton[@name=\"登录\"]"



    #Success = "//XCUIElementTypeButton[@name=\"学习\"]"
    Success = "//XCUIElementTypeTabBar[@name=\"标签栏\"]"
    ErrM = "//XCUIElementTypeStaticText[@name=\"账号或密码错误，请重新输入\"]"
    ErrM_Limit = "//XCUIElementTypeStaticText[@name=\"今日错误次数已达上限，请尝试其他登录方式\"]"

    def Login_Password(self, username, password):
        self.find_element_and_click(self._login_password)
        self.find_element(self.usernameInput).clear()
        self.find_element(self.passwordInput).clear()
        self.find_element(self.usernameInput).send_keys(username)
        self.find_element(self.passwordInput).send_keys(password)

    def Login_Password_Success(self, username, password):
        self.Login_Password(username, password)
        self.find_element(self.submitLogin).click()
        self.find_element(self._login_password_1).click()
        return self.find_element(self.Success)

    def Login_Password_WithErr(self, username, password):
        self.Login_Password(username, password)
        self.find_element(self.submitLogin).click()
        return self.find_element(self.submitLogin)

    def Login_Password_WithErr_Limit(self, username, password):
        self.Login_Password(username, password)
        self.find_element(self.submitLogin).click()
        self.find_element(self.submitLogin).click()
        self.find_element(self.submitLogin).click()
        return self.find_element(self.submitLogin)

