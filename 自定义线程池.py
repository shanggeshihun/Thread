# _*_coding:utf-8 _*_
# @Time　　 : 2019/10/24   22:58
# @Author　 : zimo
# @File　   :自定义线程池.py
# @Software :PyCharm
# @Theme    :
import time
import threading
from queue import Queue
def target(q):
    while True:
        msg=q.get()
        for i in range(5):
            print('running thread-{}:{}'.format(threading.get_ident(),i))
            time.sleep(1)
def pool(workers,queue):
    for n in range(workers)P:
        t=threading.Thread(target=target,args=(queue,))
        t.daemon=True
        t.start()
queue=Queue()
# 创建一个线程池，并设置线程数为5
pool(5,queue)
for i in range(100):
    queue.put('start')
# 消息都被消费才能结束
queue.join()
