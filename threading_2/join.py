# _*_coding:utf-8 _*_
# @Time　　 : 2019/11/30   18:00
# @Author　 : zimo
# @File　   :1_add_thread.py
# @Software :PyCharm
# @Theme    :


import threading

import  time

def thread_join():
    print('T1 start\n')
    for i in range(10):
        time.sleep(1)
    print('T1 finished')

def main():
    # 多线程是同时进行的任务
    added_thread=threading.Thread(target=thread_join,name='T1')
    added_thread.start()
    print('all done\n')

def main_join():
    added_thread = threading.Thread(target=thread_join, name='T1')
    added_thread.start()
    added_thread.join()
    print('all done\n')

if __name__ == '__main__':
    # main()
    main_join()