# 通过继承threading.Thread创建线程
import threading
class mythread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num=num
        
    def run(self):
       print('I am',self.num)
        
t1=mythread(1)
t2=mythread(2)
t3=mythread(3)
t1.start()
t2.start()
t3.start()

# 方法三：使用threading.Thread直接在线程中运行函数
import threading
def run(x,y):
    for i in range(x,y):
        print(i)
        
t1=threading.Thread(target=run,args=(15,20))
t1.start()


# 二)Thread对象中的常用方法
import threading
import time
class mythread(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id=id
    def run(self):
        time.sleep(4)
        print(self.id)

t=mythread(1)
def func():
    t.start()
    print(t.isAlive())#打印线程状态
func()



