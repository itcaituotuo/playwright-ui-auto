# -*- coding:utf-8 -*-
# 作者：蔡合升
# 时间：2022/3/12 20:50
# 功能：获取路径信息

import os


class PathUtils:
    def __init__(self):
        self.path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

    def get_project_path(self):
        """
        获取项目根路径
        @return: F:\Desktop\coder\caituotuo-top\qiyuesuo-webui-auto\
        """
        return str(self.path + "\\")

    def get_project_path_v2(self):
        return self.path


if __name__ == '__main__':
    print(PathUtils().get_project_path())
