# _*_coding:utf-8 _*_
# @Time　　 : 2019/9/22   13:44
# @Author　 : zimo
#@ File　   :Queue.py
#@Software  :PyCharm

from queue import Queue
q=Queue(maxsize=0)
# 阻塞程序，等待队列消息
q.get()
# 获取消息，设置超时时间
q.get(timeout=5.0)
# 发送消息
q.put()
# 等待所有的消息都被消费完
q.join()

# 查询当前队列的消息个数
q.qsize()
# 队列消息是否都被消费完，True/False
q.empty()
# 检测队列里消息是否已满
q.full()


from queue import Queue
from threading import Thread
import time

class Student(Thread):
    def __init__(self,name,queue):
        super().__init__()
        self.name=name
        self.queue=queue
    def run(self):
        while True:
            # 阻塞程序，时刻监听老师，接收消息
            msg=self.queue.get()
            # 一旦发现点到自己名字，就赶紧答到
            if msg==self.name:
                print('{}:到！'.format(self.name))
class Teacher:
    def __init__(self,queue):
        self.queue=queue
    def call(self,student_name):
        print('老师:{}来了没?'.format(student_name))
        # 发送消息，要点谁的名
        self.queue.put(student_name)
queue=Queue()
teacher=Teacher(queue=queue)
s1=Student(name='小明',queue=queue)
s2=Student(name='小亮',queue=queue)
s1.start()
s2.start()

print('开始点名')
teacher.call('小明')
time.sleep(1)
teacher.call('小亮')
