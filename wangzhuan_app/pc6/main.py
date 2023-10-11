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

rwf=ReadWriteFile(os.path.join(os.getcwd(),'write_info.txt'))

soft_info_rwf=ReadWriteFile(os.path.join(os.getcwd(),'soft_write_info.txt'))

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
            try_times,flag=1,'failed'
            err=''
            while try_times<=3:
                try:
                    res = requests.get(url=main_url, headers=headers, proxies=np.random.choice(proxy_list))
                    res.encoding = 'utf-8'
                    time.sleep(np.random.randint(1,5)/10)
                except Exception as e:
                    err=e
                    try_times = try_times + 1
                    time.sleep(2)
                else:
                    try:
                        self.get_subpage_url(res)
                        print('当前取出的main_url:', main_url)
                    except Exception as e:
                        print('解析main_url异常', main_url, ' 错误类型：', e)
                    flag='success'
                    break
            if flag=='failed':
                print('请求main_url异常:', main_url, ' 错误类型：', err)




    def get_subpage_url(self,res):
        """
        :param url:一级网页返回信息
        :return:二级页面地址列表
        """
        html=etree.HTML(res.text)
        app_info_url_list=html.xpath(r'//dl[@id="listCont"]/dd/p/a[@target="_blank"]/@href')
        app_info_url_list=['http://www.pc6.com'+ u for u in app_info_url_list]
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
            try_times, flag = 1, 'failed'
            err = ''
            while try_times <= 3:
                try:
                    res = requests.get(url=sub_url, headers=headers, proxies=np.random.choice(proxy_list))
                    res.encoding = 'gb2312'
                    time.sleep(np.random.randint(5,11)/10)
                except Exception as e:
                    err=e
                    try_times = try_times + 1
                    time.sleep(2)
                    # print('请求sub_url异常:', sub_url,' 错误类型：',e)
                    # sub_url_info_list.append((sub_url,'请求异常',str(e),time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))
                else:
                    try:
                        self.get_download_url(res)
                        print('当前取出的sub_url:', sub_url)
                        sub_url_info_list.append((sub_url, '请求成功','',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))
                    except Exception as e:
                        print('解析sub_url异常', sub_url,' 错误类型：',str(e))
                        sub_url_info_list.append((sub_url, '解析异常', str(e),time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))
                    flag = 'success'
                    break
            if flag=='failed':
                print('请求sub_url异常:', sub_url,' 错误类型：',err)
                sub_url_info_list.append((sub_url,'请求异常',str(err),time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))

    def get_download_url(self,res):
        """
        :param res: 二级页面返回信息
        :return:获取下载链接
        """
        html=etree.HTML(res.text)

        try:
            tmp_soft_intro = html.xpath(r'//dd[@id="soft-info"]/div/child::*[3]')[0]
            soft_intro=tmp_soft_intro.xpath('string(.)')
        except:
            soft_intro=''

        app_name = html.xpath('//dd[@id="dinfo"]/h1/text()')[0]
        soft_info_rwf.add_write('\t'.join([app_name,soft_intro]))

        download_url_str = html.xpath('//ul[@class="ul_Address"]/script[@type="text/javascript"]/text()')[0]
        download_url =re.findall(r'{Address:"(.*?)",TypeID:"(\d+)"', download_url_str)[0][0]
        id = re.findall(r'{Address:"(.*?)",TypeID:"(\d+)"', download_url_str)[0][1]
        download_url=id_link_mapping[id]+download_url.replace(id_link_mapping[id],'')
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
            download = self.download_queue.get()
            download_name = download[0]
            download_url = download[1]
            try_times, flag = 1, 'failed'
            err = ''
            while try_times <= 3:
                try:
                    res = requests.get(download_url, proxies=np.random.choice(proxy_list), stream=True)
                    time.sleep(np.random.randint(1, 5) / 10)
                    # rwf.add_write(' '.join(download))
                except Exception as e:
                    err=e
                    try_times = try_times + 1
                    time.sleep(2)
                    # print('请求download_url异常:', download_url, ' 错误类型：', e)
                    # download_url_info_list.append((download_url,'请求异常',str(e),time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))               try_times=try_times+1
                else:
                    try:
                        self.save(download_name,res)
                        print('当前取出的download_url:', download_url)
                        download_url_info_list.append((download_url, '请求成功', '',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))
                    except Exception as e:
                        print('解析download_url异常', download_url, ' 错误类型：', e)
                        download_url_info_list.append((download_url, '解析异常',str(e),time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))
                    flag = 'success'
                    break
            if flag == 'failed':
                print('请求download_url异常:', download_url, ' 错误类型：', err)
                download_url_info_list.append((download_url,'请求异常',str(err),time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())))

    def save(self,download_name,res):
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
sub_url_info_list=[]
download_url_info_list=[]

def main():
    # 清空下载记录文件
    rwf.clear_content()
    # 下载APP保存路径
    save_path=os.path.join(os.getcwd(),'app')

    main_url_queue=Queue()
    sub_url_queue=Queue()
    download_queue=Queue()

    # 主页面>>二级页面
    for i in range(1,41):
        main_url_queue.put('http://www.pc6.com/android/qq_703_{}.html'.format(i))
    main_thread_name_list=['main_thread_'+str(i) for i in range(1,6)]
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
    sub_thread_name_list = ['sub_thread_' + str(i) for i in range(1,6)]
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
    save_thread_name_list = ['save_thread_' + str(i) for i in range(1,6)]
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

    # 爬虫状态写入
    for t in sub_url_info_list:
        rwf.add_write('\t'.join(t))

    for t in download_url_info_list:
        rwf.add_write('\t'.join(t))
    print('爬虫状态写入结束')

if __name__ == '__main__':
    t1=time.time()
    main()
    t2=time.time()
    print(t2-t1)