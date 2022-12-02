import os
import time

current_dir = os.path.dirname(os.path.abspath(__file__))
flag = 0

for root, dirs, files in os.walk(current_dir):
    for file in files:
        if os.path.splitext(file)[1] == ".exe":  # os.path.splitext 将路径拆分为文件名+扩展名
            os.remove(current_dir + "\\" +  file)
            flag = 1
if flag == 1:
    print("all exe has been del")
else:
    print("current dir hasn't exe")
    
time.sleep(3)