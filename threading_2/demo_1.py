# _*_coding:utf-8 _*_
# @Time　　 : 2019/11/26   0:33
# @Author　 : zimo
# @File　   :demo_1.py
# @Software :PyCharm
# @Theme    :单线程
def demo1():
    for i in range(5):
        print('demo1--%d' % i)
def demo2():
    for i in range(5):
        print('demo2--%d' %i)
def main():
    demo1()
    demo2()
if __name__ == '__main__':
    main()

