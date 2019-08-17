'''
 @Time:         2019-08-17
 @Author:       吴润泽
'''

# 读取yaml文件的数据，并转换成python对象
# 1、打开yaml文件
# 2、使用yaml的load()函数
from common.contants import caps_dir
import os
import yaml


def get_desired_caps():
    with open(os.path.join(caps_dir,"desired_caps.yaml"),encoding="utf-8") as file:

        res = yaml.load(file,  Loader=yaml.FullLoader)
    return res


desired_caps = get_desired_caps()
