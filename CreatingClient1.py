import socket
s=socket.socket()
s.connect(('localhost',4001))
msg=s.recv(1024)
while msg:
    print('message received:',msg.decode())
    msg=s.recv(1024)
s.close()    