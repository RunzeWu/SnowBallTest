'''
 @Time:         2019-08-17
 @Author:       吴润泽
'''
import configparser
from common import contants


class ReadConfig:
    def __init__(self):
        '''
        选择环境
        '''
        self.cf = configparser.ConfigParser()
        # self.cf.read(FilePath().global_conf_path(), encoding="utf-8")
        self.cf.read(contants.global_conf, encoding="utf-8")
        button = self.cf.getboolean("switch", "button")

        if button:
            self.cf.read(contants.test_env_conf, encoding="utf-8")
        else:
            self.cf.read(contants.prod_env_conf, encoding="utf-8")

    def get_value(self, section, option):
        return self.cf.get(section, option)

    def get_int(self, section, option):
        return self.cf.getint(section, option)

    def get_float(self, section, option):
        return self.cf.getfloat(section, option)

    def get_boolen(self, section, option):
        return self.cf.getboolean(section, option)
