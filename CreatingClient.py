import socket
s=socket.socket()
host="localhost"
port=4001
s.bind((host,port))
print("server is listening on :",port)
s.listen(1)
c,addr=s.accept()
print('connection eshtablished with client from address:',str(addr))
s.send(b'hey client what are you excepting from me')
s.send('i can help you with anything :'.encode)

