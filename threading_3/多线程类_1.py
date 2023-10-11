# _*_coding:utf-8 _*_
# @Time　　 : 2019/12/23   1:27
# @Author　 : zimo
# @File　   :多线程类_1.py
# @Software :PyCharm
# @Theme    :

from fake_useragent import UserAgent
import requests,json,threading
import pandas as pd
from queue import Queue
import time

ua=UserAgent()

class CrawlThread(threading.Thread):
    def __init__(self,thread_id,fwdm_queue):
        threading.Thread.__init__(self)
        self.thread_id=thread_id
        self.fwdm_queue=fwdm_queue
    def run(self):
        while not crawl_flag:
            if self.fwdm_queue.empty():

                break
            else:
                try:
                    fwdm = self.fwdm_queue.get(False)
                    # print('当前fwdm_queue元素个数',fwdm_queue.qsize())
                    self.get_fw_info(fwdm)
                except:
                    pass
    def get_fw_info(self,fwdm):
        self.response_queue.put(fwdm)

class ParseThread(threading.Thread):
    def __init__(self,thread_id,response_queue):
        threading.Thread.__init__(self)
        self.thread_id=thread_id
        self.response_queue=response_queue
    def run(self):
        while not parse_flag:
            try:
                response = self.response_queue.get(False)
                self.parse_fw_info(response)
            except:
                pass
    def parse_fw_info(self,response):
        data_list.append(response)

data_list=[]
crawl_flag=False
parse_flag=False

def main():

    fwdm_queue = Queue()
    response_queue = Queue()

    df=pd.DataFrame(data={},columns=['fwdm','fwmj','syzt','fwjssj','zlgs'])

    with open(r'D:\work\GeoStar\SmartCity\shenzhen\南山项目\20191221中博科创接口数据\fwdm.txt','r') as f:
        fwdm_lst=f.readlines()
    for fwdm in fwdm_lst:
        fwdm_queue.put(fwdm)
        print('最初fwdm_queue元素个数',fwdm_queue.qsize())
    # 初始化采集线程(从fwdm_queue队列取，获取结果放入response_queue)
    crawl_threads = []
    crawl_name_list = ['crawl_1', 'crawl_2', 'crawl_3', 'crawl_4']
    for thread_id in crawl_name_list:
        thread = CrawlThread(thread_id, fwdm_queue)
        # 启动线程
        thread.start()
        print('当前fwdm_queue元素个数',fwdm_queue.qsize())
        # list的添加方法
        crawl_threads.append(thread)

    # 初始化解析线程(从response_queue取)
    parse_threads = []
    parse_name_list = ['crawl_1', 'crawl_2', 'crawl_3', 'crawl_4']
    for thread_id in parse_name_list:
        thread = ParseThread(thread_id, response_queue)
        # 启动线程
        thread.start()
        print('当前fwdm_queue元素个数', fwdm_queue.qsize())
        # list的添加方法
        parse_threads.append(thread)

    # 等待队列情况
    while not fwdm_queue.empty():
        print(fwdm_queue.qsize())
        pass
    # 为空则通知线程退出
    global  crawl_flag
    crawl_flag=True
    # 等待所有线程结束
    for t in crawl_threads:
        t.join()
    print('crawl_threads退出')

    # 等待队列情况
    while not response_queue.empty():
        pass
    # 为空则通知线程退出
    global parse_flag
    parse_flag=True
    # 等待所有线程结束
    for t in parse_threads:
        t.join()
    print('parse_threads退出')

    # 退出主线程
    print('退出主线程')

    for data in data_list:
        df=df.append(data,ignore_index=True)
if __name__ == '__main__':
    t1=time.time()
    main()
    t2=time.time()
    print(t2-t1)