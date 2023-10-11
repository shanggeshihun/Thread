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
def get_app_url(keyword):
    """
    :param keyword:
    :return:关键词对应的APP连接
    """
    main_url='https://s.pc6.com/?k={}'.format(keyword)
    url='http://www.pc6.com/az/882908.html'
    res=requests.get(url)
    res.encoding='gb2312'
    html=etree.HTML(res.text)
    x=html.xpath(r'//div[@class="intro-txt"]/child::*')
    for xx in x:
        print(xx.xpath('string(.)'))