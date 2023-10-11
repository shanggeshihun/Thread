# _*_coding:utf-8 _*_
# @Time　　 : 2019/10/27   23:53
# @Author　 : zimo
# @File　   :get_webgame_info.py
# @Software :PyCharm
# @Theme    :

import time
def deco(f):
    def wrapper():
        start_time=time.time()
        f()
        end_time=time.time()
        execution_time=(end_time-start_time)*1000
        print('time is %d ms' %  execution_time)
    return wrapper

@deco
def f():
    print('hello')
    time.sleep(1)
    print('world')
if __name__ == '__main__':
    f()


import time
def deco(f):
    def wrapper(a,b):
        start_time=time.time()
        f(a,b)
        end_time=time.time()
        execution_time=(end_time-start_time)*1000
        print('time is %d ms' % execution_time)
    return wrapper
@deco
def f(a,b):
    print('be on')
    time.sleep(1)
    print('result is %d' %(a+b))
if __name__ == '__main__':
    f(3,4)


import time
def deco(f):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        f(*args,**kwargs)
        end_time=time.time()
        execution_time=(end_time-start_time)*1000
        print('time is %d ms' % execution_time)
    return wrapper
@deco
def f(a,b):
    print('be on')
    time.sleep(1)
    print('result is %d' % (a+b))

@deco
def f2(a,b,c):
    print('be on')
    time.sleep(1)
    print('result is %d' % (a+b+c))

if __name__ == '__main__':
    f2(3,4,5)
    f(3,4)

def farg(arg,*args,**kwargs):
    print(arg,args,kwargs)
if __name__ == '__main__':
    farg(1,2,3,4,a=5,b=6)