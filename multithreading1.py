import threading
print('current Thread we are running is :',threading.current_thread().getName)
if threading.current_thread()==threading.main_thread():
     print('you are running the current thread which is main')
else:
    print('you are not in main thread check')