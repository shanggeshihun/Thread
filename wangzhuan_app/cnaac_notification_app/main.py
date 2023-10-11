# _*_coding:utf-8 _*_
# @Time　　 :2020/12/10/010   10:56
# @Author　 : Antipa
# @File　　 :main_single_threading_7881.py
# @Theme    :PyCharm

import requests,json,re
import os,time,math
from lxml import etree
import numpy as np
import pandas as pd
from fake_useragent import UserAgent

ua_list=UserAgent()

complaint_num=1926
max_result=50
page=math.ceil(complaint_num/max_result)
df=pd.DataFrame()

for p in range(page):
    start_position=max_result*p
    req_url='https://www.cnaac.org.cn/service//webas/admin/notice/noticeList?startPosition={0}&maxResult={1}&noticeStatus=0'.format(start_position,max_result)
    headers={
        'Host': 'www.cnaac.org.cn',
        'Referer': 'https: // www.cnaac.org.cn / bulletin.html',
        'User-Agent':np.random.choice(ua_list)
    }
    res=requests.get(url=req_url,headers=headers)
    res_to_json=json.loads(res.text)

    code=res_to_json['code']
    if code==200:
        result_data=res_to_json['body']['resultData']
        for r in result_data:
            try:
                create_date=r['createDate']
            except:
                create_date=''
            try:
                del_flag=r['delFlag']
            except:
                del_flag=''
            try:
                id=r['id']
            except:
                id=''
            try:
                appid_create_date=r['appId']['createDate']
            except:
                appid_create_date=''
            try:
                appid_del_flag=r['appId']['delFlag']
            except:
                appid_del_flag=''
            try:
                appid_id=r['appId']['id']
            except:
                appid_id=''
            try:
                appid_number=r['appId']['number']
            except:
                appid_number=''
            try:
                app_name=r['appId']['name']
            except:
                app_name=''
            try:
                app_version=r['appId']['appVersion']
            except:
                app_version=''
            try:
                app_developer=r['appId']['developer']
            except:
                app_developer=''
            try:
                md5=r['appId']['md5']
            except:
                md5=''
            try:
                url=r['appId']['url']
            except:
                url=''
            try:
                channel_name=r['appId']['channel']['name']
            except:
                channel_name=''
            try:
                virusFlag=r['appId']['virusFlag']
            except:
                virusFlag=''
            try:
                benavior=r['appId']['benavior']
            except:
                benavior=''
            try:
                virusName=r['appId']['virusName']
            except:
                virusName=''
            try:
                publishStatus=r['appId']['publishStatus']
            except:
                publishStatus=''
            try:
                platform=r['appId']['platform']
            except:
                platform=''
            try:
                finalDate=r['appId']['finalDate']
            except:
                finalDate=''
            try:
                appPackage=r['appId']['appPackage']
            except:
                appPackage=''
            try:
                importFlag=r['appId']['importFlag']
            except:
                importFlag=''
            try:
                feedbackDescription=r['appId']['feedbackDescription']
            except:
                feedbackDescription=''
            try:
                feedbackUpdateTime=r['appId']['feedbackUpdateTime']
            except:
                feedbackUpdateTime=''
            try:
                category=r['appId']['category']
            except:
                category=''
            app_info=[create_date,del_flag,id,appid_create_date,appid_del_flag,appid_id,appid_number,app_name,app_version,app_developer,md5,url,channel_name,virusFlag,benavior,virusName,publishStatus,platform,finalDate,appPackage,importFlag,feedbackDescription,feedbackUpdateTime,category]
            print(app_info)
            df=df.append([app_info])
            print(req_url)
    else:
        print('请求失败url:',req_url)
    time.sleep(1.5)
    print(p)
df.columns=['create_date','del_flag','id','appid_create_date','appid_del_flag','appid_id','appid_number','app_name','app_version','app_developer','md5','url','channel_name','virusFlag','benavior','virusName','publishStatus','platform','finalDate','appPackage','importFlag','feedbackDescription','feedbackUpdateTime','category'
]
print(df.head(2))
df.to_excel(os.path.join(os.getcwd(),'app_info_result.xlsx'))