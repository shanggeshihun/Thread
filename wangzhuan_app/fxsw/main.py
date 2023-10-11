# _*_coding:utf-8 _*_
# @Time　　 : 2020/1/13   1:38
# @Author　 : zimo
# @File　   :2鼠标事件.py
# @Software :PyCharm
# @Theme    :
import requests,json,re
import os,time
from lxml import etree
import numpy as np
from fake_useragent import UserAgent
from valid_proxy import get_valid_proxy_lst
from read_write_file import ReadWriteFile
from get_soft_link import  get_id_link_mapping
from queue import Queue
import  threading

rwf=ReadWriteFile(r'D:\learn\software_learn\NOTE\Python\Thread\wangzhuan_app\fxsw\write_info.txt')

proxy_list=get_valid_proxy_lst()
ua_list=UserAgent()
id_link_mapping=get_id_link_mapping()

# 通过主页面获取二级页面url
class SubpageThread(threading.Thread):
    def __init__(self,thread_id,main_url_queue,sub_url_queue):
        threading.Thread.__init__(self)
        self.thread_id=thread_id
        self.main_url_queue=main_url_queue
        self.sub_url_queue=sub_url_queue

    def run(self):
        while MAINPAGE_FLAG:
            headers = {
                'Accept-Encoding': 'gzip, deflate',
                'User-Agent': np.random.choice(ua_list)
            }
            main_url = self.main_url_queue.get()
            print(main_url)
            try:
                res = requests.get(url=main_url, headers=headers, proxies=np.random.choice(proxy_list))
                res.encoding = 'utf-8'
                time.sleep(np.random.randint(1,5)/10)
            except Exception as e:
                print('请求main_url异常:', main_url, ' 错误类型：', e)
            else:
                try:
                    self.get_subpage_url(res)
                    print('当前取出的main_url:', main_url)
                except Exception as e:
                    print('解析main_url异常', main_url, ' 错误类型：', e)

    def get_subpage_url(self,res):
        """
        :param url:一级网页返回信息
        :return:二级页面地址列表
        """
        html=etree.HTML(res.text)
        app_info_url_list=html.xpath(r"//dd[@class='m-nosolid-six']/a/@href")
        app_info_url_list=['http://www.fxsw.net'+ u for u in app_info_url_list]
        for url in app_info_url_list:
            global  i
            i+=1
            # print('当前线程的名字是：', threading.current_thread().name,i)
            self.sub_url_queue.put(url)


# 通过二级页面获取APP的下载链接
class DownloadUrlThread(threading.Thread):
    def __init__(self,thread_id,sub_url_queue,download_queue):
        threading.Thread.__init__(self)
        self.thread_id=thread_id
        self.sub_url_queue=sub_url_queue
        self.download_queue=download_queue

    def run(self):
        """
        :param res: 二级页面返回信息
        :return:获取下载链接
        """
        while SUBPAGE_FLAG:
            headers = {
                'Accept-Encoding': 'gzip, deflate',
                'User-Agent': np.random.choice(ua_list)
            }
            sub_url = self.sub_url_queue.get()
            try:
                res = requests.get(url=sub_url, headers=headers, proxies=np.random.choice(proxy_list))
                res.encoding = 'gb2312'
                time.sleep(np.random.randint(1,5)/10)
            except Exception as e:
                print('请求sub_url异常:', sub_url,' 错误类型：',e)
            else:
                try:
                    self.get_download_url(res)
                    print('当前取出的sub_url:', sub_url)
                except Exception as e:
                    print('解析sub_url异常', sub_url,' 错误类型：',e)

    def get_download_url(self,res):
        """
        :param res: 二级页面返回信息
        :return:获取下载链接
        """
        html=etree.HTML(res.text)
        app_name = html.xpath("//div[@class='m-sintrod-left f-fl']/span/h1/text()")[0]
        download_url_str = html.xpath('//ul[@class="ul_Address"]/script/text()')[0]
        tmp_download_url =re.findall(r'{Address:"(\d+)",TypeID:"(\d+)",SoftLinkID:"(\d+)",SoftID:"(\d+)"', download_url_str)[0]
        id = tmp_download_url[1]
        download_url="minjie/"+str(tmp_download_url[0])+"?soft_id="+str(tmp_download_url[3])
        download_url=id_link_mapping[id]+download_url
        download=(app_name,download_url)
        self.download_queue.put(download)


