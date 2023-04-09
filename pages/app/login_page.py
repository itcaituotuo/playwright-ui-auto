# author: 测试蔡坨坨
# datetime: 2023/4/10 0:11
# function:

from pages.base.base_page import BasePage


class LoginPage(BasePage):
    LOCATOR_FILE = 'locators/app/login_page.yml'

    def __init__(self, page):
        super().__init__(page, self.LOCATOR_FILE)

    def input_username(self, username):
        """
        输入用户名
        :param username: 用户名
        :return:
        """
        self.fill_('用户名输入框', username)

    def input_password(self, password):
        """
        输入密码
        :param password: 密码
        :return:
        """
        self.fill_('密码输入框', password)

    def click_login(self):
        self.click_('登录按钮')
