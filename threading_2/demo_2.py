# _*_coding:utf-8 _*_
# @Time　　 : 2019/11/26   0:35
# @Author　 : zimo
# @File　   :demo_2.py
# @Software :PyCharm
# @Theme    :多线程

import time
import threading

def say_hello():
    print('hello world')
    time.sleep(3)
    print('-----')
if __name__ == '__main__':
    for i in range(5):
        t=threading.Thread(target=say_hello)
        t.start()# 主进程会等待所有子线程运行完毕