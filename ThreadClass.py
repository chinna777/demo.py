from threading import Thread
class MyThread(Thread):
    def run(self):
        for i in range(1,11,2):
            print(i)
t=MyThread()
t.start()