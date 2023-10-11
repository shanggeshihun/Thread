# _*_coding:utf-8 _*_
# @Time　　 : 2019/11/21   15:23
# @Author　 : zimo
# @File　   :multi_thread_doudula.py
# @Software :PyCharm
# @Theme    :多线程爬虫

import threading
import requests
from lxml import etree
import os
from bs4 import BeautifulSoup
import time

BASE_PAGE_URL="http://www.doutula.com/article/list/?page="
# 页面url列表
PAGE_URL_LIST=[]
#所有表情url列表
FACE_URL_LIST=[]

for x in range(1,3):
    url=BASE_PAGE_URL+str(x)
    PAGE_URL_LIST.append(url)

# 全局锁
gLock=threading.Lock()

os.chdir(r'D:\learn\software_learn\NOTE\Python\Thread\doutula')
def producer():
    while True:
        # 多线程，每个线程（3个生产这）都会执行这个代码，只能用pop取，不能用for循环
        # 避免多个线程冲突，先锁再释放
        gLock.acquire()
        if len(PAGE_URL_LIST)==0:
            gLock.release()
            break
        else:
            page_url=PAGE_URL_LIST.pop()
            gLock.release()
            response=requests.get(page_url).text
            soup=BeautifulSoup(response,'lxml')
            img_list=soup.find_all('img',attrs={'class':'lazy image_dtb img-responsive'})
            gLock.acquire()
            for img in img_list:
                url = img['data-original']
                if not url.startswith('http:'):
                    url = "http:" + img['data-original']
                FACE_URL_LIST.append(url)
            gLock.release()

def customer():
    while True:
        gLock.acquire()
        if len(FACE_URL_LIST)==0:
            gLock.release()
            continue
        else:
            face_url=FACE_URL_LIST.pop()
            gLock.release()
            split_list=face_url.split('/')
            filename=split_list.pop()
            path=os.path.join(os.getcwd(),filename)
            res=requests.get(face_url)
            with open(path,'wb') as f:
                f.write(res.content)

def main():
    t0=time.time()
    # 创建两个多线程来作为生产者，去爬取表情url；
    for x in range(3):
        th=threading.Thread(target=producer)
        th.start()
    # 创建五个多线程来作为消费者，去把表情下载下来；
    for x in range(5):
        th=threading.Thread(target=customer)
        th.start()
    print(time.time()-t0)

if __name__ == '__main__':
    main()



# import requests
# from bs4 import BeautifulSoup
# url="http://www.doutula.com/article/list/?page=1"
# res=requests.get(url).text
# soup=BeautifulSoup(res,'lxml')
# img_list=soup.find_all('img',attrs={'class':'lazy image_dtb img-responsive'})
# print(img_list)