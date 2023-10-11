# _*_coding:utf-8 _*_
# @Time　　 : 2020/1/13   1:38
# @Author　 : zimo
# @File　   :2鼠标事件.py
# @Software :PyCharm
# @Theme    :《pc6.com》模糊搜索获取APP信息
import requests,json,re
import os,time
from lxml import etree
import numpy as np
from fake_useragent import UserAgent
# from valid_proxy import get_valid_proxy_lst
# proxy_list=get_valid_proxy_lst()
ua_list=UserAgent()


def get_app_url(keyword):
    """
    :param keyword:
    :return:关键词对应的APP信息
    """
    main_url='https://s.pc6.com/?cid=android&k={}'.format(keyword)
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': np.random.choice(ua_list)
    }
    try:
        res=requests.get(main_url, headers=headers)
        res.encoding='utf-8'
        html=etree.HTML(res.text)
        sub_url=html.xpath(r'//dl[@id="result"]/dt/a/@href')[0]

        sub_res = requests.get(sub_url, headers=headers)
        sub_res.encoding = 'gb2312'
        sub_html = etree.HTML(sub_res.text)

        base_info_list = sub_html.xpath(r"//p[@class='base']/i")

        type = base_info_list[0].xpath(r"./a/text()")[0]
        size = base_info_list[2].xpath(r"./text()")[0].split('：')[1]
        language = base_info_list[4].xpath(r"./text()")[0].split('：')[1]
        version = base_info_list[1].xpath(r"./text()")[0].split('：')[1]
        time = base_info_list[3].xpath(r"./text()")[0].split('：')[1]
        star = base_info_list[5].xpath(r"./span/@class")[0]
        developer = base_info_list[6].xpath(r"./text()")[0].split('：')[1]
        property = ''
        plat = 'Android'

        app_name=sub_html.xpath(r'//dd[@id="dinfo"]/h1/text()')[0]
        x=sub_html.xpath(r'//div[@class="intro-txt"]/child::*')
        jieshao='\n'.join([xx.xpath('string(.)').strip() for xx in x])
        info={keyword:{'app_name':app_name,'type':type,'size':size,'language':language,'version':version,'time':time,'star':star,'developer':developer,'property':property,'plat':plat,'jieshao':jieshao}}
    except:
        return None
    return info

if __name__ == '__main__':
    app_info=get_app_url('养鱼')
    print(app_info)