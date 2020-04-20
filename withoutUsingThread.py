from threading import *
class MyThread1():
    def fun1(self):
        print('hi')
        print(current_thread().getName())
        
d=MyThread1()
t=Thread(target=d.fun1)  
t.start()    
            