#encoding:utf-8
#author:wangzhicheng
#time:2020/8/3 13:58
#file:switch_timestamp.py


import datetime

#时间戳转换固定格式 2020-08-04 17:18
def switch_timestamp(timestamp):

    new_time=datetime.datetime.fromtimestamp(timestamp)
    new_time = str(new_time)[:16]

    return  str(new_time)


if __name__ == '__main__':
    print(switch_timestamp(1596532684))

