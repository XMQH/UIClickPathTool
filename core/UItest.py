import os
import sys
from airtest.core.api import *

device = os.popen("adb devices").read()

device_name = device.replace('List of devices attached\n', "")
device_name = device_name.replace('\tdevice', "")

device = connect_device("Android://localhost:5037/" + device_name)
work_path = sys.path[0]
nsslog_path = "/sdcard/Android/data/com.tencent.tmgp.speedmobile/files/Nsslog"

device.adb.pull(nsslog_path, work_path)
current_logpath = work_path + '\\nsslog\\'
current_nsslog = os.listdir(current_logpath)[-1]

print(current_nsslog)
print(work_path + '\\nsslog\\', current_nsslog)

p = 0
with open(work_path + '\\nsslog\\' + current_nsslog, 'rb') as f:
    f.seek(p, 0)
    while True:
        lines = f.readlines()
        if lines:
            print(lines)
            p = f.tell()
            f.seek(p, 0)
            time.sleep(1)


