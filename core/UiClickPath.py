#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/11 19:36
# @Author  : jhuang
# @File    : __init__.py.py
# @Software: PyCharm
# @Description:
import os.path
import shutil
import time
from multiprocessing import Process, Queue
from airtest.core.api import connect_device, auto_setup
from tkinter import *
import pyperclip

from core.UiWindow import ui_window
import logging

logger = logging.getLogger("airtest")
logger.setLevel(logging.ERROR)

auto_setup(__file__)
auto_setup(__file__, devices=["Android:///"])

phone_nsslog_path = "/sdcard/Android/data/com.tencent.tmgp.speedmobile/files/Nsslog/"
pull_nsslog_path = os.path.abspath(os.path.dirname(__file__))
print("电脑端日志存放目录：" + pull_nsslog_path)

# 连接手机
dev = connect_device("Android:///")

# 检查是否存在日志文件

# 每次启动游戏前先清空手机内游戏日志和已推送到电脑的日志
# TODO 手机

# if os.path.exists(pull_nsslog_path):
#     shutil.rmtree(pull_nsslog_path)

# 启动游戏
start_app = dev.start_app("com.tencent.tmgp.speedmobile")
time.sleep(5)

# 开启UI路径输出开关

"""
    获取游戏最新的Nsslog日志
"""

dev.adb.pull(phone_nsslog_path, pull_nsslog_path)

current_logpath = pull_nsslog_path + "\\Nsslog\\"
current_nsslog = os.listdir(current_logpath)[-1]
print("正在读取的游戏日志文件：" + current_nsslog)

list = []  # 所有按钮路径


def get_uipath_lines():
    p = 0
    while True:
        dev.adb.pull(phone_nsslog_path, pull_nsslog_path)
        with open(current_logpath + current_nsslog, 'rb') as f:
            f.seek(p, 0)
            data = f.readlines()
            for line in data:
                line = str(line)
                if '[UIClickDebugPath]' in line:
                    UIname = line.split('[UIClickDebugPath]')[1]
                    UIname = UIname.replace("\\n'", "")
                    print("UI点击路径：" + UIname)
                    p = f.tell()
                    f.seek(p, 0)
                    time.sleep(1)


# uipath = ''
# if len(list) > 0:
#     uipath = str(list[-1])

get_uipath_lines()
