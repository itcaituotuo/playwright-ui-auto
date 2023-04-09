# author: 测试蔡坨坨
# datetime: 2023/4/9 23:52
# function: 基类，对Playwright库进行二次封装

from utils.yaml_utils import YamlUtils


class BasePage:
    def __init__(self, page, locator_file):
        """
        实例化BasePage类时，最先执行的是__init__()方法，该方法的入参就是BasePage类的入参
        :param page:
        :param locator_file: 页面元素管理文件，例如：locators/app/login_page.yml
        """
        self.page = page
        self.locator_file = locator_file

    def get_by(self, loc_type, loc_value):
        loc_type = str(loc_type).lower()
        if loc_type == 'xpath':
            return self.page.locator(loc_value)

    def locator_(self, key):
        """
        定位元素
        :param key: 元素名称
        :return: 元素对象
        """
        print(self.locator_file)
        elements = YamlUtils().get_yaml(self.locator_file)
        loc_type = elements[key]['type']
        loc_value = elements[key]['value']
        return self.get_by(loc_type, loc_value)

    def click_(self, key):
        """
        点击元素
        :param key:
        :return:
        """
        self.locator_(key).click()

    def fill_(self, key, text):
        """
        输入文本
        :param key:
        :param text: 文本值
        :return:
        """
        self.locator_(key).fill(text)
