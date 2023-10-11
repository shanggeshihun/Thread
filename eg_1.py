# _*_coding:utf-8 _*_
# @Time　　 : 2019/9/19   21:57
# @Author　 : zimo
#@ File　   :eg_1.py
#@Software  :PyCharm

import time
from threading import Thread
# 自定义线程函数
def main(name='Python'):
    for i in range(2):
        print('hello',name)
        time.sleep(1)
# 创建线程01，不指定参数
thread_01=Thread(target=main)
# 启动线程
thread_01.start()

# 创建线程02，指定参数，注意逗号
thread_02=Thread(target=main,args=('Liuan',))
thread_02.start()


import threading
def job1():
    global n, lock
    # 获取锁
    lock.acquire()
    for i in range(10):
        n += 1
        print('job1', n)
    lock.release()
def job2():
    global n, lock
    # 获取锁
    lock.acquire()
    for i in range(10):
        n += 10
        print('job2', n)
    lock.release()
n = 0
# 生成锁对象
lock = threading.Lock()
t1 = threading.Thread(target=job1)
t2 = threading.Thread(target=job2)
t1.start()
t2.start()