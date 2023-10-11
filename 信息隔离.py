# _*_coding:utf-8 _*_
# @Time　　 : 2019/10/24   0:42
# @Author　 : zimo
# @File　   :信息隔离.py
# @Software :PyCharm
# @Theme    :

# threading.local 可以控制变量的隔离，即使是同一个变量在不同的线程中，其值也是不能共享的
from threading import local,Thread,currentThread
# 定义一个local实现
local_data=local()
# 在主线中，存入name这个变量
local_data.name='local_data'
class MyThread(Thread):
    def run(self):
        print('赋值前-子线程:',currentThread(),local_data.__dict__)
        local_data.name=self.getName()
        print('赋值后-子线程:',currentThread(),local_data.__dict__)
if __name__=='__main__':
    print('开始前-主线程:',local_data.__dict__)
    t1=MyThread()
    t1.start()
    t1.join()
    t2=MyThread()
    t2.start()
    t2.join()
    print('结束后-主线程:',local_data.__dict__)