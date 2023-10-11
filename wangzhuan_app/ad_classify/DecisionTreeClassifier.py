# _*_coding:utf-8 _*_
# @Time　　 :2020/12/4/004   12:46
# @Author　 : Antipa
# @File　　 :DecisionTreeClassifier.py
# @Theme    :PyCharm

import numpy as np
import pandas as pd
import pandas_profiling as pdf
import os
import matplotlib.pyplot as plt
from_file_path=os.path.join(os.getcwd(),'file','result.xlsx')
df=pd.read_excel(from_file_path)
df.fillna(value=0,inplace=True)


feature_columns=['device_10', 'package_cnt', 'kh_sample_cnt', 'kh_black_sample_cnt','kh_black_sample_cnt_per','sample_cnt', 'black_sample_cnt','black_sample_cnt_per', 'tuia_sdk_samples','tuia_sdk_samples_flag', 'meishu_sdk_samples','meishu_sdk_samples_flag', 'ad_value_cnt', 'risk_value_cnt']
label_columns=['type']
df_feature=df[feature_columns]
df_label=df[label_columns]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(df_feature, df_label,test_size=1,random_state=1)

from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor

regr = DecisionTreeClassifier(max_depth=4)
regr.fit(X_train, y_train)

from six import StringIO
import pydotplus
from sklearn import tree
# 输出决策树文件.dot

dot_data = StringIO()
# 单独安装graphviz.msi 软件
tree.export_graphviz(regr,
                     out_file=dot_data,
                     max_depth=4,
                     feature_names=feature_columns,
                     class_names=['1','0'],
                     filled=True,
                     rounded=True,
                     special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())

tree_out_file=os.path.join(os.getcwd(),'file','tree.png')
tree_out_file_pdf=os.path.join(os.getcwd(),'file','tree.pdf')

graph.write_png(tree_out_file)  #当前文件夹生成out.png
graph.write_pdf(tree_out_file_pdf)  #当前文件夹生成out.png
