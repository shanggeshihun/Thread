# _*_coding:utf-8 _*_
# @Time　　 : 2019/10/28   14:23
# @Author　 : zimo
# @File　   :test_es.py
# @Software :PyCharm
# @Theme    :根据楼栋编码查询楼栋名称
import json
import requests
# ip="http://192.168.1.193:9200/"
ip="http://10.200.66.38:9201/"
index_name="ksj_jck_ld_dagl"
url=ip+index_name+'/'+index_name+'/_search'
json_data={"query":{"match":{"tydzbm":"4403050010080700094"}},"_source":"ldmc"}
print(type(json_data))
resp=requests.post(url,data=json.dumps(json_data))
print(resp.status_code)
result=resp.text
result_json=json.loads(result)
docu_lst=result_json['hits']['hits']
print(docu_lst)

