# encoding:utf-8
# author:wangzhicheng
# time:2019/12/18 15:33
# file:handle_mysql.py


import pymysql
from Common.handle_yaml import do_yaml


class HandleMysql:
    """处理数据库"""

    def __init__(self, config=do_yaml.read_yaml("mysql", "config")):
        # yaml中获取连接数据库的相关信息
        self.config = config
        # 连接数据库
        self.cnn = pymysql.connect(**self.config)
        # 创建游标，pymysql.cursors.DictCoursor 查询的数据以字典格式返回{}
        self.cursor = self.cnn.cursor(cursor=pymysql.cursors.DictCursor)

    def read_mysql(self, sql=do_yaml.read_yaml("mysql", "query_state_sql"), args=None, is_less=True):
        # 执行sql语句
        self.cursor.execute(sql, args)
        self.cnn.commit()

        # 如果查询的是多条数据就用fetchall，单条数据就用fetchone
        if is_less:
            value = self.cursor.fetchone()
        else:
            value = self.cursor.fetchall()

        return value

    def close(self):
        # 先关闭游标
        self.cursor.close()
        # 再关闭数据库
        self.cnn.close()


if __name__ == '__main__':
    print(HandleMysql().read_mysql("select lng from t_cloud_printer_info where msn= %s;", "testWap499")["lng"])

    from TestDatas.DeviceMoreInfoPageDatas import DeviceMoreInfoPageDatas as DMIPD

    HandleMysql().read_mysql(do_yaml.read_yaml("mysql", "update_log_swith_off"), DMIPD.SN)

