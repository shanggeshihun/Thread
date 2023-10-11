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

sub_url='http://www.9ht.com/xz/434958.html'

headers = {
                'Accept-Encoding': 'gzip, deflate',
                'User-Agent': np.random.choice(ua_list)

            }
res = requests.get(url=sub_url, headers=headers, proxies=np.random.choice(proxy_list))
res.encoding = 'gbk2312'
html=etree.HTML(res.text)
app_name = html.xpath('//div[@class="dico"]/h1/text()')[0]
download_url_str = html.xpath('//ul[@class="ul_Address"]/script[@type="text/javascript"]/text()')[0]
download_url =re.findall(r'{Address:"(.*?\.apk)",TypeID:"(\d+)"', download_url_str)[0][0]
id=re.findall(r'{Address:"(.*?\.apk)",TypeID:"(\d+)"', download_url_str)[0][1]
print(download_url,id)