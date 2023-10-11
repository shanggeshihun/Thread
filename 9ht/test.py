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
from queue import Queue
import  threading

proxy_list=get_valid_proxy_lst()
ua_list=UserAgent()

def test():
    i = 0
    while i < 3:
        print(i)
        i+=1
    print('222')

if __name__ == '__main__':
    test()