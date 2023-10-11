# _*_coding:utf-8 _*_
# @Time　　 : 2019/12/1   9:56
# @Author　 : zimo
# @File　   :多线程爬虫案例_1.py
# @Software :PyCharm
# @Theme    :
import threading
from fake_useragent import UserAgent
from queue import Queue
import requests
from lxml import  etree

ua=UserAgent()
queue=Queue() # 创建一个队列

class CrawlThread(threading.Thread):
    """
    获取线程类
    """
    def __init__(self,thread_id,queue):
        threading.Thread.__init__(self)
        self.thread_id=thread_id
        self.queue=queue
    def run(self):
        print('启动了线程,{}'.format(self.thread_id))
        self.crawl_spider()
        print('退出其线程,{}'.format(self.thread_id))
    def crawl_spider(self):
        while True:
            if self.queue.empty():# 判断队列是否为空
                break
            else:
                page=self.queue.get()# 获取队列的元素
                print('当前正在工作的线程是,{},正在采集第{}个页面'.format(self.thread_id,page))
                url="https://www.qiushibaike.com/8hr/page/{}".format(page)
                headers={
                    "User-Agent":ua.random
                }
                try:
                    content=requests.get(url,headers=headers)
                    data_queue.put(content.text)
                except Exception as e:
                    print('采集线程错误:',e)# e 描述捕获的异常值

class ParserThread(threading.Thread):
    """
    解析网页的类
    """
    def __init__(self,thread_id,queue,file):
        threading.Thread.__init__(self)
        self.thread_id=thread_id
        self.queue=queue
        self.file=file
    def run(self):
        print('启动了线程,{}'.format(self.thread_id))
        while not flag:
            try:
                item=self.queue.get(False) # get 的参数为false时，队列为空，会抛出异常
                self.parse_data(item)
            except:
                pass
        print('退出了线程,{}'.format(self.thread_id))
    def parse_data(self,item):
        """
        解析网页内容的函数
        :param item:
        :return:
        """
        try:
            html=etree.Html(item)
            # 匹配段子所有内容
            result=html.xpath('//div[contains(@id,"qiushi_tag"')
            for site in result:
                try:
                    img_url=site.xpath(".//img/@src")[0]
                    title=img_url.xpath(".//h2")[0].text
                    content=img_url.xpath('.//div[@class="content"]/span')[0].text.strip()
                    response={
                        'img_url':img_url,
                        'title':title,
                        'content':content
                    }
                    self.file.write(json.dumps(response,ensure_ascii=False).encode('utf-8')+'\n')
                except:
                    pass
        except:
            pass
# 方法写好，调用即可
data_queue=Queue()
flag=False

def main():
    output=open('qiushi.json','a')
    page_queue=Queue(56)
    for page in range(1,11):
        page_queue.put(page)

    # 初始化采集线程
    crawl_threads=[]
    crawl_name_list=['crawl_1','crawl_2','crawl_3']
    for thread_id in crawl_name_list:
        thread=CrawlThread(thread_id,data_queue)
        # 启动线程
        thread.start()
        # list的添加方法
        crawl_threads.append(thread)

    # 初始化解析线程
    parse_threads = []
    parse_name_list = ['crawl_1', 'crawl_2', 'crawl_3']
    for thread_id in parse_name_list:
        thread = ParserThread(thread_id, page_queue,output)
        # 启动线程
        thread.start()
        # list的添加方法
        parse_threads.append(thread)

    # 等待队列情况
    while not page_queue.empty():
        pass

    # 等待所有线程结束
    for t in crawl_threads:
        t.join()

    while not data_queue.empty():
        pass

    # 为空则通知线程退出
    global flag
    flag=True
    for t in parse_threads:
        t.join()
    print('退出主线程')
    output.close()

if __name__ == '__main__':
    main()