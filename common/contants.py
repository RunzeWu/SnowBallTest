'''
 @Time:         2019-08-17
 @Author:       吴润泽
'''
import os
import time

#框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdatas_dir =  os.path.join(base_dir,"testdata")
testcases_dir =  os.path.join(base_dir,"testcases")

logs_dir =  os.path.join(base_dir,"outputs", "logs")
log = os.path.join(logs_dir,time.strftime('%Y-%m-%d')+".log")

allure = os.path.join(base_dir, "outputs", "allure")

screenshot_dir = os.path.join(base_dir,"outputs","screenshots")
screenshot_img = os.path.join(screenshot_dir, str(int(time.time()))+".png")

#caps
caps_dir = os.path.join(base_dir,"desired_caps")

conf_dir = os.path.join(base_dir,"conf")

global_conf = os.path.join(conf_dir,"global.conf")
test_env_conf = os.path.join(conf_dir,"test_env.conf")
prod_env_conf = os.path.join(conf_dir,"prod_env.conf")