# 通过APP下载链接保存文件
class SaveThread(threading.Thread):
    def __init__(self,thread_id,download_queue,save_path):
        threading.Thread.__init__(self)
        self.thread_id=thread_id
        self.download_queue=download_queue
        self.save_path=save_path

    def run(self):
        while DOWNLOAD_FLAG:
            self.save()

    def save(self):
        download=self.download_queue.get()
        print(download)
        rwf.add_write(' '.join(download))

        download_name = download[0]
        download_url = download[1]
        try:
            res = requests.get(download_url, proxies=np.random.choice(proxy_list),stream=True)
        except Exception as e:
            print(download_url,'-',e)
        else:
            time.sleep(np.random.randint(1,5)/10)
            with open(os.path.join(self.save_path, download_name + '.apk'), 'wb') as f:
                # f.write(res.content)
                for chunk in res.iter_content(chunk_size=10240):
                    if chunk:
                        f.write(chunk)
                        f.flush()


i=1
MAINPAGE_FLAG=True # 主页面的队列非空标识
SUBPAGE_FLAG=True # 二级面的队列非空标识
DOWNLOAD_FLAG=True # 下载链接队列非空标识


def main():
    # 清空下载记录文件
    rwf.clear_content()
    # 下载APP保存路径
    save_path=r'D:\learn\software_learn\NOTE\Python\Thread\wangzhuan_app\fxsw\app'

    main_url_queue=Queue()
    sub_url_queue=Queue()
    download_queue=Queue()

    # 主页面>>二级页面
    for i in range(2,3):
        main_url_queue.put('http://www.fxsw.net/class/19_{}.html'.format(i))
    main_thread_name_list=['main_thread_'+str(i) for i in range(1,2)]
    main_thread_list=[]
    for thread_id in main_thread_name_list:
        thread=SubpageThread(thread_id,main_url_queue,sub_url_queue)
        thread.start()
        main_thread_list.append(thread)
    while not main_url_queue.empty():
        # print('当前运行的所有的线程数',len(threading.enumerate()))
        pass
    #    通知主页面>>二级页面线程结束
    global MAINPAGE_FLAG
    MAINPAGE_FLAG=False
    #    等待主页面>>二级页面线程结束
    for t in main_thread_list:
        t.join()
    print('二级页面队列元素大小：',sub_url_queue.qsize())
    print('主页面>>二级页面线程 退出')

    # 二级页面>>下载链接
    sub_thread_name_list = ['sub_thread_' + str(i) for i in range(1, 10)]
    sub_thread_list = []
    for thread_id in sub_thread_name_list:
        thread = DownloadUrlThread(thread_id, sub_url_queue, download_queue)
        thread.start()
        sub_thread_list.append(thread)
    while not sub_url_queue.empty():
        pass
        # print('当前运行的所有的线程数', len(threading.enumerate()))
    #    通知二级页面>>下载链接结束
    global SUBPAGE_FLAG
    SUBPAGE_FLAG = False
    #    等待二级页面>>下载链接结束
    for t in sub_thread_list:
        t.join()
    print('下载队列元素大小：', download_queue.qsize())
    print('二级页面>>下载链接 退出')

# 下载链接>>保存文件
    save_thread_name_list = ['save_thread_' + str(i) for i in range(1, 8)]
    save_thread_list = []
    for thread_id in save_thread_name_list:
        thread = SaveThread(thread_id, download_queue,save_path)
        thread.start()
        save_thread_list.append(thread)
    while not download_queue.empty():
        pass
        # print('当前运行的所有的线程数', len(threading.enumerate()))
    #    通知下载链接>>文件保存结束
    global DOWNLOAD_FLAG
    DOWNLOAD_FLAG = False
    #    等待下载链接>>文件保存结束
    for t in save_thread_list:
        t.join()
    print('下载链接>>文件保存 退出')


if __name__ == '__main__':
    t1=time.time()
    main()
    t2=time.time()
    print(t2-t1)