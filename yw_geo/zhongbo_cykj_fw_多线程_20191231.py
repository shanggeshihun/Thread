# _*_coding:utf-8 _*_
# @Time　　 : 2019/12/21   16:46
# @Author　 : zimo
# @File　   :zhongbo_cykj_fw.py
# @Software :PyCharm
# @Theme    :中博科创 产业空间 房屋信息 多线程

from fake_useragent import UserAgent
import requests,json,threading
import pandas as pd
from queue import Queue
import time

ua=UserAgent()


class CrawlThread(threading.Thread):
    def __init__(self,thread_id,fwdm_queue,response_queue):
        threading.Thread.__init__(self)
        self.thread_id=thread_id
        self.fwdm_queue=fwdm_queue
        self.response_queue=response_queue
        self.token=self.get_token()
        self.access_token=self.get_access_token()
    def get_token(self):
        token='575cbcd216ae482277e97f857cc0384e'
        return  token
    def get_access_token(self):
        access_token = '8855e27a-eae4-4177-b01e-03536c1ac882'
        return access_token
    def run(self):
        while not crawl_flag:
            if self.fwdm_queue.empty():
                break
            else:
                try:
                    fwdm = self.fwdm_queue.get(False)
                    self.get_fw_info(fwdm)
                except Exception as e:
                    print(e)
                    pass
    def get_fw_info(self,fwdm):
        url = 'http://58.250.250.222:59540/open/queryfwzl?houseNumber={0}&token={1}'.format(fwdm, self.token)
        headers = {
            'access_token': self.access_token,
            'User-Agent': ua.random
        }
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        response = res.text
        self.response_queue.put((fwdm,response))

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
            except Exception as e:
                print(e)
                pass
    def parse_fw_info(self,response):
        res = json.loads(response[1])
        data= res['body']['data']
        data['fwdm'] = response[0].strip()
        print(data)
        data_list.append(data)

data_list=[]
crawl_flag=False
parse_flag=False

def main():

    fwdm_queue = Queue()
    response_queue = Queue()

    df=pd.DataFrame(data={},columns=['fwdm','fwmj','syzt','fwjssj','zlgs','wymc','zjdj'])

    with open(r'D:\work\GeoStar\SmartCity\shenzhen\南山项目\数据对接&同步类\中博科创接口数据_20191221\fwdm.txt','r') as f:
        fwdm_lst=f.readlines()
    for fwdm in fwdm_lst:
        fwdm_queue.put(fwdm)

    # 初始化采集线程(从fwdm_queue队列取，获取结果放入response_queue)
    crawl_threads = []
    crawl_name_list = ['crawl_1', 'crawl_2', 'crawl_3', 'crawl_4']
    for thread_id in crawl_name_list:
        thread = CrawlThread(thread_id, fwdm_queue,response_queue)
        # 启动线程
        thread.start()
        # list的添加方法
        crawl_threads.append(thread)

    # 初始化解析线程(从response_queue取)
    parse_threads = []
    parse_name_list = ['crawl_1', 'crawl_2', 'crawl_3', 'crawl_4']
    for thread_id in parse_name_list:
        thread = ParseThread(thread_id, response_queue)
        # 启动线程
        thread.start()
        # list的添加方法
        parse_threads.append(thread)

    # 等待队列情况
    while not fwdm_queue.empty():
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
    df.to_excel(r"C:\Users\Administrator\Desktop\zhongbo_cykj_addfield_fw_mutithreading_.xlsx")

if __name__ == '__main__':
    t1=time.time()
    main()
    t2=time.time()
    print(t2-t1)