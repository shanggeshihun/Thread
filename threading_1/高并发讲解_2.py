# _*_coding:utf-8 _*_
# @Time　　 : 2019/11/26   0:15
# @Author　 : zimo
# @File　   :高并发讲解_2.py
# @Software :PyCharm
# @Theme    :通过继承线程类实现多线程

import threading
import time
class MyThread(threading.Thread):
    def run(self):
        for i in range(5):
            msg=self.name+str(i)
            print(msg)

if __name__ == '__main__':
    t=MyThread()
    t.start()
