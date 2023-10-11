# _*_coding:utf-8 _*_
# @Time　　 : 2019/9/19   22:48
# @Author　 : zimo
#@ File　   :eg_2.py
#@Software  :PyCharm
import time
from threading import Thread

# CPU计算密集型
def count(x=1, y=1):
    # 使程序完成150万计算
    c = 0
    while c < 500000:
        c += 1
        x += x
        y += y


# 磁盘读写IO密集型
def io_disk():
    with open("file.txt", "w") as f:
        for x in range(5000000):
            f.write("python-learning\n")


# 网络IO密集型
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
url = "https://www.tieba.com/"

def io_request():
    try:
        webPage = requests.get(url, headers=header)
        html = webPage.text
        return
    except Exception as e:
        return {"error": e}


# 【模拟】IO密集型
def io_simulation():
    time.sleep(2)

def timer(mode):
    def wrapper(func):
        def deco(*args, **kw):
            type = kw.setdefault('type', None)
            t1=time.time()
            func(*args, **kw)
            t2=time.time()
            cost_time = t2-t1
            print("{}-{}花费时间：{}秒".format(mode, type,cost_time))
        return deco
    return wrapper

@timer("【单线程】")
def single_thread(func, type=""):
    for i in range(10):
              func()

# 单线程
single_thread(count, type="CPU计算密集型")
single_thread(io_disk, type="磁盘IO密集型")
single_thread(io_request,type="网络IO密集型")
single_thread(io_simulation,type="模拟IO密集型")

@timer("【多线程】")
def multi_thread(func, type=""):
    thread_list = []
    for i in range(10):
        t=Thread(target=func, args=())
        thread_list.append(t)
        t.start()
    e = len(thread_list)

    while True:
        for th in thread_list:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break

@timer("【多线程】")
def multi_thread(func, type=""):
    thread_list = []
    for i in range(10):
        t=Thread(target=func, args=())
        thread_list.append(t)
        t.start()
    e = len(thread_list)

    while True:
        for th in thread_list:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break

    @timer("【多进程】")
    def multi_process(func, type=""):
        process_list = []
        for x in range(10):
            p = Process(target=func, args=())
            process_list.append(p)
            p.start()
        e = process_list.__len__()

        while True:
            for pr in process_list:
                if not pr.is_alive():
                    e -= 1
            if e <= 0:
                break