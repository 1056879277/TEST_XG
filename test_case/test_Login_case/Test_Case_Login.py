from page.app import App
from page.Login_page import LoginPage
import pytest
from time import sleep
class Test_Case_Login:

    def setup(self):

        self.login_page_setup = App.start().to_Login()
        #App.start().to_login()

    # ("密码错误登录")
    def test_Login_Password_WithErr(self):
        username = "18359202745"
        password = "123"
        expectedErrM = "登录"#"账号或密码错误，请重新输入"
        errM = self.login_page_setup.Login_Password_WithErr(username, password).text
        print(errM)
        assert expectedErrM == errM

    #("密码错误登录上限")
    def test_Login_Password_WithErr_Limit(self):
        username = "18359202745"
        password = "123"
        expectedErrM = "登录"#"今日错误次数已达上限，请尝试其他登录方式"
        errM = self.login_page_setup.Login_Password_WithErr_Limit(username, password).text
        print(errM)
        assert expectedErrM == errM

    #("正确登录")
    def test_Login_Password_Success(self):
        username = "18046206846"
        password = "cjb123"
        expectedSu = "标签栏"
        #
        print("test_Login")
        Success = self.login_page_setup.Login_Password_Success(username, password).text
        assert expectedSu == Success

#    def test_Logout(self):
#       self.login_page_setup.Log_out()

    def teardown(self):
        sleep(5)
        #App.quit()


if __name__ == 'main':
    pytest.main("-s Test_Case_Login.py")


    '''

    #@DisplayName("账号错误登录")
    def loginWithErrUsername():
        String username = "111"
        String password = "123456"
        String expectedErrM = "请输入正确的帐号！"

        String errM = loginPage.loginWithErrUsername(username, password)
        assertThat(errM,equalTo(expectedErrM))



    #("空密码登录")
    def loginWithoutPassword():
        String username = "376057520"
        String password = ""
        String expectedErrM = "你还没有输入密码！"
        String errM = loginPage.loginWithoutPassword(username, password)
        assertThat(errM,equalTo(expectedErrM))



    #("正确登录")
    def logSuccess():
        String username = "376057520"
        String password = "xxx"
        loginPage.loginSuccess(username,password)


    '''