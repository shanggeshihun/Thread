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

sub_url='https://www.18touch.com/downs_9248_pc_and_2.html'

headers = {
                'Accept-Encoding': 'gzip, deflate, br',
                'User-Agent': np.random.choice(ua_list)

            }
res = requests.get(url=sub_url, headers=headers)
print(res.status_code)
# res.encoding = 'gbk2312'
# html=etree.HTML(res.text)
# app_name = html.xpath(r"//dd[@class='m-nosolid-six']/a/@href")
# print(app_name)

#
with open(r'D:\learn\software_learn\NOTE\Python\Thread\9ht\app\赢金配资网.apk', 'wb') as f:
    # f.write(res.content)
    for chunk in res.iter_content(chunk_size=10240):
        if chunk:
            f.write(chunk)
            f.flush()