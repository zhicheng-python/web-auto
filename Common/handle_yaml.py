# encoding:utf-8
# author:wangzhicheng
# time:2020/5/8 9:45
# file:handle_yaml.py


import yaml
from Common.handle_path import do_path


class HandleYaml:
    """读取写入配置文件"""

    # 读取配置文件
    def read_yaml(self, section, option):
        with open(file=do_path.config_file_path, encoding="utf8") as f:
            value = yaml.load(f, Loader=yaml.FullLoader)

        return value[section][option]

    # 写入配置文件
    def write_yaml(self, datas):
        with open(file=do_path.config_file_path, mode="w", encoding="utf8") as f:
            yaml.dump(data=datas, stream=f, allow_unicode=True)  # allow_unicode=True 写入中文不会乱码


# 实例化
do_yaml = HandleYaml()

if __name__ == '__main__':
    datas = {"logging":
                 {"collect_level": "DEBUG",
                  "output_level": "DEBUG",
                  "name": "mylogger",
                  "datefmt": "%Y/%m/%d %H:%M:%S",
                  "fmt": "%(asctime)s-%(name)s-%(levelname)s-%(message)s"}}

    # do_yaml.write_yaml(datas)

    print(do_yaml.read_yaml("logging", "name"))
