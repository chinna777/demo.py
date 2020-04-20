from threading import *
def printmachine():
    print(current_thread().getName())
    i= 0
    print
    while i<=10:
        print(i)
        i+=1
print(current_thread().getName())         
dan=Thread(target=printmachine)
dan.start()
