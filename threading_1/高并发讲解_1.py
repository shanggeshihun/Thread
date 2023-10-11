# _*_coding:utf-8 _*_
# @Time　　 : 2019/11/26   0:11
# @Author　 : zimo
# @File　   :高并发讲解_1.py
# @Software :PyCharm
# @Theme    :一次性打印多个
import time
import threading
def sorry():
    print('sorry')
    time.sleep(1)

if __name__ == '__main__':
    for i in range(5):
        t=threading.Thread(target=sorry)
        t.start()