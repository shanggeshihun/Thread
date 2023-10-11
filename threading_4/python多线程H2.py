# Python多线程爬虫
#对比了单线程和多线程两种爬虫实现，得出了并行爬虫高效率的结论
# 1 爬虫的实现
#该爬虫简单的实现了对2345导航网站的网址进行爬取，为了便于后边的多线程爬虫实验，我们需要获取500多个网址库。爬取深度为1
from bs4 import BeautifulSoup
def getWeb():
    headers={\
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)'\
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140'\
    ' Safari/537.36',\
    'Host':'www.2345.com'
    }
    r=requests.get('http://www.2345.com/',headers=headers)
    bs=BeautifulSoup(r.text,'lxml')
    strs=''
    for i in fc:
        if (re.match('http',i,get('href'))!=None):
            strs+='\n'+i.get('href')
    return strs
    
#2 文件操作
def writeToFile(URI,data):
    f=open(URI,'w+')
    f.write(data)
    f.close()
    
# 3 爬去的网址库如下

# 4 实现多线程爬虫
import threading
import requests
import time
from queue import Queue
threads=[]
start=time.time()
# 建立队列，存储爬取网址
#maxsize可以限制队列的大小。如果队列的大小达到了队列的上限，就会加锁，加入就会阻塞，直到队列的内容被消费掉。maxsize的值小于等于0，那么队列的尺寸就是无限制的
que=Queue(1000)
#线程类，每个子线程调用，继承Thread类重写run函数，以便执行我们的爬虫函数
class MyThread(threading.Thread):
    def __init__(self,threadName,que):
        threading.Thread.__init__(self)
        self.threadName=threadName
        self.que=que
    def run(self):
        print('start ' + self.threadName)
        while True:
            try:
                crawler(self.name,self.que)
            except:
                break
        print('exiting'+self.name)
# 爬取的函数，爬虫的程序
def crawler(threadName,que):
# 从队列里取数据。如果为空的话，blocking = False 直接报 empty异常。如果blocking = True，就是等一会，timeout必须为 0 或正数。None为一直等下去，0为不等，正数n为等待n秒还不能读取，报empty异常。
    url=que.get(timeout=2)
    try:
        r=requests.get(url,timeout=15)
        print(que.qsize(),threadName,r.status_code,url)
    except:
        print('Error')
threadList=['thread-1','thread-2','thread-3','thread-4','thread-5','thread-6','thread-7']
 
# filling the queue
f=open('./website1.txt','r')
ss=''
ss=f.read()
f.close()
webList=[]
webList=ss.split('\n')
for url in webList:
    que.put(url)
# create the queue
for tName in threadList:
    thread=MyThread(tName,que)
    thread.start()
    threads.append(thread)
# 同步线程，避免主线程提前终止，保证整个计时工作
for t in threads:
    t.join()
end=time.time()
print('the total time is',end-start)



    
    
