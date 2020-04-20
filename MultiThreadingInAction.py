from threading import *
from time import sleep
def fun1():
    print('hey how r u ?')
    print(current_thread().getName())
def fun2():
    print('hey who are you')
    sleep(0.5)
    print(current_thread().getName())
    
t=Thread(target=fun1)
t.start()
t1=Thread(target=fun2)
t1.start()
t2=Thread(target=fun2)
t2.start()
