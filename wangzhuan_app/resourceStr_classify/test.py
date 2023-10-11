# _*_coding:utf-8 _*_
# @Time　　 :2020/10/29/029   15:42
# @Author　 : Antipa
# @File　　 :resourceStr_classify.py
# @Theme    :PyCharm

import os
with open(os.path.join(os.getcwd(),'resourceStr.txt'),'r',encoding='utf-8') as f:
    # resourceStr = f.read()
    resourceStr_lines=f.readlines()
print(resourceStr_lines)
