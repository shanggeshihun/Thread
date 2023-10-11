from time import ctime
import threading
from queue import Queue

Flag = True


def coding(q1, q2):
    while Flag:
        print(q1.get())
        q2.put(1)


def main():
    print('thread %s is running...' % threading.current_thread().name)

    q1 = Queue()
    q2 = Queue()
    for i in range(1000):
        q1.put(i)
    t1 = threading.Thread(target=coding, args=(q1, q2))
    t1.start()
    while not q1.empty():
        pass
    global  flag
    flag = False

    print('11111111111111111')
    while not q2.empty():
        i = q2.get()
        print('resourceStr_classify:', i)

    print('over')
    t1.join()

if __name__ == '__main__':
    main()
