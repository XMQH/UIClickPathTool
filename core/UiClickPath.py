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

from airtest.core.android import Android
from airtest.core.api import connect_device, auto_setup

auto_setup(__file__)
auto_setup(__file__, devices=["Android:///"])


phone_nsslog_path ="/sdcard/Android/data/com.tencent.tmgp.speedmobile/files/Nsslog"
push_nsslog_path = os.path.abspath("../Nsslog/")
print(push_nsslog_path)
# 连接手机
dev = connect_device("Android:///")
# 每次启动游戏前先清空手机内游戏日志和已推送到电脑的日志
dev.shell("rm -rf " + phone_nsslog_path)
if os.path.exists(push_nsslog_path):
   shutil.rmtree(push_nsslog_path)
# 启动游戏
dev.start_app("com.tencent.tmgp.speedmobile")
# 判断是否点击了游戏内按钮

"""
    获取游戏最新的Nsslog日志
"""
android = Android()


while True:
   dev.adb.push(phone_nsslog_path, push_nsslog_path)
   print("1111")
   time.sleep(0.1) # 每隔0.1s向电脑托送日志 与实时读取日志是否回产生冲突？

#