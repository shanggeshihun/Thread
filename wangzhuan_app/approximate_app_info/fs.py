# _*_coding:utf-8 _*_
# @Time     :2020/10/23 0023   下午 11:28
# @Author   : Antipa
# @File     :fs.py
# @Theme    :《飞速下载》模糊搜索获取APP信息
import requests
from lxml import etree

def get_app_url(keyword):

    # 查找关键词
    url='https://s.9fs.com/?f=1&k={}&cid=sjrj'.format(keyword)
    try:
        res=requests.get(url)
        html=etree.HTML(res.text)
        app_url_list=html.xpath(r"//dl[@id='result']/dt/a/@href")
        # APP链接
        app_url=app_url_list[0]
        # APP详情
        app_res=requests.get(app_url)
        app_res.encoding='gb2312'
        app_html=etree.HTML(app_res.text)
        # APP下载地址
        download_url=app_html.xpath(r"//ul[@class='m-down-ul info']/li/a/@href")[0]

        base_info_list=app_html.xpath(r"//div[@class='f-fl m-sjconter']/div/ul/li")
        type=base_info_list[0].xpath(r"./span/a/text()")[0]
        size=base_info_list[1].xpath(r"./b/text()")[0]
        language=base_info_list[2].xpath(r"./span/text()")[0]
        version=base_info_list[3].xpath(r"./span/text()")[0]
        time=base_info_list[4].xpath(r"./span/text()")[0]
        star=base_info_list[5].xpath(r"./span/@class")[0]
        developer=base_info_list[6].xpath(r"./span/text()")[0]
        property=base_info_list[7].xpath(r"./span/text()")[0]
        plat=base_info_list[8].xpath(r"./span/text()")[0]

        app_name=app_html.xpath(r"//div[@class='m-sjlinfo']/h1/text()")[0]

        x=app_html.xpath(r"//div[@class='m-center']/child::*")
        jieshao='\n'.join([xx.xpath('string(.)').strip() for xx in x])

        info={keyword:{'app_name':app_name,'type':type,'size':size,'language':language,'version':version,'time':time,'star':star,'developer':developer,'property':property,'plat':plat,'jieshao':jieshao}}
    except:
        return None
    return info

if __name__ == '__main__':
    keyword = '同城公约'
    app_info=get_app_url(keyword)
    print(app_info)