# author: 测试蔡坨坨
# datetime: 2023/4/10 0:47
# function:

from utils.yaml_utils import YamlUtils


class ConfigUtils:
    APPLICATION_FILE = 'config/application.yml'

    def get_application(self):
        """
        读取配置信息
        :return:
        """
        return YamlUtils().get_yaml(self.APPLICATION_FILE)

    def get_url(self):
        """
        读取网站地址
        :return: URL
        """
        return self.get_application()['url']

    def get_data(self):
        """
        获取配置文件中的data信息
        :return:
        """
        return self.get_application()['data']


if __name__ == '__main__':
    print(ConfigUtils().get_application())
    print(ConfigUtils().get_url())
    print(ConfigUtils().get_data())
