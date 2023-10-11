# 单线程
from time import ctime,sleep

def music():
	for i in range(2):
		print('i was listening to music. %s' %ctime())
		sleep(1)
		
def movie():
	for i in range(2):
		print('i was at the movie! %s' % ctime())
		sleep(5)

if __name__=='__main__':
	music()
	movie()
	print('all over %s' %'ctime)
"""
I was listening to music. Thu Apr 17 10:47:08 2014
I was listening to music. Thu Apr 17 10:47:09 2014
I was at the movies! Thu Apr 17 10:47:10 2014
I was at the movies! Thu Apr 17 10:47:15 2014
all over Thu Apr 17 10:47:20 2014
"""

import threading
from time import ctime,sleep

def music(func):
	for i in range(2):
		print('i was listening to %s. %s' %(func,ctime()))
		sleep(1)

def movie(func):
	for i in range(2):
		print('i was at the %s! %s' %(func,ctime()))
		sleep(5)

if __name__=='__main__':
	music('爱情买卖')
	movie('爱凡达')
	print('all over %s '%ctime())
	
"""
I was listening to 爱情买卖. Thu Apr 17 11:48:59 2014
I was listening to 爱情买卖. Thu Apr 17 11:49:00 2014
I was at the 阿凡达! Thu Apr 17 11:49:01 2014
I was at the 阿凡达! Thu Apr 17 11:49:06 2014
all over Thu Apr 17 11:49:11 2014
"""











# 多线程
import threading
from time import ctime,sleep

def music(func):
	for i in range(2):
		print('i was listening to %s %s' %(func,ctime())
		sleep(1)

def movie(func):
	for i in range(2):
		print('i was at the movie %s %s' %(func,ctime())
		sleep(5)
		
threads=[]
t1=threading.Thread(target=music,args=('爱情买卖',))
threads.append(t1)
t2=threading.Thread(target=movie,args=('爱凡达',))
threads.append(t2)

if __name__=='__main__':
	for t in threads:
		t.setDaemon(True)
		t.start()
	print('all over %s' %ctime())
	

	
	

	
# player.py
from time import sleep,ctime
import threading
def music(func):
	for i in range(2):
		print('Start playing :%s ! %s' %(func,ctime())
		sleep(2)

def movie(func):
	for i in range(2):
		print('Start playing: %s! %s' %(func,ctime())
		sleep(5)

def player(name):
	r=name.split('.')[1]
	if r=='mp3':
		music(name)
	else:
		if r=='mp4':
			move(name)
		else:
			print('error:the format is not recognized')
list=['爱情买卖.mp3','阿凡达.mp4']
threads=[]
files=range(len(list))

# 创建线程
for i in files:
	t=threading.Thread(target=player,args=(lsit[i],))
	threads.append(t)
if__name__=='__main__':
	# 启动线程
	for i in files:
		threads[i].start()
	for i in files:
		threads[i].join()
	print('end:%s' % ctime())
	


		