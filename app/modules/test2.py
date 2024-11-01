import re
import subprocess
import cv2
import os

device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
df = str(subprocess.check_output("lsusb"), 'utf-8')
print(df)
for i in df.split('\n'):
    if i:
        info = device_re.match(i)
        if info:
            dinfo = info.groupdict()
            if "Microdia Webcam Vitade AF" in dinfo['tag']:
                print ("Camera found.")
                bus = dinfo['bus']
                device = dinfo['device']
                print(bus, device)
                break

device_index = None
for file in os.listdir("/sys/class/video4linux"):
    real_file = os.path.realpath("/sys/class/video4linux/" + file)
    print(file)
    print (real_file)
    print(real_file[-1])
    print ("/" + str(bus[-1]) + "-" + str(int(device[-1])-1) + "/")
    if "/" + str(bus[-1]) + "-" + str(int(device[-1])-1) + "/" in real_file:
        device_index = real_file[-1]
        print ("Hurray, device index is " + str(device_index))
