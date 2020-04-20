import socket
s=socket.socket()
host='localhost'
port=6465
s.bind((host,port))
print("the server is ready to listening at port:" ,port)
s.listen(1)
c,addr=s.accept()
print('the adress of client is:',addr)
fileName=c.recv(1024)
try:
    f=open(fileName,'rb')
    cont=f.read()
    print("wait iam fetching file info for u")
    c.send(cont.encode())
except FileNotFoundError:
    print('file does not exsist')
s.close()
