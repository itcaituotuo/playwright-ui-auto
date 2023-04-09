# author: 测试蔡坨坨
# datetime: 2023/4/10 0:40
# function: 登录页 业务层

from pages.app.login_page import LoginPage
from utils.config_utils import ConfigUtils


class BizLogin:
    def __init__(self, page):
        self.login_page = LoginPage(page)

    def login(self, username=ConfigUtils().get_data()['username'], password=ConfigUtils().get_data()['password']):
        """
        登录
        :param username: 用户名
        :param password: 密码
        """
        # 1.输入用户名
        self.login_page.input_username(username)
        # 2.输入密码
        self.login_page.input_password(password)
        # 3.点击登录
        self.login_page.click_login()
