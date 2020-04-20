from threading import *
from time import *

class Producer:
    def __init__(self):
        self.products=[]
        self.c=Condition()
    def produce(self):
        
        for i in range (1,5):
            self.c.acquire()
            self.products.append('product'+str(i))
            
            sleep(0)
            print('product added to List')
            
            self.c.notify()
            self.c.release()
class Consumer():
    def __init__(self,prod):
        self.prod=prod
    def consume(self):
            self.prod.c.acquire()
            self.prod.c.wait(timeout=0)
            
            self.prod.c.release()
            print('ordershipped',self.prod.products)
            
p=Producer()
c=Consumer(p)
t=Thread(target=p.produce)
t1=Thread(target=c.consume)
t.start()
t1.start()
