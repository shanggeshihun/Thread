# _*_coding:utf-8 _*_
# @Time　　 : 2019/11/26   0:23
# @Author　 : zimo
# @File　   :高并发讲解_3.py
# @Software :PyCharm
# @Theme    :
import time
import threading
num=0
# 创建一把锁
mutex=threading.Lock()
class MyThread(threading.Thread):
    def run(self):
        global num
        mutex_flag=mutex.acquire()
        print('线程%s的锁状态为%d' %(self.name,mutex_flag))
        # 判断上锁是否成功
        if mutex_flag:
            num+=1
            # time.sleep(1)
            msg=self.name+'set num to' +str(num)
            print(msg)
            # 解锁
            mutex.release()

def test():
    for i in range(5):
        t=MyThread()
        t.start()

if __name__ == '__main__':
    test()