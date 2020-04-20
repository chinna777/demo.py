from threading import *
from time import *
class Producer:
    def __init__(self):
        self.products=[]
        self.orderplaced = False
    def produce(self):
        for i in range (1,5):
            self.products.append('product'+str(i))
            print('product added to List')
            sleep(1)
            self.orderplaced = True
class Consumer():
    def __init__(self,prod):
        self.prod=prod
    def consume(self):
        while self.prod.orderplaced == False:
            sleep(1)
        print('ordershipped',self.prod.products)
p=Producer()
c=Consumer(p)
t=Thread(target=p.produce)
t1=Thread(target=c.consume)
t.start()
t1.start()
