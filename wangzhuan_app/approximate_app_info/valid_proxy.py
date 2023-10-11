# _*_coding:utf-8 _*_
# @Time　　 :2020/10/1/001   10:38
# @Author　 : 
#@ File　   :valid_proxy.py
#@ Desc     :

from fake_useragent import UserAgent
import requests
import numpy as np
from lxml import etree



def get_proxy_lst():
    user_agent=UserAgent()
    proxy_lst=[]
    url='http://www.data5u.com/'
    headers={
        "Accept-Encoding":"gzip, deflate",
        "User-Agent":np.random.choice(user_agent)
    }
    res=requests.get(url,headers=headers)
    # res.encoding='utf-8'
    html=etree.HTML(res.text)
    proxy_info=html.xpath('//li[@style="text-align:center;"]/ul[@class]')
    for p in proxy_info[1:]:
        http=p.xpath('./span/li/text()')[3]
        ip=p.xpath('./span/li/text()')[0]
        port=p.xpath('./span/li/text()')[1]
        tmp_lst={http:http+"://"+ip+":"+port}
        proxy_lst.append(tmp_lst)
    return proxy_lst

def check_proxy(proxy):
    """
    :param proxy代理
    :return: 返回bool
    """
    import json
    url='http://httpbin.org/ip'
    flag=True
    try:
        response = requests.get(url, proxies=proxy,timeout=(3,7))
        if response.status_code==200:
            response_dict=json.loads(response.text)
        else:
            flag=False
    except:
        flag=False
    return flag


def get_valid_proxy_lst():
    valid_proxy_dict_list=[]
    proxy_dict_list=get_proxy_lst()
    for proxy in proxy_dict_list:
        f=check_proxy(proxy)
        if f:
            valid_proxy_dict_list.append(proxy)
    return valid_proxy_dict_list

# def get_valid_proxy_lst():
#     return [{'https': 'https://49.70.99.148:8246'}, {'https': 'https://49.70.32.18:8610'}, {'https': 'https://27.43.184.237:9047'}, {'https': 'https://220.167.42.15:8772'}, {'https': 'https://171.35.170.190:8910'}, {'https': 'https://115.221.243.107:8185'}, {'https': 'https://120.83.104.174:8231'}, {'https': 'https://60.169.134.5:9070'}]


if __name__ == '__main__':
    t=get_valid_proxy_lst()
    print(t)