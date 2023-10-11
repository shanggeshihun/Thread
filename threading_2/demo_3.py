# _*_coding:utf-8 _*_
# @Time　　 : 2019/11/26   0:44
# @Author　 : zimo
# @File　   :demo_3.py
# @Software :PyCharm
# @Theme    :
import  time
import threading

def demo1():
    for i in range(3):
        print('demo1---%d' % i)
        time.sleep(1)
        print('-----')
def demo2():
    for i in range(3):
        print('demo2---%d' %i)
        time.sleep(1)
        print('-----')
if __name__ == '__main__':
    print('--开始--:%s' % time.ctime())
    t1=threading.Thread(target=demo1)
    t2=threading.Thread(target=demo2)
    t1.start()
    t2.start()

    while True:
        length=len(threading.enumerate())
        print('当前运行的线程数:%d' % length)
        if length<=1:# 执行主进程
            break
        time.sleep(0.5)