# _*_coding:utf-8 _*_
# @Time　　 : 2019/12/21   16:46
# @Author　 : zimo
# @File　   :zhongbo_cykj_fw.py
# @Software :PyCharm
# @Theme    :中博科创 产业空间 房屋信息 单线程

from fake_useragent import UserAgent

import requests,json,time
import pandas as pd

ua=UserAgent()

def get_token():
    token='575cbcd216ae482277e97f857cc0384e'
    return token

def get_access_token():
    access_token='6e2c38b2-eb92-4ccb-b04d-c4a73e909b9d'
    return access_token

def get_fw_info(fwdm):
    token_ = get_token()
    access_token_=get_access_token()

    url='http://58.250.250.222:59540/open/queryfwzl?houseNumber={0}&token={1}'.format(fwdm,token_)
    headers={
        'access_token':access_token_,
        'User-Agent':ua.random
    }
    try:
        res=requests.get(url,headers=headers)
        res.encoding='utf-8'
        response=res.text
    except Exception as e:
        print(e)
        response=None
    return response

def parse_info(res):
    pass
if __name__ == '__main__':
    t1=time.time()
    df=pd.DataFrame(data={},columns=['fwdm','fwmj','syzt','fwjssj','zlgs'])
    with open(r'D:\work\GeoStar\SmartCity\shenzhen\南山项目\20191221中博科创接口数据\fwdm.txt','r') as f:
        fwdm_lst=f.readlines()
    for fwdm in fwdm_lst:
        res=get_fw_info(fwdm)
        if not res:
            continue
        res_json=json.loads(res)
        print(res_json)
        body=res_json['body']
        if not body:
            continue
        data=body['data']
        data['fwdm']=fwdm
        print(data)
        df=df.append(data,ignore_index=True)
    t2=time.time()
    print(t2-t1)
    # print(df.to_excel(r"C:\Users\Administrator\Desktop\zhongbo_cykj_fw_singlethreading.xlsx"))