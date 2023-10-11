# _*_coding:utf-8 _*_
# @Time　　 : 2019/10/26   16:13
# @Author　 : zimo
# @File　   :寻找最佳特征GBDT.py
# @Software :PyCharm
# @Theme    :

# 定义训练数据
train_data=[[5.1,3.5,1.4,0.2],[4.9,3.0,1.4,0.2],[7.0,3.2,4.7,1.4],[6.4,3.2,4.5,1.5],[6.3,3.3,6.0,2.5],[5.8,2.7,5.1,1.9]]
# 定义label
label_data=[[1,0,0],[1,0,0],[1,0,0],[0,1,0],[0,0,1],[0,0,1]]
# index 表示的第几类
def find_best_loss_and_split(train_data,label_data,index):
    sample_numbers=len(label_data)
    feature_numbers=len(train_data[0])
    current_label=[]

    # define the min loss
    min_loss=10000000

    # feature represents the dimensions of the feature
    feature=0

    # split represents the detail split value
    split=0

    # get current label
    for label_index in range(0,len(label_data)):
        current_label.append(label_data[label_index][index])


    # trans all features
    for feature_index in range(0,feature_numbers):
        ## current feature value
        current_value=[]
        for sample_index in range(0,sample_numbers):
            current_value.append(train_data[sample_index][feature_index])
        L=0
        ## different label_data value
        for index in range(0,len(current_value)):
            r1=[]
            r2=[]
            y1=0
            y2=0

            for index_1 in range(0,len(current_value)):
                if current_value[index_1]<current_value[index]:
                    r1.append(index_1)
                else:
                    r2.append(index_1)
            ## calculate the samples for first class
            sum_y=0
            for index_r1 in r1:
                sum_y+=current_label[index_r1]
            if len(r1)!=0:
                y1=float(sum_y)/float(len(r1))
            else:
                y1=0
            ## calculate the smaples for second class
            sum_y=0
            for index_r2 in r2:
                sum_y+=current_value[index_r2]
            if len(r2)!=0:
                y2=float(sum_y)/float(len(r2))
            else:
                y2=0


            ## trans all samples to find minium loss and best split
            for index_2 in range(0,len(current_value)):
                if index_2 in r1:
                    L+=float((current_label[index_2]-y1))*float((current_label[index_2]-y1))
                else:
                    L += float((current_label[index_2] - y2)) * float((current_label[index_2] - y2))
            if L<min_loss:
                feature=feature_index
                split=current_value[index]
                min_loss=L
    return min_loss,split,feature

if __name__ == '__main__':
    for index in range(len(label_data[0])):
        result = find_best_loss_and_split(train_data, label_data, index)
        print(result)