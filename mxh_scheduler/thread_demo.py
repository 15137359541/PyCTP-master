# coding:utf-8
import threading
import time

def action(arg):
    time.sleep(1)
    print  ('sub thread start!the thread name is:%s\r' % threading.currentThread().getName())
    res = ('the arg is:%s\r' %arg)
    print(res)
    with open("logging.txt",'a')as f:
        f.write(res)
    time.sleep(1)
thread_list = []#线程存放列表
for i in range(4):
    t =threading.Thread(target=action,args=(i,))
    t.setDaemon(True)
    thread_list.append(t)
#这样写法会让程序依次执行，失去了多线程的效果
# for t in thread_list:
#     t.start()
#     t.join()

for t in thread_list:
    t.start()

for t in thread_list:
    t.join()

print ('main_thread end!')