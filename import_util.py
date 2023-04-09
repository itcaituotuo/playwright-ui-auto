# author: 蔡合升
# datetime: 2022/12/4 16:59
# function: 使用isort对import进行排序，使用autoflake删除未使用的import

import os

from utils.path_utils import PathUtils


class ImportUtil:
    def __init__(self):
        self.project_root = PathUtils().get_project_path()

    def rm_all_unused_import_and_isort(self):
        filepath_list = []
        all_module_list = []
        all_module_str = ""
        for root, folder_names, file_names in os.walk(self.project_root):
            for file_name in file_names:
                # 文件绝对路径
                file_path = root + os.sep + file_name
                filepath_list.append(file_path)
                # 最后一个.号进行拆分
                file = str(file_path).rsplit(".")
                if len(file) == 2:
                    if str(file[1]) == "py":
                        all_module_list.append(str(file[0]) + ".py")
        # 找出项目中所有.py文件，拼接成字符串，用空格隔开
        for i in all_module_list:
            all_module_str += str(i) + " "
        cmd1 = "autoflake -i --remove-all-unused-imports {}".format(all_module_str)
        cmd2 = "isort {}".format(self.project_root)
        os.system(cmd1)
        os.system(cmd2)
        print(cmd1)
        print(cmd2)


if __name__ == "__main__":
    ImportUtil().rm_all_unused_import_and_isort()
