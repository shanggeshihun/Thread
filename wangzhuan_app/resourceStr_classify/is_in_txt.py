# _*_coding:utf-8 _*_
# @Time     :2020/10/25 0025   下午 11:30
# @Author   : Antipa
# @File     :is_in_txt.py
# @Theme    :PyCharm

keyword_str='下庄|上庄|投注|下注|付费观看|弹幕|聊天室|游戏充值|游戏区服|游戏登录|游戏账号|游戏充值|学生|院校|考研|教育|疾病|患者|毛坯|无码|女优|番号|相亲|红娘|股票代码|证券代码|理赔|垫付|银行托管|租赁|银行存管|存管账户|主播榜|云闪付|银行理财|贵金属|保单|K线|采购商|供应商'
keyword_list=keyword_str.split('|')

with open(r'D:\learn\software_learn\NOTE\Python\Thread\wangzhuan_app\test\txt_file.txt','r',encoding='utf-8') as f :
    txt=f.read()

k_in_txt_list=[]
for k in keyword_list:
    if k in txt:
        k_in_txt_list.append(k)
print(k_in_txt_list)
