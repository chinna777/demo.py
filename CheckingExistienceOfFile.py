import os,sys
if os.path.isfile("myAss1.txt"):
    f=open("myAss.txt",'r')
    
    s=f.read()
    f.seek(0)
    print(s)
    f.close()
else:
    print('file does not exsist')
    sys.exit()
