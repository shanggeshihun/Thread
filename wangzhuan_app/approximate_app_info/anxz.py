# _*_coding:utf-8 _*_
# @Time     :2020/10/29 0029   下午 11:48
# @Author   : Antipa
# @File     :anxz.py
# @Theme    :《anxz.com》模糊搜索获取APP信息

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
    # 安卓版本
    main_url='https://www.anxz.com/search/{}-2.html'.format(keyword)
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'User-Agent': np.random.choice(ua_list)
    }
    try:
        res=requests.get(main_url, headers=headers)
        res.encoding='utf-8'
        html=etree.HTML(res.text)
        sub_url=html.xpath(r"//div[@class='m-solist']/div/dl/dt/a/@href")[0]

        sub_url='https://www.anxz.com'+sub_url

        sub_res = requests.get(sub_url, headers=headers)
        sub_res.encoding = 'utf-8'
        sub_html = etree.HTML(sub_res.text)

        base_info_list=sub_html.xpath(r"//div[@id = 'param-content']/ul/li")

        type = base_info_list[3].xpath(r"./span/text()")[0]
        size = base_info_list[0].xpath(r"./span/text()")[0]
        language = base_info_list[2].xpath(r"./span/text()")[0]
        version = sub_html.xpath(r"//div[@id='softTit']/span/text()")[0]
        time = base_info_list[1].xpath(r"./span/text()")[0]
        star = sub_html.xpath(r"//div[@id='pingfen']/div[@class='star_r']/text()")[0]
        developer = base_info_list[5].xpath(r"./span/text()")[0]
        property = base_info_list[4].xpath(r"./span/text()")[0]
        plat = base_info_list[6].xpath(r"./span/text()")[0]

        app_name=sub_html.xpath(r'//div[@id="softTit"]/h1/text()')[0]
        x=sub_html.xpath(r"//div[@id = 'soft-intro']/child::*")
        jieshao='\n'.join([xx.xpath('string(.)').strip() for xx in x])
        info={keyword:{'app_name':app_name,'type':type,'size':size,'language':language,'version':version,'time':time,'star':star,'developer':developer,'property':property,'plat':plat,'jieshao':jieshao}}
    except Exception as e:
        print(e)
        return None
    return info

if __name__ == '__main__':
    app_info=get_app_url('微信')
    print(app_info)